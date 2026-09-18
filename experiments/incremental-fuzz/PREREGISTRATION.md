# Stateful incremental-model testing: preregistration

Registered before implementation or execution of this benchmark, 2026-09-18.

## Hypothesis and boundary

Property-based generation of ordered source changes, followed by execution of real dbt incremental materializations and comparison with a full-refresh oracle, can expose sequence-dependent data errors absent from a static full-refresh fixture and simple uniqueness/not-null checks. Hypothesis supplies generation/shrinking, dbt-duckdb supplies actual materialization, and DuckDB supplies isolated databases and exact row comparison.

This is a mechanism experiment using deliberately synthetic data and seeded model defects. It cannot estimate production bug prevalence, comparative commercial-product accuracy, support costs, buyer conversion, or warehouse-dialect fidelity. The expected behavior contract is current-state equality with a deterministic full refresh; history-preserving models are excluded.

## Inputs, cases, and controls

Synthetic order rows have a stable primary key, event timestamp, ingestion sequence, and amount. Trace actions append or correct source records, run a model, or replay an unchanged source. The trace generator is fixed before execution. Discovery cases are a late arrival, equal-watermark boundary, and repeated batch. Separately specified holdouts are an old-key correction and a same-timestamp correction; these were supplied by a different Astra researcher before implementation.

Compare on the same source histories:

1. A static full-refresh check plus standard primary-key/non-null invariants.
2. A hand-written ordered two-batch smoke test.
3. Generated ordered traces and exact incremental-versus-full-refresh equality checks.

Baselines are explicit local test strategies, **not** representations of the full capabilities of dbt, SQLMesh, Datafold, or any commercial platform. A competent engineer can write equivalent sequence tests; the potential advantage is generating and reducing those tests automatically.

Include both deliberately defective and corrected model variants. Record all variants and failures, including implementation failures and cases the generator misses. Preserve minimized traces, actual dbt outputs, full-refresh expected rows, installed versions, commands, and runtime. If a fast surrogate is used during generation, state its limitations and replay every claimed finding against actual dbt; never count a surrogate-only finding as successful integration.

## Prospective success and kill criteria

- Find and replay at least three distinct seeded temporal failures, including at least one holdout, using actual dbt materialization.
- At least two findings must pass the static full-refresh/key baseline on the same inputs before the temporal discrepancy is shown.
- A corrected implementation must produce no reported discrepancy on the same bounded generated/holdout corpus. This is not a proof of correctness.
- Export at least one reproducible reduced counterexample of no more than four operations/batches; report original versus reduced size if shrinking occurs. Do not call an already minimal generated trace “shrunk.”
- Complete the local experiment within 30 minutes of execution time and without external services or customer data. Record elapsed time rather than promising CI performance.
- Kill the technical claim if findings cannot be replayed in dbt, if the oracle is invalid for the contract, or if corrections merely suppress the checker. Do not change thresholds after observing results.

The broader v2 pursuit decision still requires independent research and judging against current alternatives, concrete commercial evidence, compatible exact-version licenses, and a bounded customer-validation plan.
