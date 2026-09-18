from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field, HttpUrl, model_validator


class Record(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)


class Query(Record):
    field: str
    query: str
    rationale: str


class Plan(Record):
    queries: Annotated[list[Query], Field(min_length=16, max_length=64)]

    @model_validator(mode="after")
    def diversity(self):
        if len({q.field.casefold().strip() for q in self.queries}) < 12:
            raise ValueError("Discovery needs at least 12 distinct fields")
        return self


class Repository(Record):
    full_name: str
    url: HttpUrl
    description: str
    stars: int
    forks: int
    topics: list[str]
    license: str
    pushed_at: str
    fields: list[str]
    queries: list[str]
    retrieved_at: str


class Selection(Record):
    repositories: list[str]
    reasoning: str


class Component(Record):
    repository: str
    role: str
    necessity: str


class Idea(Record):
    title: str
    thesis: str
    components: Annotated[list[Component], Field(min_length=2, max_length=6)]
    buyer: str
    painful_workflow: str
    novel_mechanism: str
    business_model: str
    integration_plan: str
    cheapest_falsification: str


class Ideas(Record):
    ideas: list[Idea]


class Evidence(Record):
    url: HttpUrl
    title: str
    claim: str
    finding: str
    kind: Literal["demand", "pricing", "competitor", "technical", "license"]
    supports: bool


class Research(Record):
    evidence: list[Evidence]
    buyer_analysis: str
    competitive_analysis: str
    integration_analysis: str
    license_analysis: str
    unit_economics: str
    distribution: str
    unresolved_critical_assumptions: list[str]
    next_experiment: str


class Critique(Record):
    strongest_objections: list[str]
    existing_alternatives: list[str]
    evidence_gaps: list[str]
    fatal_flaws: list[str]
    what_would_change_my_mind: str


Score = Annotated[int, Field(ge=0, le=10)]


class Scores(Record):
    novel_synergy: Score
    buyer_pain: Score
    willingness_to_pay: Score
    feasibility: Score
    defensibility: Score
    distribution: Score
    evidence: Score


class Judgment(Record):
    verdict: Literal["pursue", "watch", "reject"]
    scores: Scores
    confidence: Annotated[float, Field(ge=0, le=1)]
    demand_verified: bool
    differentiation_verified: bool
    integration_verified: bool
    license_compatible: bool
    fatal_flaws: list[str]
    rationale: str
    disconfirming_evidence: str
    next_experiment: str


class Decision(Record):
    accepted: bool
    score: float
    reasons: list[str]


class Result(Record):
    idea: Idea
    research: Research
    critique: Critique
    judgment: Judgment
    decision: Decision
