# MEP access options: independent hold of the original prototype

**The original candidate does not pass v2. Hold commercial pursuit and preserve the experiment.** It misses its frozen comparative target and has an independently reproduced input-validation defect. No numerical score is needed to compensate for these failed noncompensable gates. This is a conclusion about the current evidence and implementation, not proof that contractor access-preparation services cannot be a business.

Independent Astra reviewer B, 2026-09-18. I did not propose or implement the candidate. I inspected original source SHA-256 `cd596f18d56048cc7a9b5378793d6f1f2276d5bf3952ad99fc816deeb23f854b`, the published protocol `4464c4d`, complete result files, original authored IFC files, commercial/prior-art sources and the reported deviations. Proposer artifacts were not changed.

## Comparative result

I independently recomputed the summary from individual outputs, excluding the two duplicate replay files:

| Measure | Observed |
|---|---:|
| Original and transformed-graph results | 69 |
| Found / no roadmap route | 45 / 24 |
| Randomized fixture runs | 36 across 12 fixtures |
| Wins over both prescribed baselines | **0** |
| No graph route despite a verified manual-proxy route | 12 |
| Found joint route more expensive than manual proxy | 10 |

The protocol required improvement over both the stronger greedy policy and the route proxy on at least three randomized fixtures, with the stated magnitude and no invalid paths. It achieved none. Roadmap sparsity matters: finite-graph optimality does not make the graph's route the best geometric option. The rotation-required and 0.91m opening cases had valid manually specified motions, but no successful roadmap route within the frozen budget. This is search failure, not infeasibility.

I separately verified all 71 completed result/graph pairs, including the two replays. The checker does **not import the prototype**. It reconstructs rectangular IFC extrusions and nested placements analytically, then compares them with actual IfcOpenShell mesher output. Maximum discrepancy was approximately `3.18e-14m`. It independently enumerates finite removal subsets, recomputes Dijkstra cost/length optima, checks selected edge-mask unions and one-time intervention costs, and checks found motions with a separate conservative arc-length displacement bound. All 47 found joint paths, 178 reported-valid manual paths and 94 greedy paths passed. All finite-graph optima agreed. These counts include replays; they are not additional independent discoveries.

Thus the original complete fixtures support successful IFC/OMPL/geometry/ID/cost integration and sound finite-graph outputs. The proposed comparative improvement was not demonstrated. No timing of an actual analyst, project-cost saving or purchase was observed.

## Independently reproduced input defect

In a separate in-memory probe, I removed the blocked fixture's wall classification entry from `metadata.interventions`, keeping both its actual IFC solid and its ID entry. `Scene` still parsed the wall, but constructed zero obstacles and accepted a straight path through it. The original files were unchanged. This violates the promised treatment of unclassified obstacles as forbidden. The parser also accepts NaN and positive-infinite intervention costs instead of rejecting them as unknown/nonfinite inputs.

The defect is not evidence that the 45 paths in complete original fixtures intersect their declared solids; the independent checks above found no such problem. It does mean the current importer cannot safely support the proposed customer-input study. In addition, source inspection shows it enumerates only `IfcBuildingElementProxy`, the class used by the synthetic author. It must not be described as covering arbitrary represented IFC classes. Unsupported represented geometry needs explicit rejection or actual parsing, rather than silently falling outside the obstacle inventory.

The first 30 geometry/unit/motion controls were frozen with the implementation. A separate helper for missing geometry, unknown units and bad costs was frozen at 09:02:53 UTC, after the first intact roadmap run. That was a disclosed sequencing deviation. It passed its five selected tests, but did not test the independently discovered coverage/nonfinite cases. Later tests do not retroactively become preregistered controls, and passing selected controls does not justify a general fail-closed claim.

## Gate assessment

- **Comparative mechanism / failure-and-baseline gates: fail.** Zero qualifying dual-baseline wins against the fixed success rule. Genuine library use alone does not satisfy the advantage requirement.
- **Customer-input readiness: blocked in this implementation.** Omitted classifications can erase real obstacles, and nonfinite costs are accepted. The proposed human-reviewed pilot still needs trustworthy input rejection; a disclaimer does not repair an omitted solid.
- **Executed integration: supported only within the complete, synthetic, planar fixtures.** The independent checks support this narrower finding and should be retained as a useful engineering artifact.
- **Paid category and plausible acquisition: supported.** Existing access-analysis services, contractor projects, BIM consulting prices and scan-to-BIM providers establish a real workflow and procurable inputs. These facts neither rescue a failed benchmark nor vanish because the prototype failed.

No endorsement of real equipment movement, rigging, structural adequacy or operational clearance follows from this study. The prototype models level rigid translation/yaw and declares geometry-only outputs; that appropriately bounded research use is distinct from customer-input correctness.

## Practical refinement versus moving on

Fixing the importer is justified before *any* future customer-file use, but is routine correctness work and cannot create the missing comparative advantage. More planner time, hand-designed greedy traps or retuned synthetic layouts would not establish buyer value. They should not be used to relabel this failed prospective result.

The business hypothesis can remain on a watch list: an integrator might value quicker IFC-linked alternatives, reliable clearance reporting, or repeatable cost worksheets even if a simple route strategy is adequate. The separate pre-result memo records [IMS's direct service](https://fl-ims.com/services/installation-path-interference-analysis), [a real Navisworks preparation workflow](https://www.autodesk.com/autodesk-university/class/4D-Machine-Installation-Using-Navisworks-2023), and [BIM integration rates](https://www.buildingsmartromania.org/en/consultanta). None measures the entrant's incremental labor benefit.

I recommend moving active discovery onward. Reopen this candidate only if a qualified contractor/integrator identifies a specific recurring preparation task that existing tools leave costly, supplies an authorized example and agrees to a concrete deliverable/value test. That would justify a freshly frozen study on new evidence, potentially using the simplest effective method. No customer contact is authorized or performed here. Known algorithms and existing suppliers are not the rejection reason; the failed declared comparison and unrepaired input boundary are.

## Reproduction

Use the exact environment/dependencies preserved with the original experiment. Both scripts take the experiment directory as their first argument:

```sh
python verify_results.py /absolute/path/to/experiment
python input_boundary_probe.py /absolute/path/to/experiment
```

`verify_results.py` reads all complete result/graph pairs present at invocation and checks analytic geometry, finite-graph objectives and reported valid paths. It does not regenerate OMPL roadmaps, validate every unused graph edge, or certify real geometry. `input_boundary_probe.py` loads the frozen implementation and replaces metadata reads only in memory; it writes only its own result file. Both emit results beside the verification script. Original source copies and hashes are included for publication/replay.
