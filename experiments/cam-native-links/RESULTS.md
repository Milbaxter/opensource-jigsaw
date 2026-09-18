# CAM native headroom screen: HOLD

The registered screen returned **HOLD_INSUFFICIENT_HEADROOM**. Its restricted, full-endpoint-clearance subset contained no non-straight routing problem. No Detour implementation or commercial pursuit pass follows from this run.

This result covers one actual CC BY 4.0 upstream FreeCAD regression fixture, with three planar footprints and two explicit stepover settings. It is not a full FreeCAD/OCC job replay or a customer manufacturing workload. It does not show that FreeCAD generally has no linking bottleneck.

## What passed

- All 22 independently specified geometry/topology/input controls passed.
- All six traced native output structures matched each of three untraced full-kernel runs: 18 whole-kernel equality comparisons.
- All 147 recorded native ResolveLinkPath requests replayed three times: 441 matching success/failure outcomes. The 129 successful requests also had identical path coordinates and Clipper Z tags in all 387 successful replays. The 18 failed proposals matched their failure outcome; a partial failed path was not an equivalence endpoint.
- Native source/binary/input freezes remained unchanged. There were no native errors, equality failures, runtime resource aborts or unplanned missing workloads in the repaired run.

## Measured observations

| Fixed native configuration | Requests | Median native CPU (s) | Median native wall (s) | Eligible full endpoints |
|---|---:|---:|---:|---:|
| Upper face, 20% stepover | 26 |0.222315|0.223082|4|
| Upper face, 75% stepover |4|0.078182|0.078605|0|
| Lower face with hole, 20% |27|0.765240|0.771016|0|
| Lower face with hole, 75% |10|0.177595|0.178359|1|
| Projected union with hole, 20% |59|2.871388|2.893443|2|
| Projected union with hole, 75% |21|0.313445|0.321271|6|

Across all requests, the sum of median isolated native replay CPU was 2.875791 s, versus 4.428165 s summed whole-kernel median CPU. The roughly 65% ratio is an **isolated-call profile**, not a demonstrated achievable whole-kernel speedup or a measured additive timing decomposition. It justified proceeding past the prospective cheap negative bound. There were 18 native failed proposals across four configurations; proposals may be discarded by the enclosing engagement selection, so those failures do not equal 18 actual retracts.

The conservative geometric screen then found:

- 126 requests had an endpoint inside an eroded hole rather than the retained center-space component.
- 8 had eroded boundary topology rejected by the frozen simple/disjoint-boundary rules.
- 13 passed full endpoint eligibility. All 13 had an already-clear direct segment; together their isolated replay CPU was 0.000798 s. Their components also exceeded the planned 128-vertex graph scope cap.

Thus there were **zero eligible non-straight requests**, zero recovered proposals and zero real-request visibility-graph solves. The small synthetic graph control did execute as part of the 22 controls. All exclusions were recorded; no endpoint clearance, topology rule, input, cap or threshold was changed in response.

Acquisition, native controls and replay took 30.252 s of harness wall time; geometric screening took 14.164 s. Cumulative observed peak RSS was 33,898,496 bytes. Native CPU/wall timing is separated from trace logging, process polling and geometric screening overhead.

## Environment failure and prospective repair

The original published runner stopped before the first control/native call because macOS rejected RLIMIT_AS in preexec. Its zero-workload HOLD_CONTROL_OR_RESOURCE attempt remains unchanged in `results/`. A separate diagnostic confirmed the unsupported limit setting. Parent published the environment-only repair before the second attempt: owned-process-group RSS polling plus endpoint ru_maxrss checks, with unchanged 2 GiB threshold, inputs, binaries, controls and decision rules. Polling is explicitly not an instantaneous hard VM guarantee.

Prospective source/protocol commit: 355bc51. Prospective resource-only repair commit: 1e34584. Original source freeze:61e3d41ab66bb47d4fe06403db0e6c31a3544ad76c8439dd80af7117c41c0c73. Repaired execution freeze:3dff738ca63f16f068adcaabea693bc452e130ac4420a2df063ec250ddee7c27. Repaired execution began 2026-09-18T11:47:43Z.

## Interpretation and possible next work

The full-endpoint policy successfully avoided ambiguous native lead-in/out exceptions, but excluded almost all costly requests. It cannot answer whether an adapter preserving the native trimmed-endpoint policy would help. The native source's existing roadmap anticipates endpoint connectors. Investigating that bridge would require a separately frozen, source-justified endpoint mapping and full enclosing-kernel comparison, including lead extension/smoothing and strong simple routing. The present 147 requests can serve as development evidence, not an unseen confirmation set.

No machining savings, operator hours, willingness to buy, profitability, or whole-machine safety were measured. The paid category and unresolved buyer-acquisition questions remain as described in SCREEN.md. This original HOLD is retained regardless of any future experiment.

## Publication packet

`results-resource-repair.tar.gz` contains all 1,408 repaired-run output files plus an archive provenance manifest. Original local files are untouched. Only execution-path strings in public process metadata are normalized to `<experiment>` and `python3`; the manifest records original and public hashes for every file and identifies changed entries. Native observations, traces, timings, numerical inputs and equality results are unchanged. Top-level summary/control files are also supplied separately for review. No executable binaries or full upstream source copies are included.
