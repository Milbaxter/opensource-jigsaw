# Independent attempt002 completion and alignment review

2026-09-18. Read-only inspection of the frozen protocol/source, pinned writer source and retained outputs. No new serialization, encoding, rendering, allocation, or held-out inspection. Hashes and raw GLB layout facts are in STATIC-EVIDENCE.json.

## Recorded outcome and exposure

Attempt002 at9d0a19c9793276cdfae1185421c520df997609d3 **self-aborted** on `Serialized conservative size bound violated`. This occurred in a first5MB preset size check, before a configuration quality render. The failure record reports795.375 effective seconds,220.883 actual new wall seconds and574.492 original preprocessing seconds. The parent did not cause this stop.

All18 retained SpatialPack recipes completed in198.491 seconds with no reported comparator failure. The smallest emitted artifact was5,459,160 bytes, above all three frozen ceilings. Every record is rejected for bytes. This is completion of the frozen restricted recipe frontier, not proof that no SpatialPack configuration/product can fit. Actual source-to-GLB controls, byte sizes, original materials/images and authored-control outcomes have been exposed. The logged configuration and SpatialPack-quality event counts are both0. No selection seal or held-out record exists. Two FlightHelmet cells were recorded as writer-family-infeasible from the nonimage floor; no candidate quality result is known.

## Completion semantics verdict

The prose instructs the comparator to reject over-budget outputs and select the best feasible output. It defines advantage against the strongest baseline among feasible cells and requires integrity/byte checks. It does not explicitly state that every method must find a feasible output. Conversely, the published code is declared authoritative and implements `complete = rows.length === 5 && ...`, requiring all five outputs. The disagreement is therefore real. It is not appropriate to silently reinterpret attempt002 or retroactively pass it.

A **prospective code/text clarification is defensible** before quality/held-out exposure. This is nevertheless a post-exposure amendment prompted by the known vendor byte frontier; disclose that fact. It is not an independent fresh preregistration of those feasibility observations. The byte-bound failure already makes the historical attempt unsuccessful regardless of the completion ambiguity.

The following general rule is sound if fixed before another run:

1. Record each method as completed-with-feasible-output, completed-with-no-feasible-output, failed/censored, or unexecuted. Reaching the algorithm's declared configuration budget normally is a completed bounded search; a wall-time/resource cap or missing required comparator is not.
2. Require all prescribed method runs to complete without errors/censoring. A fully enumerated finite comparator with every output over the ceiling may be complete with no feasible output. A heuristic's exhausted search with no output is a search outcome, not a mathematical global infeasibility certificate.
3. A quality-comparable cell requires an actual feasible candidate and at least one actual feasible baseline. Compare against the strongest feasible baseline, preserving every other method's status and its byte frontier. Do not assign an invented zero or infinite quality error to an absent output, and do not count a feasibility-only gain as a quality win.
4. Preserve all frozen cells. Candidate failure, missing controls, a failed/censored method, or no quality comparator cannot be quietly dropped to obtain a global pass. Structurally excluded cells need the same previously specified writer-family justification, reported separately from universal infeasibility.
5. Keep all algorithms, assets, budgets, configuration limits, views,15% relative/.001 absolute thresholds,10% regression bound, and two-assets requirement unchanged. No new smaller vendor recipe, mesh simplification, relaxed integrity check or extra search budget is justified by this amendment.

No fresh quality holdout is strictly required for this narrow repaired-harness comparison: no quality outcomes or held-out views have been used to choose algorithms or thresholds, and the protocol already allows preserved prospective bug repair before held-out evaluation. The resulting conclusion must be labelled an amended case study with both failed attempts disclosed. It cannot be claimed as an unchanged original-protocol pass. If further repairs use observed selection quality to alter search choices or success rules, a fresh preregistration/independent confirmation becomes necessary; after held-out exposure, the protocol itself requires a new split.

## Independent byte-alignment diagnosis

Pinned `@gltf-transform/core` package version4.5.0, `dist/index.js` around4987–4996, appends each image and then pads the **absolute cumulative binary cursor** to a multiple of8. The frozen bound subtracts sum(round4(image bytes)) from original BIN length, calls the remainder nonimage bytes, and assumes that remainder is invariant. Its CP-SAT image coefficients also use round4. This is a genuine arithmetic/model error: representation padding varies with image-length residues and was incorrectly embedded in the supposed invariant geometry floor.

Merely replacing round4 with round8 while retaining a residual computed from the original image layout is insufficient. Independent parsing of the four retained originals gives:

| Asset | First image offset | Offset mod8 | BIN−sum(round8(payload)) |
|---|---:|---:|---:|
| BoomBox |207816|0|207816|
| FlightHelmet |3227148|4|3227152|
| ToyCar |3664368|0|3664368|
| WaterBottle |149412|4|149408|

WaterBottle's residual is four bytes **below its real nonimage prefix**. The first-image padding depends jointly on the prefix and payload residue. This confirms the corner case is present in the actual workload, not a hypothetical extension.

For a proven fixed prefix P followed by images with no variable interleaved/trailing data, a safe conservative BIN bound is `ceil8(P) + sum(ceil8(image_size))`. The true nonimage floor is P (plus any independently verified fixed suffix), not the original padding-contaminated residual. Alternatively model the exact first-image cursor and subsequent padded contributions. Maintain four-byte JSON/GLB chunk padding where the file format requires it; image-section alignment is the separate pinned-writer behavior.

Before another execution, inspect/validate the assumed image bufferView order, actual unpadded lengths, contiguous image section, fixed prefix/suffix, and topology across all source models and serialization probes. Add explicit residue0–7 controls with both aligned and unaligned prefixes, including this WaterBottle case; verify exact-size upper bounds across codec combinations and JSON digit/extension changes. Use the same proved image costs in the solver. A violated invariant must still stop rather than add an arbitrary slack constant.

This report diagnoses the frozen source and specifies review conditions. It does not certify a repair not yet supplied, score the candidate, or establish useful quality improvement. Any new source must be independently checked and frozen before execution.
