import pytest

from opensource_jigsaw.models import Critique, Ideas, Judgment, Research, Selection
from opensource_jigsaw.pipeline import analyze
from opensource_jigsaw.storage import read, save


class FakeAstra:
    def __init__(self, case, empty=False, fail_at=None):
        self.case = case
        self.empty = empty
        self.fail_at = fail_at

    def ask(self, task, payload, schema, *, web=False):
        idea, research, critique, judgment, catalog = self.case
        if schema is self.fail_at:
            raise RuntimeError("Budget exhausted")
        if schema is Selection:
            return Selection(repositories=list(catalog), reasoning="Synthetic selection")
        if schema is Ideas:
            return Ideas(ideas=[] if self.empty else [idea])
        assert web, "Every due-diligence stage must request live search"
        return {Research: research, Critique: critique, Judgment: judgment}[schema]


def test_end_to_end_three_components_and_reproducible_report(tmp_path, case):
    results = analyze(tmp_path, FakeAstra(case), case[4], candidates=1)
    assert len(results) == 1
    assert len(read(tmp_path / "accepted.json")) == 1
    assert read(tmp_path / "summary.json")["status"] == "complete"
    assert "90.0/100" in (tmp_path / "report.md").read_text()


def test_zero_candidates_is_success_not_fabricated_winner(tmp_path, case):
    assert analyze(tmp_path, FakeAstra(case, empty=True), case[4], candidates=1) == []
    assert read(tmp_path / "results.json") == []
    assert read(tmp_path / "accepted.json") == []
    assert read(tmp_path / "summary.json")["accepted"] == 0


def test_failure_never_leaves_old_winners_marked_complete(tmp_path, case):
    save(tmp_path / "accepted.json", [{"stale": True}])
    with pytest.raises(RuntimeError, match="Budget"):
        analyze(tmp_path, FakeAstra(case, fail_at=Critique), case[4], candidates=1)
    assert read(tmp_path / "summary.json")["status"] == "partial"
    assert read(tmp_path / "accepted.json") == []


def test_model_cannot_smuggle_unknown_repo_into_shortlist(tmp_path, case):
    class BadAstra:
        def ask(self, *args, **kwargs):
            return Selection(repositories=["fake/repo"], reasoning="Untrusted")

    with pytest.raises(ValueError, match="unknown repositories"):
        analyze(tmp_path, BadAstra(), case[4], candidates=1)
