import io
import json
from urllib.error import HTTPError

import pytest

from opensource_jigsaw.github import GitHub, collect, diverse_limit
from opensource_jigsaw.models import Plan, Query


def item(name, **extra):
    return {
        "full_name": name,
        "html_url": f"https://github.com/{name}",
        "description": "Fixture",
        "stargazers_count": 100,
        "forks_count": 10,
        "topics": [],
        "license": {"spdx_id": "MIT"},
        "pushed_at": "2026-01-01",
        "private": False,
        "archived": False,
        "fork": False,
        **extra,
    }


def plan():
    return Plan(
        queries=[
            Query(field=f"field{i}", query=f"topic:field{i}", rationale="Coverage")
            for i in range(16)
        ]
    )


def test_collector_deduplicates_preserves_provenance_and_filters(tmp_path):
    class Client:
        retrieved_at = "2026-01-01T00:00:00Z"

        def get(self, path, params):
            assert "is:public fork:false archived:false" in params["q"]
            return {
                "items": [
                    item("shared/repo"),
                    item("secret/repo", private=True),
                    item("archived/repo", archived=True),
                    item("fork/repo", fork=True),
                ],
                "total_count": 4,
                "incomplete_results": False,
            }

    catalog = collect(Client(), plan(), tmp_path, per_query=100)
    assert list(catalog) == ["shared/repo"]
    assert len(catalog["shared/repo"].fields) == 16
    assert len(catalog["shared/repo"].queries) == 16


def test_pagination_includes_partial_last_page_and_balances_fields(tmp_path):
    calls = []

    class Client:
        retrieved_at = "2026-01-01T00:00:00Z"

        def get(self, path, params):
            calls.append(params)
            field = params["q"].split()[0].split(":")[1]
            page = params["page"]
            return {
                "items": [item(f"{field}/repo{page}-{i}") for i in range(100)],
                "total_count": 200,
                "incomplete_results": False,
            }

    catalog = collect(Client(), plan(), tmp_path, max_repos=2000, per_query=101)
    assert len(catalog) == 1616
    assert len(calls) == 32
    limited = diverse_limit(catalog, 16)
    assert len({r.fields[0] for r in limited.values()}) == 16


def test_request_cache_preserves_original_timestamp(tmp_path, monkeypatch):
    monkeypatch.setenv("GH_TOKEN", "synthetic-token")
    requests = []

    def open_request(req, timeout):
        requests.append(req)
        return io.BytesIO(json.dumps({"items": []}).encode())

    monkeypatch.setattr("opensource_jigsaw.github.urlopen", open_request)
    client = GitHub(tmp_path)
    assert client.get("/search/repositories", {"q": "topic:water"}) == {"items": []}
    timestamp = client.retrieved_at
    assert client.get("/search/repositories", {"q": "topic:water"}) == {"items": []}
    assert client.retrieved_at == timestamp and len(requests) == 1
    assert "synthetic-token" not in next(tmp_path.glob("*.json")).read_text()


def test_secondary_rate_limit_retries_then_succeeds(tmp_path, monkeypatch):
    monkeypatch.setenv("GH_TOKEN", "synthetic-token")
    delays = []
    responses = [
        HTTPError(
            "https://api.github.com/search/repositories",
            403,
            "rate",
            {},
            io.BytesIO(b'{"message":"secondary rate limit"}'),
        ),
        io.BytesIO(b'{"items":[]}'),
    ]

    def open_request(*args, **kwargs):
        response = responses.pop(0)
        if isinstance(response, Exception):
            raise response
        return response

    monkeypatch.setattr("opensource_jigsaw.github.urlopen", open_request)
    monkeypatch.setattr("opensource_jigsaw.github.time.sleep", delays.append)
    assert GitHub(tmp_path).get("/search/repositories") == {"items": []}
    assert delays == [60]


def test_permission_failure_is_not_retried(tmp_path, monkeypatch):
    monkeypatch.setenv("GH_TOKEN", "synthetic-token")

    def fail(*args, **kwargs):
        raise HTTPError("https://api.github.com/x", 403, "denied", {}, io.BytesIO(b"Forbidden"))

    monkeypatch.setattr("opensource_jigsaw.github.urlopen", fail)
    with pytest.raises(RuntimeError, match="HTTP 403"):
        GitHub(tmp_path).get("/x")
