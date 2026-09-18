# Public incremental-model validation evidence — follow-up

Observed 2026-09-18. These sources support further investigation of the paid validation workflow, not entrant demand or a changed score. No outreach occurred.

## Direct workflow and strong alternatives

- [Ryan Hawkins, CHOP migration interview](https://www.datafold.com/data-migration-guide/healthcare-data-migration-ryan-hawkins/): a named practitioner describes tracking refresh requirements across incremental dependencies while scaling from four to sixteen engineers; large reloads took hours. They built and maintained a custom validator and PR automation. This is vendor-hosted first-person evidence, and an explicit counterexample to assuming every buyer prefers buying a new validator. It supports orchestration/setup pain, not a claim that this fuzzer would have prevented the incidents.
- [Recce's session-base diagnosis](https://blog.reccehq.com/session-base-per-pr-why-data-reviews-lie): differently scoped CI and production histories can produce huge, unhelpful differences. Recce documents matched builds as its remedy. Any temporal fuzzer must freeze time/target/input contracts and abstain when full-refresh equivalence is inapplicable. It cannot count intentionally unequal histories as bugs.
- [Infinite Lambda incremental validation](https://github.com/infinitelambda/dbt-audit-helper-ext/blob/main/docs/validation-incremental-load.md): existing OSS automation uses two or sometimes three consecutive source snapshots and compares full/incremental behavior. This is a stronger baseline than only mocked unit tests. Source-history generation/minimization must add practical value over it.
- [Gnosis Cerebro](https://github.com/gnosischain/dbt-cerebro): its public operational documentation describes append-watermark misses after historical source backfills, and a targeted gap-window refresh remedy. Inspect exact code/license/adapter and history before using as a benchmark. It is not yet a reproduced bug in this research.

## Paid category and procurement scope

- [STP dbt health check](https://strattech.consulting/dbt-health-check/) sells structured code, architecture, testing and deployment review, including incremental strategies. No price or actual purchase of this narrower fuzzer was verified.
- [Northgrain consulting](https://northgraindata.com/services/dbt-consulting) offers audits, unit tests/contracts and incremental-model performance work. Its refund example demonstrates a vendor's sales explanation, not an independently documented customer incident or freely licensed benchmark.
- [Datafold/AstraZeneca case study](https://www.datafold.com/case-study/astrazeneca-informatica-to-dbt-cloud-migration/) reports a broad migration of about 800 workflows, most with complex incremental behavior, with named customer statements and automated parity validation. Its quoted competing timeline/budget apply to the whole migration, not the price/value of incremental fuzzing. Treat vendor-reported results as category evidence; do not convert them into this entrant's revenue forecast.

## Excluded impact claim

[Microsoft dbt-fabric #397](https://github.com/microsoft/dbt-fabric/issues/397) documents dropping a target before a failed recreation. A model-equivalence history generator does not inherently test transactional infrastructure failure. Do not count this as a detected/preventable incident unless a separate actual fault-injection protocol proves that capability.

## Practical question for the next experiment

Can an adapter consume eligible real models, generate and reduce histories without a model-specific handwritten surrogate, and return useful reproducible counterexamples with materially less fixture setup than the strongest existing snapshot/manual suite? Models outside the proven dialect, source-access, determinism and equivalence contract must be rejected explicitly. More variants of the original toy SQL do not answer this question.
