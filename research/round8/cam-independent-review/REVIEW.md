# Independent CAM linking screen

Observed 2026-09-18T11:13:43.895009+00:00. Source/schema inspection only: no FreeCAD import, CAD recomputation, path generation, solver run or comparative measurement. This note does not authorize an experiment or assign a pursuit score.

## Current finding

A generic proposal to add collision-aware low retracts to FreeCAD is too broad: both commercial CAM and current FreeCAD already implement substantial versions. A narrower, testable integration target does exist in FreeCAD's own Adaptive planner: replacing a bounded heuristic for links through already-cleared stock. It is not a novel algorithm claim; the source explicitly suggests a shortest-path replacement. A benchmark is conditionally possible if the author can capture actual internal link requests from pinned lawful fixtures without changing the cutting sequence or selecting cases by outcome. No practical advantage is established yet.

Version pins: current inspected main `691a041981b7972d3170ceadb96163019712d2b0`; latest released version observed `1.1.3` (published 2026-07-25T04:53:36Z), commit `145529fe741292ff0b3977a01195bf0247425794`. Do not infer current behavior from the original issue's1.0.1 build. The new shared `Path/Base/Generator/linking.py` and its unit tests exist at main and are absent at the inspected1.1.3 path. Exact source URLs/hashes, including404 checks, are in `source-manifest.json`.

## Issue and existing implementation

[FreeCAD22599](https://github.com/FreeCAD/FreeCAD/issues/22599), opened July2025, remains open. Its report describes excessive inter-feature vertical movement; discussion distinguishes internal linking from drilling-cycle postprocessing. It supplies proposed collision-aware linking logic and35comments, but no attached reproducible CAM workload was found in the inspected body/comments. An open issue is not proof the proposed functionality remains wholly unimplemented.

Current main's [linking generator](https://github.com/FreeCAD/FreeCAD/blob/691a041981b7972d3170ceadb96163019712d2b0/src/Mod/CAM/Path/Base/Generator/linking.py) tests supplied solids at candidate heights, supports line, diameter and tool-shape collision representations, and has upstream tests. [Drilling](https://github.com/FreeCAD/FreeCAD/blob/691a041981b7972d3170ceadb96163019712d2b0/src/Mod/CAM/Path/Op/Drilling.py) calls it with model solids and selectable collision strategies. This is not automatically a historical remaining-stock model or a general fixture/holder certificate. The helper's horizontal travel check should not be described as validating an entire machine motion.

Current [Adaptive.cpp](https://github.com/FreeCAD/FreeCAD/blob/691a041981b7972d3170ceadb96163019712d2b0/src/Mod/CAM/libarea/Adaptive.cpp) already checks swept tool-radius paths against progressively cleared polygons. `ResolveLinkPath` searches detours subject to a length ratio, iteration bound and CPU timeout. Its source proposes a triangulation/shortest-path replacement for improved runtime and paths. Therefore the credible wedge is a tested integration replacing this specific search, not the discovery of stock-aware linking or generic navigation algorithms. The source-cited [Lee–Preparata1984 paper](https://doi.org/10.1002/net.3230140304) describes established shortest-path methods for restricted planar domains; its complexity guarantee should not be transferred unqualified to arbitrary multiply-connected stock.

## Strong alternatives and counterevidence

1. Compare the exact current native Adaptive implementation on identical recorded stock, endpoints and policy. Keep the ordinary configured ratio and include a prospectively bounded higher-ratio/time alternative if the claim depends on a timeout setting; do not compare only to unconditional full retracts.
2. Use a robust visibility graph plus shortest-path search as a strong small-instance reference on the same configuration-space domain. Include graph construction and geometry conversion in cold timings, with separately reported amortized reuse where legitimate. A tiny fixture may make this simple method sufficient; that is a valid reason to stop.
3. Current shared linking generator is a meaningful plane-choice baseline for the original issue, but it is a different problem from an intra-cleared-region Adaptive detour. Do not mix their denominators or call sites.
4. [Fusion's official stay-down controls](https://help.autodesk.com/cloudhelp/ENU/Fusion-CAM/files/GUID2E5ABA80-7240-4F1A-989C-2410C4A0CCE5.htm) and [its June2026 explanation of remaining-material clearance](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/Meaning-of-Minimum-Stay-Down-Clearance-parameter-in-2D-Adaptive-toolpath-in-Autodesk-Fusion.html) show mature commercial functionality. [Autodesk's current guidance](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/PTB/Optimizing-toolpath-generation-in-the-Fusion-360-CAM-workspace.html) describes the tradeoff between stay-down search, generation cost and detour length. Existing paid products support the market category; this offline test cannot establish superiority to Fusion without running its comparable workflow.

## Lawful input candidates

The following are exact repository fixtures, inspected only as ZIP/XML containers. Download URLs, hashes, sizes, embedded license metadata and object inventories are in `fixture-inspection.json`.

| File | Embedded rights | Useful content / limitation |
|---|---|---|
| CAMTests/test_adaptive.fcstd |CC BY4.0|20,661-byte upstream geometric fixture; no saved CAM path. TestPathAdaptive creates the job/operation. Best initial reproducibility seed, not a production job.|
| CAMTests/Drilling_1.FCStd |CC BY4.0|266,675-byte multi-feature model; useful for original drilling-plane question, not automatically an Adaptive linking workload.|
| DemoParts/motor_mount_inch.fcstd |CC BY3.0|17,451-byte upstream sample model; saved model geometry rather than a manufacturing trace.|
| DemoParts/strange_part_with_holes.fcstd |CC BY3.0|39,670-byte upstream sample model with pockets/holes; same workload limitation.|
| CAMTests/Fixtures/test_28534_truncated_pocket.FCStd |All rights reserved|Although it contains a CAM operation and saved path, exclude absent clarification; do not assume repository-wide source licensing overrides its explicit embedded declaration.|

[CC BY4.0](https://creativecommons.org/licenses/by/4.0/) and [CC BY3.0](https://creativecommons.org/licenses/by/3.0/) permit commercial reuse/adaptation with the applicable attribution conditions. Preserve the model source, license link and modifications; where creator metadata is empty, retain repository/fixture provenance rather than inventing an author. The source files inspected carry LGPL notices; preserve notices if adapting/distributing code. No raw fixture or third-party source needs to be republished in the research packet.

## Safest decisive offline measurement

Freeze a small exact fixture/operation set and extraction rules before generating paths. Use the upstream TestPathAdaptive setup as a documented seed, then prospectively select additional lawful models by geometry/schema rather than observed routing outcomes. Any synthetic obstacles are separately labeled controls, not extra real customer jobs.

Record each native `ResolveLinkPath` input at the moment it is called: cleared polygon topology, scale factor, tool radius, step-over/clearance values, endpoints, ratio/time policy and original return path/failure reason. `ResolveLinkPath`, `IsClearPath`, `FindLinkPath` and historical `ClearedArea` are private native internals in Adaptive.hpp; obtaining these snapshots probably requires a small instrumented native build. Final part geometry or final cleared stock is not a valid substitute for the stock state at each link. Freeze instrumentation separately and show it leaves original outputs unchanged.

Compare only replacement noncutting links, preserving original cutting/lead sequence and endpoints. Report collision-valid retained links, unresolved/retracted links, full link length, vertical travel for the full fallback, and CPU/wall time. Preserve a common detour-ratio policy: fewer retracts alone can trade for arbitrarily long paths. Do not translate millimetres into machining seconds without actual machine dynamics.

Native clearance semantics require care: default ratio is3; the heuristic uses step-over-based clearance and trims checked first/last segments near the lead endpoints, with different handling for short links. A replacement cannot buy extra feasible links by reducing the clearance. A naive global polygon erosion can also reject legitimate native endpoint handling. Specify one equivalent endpoint policy, validate swept cutter clearance independently, and retain original fallback when uncertain. Include disconnected cleared islands, narrow passages, holes, near-tangent segments, duplicate/degenerate vertices and endpoint boundary cases as controls. A planar cutter-footprint test does not validate holders, clamps absent from inputs, spindle dynamics or an entire CNC machine.

Proceed to a frozen benchmark only if authentic native requests can be captured with manageable build effort and a plausible advantage remains over both the native planner and the strong simple reference. If capture requires an impractical integration, cases are almost all direct links, or the simple reference already meets the workload economically, record HOLD without constructing an artificial complex workload. Current status: conditional source/data lead; no measured advantage, no prototype execution.
