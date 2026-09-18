import pytest
from pydantic import ValidationError

from opensource_jigsaw.gate import decide
from opensource_jigsaw.models import Scores


def test_three_way_combination_passes_all_gates(case):
    decision = decide(*case)
    assert decision.accepted and decision.score == 90 and not decision.reasons


@pytest.mark.parametrize(
    "field,value",
    [
        ("verdict", "watch"),
        ("confidence", 0.79),
        ("demand_verified", False),
        ("differentiation_verified", False),
        ("integration_verified", False),
        ("license_compatible", False),
        ("fatal_flaws", ["Data unavailable"]),
    ],
)
def test_high_score_cannot_override_hard_gate(case, field, value):
    setattr(case[3], field, value)
    assert not decide(*case).accepted


def test_dimension_floor_blocks_high_average(case):
    case[3].scores = Scores(
        novel_synergy=10,
        buyer_pain=10,
        willingness_to_pay=10,
        feasibility=10,
        defensibility=6,
        distribution=10,
        evidence=10,
    )
    result = decide(*case)
    assert result.score == 96 and not result.accepted


def test_unknown_license_fails_closed(case):
    case[4]["water/model"].license = "NOASSERTION"
    assert not decide(*case).accepted


def test_readme_popularity_is_not_demand(case):
    case[1].evidence = [e for e in case[1].evidence if e.kind not in {"demand", "pricing"}]
    assert not decide(*case).accepted


def test_disconfirming_license_evidence_cannot_satisfy_source_gate(case):
    for evidence in case[1].evidence:
        if evidence.kind == "license":
            evidence.supports = False
    assert not decide(*case).accepted


def test_two_pages_from_one_publisher_are_insufficient(case):
    case[1].evidence[1] = case[1].evidence[0].model_copy()
    assert not decide(*case).accepted


def test_critical_unknown_or_critic_veto_blocks(case):
    case[1].unresolved_critical_assumptions = ["Buyer cannot provide needed data"]
    assert not decide(*case).accepted
    case[1].unresolved_critical_assumptions = []
    case[2].fatal_flaws = ["Existing product already implements the mechanism"]
    assert not decide(*case).accepted


def test_invented_or_repeated_components_rejected(case):
    case[0].components[0].repository = "invented/repo"
    assert not decide(*case).accepted
    case[0].components[0].repository = "math/solver"
    assert not decide(*case).accepted


def test_same_field_components_rejected(case):
    for repo in case[4].values():
        repo.fields = ["same field"]
    assert not decide(*case).accepted


@pytest.mark.parametrize("value", [11, -1, 9.1, "9", True])
def test_invalid_scores_are_never_coerced(case, value):
    values = case[3].scores.model_dump()
    values["evidence"] = value
    with pytest.raises(ValidationError):
        Scores.model_validate(values)
