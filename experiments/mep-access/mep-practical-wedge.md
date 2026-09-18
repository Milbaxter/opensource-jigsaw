# MEP access-option service: practical wedge requiring validation

Unscored extension of the parent's discovery, not a world-first path-planning claim. No prototype or outreach. Existing research and suppliers validate the workflow; they do not automatically reject this opportunity.

## Defined buyer and delivery

A mechanical contractor's preconstruction estimator already buying BIM/scanning or rigging support could buy an **access-options packet** before committing to replacement equipment: a ranked set of reversible obstacle changes, associated candidate motion paths, minimum modeled clearances, input uncertainties and a contractor-supplied cost worksheet. Feed the packet into existing qualified engineering review. Avoid a new enterprise system or an operational lifting plan.

Candidate combination: IfcOpenShell extracts explicitly identified solid geometry and component IDs; OMPL supplies candidate rigid-body motions; a minimum-constraint-removal/weighted subset solver searches which permitted obstacles to temporarily remove; a BCF/IFC-linked report returns options to the existing BIM workflow. Each component has a separate role. Exact dependencies, rights and fit-for-purpose collision validation would need preregistration before a run.

The narrow *testable* advantage is fewer manually configured route/obstacle variants for the same declared geometry and candidate equipment—not an unsupported claim to replace an engineer. Existing engineering services might offer this already, so that is an empirical competitive question, not assumed whitespace.

## Evidence and practical boundary

C&S describes scanning an existing chiller facility for a major replacement in a few hours, supporting the existence of a digital-input acquisition workflow. It does not state access-option planning labor, and scan duration cannot be reused as planning labor saved. [C&S project](https://www.cscos.com/projects/chiller-replacement-and-plant-upgrades/).

A specialist scan-to-BIM supplier explicitly says removal-route clearances can change the equipment purchased; it models hangers/supports and access zones. This suggests an equipment-selection/bid-stage use case and also shows that incomplete geometry would defeat a simplistic demo. [MaRS MEP service](https://scantobimsolutions.com/services/mep-bim-modeling.html).

Parent sources document real constrained removals and a direct commercial analysis service. Project total value and total installation man-hours are **not** proof of analysis fees or recoverable savings. [Moore project](https://www.mooreusa.com/projects/empr-chilled-water-plant/), [PSC removal](https://pscind.com/projects/chiller-removal-and-replacement), [IMS service](https://fl-ims.com/services/installation-path-interference-analysis).

The2016 BIM/OMPL work and minimum-constraint-removal literature make algorithmic feasibility more plausible while reducing novelty claims. An implementation/service opportunity still needs a measured setup/coverage/cost difference. [BIM/OMPL paper](https://www.iaarc.org/publications/fulltext/ISARC2016-Paper008.pdf), [MCR paper](https://ojs.aaai.org/index.php/AAAI/article/view/12100).

## Credible comparison and next gate

Before prototype selection, obtain published or authorized evidence of the present estimator workflow: who supplies geometry, how many route variants are normally examined, analyst time per variant, which removals can be priced, and whether a paid incumbent already optimizes these automatically. These facts remain unknown. Publicly available project descriptions support pain but not the claimed workflow reduction.

A useful bounded local proof would use a declared synthetic IFC facility and multiple held-out layouts, including feasible, infeasible, orientation-sensitive, and uncertain-clearance cases. Compare against the same fixed-budget OMPL motion planner with no removals, with a simple cheapest-obstacle greedy policy, and with exhaustive obstacle-subset enumeration on small cases. For each reported advantage, independently verify the motion's swept geometry; do not use bounding-box rejection as the strongest baseline or accept a finite waypoint check as a continuous collision certificate. Include data/setup costs and report failure to find a path as unknown unless infeasibility is independently proved.

Only after such a bridge and an actual manual-workflow baseline would a small paid-validation proposal be credible. Safety-critical rigging, supports, floor capacity, temporary structural work, human access and final clearances remain in qualified engineering scope. An offline geometry options report is not an execution authorization. Input geometry rights and as-built availability must be obtained; synthetic inputs establish neither.

Current decision: **research hold, no ready prototype or score**. The practical wedge is more plausible than claiming a new planning algorithm, but labor/economic differentiation is the missing fact. Do not manufacture an easier comparison solely to obtain a passing demo.
