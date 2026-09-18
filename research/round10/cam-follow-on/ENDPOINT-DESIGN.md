# Prospective follow-on design — not a protocol or result

The completed round-7 decision remains `HOLD_INSUFFICIENT_HEADROOM`. That study's full-clear endpoint restriction excluded the expensive native calls. Its 147 requests are now **development data**, not unseen confirmation inputs. No new path-generation or performance evaluation has been run for this follow-on.

## Purchased task and exact proposed benefit

An offline FreeCAD CAM kernel extension for human-reviewed adaptive-operation preparation: reduce repeated computation spent finding links through already cleared stock while preserving the surrounding native engagement, lead and cutting logic. The relevant paid category is CNC programming, not machine-cycle optimization or autonomous machine control. The existing small fixture only demonstrates a potential computational bottleneck; its seconds of runtime do not establish willingness to pay or meaningful production-scale savings.

The mechanism combines native FreeCAD/Clipper cleared-stock states, Clipper2 constrained triangulation, and the Detour game-navigation corridor/funnel implementation. This is explicitly the family of improvement suggested in FreeCAD's own `ResolveLinkPath` TODO. It is an implementation opportunity, not a claim of new path-planning research. An optimized visibility-graph planner is an essential comparator; if it wins, Detour has not justified its complexity.

## Exact source semantics

Pinned FreeCAD commit: `691a041981b7972d3170ceadb96163019712d2b0`. Source is the same exact file used in round 7. `ResolveLinkPath` starts with `c = stepOverScaled` and `d = 2*stepOverScaled`. If `d > distance(start,end)/2`, it sets `d = distance(start,end)/2` and `c = 0`. For a segment incident to the original start, it tests the point obtained by moving **d along that segment's direction**. For a segment incident to the original end, it moves **d backward along that segment's direction**. Conversion to the native integer `IntPoint` truncates coordinates. This is not cumulative-arclength trimming, not a fixed Cartesian offset, and not necessarily a point lying within a very short first/last segment.

`IsClearPath` uses a round-capped Clipper sweep of radius `toolRadiusScaled+c` and accepts a remaining difference area smaller than one native square unit. An independent exact boundary-distance test may be stricter. Any discrepancies must be recorded, not silently labeled native bugs or erased by weakening the independent check.

`FindLinkPath` subsequently moves at least `stepOverScaled/2` from the successful link's tail into the cutting lead, extending this reassignment if the native zero-extra-clearance test fails. It then smooths the link and lead together. Therefore a replay-only route cannot establish the clearance of the final emitted `mtLinkClear` path. Successful replacement also changes which engagement proposal wins; identical final cutting paths are not a valid general requirement for the replacement.

## Proposed shared endpoint adapter

Both planners must receive the same finite endpoint connection set, the same conservative center region, the same maximum detour ratio, and the same fallback policy. No candidate-specific endpoint relaxation.

Construct a conservative center region by eroding the actual captured cleared-stock polygon by `R+c+margin`. Keep the original stock polygon for independent verification. Ring simplicity, orientation/nesting, disconnected components, touching contours and numeric range require explicit validation. Do not infer that an approximate rounded offset alone certifies continuous clearance.

For an endpoint outside the center region, the native check begins approximately on a circle of radius `d` around it. A source-faithful finite connector construction can derive angular intervals from intersections of this circle with center-region boundary segments, choose fixed interior directions within those intervals, and extend to a point slightly beyond the trim circle. Every proposed connector must then pass the **exact integer-trimmed native policy** and independent continuous clearance on its checked portion. Empty/narrow/degenerate intervals may be rejected. This is a bounded port set, not a globally complete endpoint solver.

The exact port rule, rounding, margin, tie order and limits must be frozen before development execution. A simpler first implementation may use a predetermined finite direction set with the same validators, but must not claim completeness or retune directions after seeing failures. For center-region endpoints, the implementation must still apply the native first/last-segment policy to the final route. Short first/last edges cannot silently switch to cumulative trimming.

For each output polyline, independently verify endpoint identity, finite/integer coordinate range, no zero-length interior edges, total length no greater than native ratio times direct distance, and continuous containment/clearance of every native-checked segment. Preserve all rejected proposals and reasons. Unsupported topology, numeric limits, failed/partial search and failed verification lead to the unchanged native fallback, with all attempted work charged.

## Genuine Detour bridge and numerical limits

Pinned Detour release `v1.6.0`, commit `6dc1667f580357e8a2154c28b7867bea7e8ad3a7`, Zlib license. `dtNavMeshCreateParams` accepts explicit polygon vertices/adjacency, so Clipper2 triangles can populate a flat single-tile mesh without Recast voxelization. Native XY maps to Detour XZ; height is constant.

The builder accepts unsigned-short vertices. Native stock snapshots include a large outside-cleared region, so raw global bounds are inappropriate. For a route with length at most `L = ratio*distance(a,b)`, every point is within distance `L/2` of `(a+b)/2` by the triangle inequality. Intersecting the center region with the outward-rounded axis-aligned square of half-width `L/2` therefore preserves every ratio-valid route. An added fixed outward margin handles bound rounding. This is a geometric reduction implied by the existing ratio constraint, not an input-specific workload simplification.

A translation of this cropped domain to a local integer origin with unit cell size can preserve integer coordinates only when the extent and vertex/index limits fit. Otherwise reject/fallback; do not silently rescale, quantize or merge vertices. Detour floating output must be converted back with a frozen rule and independently verified. Polygon adjacency must be checked against shared undirected edges, winding, manifoldness and exact total covered area; holes must remain holes. No off-mesh links should bypass stock geometry.

Detour performs corridor search followed by a funnel-style straight path. This does **not** establish a globally shortest planar path. Reject partial paths, exhausted-node or truncated-buffer statuses, failure to reach the actual end polygon, and any verification failure. Rebuilding the changing-stock mesh, endpoint generation, queries, validation and fallback all count in end-to-end cost. No uncharged reuse of a mesh from a different cleared-stock state.

## Strong comparisons and outer integration

Compare unchanged native Resolve, a direct-link-only policy with native fallback classification, optimized C++ lazy visibility-graph A* on the same ports/domain, and Detour. Both graph methods receive identical deduplication and any spatial indexing. On small domains, an exhaustive visibility graph supplies the reference for the chosen finite-port problem; it is not an oracle over every possible endpoint direction. Report total path lengths, success/fallback counts and CPU/wall cost, not guessed machining seconds.

Stage A should establish adapter/mesh correctness using synthetic exact controls and the existing 147 development requests. It cannot establish a new performance result. Stage B needs separately frozen unseen lawful source geometry and operation selection, followed by full native-kernel replacement with unchanged outer lead/cutting logic. All methods must run that same kernel-level workload. Native/no-instrumentation baselines remain necessary because tracing changes timed native search caps.

Capture the native stock state at the relevant FindLink call and inspect the final post-reassignment/post-smoothing clear-link portions. Independently check those portions with the physical tool radius under an explicitly defined conservative policy. An unsupported or failed check cannot be hidden by citing successful pre-smoothing Resolve validation. This remains planar offline geometric preparation, with no holder, fixture, machine-dynamics or rigging clearance claim.

## Remaining decisions before protocol freeze

1. Lawful unseen input extraction: actual CC-BY FreeCAD demo geometry, with exact BREP/face provenance and an input-only selection rule. Full FreeCAD job equivalence must not be implied by a standalone footprint kernel test.
2. A precise bounded connector rule and clearance policy that the independent reviewer can reproduce without importing the candidate.
3. A modest stage-A code scope and exact source controls before any development shaping/path execution.
4. Buyer-relevant confirmation endpoint: end-to-end time reduction against the strongest simple planner, not only faster isolated calls, with an absolute saving floor justified by the preparation workload. No threshold chosen from the forthcoming results.
5. A capped human-reviewed acquisition test; no assumption that customer models or real production workflow timings have already been obtained.

No pass, score, safety certification, profitability or measured human-labor claim is made here.
