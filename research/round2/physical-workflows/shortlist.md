# C07: cartonization boundary counterexamples — proposal only

**Status:** selected for the cheapest falsification opportunity in this lane, not for a passing business or v2 score. No prototype has run. This document is a proposed experiment design, **not a published preregistration**. Parent must freeze/publish the final design before execution. Another agent must judge it because this lane proposed it.

## Narrow mechanism and buyer

Apply software property-based testing to package geometry and dimensional billing: perturb a packing plan within explicitly supplied manufacturing/measurement bounds, check physical containment plus declared billing rules, and shrink any failure into a reproducible minimal fixture. The output is a human-readable counterexample that a packing/WMS integration engineer can put into regression tests. It does not claim that a carrier invoice is incorrect, estimate a customer's savings, or certify transport safety.

Three OSS components have distinct proposed roles:

- [Hypothesis](https://github.com/HypothesisWorks/hypothesis): generates structured perturbations and simplifies failing examples; [current documentation](https://hypothesis.readthedocs.io/en/latest/).
- [Pint](https://github.com/hgrecco/pint): normalizes declared measurement units and rejects dimensionally invalid conversions; [tutorial](https://pint.readthedocs.io/en/latest/getting/tutorial.html).
- [trimesh](https://github.com/mikedh/trimesh): represents transformed product/carton boxes and independently recomputes spatial bounds; [box primitives](https://trimesh.org/trimesh.primitives.html), [bounds operations](https://trimesh.org/trimesh.bounds.html).

Top-level license evidence is recorded in `shortlist-license-evidence.json`: Hypothesis MPL-2.0 with explicitly noted exceptions, Pint a permissive BSD-style license, and trimesh MIT. Exact install versions, exceptions, transitive dependencies and delivery obligations must be checked before any experiment. No model weights or customer data are essential for a synthetic technical proof.

## Verified evidence; no inferred uniqueness

- [FedEx Singapore's dimension-weight FAQ](https://www.fedex.com/en-sg/customer-support/faq/invoices-and-payments/fees-and-charges/calculate-dimensional-weight.html) explicitly describes rounding each dimension upward and computing dimensional weight. Use this jurisdiction-specific published rule only; do not silently generalize to every carrier/service/date. [UPS's shipping-dimension guidance](https://www.ups.com/us/en/support/shipping-support/shipping-dimensions-weight) establishes that dimensions affect charges and service eligibility, without proving a customer has this bug.
- [Paccurate pricing](https://paccurate.io/pricing) advertises plans starting at $249/month. This supports a paid cartonization category, not willingness to buy an additional verifier.
- [Paccurate's API documentation](https://docs.paccurate.io/docs/on-demand-cartonization) already supports price thresholds and cost-aware box selection. [Its dimensional-data article](https://paccurate.io/posts/dimensional-data-accuracy-packing-efficiency) discusses bad SKU dimensions. Neither cost optimization nor awareness of measurement problems is new.
- [Shipware](https://shipware.com/solutions/invoice-audit-recovery/) already audits dimensional/weight charges. This proposal would target pre-shipment engineering fixtures, but demand for that difference remains unverified.
- [Packvium](https://packvium.com/) explicitly describes an independent validator, consistent physical units, and reachable unloading order. “Independent geometric validation” is therefore not unique. Its implementation and relevant terms need inspection before claiming a missing capability.
- [ISTA's services directory](https://www.ista.org/find_a_lab_or_services.php) provides an identifiable discovery channel for packaging businesses. Membership does not establish WMS expertise, receptiveness, or permission to send unsolicited messages.

## The strongest objection comes before the demo

For a fixed axis-aligned carton with monotonic dimensional tariffs, checking the upper interval endpoints can establish worst-case billed dimensions directly. There is no need for a fuzzer. A simple analytic interval/corner checker may equal or outperform this proposed combination with less code and a stronger guarantee.

Therefore **do not advance based on finding a threshold crossing missed by nominal inputs alone**. That would only demonstrate that uncertainty matters. The experiment must show a useful remaining capability against the analytic checker: for example, a faithful minimal reproduction of a failure through a real packing adapter with discrete box/rotation choices. If that requires inventing an unnecessarily complicated adapter or deliberately broken packing code, kill this hypothesis.

## Proposed preregistration contents

1. **Inputs:** rights-owned, clearly labeled synthetic packing-plan fixtures in an explicitly documented public-style schema. Include three geometry regimes (well inside limits, one threshold-adjacent, several discrete box/rotation choices), mixed valid units, unsupported units, boundary equalities, and empty/invalid geometry. Define realistic uncertainty intervals before generation; no claim that the intervals characterize an actual warehouse. Keep all fixtures, seeds and attempts.
2. **Baseline A:** nominal-input geometry and billing check. **Baseline B, mandatory:** exact unit normalization plus interval/corner analysis for monotonic fixed-carton cases. **Baseline C:** exhaustive small-case enumeration for discrete cases, used as the independent oracle. The candidate cannot claim superiority merely by outperforming A.
3. **Essential bridge:** normalized quantities enter actual geometry checks; resulting constraints and the declared billing rules drive Hypothesis; a failing example becomes a replayable artifact. Pin versions/commits and environment, log commands/outputs, retain failed runs. No screenshot-only evidence.
4. **Correctness criteria:** zero disagreements with exhaustive enumeration on the preregistered finite corpus; invalid units/data fail closed; no incorrect safe verdict in known unsafe cases. No random search may claim exhaustive safety.
5. **Added-value criterion:** candidate yields at least one independently confirmed, smaller replay fixture through a genuine adapter where Baseline B is insufficient, without sacrificing correctness; compare construction/replay time and artifact size against exhaustive enumeration and a hand-authored reduction script. Predefine the minimization ordering. “Small” alone is not a universal guarantee of global minimality.
6. **Kill criteria:** no additional actionable output beyond interval analysis; inferior clarity or effort to a simple reduction script; need for unavailable proprietary inputs; compatibility/license ambiguity; only artificial adapter bugs produce the improvement; or total implementation/debug time exceeds eight engineer-hours. Do not alter these after observing results.
7. **Budget and owner:** parent-designated engineer; eight hours maximum, zero paid APIs/cloud purchases, local-only computation. An eight-hour cap is a proposed allocation, not work already authorized or performed here.

## A separate commercial experiment would still be needed

If the technical proof passes, propose—with user authorization—a two-week exploratory trial to at most ten relevant packing integrators or consultants. Ask for a small, explicitly shareable historical plan and for comparison against their existing checks. Before any outreach, freeze a spend cap, minimum sample quality, and success criteria such as at least three completed workflow reviews, two genuinely new and accepted regression fixtures, and one stated willingness to pay for a bounded audit. These are hypotheses and proposed targets, not observations. Stop if existing checks already produce the same fixtures, the recipient cannot share usable plans, or expected service/support work overwhelms the offered price.

**Recommendation to parent:** spend first on the other lanes if they have cleaner comparative mechanisms. C07 is a useful bounded falsification target, but this research does not justify a high novelty, distribution, defensibility, or evidence score. No v2 gate has been waved through.

## Superseding bounded protocol

The generic tolerance proposal above is superseded by `preregistration.md`: a specific unmodified-engine non-monotonicity search with best-of-two sorting baseline, an independently verified constructive cheaper placement, and a narrowly versioned carrier fee component. No prototype has run at protocol preparation time. Parent publication must precede execution; no business score is assigned here.
