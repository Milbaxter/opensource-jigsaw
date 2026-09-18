# R2-B01 — Stateful incremental-model regression campaigns

Research decision: **strongest candidate in this branch; no pass declared**. The parent is running the essential integration experiment. A bounded paid validation study is more plausible than a defensible standalone platform. Newness is a focused implementation and delivery wedge, not an invented testing technique.

## Narrow buyer and purchase

Buyer hypothesis: the delivery lead of a dbt consultancy with several customer projects containing incremental revenue/order marts, or an analytics engineering manager responsible for those marts. Sell an initial adapter-specific correctness audit with replayable regression fixtures. Do not initially promise arbitrary Snowflake/BigQuery semantics from a DuckDB execution.

The recurring workflow is a PR changing incremental filters, unique keys, aggregation grain, or merge configuration. A clean CI database can pass while a populated target diverges on a second run. Proposed output: the smallest admissible sequence of input batches and dbt invocations that causes incremental output to disagree with a full-refresh oracle, followed by an executable regression artifact.

Paid-category evidence is real but product conversion is untested: [Recce's current pricing](https://reccehq.com/pricing/) offers a Team tier at $250/month billed annually for 1,000 agent reviews and unlimited custom checks. [Datafold pricing](https://www.datafold.com/faq/how-does-datafolds-pricing-work/) sells validation in a platform and separately for migrations. Its [CHG customer story](https://www.datafold.com/case-study/chg-healthcare-mysql-to-snowflake-migration/) reports a planned $10,000/week consulting budget for a much larger migration; this is a vendor-published customer account, not a price for this proposed tool. The initial audit price should be tested, not inferred from those numbers.

Accessible validation population: [dbt's consulting partner directory/program](https://www.getdbt.com/partners), the public practitioners in issue discussions, and maintainers of public dbt adapter projects. These are identifiable prospective interview/audit participants, not opted-in customers. No contact was made.

## Verified pain and the precise gap

- [dbt discussion #5745](https://github.com/dbt-labs/dbt-core/discussions/5745) explicitly asks for generated input tests of properties including incremental idempotence and commutativity. It establishes a practitioner request, not broad market size.
- [dbt #8664](https://github.com/dbt-labs/dbt/issues/8664) remains open: testing output after insert/merge/delete+insert materialization. Its example is a partitioned incremental daily active user model.
- [Current dbt unit test documentation](https://docs.getdbt.com/docs/build/unit-tests), inspected September 18 and marked updated September 16, supports overriding `is_incremental()` and mocking `this`. It tests rows to be inserted/merged, and explicitly does not test the resulting merged target. It also offers experimental local DuckDB unit tests. Thus neither “dbt cannot test incremental logic” nor “local DuckDB tests are new” is defensible.
- [Discussion #10226](https://github.com/dbt-labs/dbt-core/discussions/10226) describes testing isolated states without transitions. The original asker later says the suggested workaround appears sufficient for their corner cases. Preserve this counterevidence.
- [SQLMesh comparisons](https://sqlmesh.readthedocs.io/en/stable/comparisons/) documents why a max-date pattern misses historical gaps and offers interval tracking. This supports a technical failure mode while also identifying a substantive alternative.

## Essential OSS bridge

1. **Hypothesis** supplies generated operation sequences and shrinking, transferring state-machine/differential testing from application libraries to analytical materialization. [Stateful API](https://hypothesis.readthedocs.io/en/latest/stateful.html).
2. **dbt Core + dbt-duckdb** must execute real full-refresh and incremental materialization macros. Merely reimplementing a merge in Python would fail the essential-bridge gate.
3. **DuckDB** provides isolated persisted targets and a second database/schema for full-refresh oracle execution. Compare bags of rows, not sets, so duplicate failures remain visible.

Minimal generator contract: model selection; unique/business key; event timestamp and optionally ingestion/update timestamp; valid ranges/nullability; permitted lateness; whether old records can change; permitted duplicate delivery; exact compared columns; equality tolerances if any. This contract makes generated examples meaningful. Full-refresh equality is inappropriate for intentionally history-preserving or non-equivalent models; those must be excluded or require a different property.

Adapter flow: generate immutable batch trace → reset isolated state → load first batch → run dbt full-refresh once → load later batches and call ordinary `dbt run` after each → build a fresh oracle from the same accumulated admissible source state → compare outputs → ask Hypothesis to shrink a failing trace → persist input CSV/JSON, SQL/model digest, dependency versions, dbt commands, and diff.

Run recipe for a parent prototype: create a Python 3.11+ venv; install pinned `dbt-duckdb`, `duckdb`, `hypothesis`; create one actual dbt project with a seed/source and an incremental model; use `dbtRunner().invoke(...)` or subprocess calls; close DuckDB connections before invoking dbt; reset target/oracle separately per test; store the shrunk trace. Exact versions and measured output belong to the parent's demo, not this research dossier.

## Baselines and adversarial cases proposed before demo results

Do not compare only with no testing. Report both ordinary fresh-database CI and a modest hand-written two-batch regression suite. The latter is a serious low-cost substitute.

Pre-register success as at least one extra real materialization failure detected beyond the fixed suite within a bounded runtime, deterministic replay of the minimized trace, and no failures on repaired positive controls under the same admitted inputs. Measure setup time and run count; a fuzzer slower to configure than four fixture tests may have no saleable advantage.

Candidate heldout failure families: a distinct event arriving at exactly the previous watermark; an old event corrected with a newer ingestion timestamp; replay of an already-delivered batch; a late changed dimension affecting old facts; a partition refresh that removes/replaces the wrong grain. These were proposed independently of the parent's result. Do not label intentionally disallowed late arrivals as defects. Wrong append/merge configuration can be useful, but it is not evidence of a deep algorithmic discovery.

An additional benchmark should mutate real public models, retain their documented assumptions, and compare detection against dbt unit tests, a hand-authored integration harness, and available dblect checks. Synthetic demonstrations establish plumbing and mechanism, not prevalence or ROI.

## Competitor audit, including adverse evidence

| Alternative | Inspected capability | Consequence |
|---|---|---|
| Native dbt unit tests | Fixed mock inputs, incremental/full branches, experimental local execution | Strong free baseline; materialized multi-run sequence generation is the narrower distinction |
| Hand-written dbt integration tests | User can seed, run twice, compare tables using ordinary CLI/Python | This is often sufficient; reduce setup and shrinking effort to justify purchase |
| SQLMesh | Fixed input/output tests, generated tests from query results, tracked intervals, gap filling, dbt compatibility with adjustments | Can prevent several proposed defects; no claim that it lacks incremental support. [Tests](https://sqlmesh.readthedocs.io/en/stable/concepts/tests/), [dbt integration](https://sqlmesh.readthedocs.io/en/stable/integrations/dbt/) |
| Datafold | Value-level production/development comparison and CI integration | Can catch output differences on available data; inspected pages do not establish automatic adversarial multi-run generation. [Deployment testing](https://www.datafold.com/data-deployment-testing/) |
| Recce | Base/current environment diffs, custom queries/checklists, paid CI agent | Existing review/distribution surface; our trace could be a plugin, not another review platform. [Cloud vs OSS](https://docs.reccehq.com/whats-recce/cloud-vs-oss/) |
| Elementary | Anomaly, schema, custom Python/data tests and paid test-coverage agents | Arbitrary custom tests could host this harness. Do not claim theoretical incapability. [Test documentation](https://docs.elementary-data.com/data-tests/introduction) |
| Soda | Data contracts, rule/schema verification, CI/API execution | Established data-quality budget; not the same generated temporal test in inspected docs. [Data testing](https://docs.soda.io/data-testing) |
| **dblect** | Static semantic checks; real dbt/DuckDB harness; dual incremental compilation; runtime Hypothesis/replay roadmap | **Closest and material prior art.** Generic combination novelty is disproven; see below |
| Lineage Fuzzer | Deterministic synthetic fault campaign, observed/control coverage and restoration | Adjacent recent proof that metadata-driven data fault testing is already being built. [Creator's project](https://devpost.com/software/lineage-fuzzer) |

The dblect source was cloned at commit `8ebf61e9ad2c5b50484f6a63941503b177061b5d`. Its [current capabilities](https://github.com/dvryaboy/dblect/blob/8ebf61e9ad2c5b50484f6a63941503b177061b5d/docs/current_state/capabilities.md) separates shipped static checks and the DuckDB harness from the unshipped runtime half. Its [decisions](https://github.com/dvryaboy/dblect/blob/8ebf61e9ad2c5b50484f6a63941503b177061b5d/questions_and_decisions.md) explicitly include Duplicate, LateRow, replay/shrinking, and multi-step incremental state machines deferred from v1. That is conceptual overlap even before shipment. A focused working implementation can still be commercially useful, but cannot be called a new discovery. An extension of dblect with paid adapter testing/support is a plausible revised wedge.

## License and packaging evidence

Primary license texts were retrieved and hashed in `components.json`: Hypothesis is **MPL-2.0**, despite GitHub's `NOASSERTION`; DuckDB MIT; dbt-duckdb and dbt Core Apache-2.0. A separately authored harness can combine these under their respective terms; retain notices and account for MPL-covered files if modifying/distributing them. Do not relabel all dependencies MIT. This is a component-level compatibility finding, not an audit of a final lockfile/container. dblect is Apache-2.0. Optional SQLGlot is MIT.

Current Soda Core main is Elastic License 2.0 and VeriEQL is CC-BY-NC-SA-4.0; neither should be treated as ordinary permissive OSS components for this commercial bundle. They are not required by this candidate. Archived Datafold data-diff is not necessary either.

## Scores and falsification

Pre-demo conservative score: novelty 7, pain 8, payment 7, feasibility 8, defensibility 5, distribution 7, evidence 8 = **72.5/100**. Confidence 0.78 in this research decision. It does **not** currently clear the 80 threshold or defensibility floor. Positive execution could improve feasibility/evidence; it cannot erase dblect prior art or prove payment. A consultancy wedge may improve defensibility through adapter corpus/support and project access, but these assets do not exist yet.

Next bounded validation: recruit 3–5 willing consulting leads; select ten eligible real incremental models; measure new useful defects, setup/runtime, false positives, and whether minimized fixtures shorten diagnosis versus their current tests. Ask for paid audit commitments rather than feedback-only enthusiasm. Stop if native/manual tests are comparably cheap, no additional meaningful failures appear, or prospective buyers see this only as a free framework feature. The experiment is accessible without private production rows, but representative model/configuration access still requires agreement.
