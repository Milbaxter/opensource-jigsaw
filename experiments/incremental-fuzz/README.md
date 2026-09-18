# Real incremental materialization + generated counterexamples

**Technical mechanism demonstrated; no pursuit decision implied.** Synthetic source histories, intentionally defective model variants, and a declared current-state contract isolate the mechanism. No production bug rate or business outcome is established.

The frozen [preregistration](PREREGISTRATION.md) predates execution. Hypothesis searches and minimizes ordered event batches in a fast Python surrogate. Every reported counterexample is then replayed through **actual dbt-duckdb materializations**, while a separate dbt table model rebuilds the full-refresh oracle from the same current source. The output records actual and expected rows after every batch.

## Observed results

Five scenario families reproduce a discrepancy: late arrival, equal-watermark arrival, repeated source replay, old-key correction, and same-timestamp correction. The same source histories pass full-refresh and basic key/non-null checks. Four incremental scenarios also retain unique, non-null keys while silently losing or retaining stale data; the repeated-append defect is additionally caught by uniqueness testing. A conventional ordered two-batch smoke test passes the defective event-watermark model.

All five counterexamples stop failing with the tested ingestion-watermark correction under this benchmark's monotonic ingestion-sequence contract. Two hundred additional generated **surrogate-only** control traces pass; they are not represented as real dbt executions. Deletes, history-preserving semantics, schema changes, multi-table relationships, concurrent writes, cloud adapters and production-scale runtimes remain untested.

### Attempt history

- [Run 1](run1/results.json) executed successfully. Inspection revealed a **case-labeling error**: the supposed late-arrival classifier could compare against a timestamp introduced in the same batch, so its counterexample was actually an equal-watermark defect. The mismatch was real, but it did not establish the intended third scenario family. Original output is preserved.
- The classifier was corrected to compare only against previous batches. [Run 2](run2/results.json) reran the unchanged preregistered case families and thresholds; all checks passed. Its late-arrival trace now tests a genuinely older timestamp than the preceding batch's watermark. No model fix or success threshold was changed to obtain this result.

Hypothesis returns two-batch counterexamples here. We do not claim a measured percentage reduction from an unrecorded initial trace. Exact dependency versions, elapsed time, intermediate SQL, and raw observed rows are saved with each run.

## Reproduce

Use Python 3.11 and a separate environment:

```sh
python3.11 -m venv .venv-benchmark
.venv-benchmark/bin/pip install -r experiments/incremental-fuzz/requirements.txt
.venv-benchmark/bin/python experiments/incremental-fuzz/benchmark.py --out runs/dbt-proof
```

Existing output directories containing `results.json` are rejected to preserve attempts. The run uses synthetic local data and disables dbt usage telemetry. Inspect `results.json`; its `checks` must all be true. This is a bounded experiment, not a general data testing product.

## Competitive boundary

The [research dossier](../../research/round2/developer-workflows/dossier-incremental.md) identifies strong substitutes and **exact conceptual prior art** in dblect's multi-step replay roadmap. Local DuckDB testing is already present in current dbt documentation. The potential narrow implementation advantage is automatic temporal trace generation and reduction followed by actual successive materializations—not inventing property-based testing, local dbt tests, or the full-refresh oracle. A capable engineer can write equivalent tests manually. This benchmark does not compare implementation effort or performance against a completed competitor system.
