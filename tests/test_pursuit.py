import hashlib

import pytest

from opensource_jigsaw.pursuit import (
    Artifact,
    Check,
    Experiment,
    Gates,
    PursuitReview,
    Rights,
    ScoreReasons,
    assess,
)


@pytest.fixture
def review(case, tmp_path):
    artifacts = []
    for role in ["protocol", "implementation", "results"]:
        path = tmp_path / f"{role}.txt"
        path.write_text(f"Synthetic fixture for {role}; not a real research result.")
        artifacts.append(
            Artifact(
                role=role, path=path.name, sha256=hashlib.sha256(path.read_bytes()).hexdigest()
            )
        )
    check = Check(
        passed=True,
        reasoning="Synthetic reviewed evidence for a unit test.",
        references=["results.txt"],
    )
    return PursuitReview(
        rubric_version="v2",
        candidate_id="synthetic",
        reviewer="Synthetic test reviewer",
        idea=case[0],
        scores=case[3].scores,
        score_reasons=ScoreReasons(
            **{name: "Synthetic reason" for name in case[3].scores.model_dump()}
        ),
        confidence=0.9,
        confidence_basis="Synthetic fixture",
        recommendation="pursue_validation",
        gates=Gates(**{name: check.model_copy() for name in Gates.model_fields}),
        evidence=case[1].evidence,
        rights=[
            Rights(
                repository=name,
                version="1.0",
                license="MIT",
                source=f"https://github.com/{name}/blob/v1.0/LICENSE",
                obligations="Retain notices",
            )
            for name in case[4]
        ],
        artifacts=artifacts,
        unresolved_blockers=[],
        remaining_hypotheses=["Customer conversion"],
        experiment=Experiment(
            owner="Test owner",
            buyer="Test buyer",
            recruitment_channel="Test",
            sample_size=3,
            max_days=14,
            max_engineering_hours=20.0,
            max_cash_usd=100.0,
            baseline="Current workflow",
            success_metrics=["Synthetic success metric"],
            kill_metrics=["Synthetic kill metric"],
            limitations=["No commercial outcome established"],
        ),
    )


def test_v2_does_not_require_proven_customer_conversion(review, tmp_path):
    decision = assess(review, tmp_path)
    assert decision.accepted and decision.score == 90


@pytest.mark.parametrize("gate", list(Gates.model_fields))
def test_every_hard_gate_blocks_even_with_high_scores(review, tmp_path, gate):
    getattr(review.gates, gate).passed = False
    result = assess(review, tmp_path)
    assert result.reasons == [f"Failed gate: {gate}"]


def test_changed_benchmark_cannot_keep_previous_approval(review, tmp_path):
    (tmp_path / "results.txt").write_text("Altered output")
    result = assess(review, tmp_path)
    assert not result.accepted
    assert "Artifact changed after review: results.txt" in result.reasons


def test_missing_protocol_blocks_pursuit(review, tmp_path):
    review.artifacts = [a for a in review.artifacts if a.role != "protocol"]
    assert not assess(review, tmp_path).accepted


@pytest.mark.parametrize("path", ["../outside.txt", "/tmp/outside.txt"])
def test_artifacts_cannot_escape_evidence_root(review, tmp_path, path):
    review.artifacts[0].path = path
    result = assess(review, tmp_path)
    assert any("escapes review root" in reason for reason in result.reasons)


def test_blocker_is_not_an_allowed_commercial_hypothesis(review, tmp_path):
    review.unresolved_blockers = ["No usable rights to essential dataset"]
    assert not assess(review, tmp_path).accepted


def test_passing_each_floor_alone_does_not_pass_total(review, tmp_path):
    from opensource_jigsaw.models import Scores
    from opensource_jigsaw.pursuit import MINIMUMS

    review.scores = Scores(**MINIMUMS)
    result = assess(review, tmp_path)
    assert result.score == 73.5 and not result.accepted


def test_noncommercial_component_is_not_fixed_by_high_score(review, tmp_path):
    review.rights[0].license = "CC-BY-NC-4.0"
    assert not assess(review, tmp_path).accepted
