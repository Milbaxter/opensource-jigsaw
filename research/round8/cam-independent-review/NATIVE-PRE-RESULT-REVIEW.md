# CAM native screen: independent prospective review

Recorded 2026-09-18T11:27:36.107080+00:00. Protocol/source checkpoints and hashes are in `NATIVE-STATIC-AUDIT.json`. No native kernel, toolpath, geometry engine or routing algorithm has been executed by this reviewer. This is readiness review for a negative/access/headroom screen, not a pursuit score.

## Verified inputs and native instrumentation

Independent ZIP/XML parsing verified the licensed fixture hash, all three box dimensions/placements/identity rotations, Boolean operand links and through-hole Z extents. Exact-rational cell membership on all42 open cells of the rectilinear arrangement per configuration matches the extracted footprints. Ring areas are225,600 and825mm². The six cases are two settings for each footprint, all from one upstream artifact. This validates the planar reconstruction, not an OCC job replay or six independent shop workloads. `verify-footprints.py` and `INDEPENDENT-FOOTPRINT-AUDIT.json` preserve the check.

Byte comparison against independently fetched pinned main sources confirms untouched original Adaptive.cpp/Adaptive.hpp. The prepared instrumented CPP differs only at the single ResolveLinkPath call site: snapshot before the original call and record its result afterward. The entire ResolveLinkPath body, including native clock limits, is byte-identical. The header differs only at two access labels. GetCleared directly returns the already-maintained vector; it does not introduce hidden lazy stock reconstruction.

The driver explicitly sets declared nondefault settings, including forceInsideOut=false and finishingProfile=false, and uses a noncancelling callback. Isolated replay resets the private radius, scale, stepover, ratio and stopProcessing state in fresh native objects. The short-link clearance branch matches the source condition. Trace and output writes occur outside the original function. Original whole-kernel baseline uses the no-trace source, while acquisition overhead is separate. These are appropriate controls; actual traced/untraced equality and request replay remain necessary because allocation/cache/timing perturbations can still affect a timeout-sensitive planner.

Native scalar fields on early error paths may be uninitialized; the revised driver avoids reading those fields when any error flag is present. Any such native error causes the prospective global correctness hold rather than becoming usable headroom evidence.

## Prospective geometry and scope

The fully-clear endpoint subset is conservative and avoids claiming exact equivalence to native lead endpoint exemptions. Eligibility must not be widened after outcomes. Keep all original native request counts/costs and exclusion reasons. Recovered requests can be speculative engagement/lead proposals rather than links selected into the final toolpath: a recovered proposal is headroom evidence only, never an observed reduction in actual retracts.

The complete visibility graph is a strong simple alternative. Its claim must be shortest path over the frozen polygon graph, not exact shortest path in a curved cutter configuration space. Polygon erosion uses an explicit extra margin and arc tolerance, but a final independent whole-segment verifier against original boundaries remains mandatory. Exact orientation/intersection and rational squared-distance checks can validate integer graph vertices; reject unsupported topology rather than silently repair it. Native full-path IsClearPath is a useful additional check, not a substitute for the independent verifier.

All geometry preprocessing, including rejected-request screening and direct-path tests, belongs inside the total geometry budget. Per-state rebuilds cannot be treated as free static-mesh amortization. The shared ratio limit prevents buying fewer failures with arbitrarily long detours. No planar test validates missing fixtures, holders, controller dynamics or machine time.

## Protocol clarifications resolved before execution

The revised draft prospectively chooses CPU_seconds consistently for its 1-second/20% profiling gate and distinguishes planned first-16/size-based graph sampling exclusions from an exhausted global runtime/memory budget. It explicitly limits recovered requests to proposal-level headroom. These resolve the remaining protocol wording concerns; no native algorithm has been executed. This review is not authorization to omit unfavorable cases.

The native driver and patch preparation have no remaining static blocker at this checkpoint. The orchestration and exact-geometry implementation were not yet available for review; they must be source-frozen and checked before execution. All six whole-kernel equality controls and every captured original-request replay must pass to support affirmative headroom. Planned thresholds are an exploratory decision to consider another experiment, not a measured end-to-end saving or a validated commercial opportunity.

## Post-freeze independent checking plan

Verify frozen hashes and reproduce source patch. Inspect every failure and timeout. Compare trace and all untraced output fields permitted by the native error handling; independently pair every trace begin/end and replay a bounded selection of original requests. Check source-state and endpoint hashes. Audit component/hole topology, zero/near-tangent segments and disconnected/narrow passages using independent geometry controls. Recompute sampling order, resource charges and the prospective decision. If the screen stops for insufficient headroom, retain that negative result without adding harder geometry or different offsets after inspection.

Final protocol wording checked 2026-09-18T11:30:38.990004+00:00. Native driver/patch readiness does not yet cover the pending geometry/orchestration implementation.

## Final implementation review

Checked 2026-09-18T11:37:20.565777+00:00. `GEOMETRY-ORCHESTRATOR-STATIC-REVIEW.json` records exact final protocol, driver, preparation, geometry, orchestration and compiled-binary hashes. No native/control execution or performance evaluation by this reviewer. The now-available topology validator rejects unsupported intersections, ring contacts and inconsistent nesting/orientation; exact clearance and visibility controls are specified. Original snapshots/replay preserve Clipper Z tag payloads separately from planar coordinates, and successful replay compares both. These tags are metadata, not physical tool height.

The conservative early upper-bound stop cannot affirm a result: it uses all-request CPU/failure totals, before eligibility can remove any requests. Original-boundary size exclusions now explicitly have unknown eligibility and contribute no eligible profile cost. Runtime phases reserve final serialization time and check elapsed work after their final operation. Cumulative RSS and the additional address-space cap are disclosed. The source-freeze record must include the actual rebuilt binary hashes; those binaries remain private build artifacts. No remaining static blocker for the bounded negative/headroom screen, conditional on that final freeze. This is not evidence that the executable controls pass or that commercially useful headroom exists.
