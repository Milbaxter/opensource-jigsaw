#!/usr/bin/env python3
"""Collect public GitHub repository metadata, using an existing gh login."""

import argparse
import datetime
import json
import subprocess
import time
from pathlib import Path


def request(query, per_field):
    command = [
        "gh",
        "api",
        "--method",
        "GET",
        "search/repositories",
        "-f",
        "q=" + query,
        "-f",
        "per_page=" + str(per_field),
        "-f",
        "sort=stars",
        "-f",
        "order=desc",
    ]
    for attempt in range(3):
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode == 0:
            return json.loads(result.stdout)
        rate_limited = "rate limit" in result.stderr.lower() or "HTTP 429" in result.stderr
        if not rate_limited or attempt == 2:
            raise RuntimeError(result.stderr.strip())
        time.sleep(65)
    raise RuntimeError("GitHub search failed")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--fields", type=Path, default=Path(__file__).with_name("fields.json"))
    parser.add_argument("--min-stars", type=int, default=50)
    parser.add_argument("--pushed-since", default="2025-03-01")
    parser.add_argument("--per-field", type=int, default=50)
    args = parser.parse_args()
    if not 1 <= args.per_field <= 100 or args.min_stars < 0:
        parser.error("per-field must be 1–100 and min-stars must be nonnegative")
    try:
        datetime.date.fromisoformat(args.pushed_since)
    except ValueError:
        parser.error("pushed-since must be YYYY-MM-DD")
    fields = json.loads(args.fields.read_text())
    if not isinstance(fields, dict) or not all(
        isinstance(k, str) and isinstance(v, str) for k, v in fields.items()
    ):
        parser.error("fields must be a JSON object mapping field names to search terms")
    args.output.mkdir(parents=True, exist_ok=True)
    for name in ["catalogue.json", "search-log.json"]:
        if (args.output / name).exists():
            parser.error("output already contains a capture; choose a new directory")
    records, searches = {}, []
    failures = 0
    for field, term in fields.items():
        query = (
            f"{term} is:public stars:>={args.min_stars} pushed:>={args.pushed_since} "
            "archived:false fork:false"
        )
        retrieved_at = datetime.datetime.now(datetime.UTC).isoformat()
        try:
            response = request(query, args.per_field)
        except RuntimeError as error:
            searches.append(
                {"field": field, "query": query, "retrieved_at": retrieved_at, "error": str(error)}
            )
            failures += 1
            print(f"{field}: failed: {error}", flush=True)
        else:
            excluded = 0
            for repo in response.get("items", []):
                if any(repo.get(flag) is not False for flag in ["private", "archived", "fork"]):
                    excluded += 1
                    continue
                name = repo["full_name"]
                license_info = repo.get("license")
                if name not in records:
                    records[name] = {
                        "full_name": name,
                        "html_url": repo["html_url"],
                        "description": repo.get("description"),
                        "stars": repo["stargazers_count"],
                        "topics": repo.get("topics", []),
                        "license": {
                            key: license_info.get(key) for key in ["spdx_id", "name", "url"]
                        }
                        if license_info
                        else None,
                        "pushed_at": repo["pushed_at"],
                        "language": repo.get("language"),
                        "fields": [],
                        "provenance": [],
                    }
                records[name]["fields"].append(field)
                records[name]["provenance"].append(
                    {
                        "query": query,
                        "retrieved_at": retrieved_at,
                        "source": "https://api.github.com/search/repositories",
                    }
                )
            searches.append(
                {
                    "field": field,
                    "query": query,
                    "total_matching": response["total_count"],
                    "fetched": len(response["items"]),
                    "incomplete_results": response["incomplete_results"],
                    "excluded_private_archived_fork_or_missing_flags": excluded,
                    "captured": len(response["items"]) - excluded,
                    "retrieved_at": retrieved_at,
                }
            )
            print(
                f"{field}: {len(response['items'])} rows; {excluded} excluded; "
                f"{len(records)} unique repositories",
                flush=True,
            )
        (args.output / "catalogue.json").write_text(json.dumps(list(records.values()), indent=2))
        (args.output / "search-log.json").write_text(json.dumps(searches, indent=2))
        # GitHub Search has a separate, lower rate limit than the core API.
        time.sleep(2.3)
    if failures:
        raise SystemExit(
            f"{failures} queries failed; inspect search-log.json before using the capture"
        )


if __name__ == "__main__":
    main()
