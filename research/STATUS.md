# Research status

Updated 18 September 2026. **No combination has cleared the pursuit bar yet.** A pass would recommend a named, capped validation experiment under [rubric v2](../docs/rubric-v2.md), not establish profitability. The broad published crawl contains [2,246 distinct repository names](round2/broad-crawl-counts.json); only a subset received deep investigation. Source inspection, executed experiments, and formal scores are separate below.

## Active leads

| Combination | Question being tested | Current evidence |
|---|---|---|
| glTF/KTX/Three rendering + constrained optimization | Can per-texture codec/resolution choices improve rendered fidelity at fixed bytes? | [Two failed setup attempts](../experiments/render-budget/attempt-002/outcomes/RESULTS-ATTEMPT-002.md) retained: draw-order mismatch repaired, then actual writer alignment invalidated the size bound. Zero allocation quality/held-out renders. A third prospective repair is being reviewed. |

A [new native-build scheduling lead](round10/developer-workflows/source-screen.md) is at source/design review only. No compile benchmark or score.

## Executed experiments retained

| Combination | Observed result | Decision |
|---|---|---|
| FreeCAD adaptive machining + proposed game navigation | All 441 native replay comparisons matched, but the conservative subset had no eligible non-straight request. Detour never ran. | [Restricted screen failed](../experiments/cam-native-links/RESULTS.md); [follow-on held for funded competition](round10/cam-follow-on/FUNDED-BASELINE-REVIEW.md). |
| Hypothesis + dbt/DuckDB temporal regression tests | Reproduced generated merge/full-refresh discrepancies; independent replay and comparison documented. Later real-model examples were covered by fixed schedules. | [WATCH, 76/100](round2/dbt-independent-review/judgement.md); no pass. |
| Hypothesis + 3D carton packing | Five counterexamples across three carton families, independently geometry-checked. Buyer value and durable service advantage remain insufficient. | [WATCH, 76.5/100](round2/carton-independent-review/REVIEW.md); no pass. |
| LiDAR delivery checks | Independent holdouts exposed false positives and misses; corrections and an invalid original label retained. | [Failed comparison](../experiments/lidar-delivery/README.md). |
| Microscopy segmentation + review prioritization | Six mistakes corrected within ten reviews versus seven for simple margin ranking on the held-out set. | [Failed advantage gate](../experiments/assay-qc/RESULTS.md). |
| IFC maintenance access + motion planning | No qualifying win over both baselines on the synthetic fixture experiment; additional fail-open input defects found. | [Failed experiment](../experiments/mep-access/README.md). |
| Ultrasonic reconstruction + FINUFFT | Numerical checks passed; the known-target location check failed for the tested acquisition setup. No timing benchmark ran. | [HOLD with unresolved calibration](../experiments/ultrasonic-fmc/README.md). |
| Font shaping + proposed constraint-generated test corpus | Existing proof strings already covered 98/103 and 95/101 target lookups. Independent full replay confirmed too little headroom for the registered benefit. The solver was never run. | [Stage-zero rejection](../experiments/font-corpus/README.md). |

Unscored failures are not assigned invented numerical scores. A failed experiment remains failed even when it teaches a useful lesson. The [rubric audit](rubric-audit/AUDIT.md) allows useful integration of known methods and rejects unnecessary demands for a world-first algorithm; it retains the numerical threshold and evidence gates.

## Discovery records

[Initial research](initial/research.md) · [Live CLI validation](live-validation/README.md) · [Round two](round2/README.md) · [Round three](round3/README.md) · [Round four](round4/README.md) · [Round five](round5/README.md) · [Round six](round6/README.md) · [Round seven](round7/README.md) · [Round eight](round8/README.md) · [Round nine](round9/README.md) · [Round ten](round10/README.md)

Later screens include scientific-array caching, machinery diagnostics, FMU testing, document conversion, traffic planning, and invoice validation. Their source evidence and reasons for stopping are retained in the linked rounds. No external customers have been contacted and no purchases made.
