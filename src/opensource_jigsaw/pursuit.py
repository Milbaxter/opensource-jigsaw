"""Frozen v2 gate for independently reviewed, executed validation experiments."""

import hashlib
from pathlib import Path
from typing import Annotated, Literal
from urllib.parse import urlparse

from pydantic import Field, HttpUrl

from .gate import KNOWN_LICENSES, WEIGHTS
from .models import Decision, Evidence, Idea, Record, Scores

MINIMUMS = {
    "novel_synergy": 7,
    "buyer_pain": 8,
    "willingness_to_pay": 7,
    "feasibility": 8,
    "defensibility": 6,
    "distribution": 7,
    "evidence": 8,
}


class Check(Record):
    passed: bool
    reasoning: Annotated[str, Field(min_length=20)]
    references: Annotated[list[str], Field(min_length=1)]


class Gates(Record):
    problem_and_paid_category: Check
    comparative_mechanism: Check
    executed_bridge: Check
    failure_and_baseline_checks: Check
    rights_and_access: Check
    bounded_safe_use: Check
    economic_and_acquisition_experiment: Check


class Artifact(Record):
    role: Literal["protocol", "implementation", "results", "other"]
    path: str
    sha256: Annotated[str, Field(pattern=r"^[0-9a-f]{64}$")]


class Rights(Record):
    repository: str
    version: str
    license: str
    source: HttpUrl
    obligations: str


class Experiment(Record):
    owner: str
    buyer: str
    recruitment_channel: str
    sample_size: Annotated[int, Field(ge=1)]
    max_days: Annotated[int, Field(ge=1)]
    max_engineering_hours: Annotated[float, Field(gt=0, allow_inf_nan=False)]
    max_cash_usd: Annotated[float, Field(ge=0, allow_inf_nan=False)]
    baseline: str
    success_metrics: Annotated[list[str], Field(min_length=1)]
    kill_metrics: Annotated[list[str], Field(min_length=1)]
    limitations: Annotated[list[str], Field(min_length=1)]


class ScoreReasons(Record):
    novel_synergy: str
    buyer_pain: str
    willingness_to_pay: str
    feasibility: str
    defensibility: str
    distribution: str
    evidence: str


class PursuitReview(Record):
    rubric_version: Literal["v2"]
    candidate_id: str
    reviewer: str
    idea: Idea
    scores: Scores
    score_reasons: ScoreReasons
    confidence: Annotated[float, Field(ge=0, le=1)]
    confidence_basis: str
    recommendation: Literal["pursue_validation", "watch", "reject"]
    gates: Gates
    evidence: list[Evidence]
    rights: list[Rights]
    artifacts: list[Artifact]
    unresolved_blockers: list[str]
    remaining_hypotheses: list[str]
    experiment: Experiment


def assess(review: PursuitReview, root: Path) -> Decision:
    """Verify the frozen numerical gate and integrity of reviewed local evidence.

    Hashes establish artifact integrity, not whether an experiment actually happened.
    The independent reviewer must inspect/replay the evidence before attesting to each gate.
    """
    root = root.resolve()
    scores = review.scores.model_dump()
    score = round(sum(scores[name] * weight / 10 for name, weight in WEIGHTS.items()), 2)
    failures = []
    if review.recommendation != "pursue_validation":
        failures.append(f"Reviewer recommendation: {review.recommendation}")
    if score < 80:
        failures.append(f"Weighted score {score} is below 80")
    for name, floor in MINIMUMS.items():
        if scores[name] < floor:
            failures.append(f"{name}: {scores[name]} is below {floor}")
    if review.confidence < 0.75:
        failures.append("Confidence in the bounded experiment is below 0.75")
    for name, check in review.gates.model_dump().items():
        if not check["passed"]:
            failures.append(f"Failed gate: {name}")
    if review.unresolved_blockers:
        failures.append("Unresolved blockers prevent the proposed experiment")
    names = [component.repository for component in review.idea.components]
    if len(names) != len(set(names)):
        failures.append("Components must be distinct")
    for name in names:
        matches = [entry for entry in review.rights if entry.repository == name]
        if len(matches) != 1 or matches[0].license not in KNOWN_LICENSES:
            failures.append(f"Missing or unverified exact-version rights: {name}")
    supporting = [entry for entry in review.evidence if entry.supports]
    for kind in ["demand", "pricing", "technical", "license"]:
        if not any(entry.kind == kind for entry in supporting):
            failures.append(f"Missing supporting {kind} evidence")
    if not any(entry.kind == "competitor" for entry in review.evidence):
        failures.append("Missing competitor evidence")
    commercial_hosts = {
        urlparse(str(entry.url)).hostname
        for entry in supporting
        if entry.kind in {"demand", "pricing"}
    }
    if len(commercial_hosts) < 2:
        failures.append("Need commercial evidence from at least two source domains")
    for role in ["protocol", "implementation", "results"]:
        if not any(artifact.role == role for artifact in review.artifacts):
            failures.append(f"Missing benchmark artifact: {role}")
    for artifact in review.artifacts:
        path = (root / artifact.path).resolve()
        if Path(artifact.path).is_absolute() or not path.is_relative_to(root):
            failures.append(f"Artifact path escapes review root: {artifact.path}")
        elif not path.is_file():
            failures.append(f"Artifact missing: {artifact.path}")
        elif hashlib.sha256(path.read_bytes()).hexdigest() != artifact.sha256:
            failures.append(f"Artifact changed after review: {artifact.path}")
    return Decision(accepted=not failures, score=score, reasons=failures)
