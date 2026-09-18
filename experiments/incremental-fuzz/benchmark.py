"""Generate temporal counterexamples, then replay them through actual dbt materializations.

Synthetic mechanism experiment, not a production accuracy or commercial-product benchmark.
"""

import argparse
import contextlib
import io
import json
import platform
import random
import tempfile
import time
from importlib.metadata import version
from pathlib import Path

import duckdb
from dbt.cli.main import dbtRunner
from hypothesis import find, settings
from hypothesis import strategies as st

EVENT = st.tuples(st.integers(0, 3), st.integers(1, 8), st.integers(1, 20))
TRACES = st.lists(st.lists(EVENT, min_size=0, max_size=2), min_size=2, max_size=5)
SEARCH = settings(max_examples=2000, deadline=None, database=None, derandomize=True)


def simulate(trace, variant):
    """Fast search surrogate. Every reported finding must also reproduce in actual dbt."""
    source, target = {}, []
    sequence = 0
    history = []
    for batch in trace:
        for key, timestamp, amount in batch:
            sequence += 1
            source[key] = (key, timestamp, amount, sequence)
        rows = list(source.values())
        if not history:
            target = rows
        elif variant == "append_all":
            target += rows
        else:
            column = 3 if variant == "ingestion_watermark" else 1
            watermark = max((r[column] for r in target), default=0)
            changes = [r for r in rows if r[column] > watermark]
            keys = {r[0] for r in changes}
            target = [r for r in target if r[0] not in keys] + changes
        history.append({"actual": sorted(target), "expected": sorted(rows)})
    return history


def has_kind(trace, kind):
    seen = {}
    max_timestamp = 0
    for batch_index, batch in enumerate(trace):
        if kind == "replay" and batch_index > 0 and not batch and seen:
            return True
        for key, timestamp, amount in batch:
            if batch_index > 0 and key not in seen:
                if kind == "late" and timestamp < max_timestamp:
                    return True
                if kind == "boundary" and timestamp == max_timestamp:
                    return True
        for key, timestamp, amount in batch:
            seen[key] = amount
            max_timestamp = max(max_timestamp, timestamp)
    return False


def mismatch(history):
    return any(step["actual"] != step["expected"] for step in history)


def discover():
    traces = {}
    for kind, variant in [
        ("late", "event_watermark"),
        ("boundary", "event_watermark"),
        ("replay", "append_all"),
    ]:
        trace = find(
            TRACES,
            lambda value: has_kind(value, kind) and mismatch(simulate(value, variant)),
            settings=SEARCH,
        )
        traces[kind] = {"trace": trace, "variant": variant, "source": "Hypothesis.find"}
    # Supplied by the independent researcher before implementation, not learned from outputs.
    traces["holdout_old_key_correction"] = {
        "trace": [[(0, 2, 10), (1, 8, 20)], [(0, 2, 11)]],
        "variant": "event_watermark",
        "source": "preregistered holdout",
    }
    traces["holdout_same_timestamp_correction"] = {
        "trace": [[(0, 5, 10)], [(0, 5, 12)]],
        "variant": "event_watermark",
        "source": "preregistered holdout",
    }
    return traces


def project(root, variant):
    (root / "models").mkdir()
    (root / "dbt_project.yml").write_text(
        "name: temporal_benchmark\nversion: '1.0'\nconfig-version: 2\n"
        "profile: temporal_benchmark\nmodel-paths: [models]\n"
    )
    (root / "profiles.yml").write_text(
        "temporal_benchmark:\n  target: local\n  outputs:\n    local:\n"
        f"      type: duckdb\n      path: '{root / 'data.duckdb'}'\n"
        "      schema: main\n      threads: 1\n"
    )
    (root / "models" / "sources.yml").write_text(
        "version: 2\nsources:\n  - name: raw\n    schema: main\n    tables:\n      - name: events\n"
    )
    strategy = "append" if variant == "append_all" else "delete+insert"
    model = (
        "{{ config(materialized='incremental', unique_key='order_id', "
        f"incremental_strategy='{strategy}') }}}}\n"
        "select order_id, event_ts, amount, ingestion_seq from {{ source('raw', 'events') }}\n"
    )
    if variant != "append_all":
        field = "ingestion_seq" if variant == "ingestion_watermark" else "event_ts"
        model += (
            "{% if is_incremental() %}\n"
            f"where {field} > (select coalesce(max({field}), 0) from {{{{ this }}}})\n"
            "{% endif %}\n"
        )
    (root / "models" / "subject.sql").write_text(model)
    (root / "models" / "oracle.sql").write_text(
        "{{ config(materialized='table') }}\n"
        "select order_id, event_ts, amount, ingestion_seq from {{ source('raw', 'events') }}\n"
    )
    return model


def replay(trace, variant, output, label, full_refresh=False):
    started = time.monotonic()
    history, captured = [], io.StringIO()
    with tempfile.TemporaryDirectory(prefix="jigsaw-dbt-") as directory:
        root = Path(directory)
        model = project(root, variant)
        db_path = str(root / "data.duckdb")
        with duckdb.connect(db_path) as connection:
            connection.execute(
                "create table events(order_id int, event_ts int, amount int, ingestion_seq int)"
            )
        sequence = 0
        for number, batch in enumerate(trace):
            with duckdb.connect(db_path) as connection:
                for key, timestamp, amount in batch:
                    sequence += 1
                    connection.execute("delete from events where order_id = ?", [key])
                    connection.execute(
                        "insert into events values (?, ?, ?, ?)", [key, timestamp, amount, sequence]
                    )
            args = [
                "run",
                "--project-dir",
                str(root),
                "--profiles-dir",
                str(root),
                "--no-use-colors",
                "--no-send-anonymous-usage-stats",
                "--quiet",
            ]
            if full_refresh:
                args.append("--full-refresh")
            with contextlib.redirect_stdout(captured), contextlib.redirect_stderr(captured):
                result = dbtRunner().invoke(args)
            if not result.success:
                (output / f"{label}.log").write_text(captured.getvalue())
                raise RuntimeError(f"dbt failed in {label}, batch {number}: {result.exception}")
            with duckdb.connect(db_path) as connection:
                actual = connection.execute(
                    "select * from subject order by order_id, ingestion_seq"
                ).fetchall()
                expected = connection.execute(
                    "select * from oracle order by order_id, ingestion_seq"
                ).fetchall()
                key_check = len(actual) == len({row[0] for row in actual})
                not_null = all(all(value is not None for value in row) for row in actual)
            history.append(
                {
                    "batch": number,
                    "actual": actual,
                    "expected": expected,
                    "equal": actual == expected,
                    "unique_not_null": key_check and not_null,
                }
            )
        # Paths in diagnostics are local scratch locations, not inputs or credentials.
        logs = captured.getvalue().replace(str(root), "<temporary-project>")
        (output / f"{label}.log").write_text(logs)
        (output / f"{label}.sql").write_text(model)
    return {
        "variant": variant,
        "full_refresh": full_refresh,
        "trace": trace,
        "history": history,
        "elapsed_seconds": round(time.monotonic() - started, 3),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    if (args.out / "results.json").exists():
        parser.error("Choose a fresh output directory to preserve previous attempts")
    started = time.monotonic()
    discovered = discover()
    output = {
        "data": "synthetic; seeded model defects; not production prevalence",
        "versions": {
            name: version(name) for name in ["dbt-core", "dbt-duckdb", "duckdb", "hypothesis"]
        },
        "python": platform.python_version(),
        "cases": {},
        "status": "partial",
    }
    for name, case in discovered.items():
        trace, variant = case["trace"], case["variant"]
        print(f"Replaying {name}: {len(trace)} batches", flush=True)
        result = {
            "source": case["source"],
            "discovered_trace": trace,
            "shrinking_claim": "Hypothesis minimized search; no pre-shrink size claimed",
        }
        result["incremental"] = replay(trace, variant, args.out, name)
        # Baseline uses the identical complete current-state input after each change.
        result["static_full_refresh"] = replay(trace, variant, args.out, name + "-static", True)
        result["corrected"] = replay(trace, "ingestion_watermark", args.out, name + "-corrected")
        output["cases"][name] = result
        (args.out / "results.json").write_text(json.dumps(output, indent=2) + "\n")
    smoke = [[(0, 1, 10)], [(1, 2, 20)]]
    output["ordered_smoke"] = replay(smoke, "event_watermark", args.out, "ordered-smoke")
    rng = random.Random(5745)
    controls = [
        [
            [(rng.randrange(4), rng.randrange(1, 9), rng.randrange(1, 21))]
            for _ in range(rng.randrange(2, 6))
        ]
        for _ in range(200)
    ]
    output["surrogate_control_traces"] = len(controls)
    output["surrogate_control_mismatches"] = sum(
        mismatch(simulate(trace, "ingestion_watermark")) for trace in controls
    )
    output["elapsed_seconds"] = round(time.monotonic() - started, 3)
    output["status"] = "complete"
    checks = {
        "all_five_defects_replayed": all(
            any(not h["equal"] for h in c["incremental"]["history"])
            for c in output["cases"].values()
        ),
        "all_static_full_refresh_pass": all(
            all(h["equal"] and h["unique_not_null"] for h in c["static_full_refresh"]["history"])
            for c in output["cases"].values()
        ),
        "all_corrected_replays_pass": all(
            all(h["equal"] for h in c["corrected"]["history"]) for c in output["cases"].values()
        ),
        "ordered_smoke_passes": all(h["equal"] for h in output["ordered_smoke"]["history"]),
        "under_30_minutes": output["elapsed_seconds"] < 1800,
        "generated_cases_at_most_four_batches": all(
            len(c["trace"]) <= 4 for c in discovered.values()
        ),
        "corrected_surrogate_controls_pass": output["surrogate_control_mismatches"] == 0,
    }
    output["checks"] = checks
    (args.out / "results.json").write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(checks, indent=2), flush=True)
    if not all(checks.values()):
        raise SystemExit("Benchmark did not meet the preregistered criteria")


if __name__ == "__main__":
    main()
