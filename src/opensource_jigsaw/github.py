import hashlib
import json
import os
import subprocess
import time
from collections import defaultdict, deque
from datetime import UTC, datetime
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from .models import Plan, Repository
from .storage import read, save


class GitHub:
    def __init__(self, cache: Path):
        self.cache = cache
        self.retrieved_at = ""
        self.token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
        if not self.token:
            auth = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True)
            if auth.returncode:
                raise RuntimeError("Run gh auth login or set GH_TOKEN before scraping")
            self.token = auth.stdout.strip()

    def get(self, path: str, params: dict | None = None) -> dict:
        if not path.startswith("/") or ".." in path or ":" in path:
            raise ValueError("Expected a GitHub REST API path")
        url = "https://api.github.com" + path
        if params:
            url += "?" + urlencode(params)
        key = hashlib.sha256(url.encode()).hexdigest()
        cached = self.cache / f"{key}.json"
        if cached.exists():
            stored = read(cached)
            self.retrieved_at = stored["retrieved_at"]
            return stored["data"]
        request = Request(
            url,
            headers={
                "Authorization": f"Bearer {self.token}",
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
                "User-Agent": "opensource-jigsaw/0.1",
            },
        )
        for attempt in range(6):
            try:
                with urlopen(request, timeout=45) as response:
                    data = json.load(response)
                self.retrieved_at = datetime.now(UTC).isoformat()
                save(cached, {"retrieved_at": self.retrieved_at, "data": data})
                return data
            except HTTPError as exc:
                message = exc.read().decode("utf-8", errors="replace").lower()
                rate_limited = exc.code == 429 or (
                    exc.code == 403
                    and (
                        exc.headers.get("X-RateLimit-Remaining") == "0"
                        or exc.headers.get("Retry-After") is not None
                        or "rate limit" in message
                    )
                )
                if not rate_limited and exc.code not in {500, 502, 503, 504}:
                    raise RuntimeError(f"GitHub HTTP {exc.code} for {path}") from None
                if attempt == 5:
                    raise RuntimeError(f"GitHub retry budget exhausted for {path}") from None
                reset = 0
                if rate_limited and exc.headers.get("X-RateLimit-Remaining") == "0":
                    reset = float(exc.headers.get("X-RateLimit-Reset", "0")) - time.time() + 1
                delay = max(2**attempt, float(exc.headers.get("Retry-After", "0")), reset)
                if rate_limited:
                    delay = max(60, delay)
                if delay > 300:
                    raise RuntimeError("GitHub quota exhausted; rerun later to resume") from None
                time.sleep(max(1, delay))
            except (URLError, TimeoutError):
                if attempt == 5:
                    raise RuntimeError(f"GitHub connection failed for {path}") from None
                time.sleep(2**attempt)
        raise RuntimeError("Unreachable retry state")


def diverse_limit(catalog: dict[str, Repository], maximum: int) -> dict[str, Repository]:
    groups = defaultdict(deque)
    for repo in catalog.values():
        groups[repo.fields[0]].append(repo)
    selected = {}
    while len(selected) < min(maximum, len(catalog)):
        for group in groups.values():
            if group and len(selected) < maximum:
                repo = group.popleft()
                selected[repo.full_name] = repo
    return selected


def collect(
    client: GitHub, plan: Plan, out: Path, max_repos: int = 3000, per_query: int = 100
) -> dict[str, Repository]:
    if not 1 <= per_query <= 1000 or max_repos < 2:
        raise ValueError("per_query must be 1..1000; max_repos must be at least 2")
    catalog: dict[str, Repository] = {}
    audit = []
    finished = set()
    # Round-robin pages prevents the first fields consuming the entire crawl budget.
    for page in range(1, (per_query + 99) // 100 + 1):
        for index, query in enumerate(plan.queries):
            if index in finished:
                continue
            q = f"{query.query} is:public fork:false archived:false"
            data = client.get(
                "/search/repositories",
                {
                    "q": q,
                    "sort": "stars",
                    "order": "desc",
                    "per_page": 100,
                    "page": page,
                },
            )
            retrieved = client.retrieved_at
            audit.append(
                {
                    "query": q,
                    "field": query.field,
                    "page": page,
                    "total_count": data.get("total_count"),
                    "incomplete_results": data.get("incomplete_results", False),
                    "retrieved_at": retrieved,
                }
            )
            items = data.get("items", [])[: min(100, per_query - (page - 1) * 100)]
            if len(data.get("items", [])) < 100:
                finished.add(index)
            for item in items:
                if any(item.get(flag) is not False for flag in ("private", "archived", "fork")):
                    continue
                name = item["full_name"]
                if name in catalog:
                    if query.field not in catalog[name].fields:
                        catalog[name].fields.append(query.field)
                    if q not in catalog[name].queries:
                        catalog[name].queries.append(q)
                    continue
                catalog[name] = Repository(
                    full_name=name,
                    url=item["html_url"],
                    description=item.get("description") or "",
                    stars=item["stargazers_count"],
                    forks=item["forks_count"],
                    topics=item.get("topics", []),
                    license=(item.get("license") or {}).get("spdx_id") or "UNKNOWN",
                    pushed_at=item["pushed_at"],
                    fields=[query.field],
                    queries=[q],
                    retrieved_at=retrieved,
                )
            retained = diverse_limit(catalog, max_repos)
            save(out / "catalog.json", [r.model_dump(mode="json") for r in retained.values()])
            save(out / "crawl.json", audit)
            print(f"Scraped {query.field}: {len(catalog)} unique repositories", flush=True)
    return diverse_limit(catalog, max_repos)
