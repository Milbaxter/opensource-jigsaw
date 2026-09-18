# Workload feasibility addendum —18 September2026

**HOLD the current partial-replica workload set before implementation.** This resolves the conditional question in SCREEN.md; it is not a failed performance experiment.

The independent workload audit by B found seven genuine ERA5 extraction requests in GeoscienceAustralia, ProjectPythia and Earthmover programs. Their combined float32 logical materialization footprint is46,364,868bytes (44.2MiB), including two global single-time maps and a deliberately conservative bound using the full allocated time axis for NYC history. The regional/point subsets total approximately36.3MiB. These are metadata-derived array extents, not compression ratios or timings. Source bytes read to construct them can still be much larger.

This set does not presently establish a useful joint budget-selection problem: straightforward request-specific materialization can retain every extracted cube at a modest budget, and caching reduced results can be smaller. There is no basis to invent a sub-44MiB cap, repeat frequency or query-arrival order to create a solver advantage. Known array layout methods and paid infrastructure remain valid market evidence; the proposed external solver is not justified by this workload set.

The source programs and exact data-access/rights audit are retained in B's `work/round6-workloads` packet. A future test would need a separately justified workload/budget constraint, then a prospective protocol and strong simple baselines. Production traffic is not a universal requirement; a richer authentic public program workload could suffice. No prototype, comparative evaluation, outreach or cloud purchase occurred.
