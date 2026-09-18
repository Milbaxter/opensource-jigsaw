from urllib.parse import urlparse

from .models import Critique, Decision, Idea, Judgment, Repository, Research

WEIGHTS = {
    "novel_synergy": 20,
    "buyer_pain": 20,
    "willingness_to_pay": 15,
    "feasibility": 15,
    "defensibility": 10,
    "distribution": 10,
    "evidence": 10,
}
MINIMUMS = {
    "novel_synergy": 9,
    "buyer_pain": 8,
    "willingness_to_pay": 8,
    "feasibility": 8,
    "defensibility": 7,
    "distribution": 7,
    "evidence": 8,
}
# A conservative first screen, not a substitute for checking each component's actual terms.
KNOWN_LICENSES = {
    "MIT",
    "Apache-2.0",
    "BSD-2-Clause",
    "BSD-3-Clause",
    "ISC",
    "MPL-2.0",
    "GPL-2.0",
    "GPL-3.0",
    "LGPL-2.1",
    "LGPL-3.0",
    "AGPL-3.0",
    "Unlicense",
    "CC0-1.0",
    "Zlib",
    "BSL-1.0",
    "EPL-2.0",
    "0BSD",
    "Artistic-2.0",
    "GPL-2.0-only",
    "GPL-2.0-or-later",
    "GPL-3.0-only",
    "GPL-3.0-or-later",
    "LGPL-2.1-only",
    "LGPL-2.1-or-later",
    "LGPL-3.0-only",
    "LGPL-3.0-or-later",
    "AGPL-3.0-only",
    "AGPL-3.0-or-later",
}


def idea_errors(idea: Idea, catalog: dict[str, Repository]) -> list[str]:
    names = [c.repository for c in idea.components]
    errors = []
    if len(set(names)) != len(names):
        errors.append("Repeated component")
    if any(name not in catalog for name in names):
        errors.append("Component missing from the scraped catalogue")
        return errors
    # Query labels are a discovery proxy; the judge must establish substantive distance.
    primary_fields = {catalog[name].fields[0] for name in names if catalog[name].fields}
    if len(primary_fields) < 2:
        errors.append("Components must originate in at least two discovery fields")
    return errors


def decide(
    idea: Idea,
    research: Research,
    critique: Critique,
    judgment: Judgment,
    catalog: dict[str, Repository],
) -> Decision:
    scores = judgment.scores.model_dump()
    score = round(sum(scores[k] * weight / 10 for k, weight in WEIGHTS.items()), 2)
    reasons = idea_errors(idea, catalog)
    if judgment.verdict != "pursue":
        reasons.append(f"Astra verdict: {judgment.verdict}")
    if score < 85:
        reasons.append(f"Weighted score {score} is below 85")
    for key, minimum in MINIMUMS.items():
        if scores[key] < minimum:
            reasons.append(f"{key}: {scores[key]} is below {minimum}")
    if judgment.confidence < 0.8:
        reasons.append("Confidence below 0.8")
    for key in (
        "demand_verified",
        "differentiation_verified",
        "integration_verified",
        "license_compatible",
    ):
        if not getattr(judgment, key):
            reasons.append(f"Unverified gate: {key}")
    if research.unresolved_critical_assumptions:
        reasons.append("Unresolved critical assumptions in the research")
    if critique.fatal_flaws or judgment.fatal_flaws:
        reasons.append("A critic or judge identified a fatal flaw")
    for c in idea.components:
        if c.repository in catalog and catalog[c.repository].license not in KNOWN_LICENSES:
            reasons.append(f"License needs manual verification: {c.repository}")
    evidence = research.evidence
    external_demand = {
        str(e.url)
        for e in evidence
        if e.supports
        and e.kind in {"demand", "pricing"}
        and urlparse(str(e.url)).hostname not in {"github.com", "raw.githubusercontent.com"}
    }
    if len(external_demand) < 2:
        reasons.append("Need two external sources supporting demand or willingness to pay")
    demand_hosts = {urlparse(url).hostname for url in external_demand}
    if len(demand_hosts) < 2:
        reasons.append("Commercial evidence needs two independent source domains")
    for kind in ("competitor", "technical", "license"):
        if not any(e.kind == kind and (kind == "competitor" or e.supports) for e in evidence):
            reasons.append(f"Missing {kind} evidence")
    return Decision(accepted=not reasons, score=score, reasons=reasons)
