# MEP access-options experiment: original result and critical limitations

**The components integrated, but this version did not meet the preregistered technical screen.** It showed no advantage over both strong baselines on any randomized fixture. Independent review also reproduced critical fail-open input behavior. Preserve this original experiment as an unsuccessful result; it is not a validation-ready product or a rigging/safety authorization.

Protocol commit: `4464c4d`. Original implementation SHA-256: `cd596f18d56048cc7a9b5378793d6f1f2276d5bf3952ad99fc816deeb23f854b`, frozen before fixture authoring and engine execution at 2026-09-18T09:01:13.794848+00:00. No algorithm, seed, domain, budget, or success-threshold changes were made during execution.

## Observed results

The harness authored 23 original synthetic IFC4 cases and reloaded their geometry through IfcOpenShell 0.8.5. OMPL 2.0.1 generated SE(2) PRM roadmaps with the fixed 2-second budget. Shapely 2.1.2 supported conservative interval-motion checks, followed by exact set-cost search and exhaustive subset comparisons on each retained finite graph.

| Observation | Result |
|---|---:|
| Ordinary case×seed roadmap runs | 66 |
| Additional transformed-graph unit/placement checks | 3 |
| Original roadmap runs with a verified selected path | 42 |
| Original runs with no roadmap route | 24 |
| Finite-graph oracle agreements, including transformed checks | 69/69 |
| Randomized case×seed runs | 36 across 12 fixtures |
| Randomized runs beating both manual-route proxy and best greedy baseline | **0/36** |
| Randomized fixtures with any such dual-baseline improvement | **0/12** |
| Runs where a valid manual proxy path existed but roadmap found none | 12 |
| Runs where joint cost exceeded manual proxy cost | 10 |
| Runs where joint beat manual proxy cost | 2; greedy tied joint in both |
| Runs where joint beat greedy cost | 1; manual proxy tied joint |
| Reported search-cap censoring / process errors | 0 / 0 |

The 24 no-roadmap-route results are not 24 proofs of physical impossibility. Twelve have independently checked manual candidate paths, including the rotation-required and narrow-but-feasible passage cases. The wholly spanning hard barrier and below-clearance controls are distinct geometric obstructions within the declared planar model. Every status remains in `execution/metrics.json`, with exact graphs, paths, subsets and console output.

Three transformed-graph checks preserved optimal costs after millimeter units, nested placement, translation and rotation. Two selected stored graphs were replayed in clean processes (`double/7400` and `random-7308/7401`) with matching results. Replaying stored graphs is deterministic; regenerating a wall-time-limited graph may produce different vertices on another host. The driver recorded 187.09 seconds across 65 remaining ordinary runs; the first intact run and three transformed-graph checks are separate. These are computational measurements, not analyst labor measurements.

## What the comparison actually says

The single-barrier case is an especially useful counterexample to overstating the solver: every seed selected cost 700 on its roadmap, while a declared manual route verified cost 200. The exact same-graph oracle agreed with 700 because the cheaper alternative was absent from that graph. Finite-graph optimization correctness does not establish adequate route coverage.

On `random-7305/7402`, joint search found 600 versus greedy 1000, but the manual proxy already found 600. On `random-7308/7401`, joint found 200 versus manual 1000, but the cost-aware greedy baseline also found 200. Neither qualifies as the required combined-method advantage. The original threshold—improvement over both baselines on at least 3 of 12 randomized fixtures—was missed without needing any interpretation of seed aggregation.

The method's output is conservative geometric preplanning for an idealized rigid object translating and yawing at fixed elevation. It is not full 6DOF handling, a continuous-space optimality proof, or a physical route certificate. Conservative checks concern only the geometry supplied and modeled clearance assumptions. They exclude rigging, structural capacity, stability, workers, service connections and operational execution decisions. Intervention costs are arbitrary synthetic scenario inputs, not contractor quotations or savings.

## Critical independent input failures

A separate Astra reviewer tested the original frozen code without editing its files. The probe is preserved in `independent-input-probe.json` and its source in `independent-input-probe.py.txt`.

1. An obstacle remained in parsed IFC geometry and the metadata ID map, but its intervention-classification entry was omitted. The scene then contained zero modeled obstacles and accepted a straight path through the blocked wall. This violates the requirement that unclassified geometry be forbidden or rejected.
2. NaN and positive-infinity intervention costs were accepted. The check only rejected values that compare as nonpositive; nonfinite numbers escaped it.

The original generated fixtures had complete classification and finite positive costs, so these probes do not rewrite their numerical results. They nonetheless trigger the protocol's critical failure condition and block use of this version for a pilot. A further code-review limitation is that the importer enumerates `IfcBuildingElementProxy`, the class used by these synthetic files; general IFC element-class coverage is not established and must never be implied for arbitrary as-built inputs.

The initial harness ran 30 geometry/unit controls successfully. It omitted explicit execution of five planned input-rejection checks (unknown units, missing geometry, null/zero/negative costs). A separately frozen helper ran those after the first intact roadmap and before the remaining runs; all five passed. This is disclosed in `input-control-freeze.json`. They did not test missing classification or nonfinite costs and therefore did not catch the later independent failures. There was no retrospective correction of the original code.

## Economic interpretation and next decision

There is a real existing workflow. [C&S](https://www.cscos.com/projects/chiller-replacement-and-plant-upgrades/) describes scanning an existing chiller facility for replacement work, and [MaRS](https://scantobimsolutions.com/services/mep-bim-modeling.html) explicitly offers removal-route/access modeling. [buildingSMART Romania](https://www.buildingsmartromania.org/en/consultanta) posts hourly prices for skilled BIM work. These sources support purchasable inputs and a paid adjacent category; none measures the proposed tool's labor benefit or establishes demand for it.

[IMS](https://fl-ims.com/services/installation-path-interference-analysis) is a direct paid service alternative. The [2016 BIM/OMPL work](https://www.iaarc.org/publications/fulltext/ISARC2016-Paper008.pdf) and [minimum-constraint-removal research](https://ojs.aaai.org/index.php/AAAI/article/view/12100) are relevant prior art. Their existence does not kill an implementation or service opportunity, but there must still be an evidenced practical advantage. Entire HVAC contract values and installation hours must not be presented as analysis costs saved.

Research recommendation: **hold this proposition, with independent final judgment separate.** Route seeding or more planning time could fix known coverage problems, and input validation must be corrected before reuse. But those improvements alone would not establish differentiated paid value: the best simple baseline already matched every observed favorable result. Another synthetic fixture designed to defeat greedy would not resolve that commercial gap. A fresh experiment is justified only by a concrete buyer workflow failure, with an honest current-workflow baseline and a capped test of setup effort, coverage or cost. No customer access, outreach, paid order, conversion, retention or profitability was established.

## Artifacts and replay

Publish the source mapping in `publish-manifest.json` (the actual file count is recorded there; do not infer it from prior experiments). It includes all original IFCs, generator inputs, exact roadmaps, outcomes, failures, controls, hashes, source and license provenance. No third-party binaries, README copies, license text, papers or source PDFs are republished.

Use a Python 3.12 environment with `requirements-executed.txt`. From the experiment root, replay a retained graph:

```sh
python prototype.py replay --case double --seed 7400 --graph execution/double-7400-graph.json.gz
```

The small launcher loads byte-preserved `prototype-original.py.txt`; the original code validates its frozen hash. This is forensic reproduction of an explicitly failed experimental version, not recommended operational software. The source mapping preserves original filenames/hashes without silently reformatting the frozen implementation. Do not run `run_remaining.py` over the original evidence directory if you intend to retain its first-run outputs.
