# C07 preregistration: carrier-fee-weighted packing regression witnesses

Status: **prospective protocol; no prototype executed**. Prepared 2026-09-18. Parent must publish this file in a timestamped commit before execution. Apply frozen pursuit rubric v2 (`af6fff8`, `docs/rubric-v2.md`); this protocol neither changes that rubric nor assigns a candidate score. It supersedes the generic tolerance proposal in `shortlist.md`.

## Claim and scope

Combine the unmodified **py3dbp 1.1.2** packing heuristic with **Hypothesis 6.168.0** generated/shrunk metamorphic tests and an original, narrowly scoped FedEx rule evaluator. Hypothesis produces related item lists; py3dbp produces carton decisions and placements; an independent exact geometry checker certifies a cheaper feasible witness; the rule evaluator labels a consequential fee boundary.

Hypothesis: shrinking one dimension of one item can change heuristic ordering/placement enough that **both supported volume sorting modes** fail to find an available cheap carton, despite a independently valid cheap-carton placement inherited from the larger-item case. The report would expose an avoidable *modeled fee component*, with a compact replay fixture suitable for an integrator's regression suite.

The comparator is the same unmodified engine, using the better result from both sorting modes. This is not a claim to beat Paccurate, prove global packing optimality, discover a new phenomenon in combinatorial heuristics, establish real warehouse incidence, or save a real invoice. A static carton fee calculator and ordinary endpoint bounds already solve important portions of this problem. Mere fee-threshold crossing, default-mode failure rescued by the other mode, invalid engine geometry, or a fabricated engine bug do not count.

## Inputs fixed before execution

All inputs are newly generated synthetic axis-aligned rigid cuboids; no customer data. All six orthogonal rotations are permitted. No fragility, stacking, load-bearing, dunnage, crush, or operational packing certification is modeled. Item weight is 0.5 lb each and carton tare is 1 lb. Use one carton per order only.

Four nested carton families, **outer dimensions in inches**, are fixed below. Packing inner dimensions are outer minus 0.25 inch on each axis, an explicitly synthetic wall allowance. Preserve inner/outer dimensions as separate fields. Do not bill inner dimensions.

| Family | Cheap outer | Larger outer | Intended charge boundary |
|---|---|---|---|
| A | 48 × 12 × 12 | 49 × 12 × 12 | Longest side |
| B | 30 × 30 × 7 | 31 × 31 × 7 | Second side and girth |
| C | 38 × 18 × 15 | 39 × 18 × 15 | Volume |
| D | 47 × 16 × 13 | 48 × 16 × 13 | Girth |

Dimensions and coordinates use integer quarter-inch ticks internally. Each generated case contains a family, 2–8 uniquely named items, an item index, an axis index, and a shrink amount. For each item's initial dimensions independently choose integers from 1 through that cheap carton's three inner-axis tick limits, then choose one of the six axis permutations. Index choices span all available items/axes. Shrink is 1–4 ticks, clamped to leave at least one tick. A selected dimension of one tick is an ineligible case, recorded without executing a zero shrink. Exclude initial total item volume below 20% or above 100% of cheap inner volume before engine execution; log exclusion counts. No filtering based on known heuristic failure and no hand-inserted failure fixtures. Preserve input item order.

The larger-item list is L; S changes only the selected dimension. The two lists share stable item IDs. Use the same input order for both, leaving sorting entirely to the engine.

## Engine and independent witness

Install exact package versions from the URLs/hashes in `c07-package-pins.json`; record the actual wheel/sdist hashes, Python version, OS, and transitive dependency lock. py3dbp's inspected repository is `enzoruiz/3dbinpacking`, MIT; GitHub HEAD was `31b9a40c78490da082bebde39a36e5327fb5191e`, but execution must use the separately pinned PyPI release. Its last observed push was 2023-12-14: established code, **not evidence of current maintenance**.

For every list/carton/mode create fresh Packer, Bin, and Item objects. Call `pack(bigger_first=MODE, distribute_items=False, number_of_decimals=3)` with one bin only. Run MODE false and true; do not reuse mutated items across bins or modes. Export raw item IDs, source dimensions, rotations, positions, fitted/unfitted IDs, and exceptions. Exceptions, unsupported rotations, duplicate/missing items, or invalid geometry are errors, never equivalent to a failure-to-fit result.

Among independently valid full fits, choose the smallest AHS dimension fee, breaking ties by modeled billable weight and then family carton order. If no fit exists, classify `no_fit`, not an arbitrarily expensive shipment. The interesting predicate requires:

1. L fits the cheap carton under at least one mode with independently valid geometry.
2. S fails cheap under **both** modes but has independently valid full placement in the larger carton under at least one mode.
3. Copy L's cheap placement, preserving every position and rotation, and replace the selected item's original axis length with its smaller value. An independently implemented checker verifies S in that same cheap carton.
4. The larger carton's narrowly modeled fee component exceeds the cheap carton's.

Implement the checker with exact integers and a separately written rotation permutation table. Require all item IDs exactly once, positive dimensions, nonnegative coordinates, containment, and pairwise nonoverlap on at least one axis. Face touching is allowed. Reject non-quarter-tick output rather than silently rounding it. Do not call py3dbp's collision, volume, or fit functions for this checker. A valid constructive placement proves this particular cheaper fit; no exhaustive optimality assertion follows.

## Search, comparison and shrinking

Use seeds **7000–7009**, in ascending order, independently for each method. Run two arms with the identical input domain and evaluation budget: (H) Hypothesis strategies/find with generation and shrinking; (R) standard-library pseudorandom generation without shrink-aware guidance. The strategies need not induce the same distribution; report that limitation. Do not use an existing Hypothesis example database. Each seed/arm permits up to 1,000 generated candidate evaluations, including duplicates/excluded cases; any shrinking evaluations are separately logged and capped at 1,000 per discovered candidate. Stop at the first witness per seed; continue all remaining seeds. Stop each arm after 600 seconds wall time, excluding installation and output writing; report actual coverage and time censoring. Total execution budget is at most eight engineer-hours and $25 compute; no paid services required.

Freeze implementation and record its hash before first engine execution. Log seed, arm, ordinal, full generated input or reproducible serialized representation, exclusions, classifications, elapsed time, and result hashes to a compressed JSONL trace. Retain every search outcome, error and failed search. Store full placement evidence for all candidate witnesses. Never keep only favorable seeds.

Shrink H witnesses within the unchanged domain and predicate. Report original versus reduced item count, sum of dimension ticks, and serialized byte count, without asserting a globally minimal witness. Replay every reduced candidate in a clean process. For each retained fixture, enumerate all legal 1–4 tick shrinks of every item axis around its L input, reporting all outcomes, to show its local neighborhood rather than only the selected transition.

Baselines reported on the same fixtures:

- Both single sorting modes and their best-of-two combination. A witness rescued by best-of-two fails the primary predicate.
- The uniform pseudorandom search arm at the same generation budget, with discovery count/time and no assumed Hypothesis speed advantage. If random is equally effective, say so.
- A static outer-dimension fee calculator plus an interval endpoint check. These correctly identify the declared carton fees and monotonic containment of the inherited witness. Do not misrepresent them as unable to verify the issue once a witness is known.
- An ordinary independent geometry validator on the selected larger-carton placement: it should accept that valid placement, illustrating why feasibility validation alone does not expose a cheaper feasible placement. This is a capability comparison, not a speed comparison or a comparison with all incumbent features.

## Fee oracle and predeclared controls

Use the FedEx U.S. **2026 Service Guide, updated September 11, 2026**, standard list U.S. domestic Zone 2 package scope. Record the fetched PDF hash and relevant page numbers; link it, do not republish it. Page 127 specifies dimension AHS thresholds (>48-inch longest side, >30-inch second side, >105-inch length plus girth, or >10,368 cubic inches) and $29.50 Zone 2 dimension AHS. Page 135 and the Ground terms provide upward fractional-inch rounding; calculate DIM with divisor 139 and round billable pounds upward, with the 40-lb dimension-AHS minimum. Outer axes are sorted after rounding. The output contains only AHS-dimension and modeled billable weight, **not total shipment cost**. Exclude negotiated rates, base transport charges, fuel, demand, residential, and other fees. Therefore do not label $29.50 as invoice savings or net margin.

Primary source: https://www.fedex.com/content/dam/fedex/us-united-states/services/Service_Guide_2026.pdf . An older generic FedEx dimensional-weight page still describes nearest-inch rounding; record this conflict and use the dated service guide for this versioned test.

Before search, controls must verify each cheap carton has zero dimension AHS, each larger carton has $29.50, exact-boundary versus just-over-boundary cases, and the 48.00 versus 48.01-inch rounding distinction. Also test: an exact inner-boundary fit; two face-touching boxes; an overlapping pair; an out-of-bounds item; duplicate/missing IDs; nonpositive input; all six rotations including the shrunk source axis. Fee/geometry controls may be synthetic known answers, but may not seed the engine search with an alleged failure. If a control fails, halt, correct the implementation, disclose the failed run, and hash the correction before restarting. Any change to the input domain, target predicate, budget, or success criteria requires a prospective protocol amendment and separate results.

## Outcomes and next decision

**Confirmed technical bridge:** at least one generated, reduced, clean-process replayed fixture satisfies all four predicate clauses, both baseline modes and all controls pass, and full input/placement/rule traces are retained. Report replication separately: distinct seeds and distinct carton families, deduplicating equal normalized fixtures. One witness establishes only one real heuristic counterexample under these assumptions. Zero witnesses within budget is an unsuccessful search, not proof of monotonicity. An engine geometry defect alone is a different result and does not satisfy this protocol.

**No automatic pursuit pass.** Independent Astra judging must still assess the narrow regression-service proposition against v2, including incumbent overlap, reachable budget owner, willingness to pay for this extra assurance, and durable value. Commodity test code may not support a business even if the bridge works. The researcher proposing C07 cannot provide its independent final judgment.

If technical evidence warrants a commercial experiment, proposed follow-on is an offline audit with WMS/cartonization integrators or parcel-shipping engineering teams, with no autonomous production changes. An independent owner must recruit three consenting teams via public partner/service directories and provide 100–1,000 deidentified orders per team, actual carton catalogs and applicable contract rules; synthetic data cannot substitute for this access gate. Proposed cap: three weeks, 24 engineer-hours priced at $100/hour plus $300 cash, maximum $2,700 total. Compare against each team's current rule-aware test workflow. Targets: at least two complete datasets, at least one independently confirmed consequential regression missed by that workflow, at least two hours saved per audit, and one explicit willingness to purchase a $500 repeat audit. Kill if access fails, no consequential regression is confirmed, integration exceeds eight hours per team, or no team accepts the paid repeat offer. These are proposed hypotheses/targets, not observed demand; proposed outreach is not permission to contact anyone.
