import json
import subprocess
from pathlib import Path
from types import SimpleNamespace

import pytest
from pydantic import ValidationError

from opensource_jigsaw.astra import Astra, output_schema
from opensource_jigsaw.models import Evidence, Research, Selection


def test_wire_schema_supports_structured_output_but_urls_remain_validated():
    assert '"format": "uri"' not in json.dumps(output_schema(Research))
    with pytest.raises(ValidationError):
        Evidence(
            url="file:///secret",
            title="Invalid",
            claim="x",
            finding="x",
            kind="demand",
            supports=True,
        )


def test_cached_responses_do_not_consume_budget(tmp_path, monkeypatch):
    calls = []
    monkeypatch.setattr("opensource_jigsaw.astra.shutil.which", lambda _: "/bin/codex")
    monkeypatch.setenv("GH_TOKEN", "never-forward-this")

    def run(command, **kwargs):
        calls.append(command)
        assert "GH_TOKEN" not in kwargs["env"]
        assert command[command.index("--model") + 1] == "gpt-6-astra"
        assert command[command.index("--sandbox") + 1] == "read-only"
        Path(command[command.index("--output-last-message") + 1]).write_text(
            json.dumps({"repositories": ["a/b"], "reasoning": "Fixture"})
        )
        return SimpleNamespace(returncode=0, stderr="")

    monkeypatch.setattr("opensource_jigsaw.astra.subprocess.run", run)
    astra = Astra(tmp_path, max_calls=1)
    first = astra.ask("Select", {}, Selection)
    assert astra.ask("Select", {}, Selection) == first
    assert len(calls) == 1
    with pytest.raises(RuntimeError, match="budget reached"):
        astra.ask("A different request", {}, Selection)


def test_invalid_model_response_is_not_cached(tmp_path, monkeypatch):
    monkeypatch.setattr("opensource_jigsaw.astra.shutil.which", lambda _: "/bin/codex")

    def run(command, **kwargs):
        Path(command[command.index("--output-last-message") + 1]).write_text('{"wrong":true}')
        return SimpleNamespace(returncode=0, stderr="")

    monkeypatch.setattr("opensource_jigsaw.astra.subprocess.run", run)
    with pytest.raises(ValidationError):
        Astra(tmp_path).ask("Select", {}, Selection)
    assert list(tmp_path.glob("*.json")) == []


def test_timeout_is_actionable_and_does_not_claim_success(tmp_path, monkeypatch):
    monkeypatch.setattr("opensource_jigsaw.astra.shutil.which", lambda _: "/bin/codex")

    def timeout(*args, **kwargs):
        raise subprocess.TimeoutExpired("codex", 1)

    monkeypatch.setattr("opensource_jigsaw.astra.subprocess.run", timeout)
    with pytest.raises(RuntimeError, match="timed out"):
        Astra(tmp_path, timeout=1).ask("Select", {}, Selection)
