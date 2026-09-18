import argparse
import shutil
import subprocess
import sys
from datetime import UTC, datetime
from pathlib import Path

from pydantic import ValidationError

from .astra import Astra
from .models import Result
from .pipeline import analyze, catalog_from, discover, report
from .pursuit import PursuitReview, assess
from .storage import read, save


def main():
    parser = argparse.ArgumentParser(
        description="Find rare, evidence-backed open source combinations"
    )
    parser.add_argument(
        "command", choices=["doctor", "run", "discover", "analyze", "report", "assess"]
    )
    parser.add_argument("--review", type=Path, help="Independent v2 review JSON for assess")
    parser.add_argument("--evidence-root", type=Path, default=Path("."))
    parser.add_argument(
        "--out", type=Path, default=Path("runs") / datetime.now(UTC).date().isoformat()
    )
    parser.add_argument("--max-repos", type=int, default=3000)
    parser.add_argument("--per-query", type=int, default=100)
    parser.add_argument("--candidates", type=int, default=16)
    parser.add_argument(
        "--max-model-calls",
        type=int,
        default=100,
        help="New Astra calls per invocation; cached calls are free",
    )
    parser.add_argument("--timeout", type=int, default=900, help="Seconds allowed per Astra call")
    args = parser.parse_args()
    try:
        if args.command == "doctor":
            for tool in ("gh", "codex"):
                if not shutil.which(tool):
                    raise RuntimeError(f"Missing {tool}; see README setup")
            for command in (["gh", "api", "user", "--jq", ".login"], ["codex", "login", "status"]):
                subprocess.run(command, check=True)
            print(
                "Tools and authentication ready. Astra access is checked on the first model call."
            )
            return
        if args.max_model_calls < 1 or args.timeout < 1:
            raise ValueError("Model call budget and timeout must be positive")
        if args.max_repos < 2 or not 1 <= args.per_query <= 1000:
            raise ValueError("--max-repos must be >=2; --per-query must be 1..1000")
        if not 1 <= args.candidates <= 100:
            raise ValueError("--candidates must be 1..100")
        args.out.mkdir(parents=True, exist_ok=True)
        if args.command == "assess":
            if args.review is None:
                raise ValueError("assess requires --review and a completed independent v2 review")
            review = PursuitReview.model_validate_json(args.review.read_text())
            decision = assess(review, args.evidence_root)
            save(
                args.out / "pursuit-decision.json",
                {
                    "rubric_version": "v2",
                    "candidate_id": review.candidate_id,
                    **decision.model_dump(),
                },
            )
            print(decision.model_dump_json(indent=2))
            return
        if args.command == "report":
            results = [Result.model_validate(r) for r in read(args.out / "results.json")]
            summary = read(args.out / "summary.json")
            report(
                args.out,
                catalog_from(args.out / "catalog.json"),
                results,
                complete=summary["status"] == "complete",
            )
        else:
            astra = Astra(args.out / "astra-cache", args.max_model_calls, args.timeout)
            if args.command in {"discover", "run"}:
                catalog = discover(args.out, astra, args.max_repos, args.per_query)
            else:
                catalog = catalog_from(args.out / "catalog.json")
            if args.command in {"run", "analyze"}:
                analyze(args.out, astra, catalog, args.candidates)
        print(f"Saved to {args.out.resolve()}")
    except (
        RuntimeError,
        ValueError,
        OSError,
        ValidationError,
        subprocess.CalledProcessError,
    ) as exc:
        print(f"jigsaw: {exc}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
