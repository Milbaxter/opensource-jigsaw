# CAM discovery screen — manual Astra research

Status: source inspection only, 18 September 2026. No CAM generation, planner evaluation, machine execution, score, or pursuit pass. Three concepts screened. One conditional lead remains; it is not yet ready for a performance protocol.

## 1. Inventory-aware rest-machining tool sequence — HOLD

Potential combination: OpenCAMLib cutter/surface geometry, sparse stock representation, and OR-Tools sequence/set-cover optimization. Purchased deliverable would be a reviewed roughing/rest-machining plan using a shop's actual tool inventory.

The category is already served unusually directly. Toolpath offers free tooling recommendations, inventory-aware DFM in Core ($40/seat/month annually), and automated CAM export into Fusion in Pro ($125/seat/month annually; $160 monthly). Those are advertised offers, not verified transactions or our willingness-to-pay evidence. A new solver needs a measurable advantage on a defined inventory/setup constraint; none has been established. [Toolpath pricing](https://toolpath.com/pricing)

OpenCAMLib supplies drop-cutter and push-cutter geometry, not an automatic faithful simulation of remaining stock. Adding a solver without an actual stronger planning mechanism would not establish differentiation. No prototype proposed. [OpenCAMLib documentation](https://opencamlib.readthedocs.io/en/latest/)

## 2. Controller-aware arc compression — HOLD

Potential combination: ArcWelder-style extrusion-path simplification transferred to milling, OpenCAMLib geometric checks, and Ruckig motion constraints. Purchased deliverable would be smaller reviewed NC files with preserved geometric tolerance and demonstrated controller benefit.

Fusion already replaces linear runs with arcs and explicitly accounts for machining plus smoothing tolerance; unsupported arcs can be linearized by the postprocessor. It also offers evenly spaced points in relevant finishing strategies. Therefore comparison against raw G1 output would be weak. Any practical win must include native smoothing and real controller behavior; a simulated acceleration estimate cannot establish machining time or finish quality. No lawful paired machine trace and actual residual gap were identified. [Fusion smoothing](https://help.autodesk.com/cloudhelp/ENU/Fusion-CAM/files/GUID5A951723-4797-4F5F-A7A3-45DCBCA2D26F.htm), [finishing smoothing controls](https://help.autodesk.com/view/fusion360/ENU/?contextId=MFG-REF-3D-STEEP-SHALLOW-SMOOTHING)

## 3. Game navigation for native adaptive linking — CONDITIONAL

Proposed essential transfer: FreeCAD's actual progressively cleared 2D stock polygons → conservative center-space geometry → Detour navigation-mesh corridor search and funnel path extraction → the original native link acceptance/lead handling and independent geometric verification. Detour is the game navigation component of Recast Navigation, used by major game engines; it provides pathfinding over convex-polygon meshes. This would use its actual routing capability, not rename generic graph code. Clipper2 or another audited constrained triangulator would construct the mesh; exact versions and rights remain to be pinned. [Recast Navigation](https://github.com/recastnavigation/recastnavigation), [Detour API](https://recastnav.com/group__detour.html)

The proposed paid deliverable is a bounded CAM integration/optimization service for repeated adaptive roughing jobs, with reproducible stock-state traces and reviewed toolpath changes. The primary benefit hypothesis is less regeneration overhead or fewer avoidable retracts at equal link constraints. Neither benefit is measured yet. No claim of machine safety, actual cycle-time savings, reduced operator hours, or superiority to commercial CAM follows from this screen.

### Current native capability and exact gap

Independent reviewer A pinned FreeCAD main `691a041981b7972d3170ceadb96163019712d2b0`. Its `Adaptive.cpp` already checks swept cutter area against progressively cleared stock and uses a midpoint/perpendicular detour heuristic in `ResolveLinkPath`. It limits search by CPU time, 10,000 iterations, and a keep-down length ratio. The function's own TODO explicitly proposes eroded cleared-area triangulation plus shortest-path search to improve runtime and route quality. Thus the algorithm family and proposed integration point are existing upstream ideas. The opportunity, if any, is a measured deployable implementation, not a novel invention. [Pinned native source](https://github.com/FreeCAD/FreeCAD/blob/691a041981b7972d3170ceadb96163019712d2b0/src/Mod/CAM/libarea/Adaptive.cpp#L2792)

Current main also contains a newer `Path/Base/Generator/linking.py` with solids, tool shape, and local/global clearance planes; it is absent from release 1.1.3. It would be false to claim FreeCAD generally lacks collision-aware links. Open issue #22599 supplies workflow discussion, not proof that all described gaps remain. The more specific drilling regression #22622 and boundary dressup bug #28208 are now closed and are excluded as current-gap evidence. [Current linking generator](https://github.com/FreeCAD/FreeCAD/blob/691a041981b7972d3170ceadb96163019712d2b0/src/Mod/CAM/Path/Base/Generator/linking.py), [#22599](https://github.com/FreeCAD/FreeCAD/issues/22599), [#22622](https://github.com/FreeCAD/FreeCAD/issues/22622), [#28208](https://github.com/FreeCAD/FreeCAD/issues/28208)

Fusion already has stay-down effort, retract policies, clearance/lift settings, and stock-aware behavior. Its support recommends those settings and, in some situations, manual connecting geometry. Those are mandatory practical counterevidence. A FreeCAD-only benchmark could establish a FreeCAD improvement, not superiority to Fusion. [Fusion linking controls](https://help.autodesk.com/cloudhelp/ENU/Fusion-CAM/files/GUIDA73542E9-ED9C-4BD9-A87D-3A0ECA8BEB41.htm), [vendor support](https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Tool-does-not-stay-down-despite-Keep-tool-down-enabled-in-Fusion-360-Manufacturing.html)

### Paid workflow and unresolved buyer question

Remote CAM programming is explicitly sold: RAD Precision advertises $175–200/hour depending on hour block, while CADCAMX advertises CAM programming/toolpath optimization at $15–20/hour. These validate a paid labor category with a wide price range, not a price for this plugin. RAD's page contradicts itself about credit expiration; no contractual conclusion is drawn. [RAD offers](https://radprecision.com/cnc-programming-pricing/), [CADCAMX offers](https://cadcamx.com/pricing)

Historical FreeCAD developer discussion reports substantial model-dependent adaptive calculation times, while its author emphasizes measured profiling and notes that some ordinary models already finish in seconds. That 2018 discussion is historical motivation only, not present-day timing evidence. [Native developer discussion](https://devtalk.freecad.org/t/adaptive-pathcam-operation/25881?page=7)

Decision-critical buyer uncertainty: do identifiable paying FreeCAD CAM users repeat sufficiently expensive adaptive jobs, and would they buy integration/support rather than use current settings, commercial CAM, or a free upstream fix? Native computation saved is not equal to billable labor saved. Before any commercial pursuit judgment, a capped acquisition experiment must specify recruitment, consented workloads, price offer, time budget, success and kill metrics. No contact has been made.

### Input access, scope, and next smallest test

Reviewer A inspected actual FCStd archive metadata, not just repository license labels:

- `test_adaptive.fcstd` declares CC BY 4.0 and is 20,661 bytes, SHA256 `34207b128f433c53b68f09e58a14412eac6eff36bb6f25c7baaff659bf5d7375`. It contains geometry; upstream tests create the CAM job and operations. It is a real upstream regression artifact, not evidence of an actual customer's production job.
- `motor_mount_inch.fcstd` and `strange_part_with_holes.fcstd` declare CC BY 3.0 and are actual upstream demonstration parts. Their manufacturing representativeness remains limited.
- `test_28534_truncated_pocket.FCStd` explicitly says All rights reserved and is excluded.

The authoritative URLs, hashes, and embedded rights metadata are in the independent `fixture-inspection.json`. Public issue attachments are not assumed licensed. FreeCAD source files inspected have LGPL notices; Recast/Detour declares Zlib. A complete exact dependency/build audit would precede any executable packet.

Authentic per-link start/end and historical cleared-stock state are internal/private; public Adaptive2d results do not expose them directly. A trace requires an explicitly pinned instrumented native build. Reconstructing stock from the final CAD model is not an acceptable shortcut. No instrumented build or benchmark has run.

The next prospective step, if warranted, should be a small **native-only workload and headroom screen**, with fixed lawful fixtures and upstream operation settings, recording every link request, stock hash, endpoint, clearance policy, outcome, and native time. It cannot pass the overall candidate. Its purpose is to establish input fidelity and a material bottleneck before implementing Detour. Exact inputs, stop rules, instrumentation, and thresholds are still to be specified and independently reviewed; this document is not an execution authorization or frozen protocol.

A later fair test needs exact current native C++, an optimized full visibility graph on manageable instances, and the same candidate preprocessing/validation charges. Each changed stock state requires a rebuild unless legitimate reuse is demonstrated; no uncharged static-mesh amortization. Native endpoint exceptions matter: the first/last checked portions are shortened, clearance depends on stepover, and short links differ. Candidate feasibility must not improve merely by lowering clearance. Common length-ratio limits prevent buying fewer retracts with arbitrarily long detours. Record retract count, link length, CPU, rejected/partial routes, and independent swept-geometry results; do not invent machining seconds. The recorded planar cleared-stock model excludes whole-machine, holder, fixture, and out-of-plane safety claims.

## Decision

Do not build a broad CAM optimizer. The exact adaptive-link integration point is worth a small prospective access/headroom decision if its build can stay bounded. The other two concepts remain HOLD. No score or passing candidate is claimed.
