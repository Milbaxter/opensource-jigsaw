# Open Source Jigsaw

Status: **complete**

57 repositories · 32 fields · 1 evaluated · **0 passed**

A pass means worth a validation experiment, not proven profitability. Scores are model judgments; evidence remains open to human review.

## Passed the bar

No combinations cleared every gate. The bar was not lowered.

## Rejected / watch

### Motion-aware connection sizing for electrified container terminals

**NO PASS · 44.5/100** · Astra: reject

Test whether physically informed crane scheduling can reduce a terminal’s required electrical connection and battery capacity while preserving container throughput. The supplied catalogue supports the components’ broad technical roles; it does not establish achievable savings, customer demand, integration feasibility, or license compatibility.

Buyer: The engineering director of an electrifying container-terminal operator, using its electrical connection, substation, battery, and terminal-modernization capital-planning budget. Willingness to pay is a hypothesis.

Components: [stack-of-tasks/pinocchio](https://github.com/stack-of-tasks/pinocchio), [google/or-tools](https://github.com/google/or-tools), [PyPSA/PyPSA](https://github.com/PyPSA/PyPSA)

Weighted score: 44.5/100. Reject the proposed differentiated product thesis on current evidence. Commissioned electrical-capacity engineering establishes a real purchasing workflow, but not demand for this combination or recurring software. [CIMA+ project](https://www.cima.ca/en/project/electrical-network-capacity-analysis/). No integrated benchmark demonstrates incremental savings, tractability, reliable connection downsizing, or Pinocchio's necessity. Data access, utility acceptance, delivery margins and distribution remain unresolved. No unconditional fatal flaw is established. License compatibility is supported for the named components under their obligations: [Pinocchio BSD-2-Clause](https://raw.githubusercontent.com/stack-of-tasks/pinocchio/master/LICENSE), [OR-Tools Apache-2.0](https://raw.githubusercontent.com/google/or-tools/stable/LICENSE), and [PyPSA MIT](https://raw.githubusercontent.com/PyPSA/PyPSA/master/LICENSE). This does not clear an unspecified distribution's dependencies or customer-data rights.

Gate failures:

- Astra verdict: reject
- Weighted score 44.5 is below 85
- novel_synergy: 3 is below 9
- buyer_pain: 7 is below 8
- willingness_to_pay: 4 is below 8
- feasibility: 5 is below 8
- defensibility: 3 is below 7
- distribution: 3 is below 7
- evidence: 5 is below 8
- Unverified gate: demand_verified
- Unverified gate: differentiation_verified
- Unverified gate: integration_verified
- Unresolved critical assumptions in the research

Next experiment: Before building the full stack, obtain authorized existing movement and feeder records for one terminal with a pending connection decision. First test whether simple staggering or empirical-profile scheduling already captures the available savings. Only then compare a minimal motion-aware model on held-out vessel calls under identical operational, storage and reliability constraints. Proposed hurdles: at least 10% lower required connection capacity, at most 1% throughput loss, no material vessel-deadline deterioration, and incremental value over the best inexpensive baseline exceeding modelling uncertainty and added delivery cost. Report battery MW and MWh separately. A positive replay plus a paid study commitment and preliminary engineering/utility acceptance would justify reconsideration as a services opportunity; it would not establish annual-software demand or satisfy the novelty gate by itself.

Sources:

- [CIMA+: Port of Montreal electrical network capacity analysis](https://www.cima.ca/en/project/electrical-network-capacity-analysis/): The Montreal Port Authority commissioned network-capacity and infrastructure-condition analysis. Work included updating single-line diagrams, reviewing utility and tenant agreements, calculating network capacity, simulating power flows, and studying equipment electrification. This demonstrates an established purchasing workflow; the fee and willingness to buy motion-aware scheduling are undisclosed.
- [EMA: Energy storage and smart-grid management at PSA](https://www.ema.gov.sg/news-events/news/media-releases/2022/singapores-first-energy-storage-system-at-psas-pasir-panjang-terminal): EMA reports an awarded Envision Digital-led project within an $8 million EMA–PSA partnership, including a 2 MW/2 MWh battery and demand forecasting for planning and energy management. This is independent evidence of adjacent spending, but the partnership includes hardware and public support; it is not a software price or proof of demand for this combination.
- [PEMA: Reducing Electricity Costs of Ship to Shore Container Cranes](https://www.pema.org/wp-content/uploads/2024/05/PEMA-Challenge_Peak-Electriciy-Reduction-Ship-to-Shore-Cranes.pdf): The study already varies acceleration, velocity, and deceleration under a collective power limit. At its 2,000 kW limit, simulated crane-productivity loss fell from 12.2% to 9.3% when dynamic profiles were varied; peak-related costs fell 59.5%. Actual-terminal digital-twin validation and TOS integration remained future work. This is the closest inspected counterexample to the motion-aware mechanism.
- [Geerlings, Heij and van Duin: Opportunities for peak shaving at container terminals](https://link.springer.com/article/10.1186/s41072-018-0029-y): This 2018 simulation study reports 50% peak reduction with less than half a minute of additional vessel handling time per handling hour using power limits or limits on simultaneous lifting. Its reported savings are case-specific simulation results, not demonstrated connection-capacity reductions. It establishes a demanding simple-control baseline.
- [FlexTerm: Port and terminal simulation solutions](https://www.flexterm.com/solutions): FlexTerm already markets terminal simulation, TOS emulation, infrastructure planning, and evaluation before capital expenditure. The inspected page does not establish motion-level electrical network optimization or publish pricing. It is an incumbent workflow alternative and possible integration partner.
- [HOMER Grid commercial pricing](https://homerenergy.com/homer-grid/pricing): The inspected page lists a one-user commercial annual subscription at $4,200/year and monthly billing at $665/month; enterprise pricing is custom. Listed capabilities include storage sizing, sensitivity analysis, and demand-charge reduction. This is an adjacent software price, not evidence that terminals will purchase crane scheduling.
- [Pinocchio documentation: models and inverse dynamics](https://gepettoweb.laas.fr/doc/stack-of-tasks/pinocchio/master/doxygen-html/): The documentation demonstrates URDF model loading and inverse dynamics from configuration, velocity, and acceleration to generalized joint forces/torques, with NumPy representations in Python. It does not supply a crane electrical-demand model or terminal adapter.
- [Pinocchio README](https://raw.githubusercontent.com/stack-of-tasks/pinocchio/master/README.md): The project documents C++ and Python interfaces, multiple model-description formats, testing across platforms, and use in other robotics software. These support component maturity, but do not validate crane dynamics, electrical trace accuracy, or the proposed integrated product.
- [OR-Tools: The Job Shop Problem](https://developers.google.com/optimization/scheduling/job_shop): The example represents tasks using start, end, and interval variables with precedence and machine non-overlap constraints. Crane interference, stowage restrictions, vehicle availability, and vessel deadlines still require a custom terminal model.
- [OR-Tools: CP-SAT Solver](https://developers.google.com/optimization/cp/cp_solver): CP-SAT constraints require integer representations. Time and electrical coefficients therefore need explicit discretization and scaling. The documentation distinguishes feasible solutions from proven optima and permits an unknown result after resource limits; terminal-scale runtime remains unmeasured.
- [OR-Tools source: cumulative scheduling constraint](https://raw.githubusercontent.com/google/or-tools/stable/ortools/sat/python/cp_model.py): The add_cumulative documentation requires nonnegative demand for every interval. Signed consumption/regeneration traces need a separate time-indexed balance formulation or another custom representation. Regeneration cannot simply be inserted as a negative cumulative demand.
- [PyPSA: Import and Export](https://docs.pypsa.org/latest/user-guide/import-export/): PyPSA supports programmatic network construction and CSV, netCDF, and HDF5 exchange, including component time-series files. A custom adapter must map crane identifiers, electrical buses, timestamps, units, and load profiles into this representation.
- [PyPSA: Storage optimization](https://docs.pypsa.org/latest/user-guide/optimization/storage/): Storage equations include MW dispatch, MWh state of charge, efficiencies, and snapshot duration weights. StorageUnit couples energy capacity to power through max_hours; independent sizing requires an appropriate Store/Link formulation. Default one-hour weights must be changed for short movement intervals.
- [PyPSA: Non-linear power flow](https://docs.pypsa.org/latest/user-guide/power-flow/): The documentation separates linearized optimization from nonlinear power-flow validation. The latter requires active/reactive setpoints and network impedances and produces voltages and branch flows. These documented calculations do not establish protection coordination, harmonic performance, or transient acceptability.
- [PyPSA package and dependency metadata](https://raw.githubusercontent.com/PyPSA/PyPSA/master/pyproject.toml): The inspected branch requires Python 3.11 or later and lists dependencies including NumPy, pandas, Linopy, netCDF4, and highspy, with commercial-solver support optional. It declares Production/Stable status; this is project metadata, not evidence of integrated terminal-system maturity.
- [Pinocchio BSD-2-Clause license](https://raw.githubusercontent.com/stack-of-tasks/pinocchio/master/LICENSE): The actual license permits use and redistribution with modifications. Source distributions must retain copyright, conditions, and disclaimer; binary distributions must reproduce them in accompanying materials. It does not require publication of proprietary application code.
- [OR-Tools Apache-2.0 license](https://raw.githubusercontent.com/google/or-tools/stable/LICENSE): Redistribution requires the license, applicable notices, modification notices for changed files, and relevant NOTICE attribution if supplied. The license includes a contributor patent grant with termination conditions and does not grant trademark rights.
- [PyPSA MIT license](https://raw.githubusercontent.com/PyPSA/PyPSA/master/LICENSE): The inspected license permits use, modification, distribution, sublicensing, and sale. Copyright and permission notices must accompany copies or substantial portions. It imposes no requirement to publish the proprietary application.
- [Linopy MIT license](https://raw.githubusercontent.com/PyPSA/linopy/master/LICENSE.txt): Linopy uses MIT terms, including retention of copyright and permission notices in copies or substantial portions. This checks one important dependency, not the entire deployment dependency tree.
- [HiGHS MIT license](https://raw.githubusercontent.com/ERGO-Code/HiGHS/master/LICENSE.txt): HiGHS permits commercial use under MIT terms with notice retention. Whether its performance is adequate for this particular sizing problem remains untested.
- [Eigen 3.4.0 license composition](https://gitlab.com/libeigen/eigen/-/raw/3.4.0/COPYING.README): Eigen states that it is primarily MPL-2.0, with some BSD and LGPL files. It documents EIGEN_MPL2_ONLY to exclude LGPL-covered inclusions. Dependency and build configuration therefore affect redistribution obligations.
- [Eigen MPL-2.0 license text](https://gitlab.com/libeigen/eigen/-/raw/3.4.0/COPYING.MPL2): MPL executable distribution requires availability of the covered source and instructions for obtaining it. Separate proprietary files can remain under other terms. This is file-level coverage, not a requirement to publish the whole application.
- [OR-Tools build configuration and optional solvers](https://raw.githubusercontent.com/google/or-tools/stable/CMakeLists.txt): The build configuration explicitly disables GLPK by default because it is GPLv3 and exposes several other solver options. Choosing CP-SAT at runtime does not establish what a distributed binary bundles; the exact artifact needs auditing.
