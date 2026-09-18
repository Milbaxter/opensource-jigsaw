import pytest

from opensource_jigsaw.models import (
    Component,
    Critique,
    Evidence,
    Idea,
    Judgment,
    Repository,
    Research,
    Scores,
)


@pytest.fixture
def case():
    catalog = {}
    for name, field in [
        ("water/model", "water"),
        ("math/solver", "optimization"),
        ("geo/maps", "geospatial"),
    ]:
        catalog[name] = Repository(
            full_name=name,
            url=f"https://github.com/{name}",
            description="Test fixture",
            stars=500,
            forks=30,
            topics=[field],
            license="MIT",
            pushed_at="2026-01-01T00:00:00Z",
            fields=[field],
            queries=[f"topic:{field}"],
            retrieved_at="2026-01-02T00:00:00Z",
        )
    idea = Idea(
        title="Synthetic test hypothesis",
        thesis="Synthetic, not a research finding",
        components=[
            Component(repository=n, role="A necessary capability", necessity="Required")
            for n in catalog
        ],
        buyer="Utility operations",
        painful_workflow="Planning",
        novel_mechanism="Synthetic mechanism",
        business_model="Subscription",
        integration_plan="Connect input/output adapters",
        cheapest_falsification="Pilot",
    )
    evidence = [
        Evidence(
            url=url,
            title=kind,
            claim="Synthetic claim",
            finding="Synthetic evidence",
            kind=kind,
            supports=True,
        )
        for url, kind in [
            ("https://buyer.example/need", "demand"),
            ("https://market.example/price", "pricing"),
            ("https://competitor.example/product", "competitor"),
            ("https://github.com/water/model", "technical"),
            ("https://github.com/water/model/blob/main/LICENSE", "license"),
        ]
    ]
    research = Research(
        evidence=evidence,
        buyer_analysis="Synthetic",
        competitive_analysis="Synthetic",
        integration_analysis="Synthetic",
        license_analysis="Synthetic",
        unit_economics="Assumed",
        distribution="Synthetic",
        unresolved_critical_assumptions=[],
        next_experiment="Pilot",
    )
    critique = Critique(
        strongest_objections=[],
        existing_alternatives=[],
        evidence_gaps=[],
        fatal_flaws=[],
        what_would_change_my_mind="Pilot",
    )
    judgment = Judgment(
        verdict="pursue",
        scores=Scores(
            novel_synergy=9,
            buyer_pain=9,
            willingness_to_pay=9,
            feasibility=9,
            defensibility=9,
            distribution=9,
            evidence=9,
        ),
        confidence=0.9,
        demand_verified=True,
        differentiation_verified=True,
        integration_verified=True,
        license_compatible=True,
        fatal_flaws=[],
        rationale="Synthetic",
        disconfirming_evidence="Synthetic",
        next_experiment="Pilot",
    )
    return idea, research, critique, judgment, catalog
