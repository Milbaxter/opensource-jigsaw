# Open Source Jigsaw: initial Astra discovery and skeptical review

Research snapshot: 2026-09-18T07:20:56.356076+00:00 to 2026-09-18T07:23:25.685952+00:00. This is manual Astra research supported by scripts and public sources; it was not produced by the repository CLI. Discovery and skeptical judging were separate passes by the same Astra agent, not independent human validation.

**Result: 1,320 unique public repositories captured across 30 topic fields; 19 components inspected more closely; seven combinations proposed; zero accepted.** Weighted scores range from 54.5 to 65/100, far below the 85/100 threshold. These are research hypotheses. No buyer interviews, paid pilots, working integrations, measured ROI, or profitability have been established.

## What was actually inspected

| Measure | Count |
|---|---:|
| unique catalogue repositories | 1320 |
| query result rows | 1384 |
| topic fields | 30 |
| metadata only catalogue repositories | 1313 |
| deep screened components | 19 |
| deep screened components also in catalogue | 7 |
| additional deep components | 12 |
| unique repositories across all research | 1332 |
| standard software license metadata | 973 |
| null license | 73 |
| noassertion license | 236 |
| content data license metadata | 38 |
| stars at least 1000 | 772 |
| stars below 500 | 396 |
| external sources | 22 |
| candidates | 7 |
| accepted | 0 |

The catalogue contains 1,384 search-result rows deduplicated into 1,320 repository names. Only seven of the 19 deep-screened components overlap the topic-search catalogue; 12 were added through targeted follow-up, giving 1,332 unique repositories across both sets. The 1,313 catalogue entries outside the shortlist received metadata-level screening only. We did not read 1,320 codebases or exhaustively inspect their READMEs. “Deep-screened” means direct repository metadata, primary license files, and selective API/domain/competitor documentation—not a code audit, benchmark or integration test.

### Scope and selection bias

Queries used `stars:>=50 pushed:>=2025-03-01 archived:false fork:false`, one topic per field, sorted by descending stars, up to 50 results per field. Before publication, all 30 original raw responses were checked: all 1,384 returned rows (1,320 unique repositories) explicitly had `private=false`, `archived=false` and `fork=false`; none were private, archived, forks or missing these flags. The reusable collector now additionally includes `is:public` and rejects any returned item unless all three flags are explicitly false. The original recorded queries remain unchanged for provenance. No search returned `incomplete_results=true`. Stars are a discovery proxy, not proof of users, quality, safety, active maintenance or commercial impact. A push can update documentation only. Topic labels are author supplied and noisy. Scientific tools, books, curated lists and data repositories can all appear. The query cutoff means “active” only under this explicit recency heuristic.

The threshold deliberately admits smaller scientific and industrial tools: 396 captured repositories have fewer than 500 stars, while 772 have at least 1,000. The sample is biased toward GitHub and explicit topic metadata; it is not a census of OSS and misses many important projects hosted elsewhere. The search-result metadata report is reproducible with `collector.py`; future counts will change.

### Public repository does not mean open source

973 catalogue entries have a recognized conventional software-license identifier in GitHub metadata. 38 carry content/data/public-domain-style identifiers; 236 have `NOASSERTION`; 73 have no detected license. These are screening buckets, not final legal determinations. All 1,320 are public candidates, not 1,320 commercially reusable software packages. Dataset, model-weight, trademark and dependency terms can differ.

License-file checks found why detection cannot be used as a binary filter: WNTR declares Revised BSD, PyMC declares Apache-2.0 plus MIT code, and Valhalla redirects to its MIT COPYING file despite `NOASSERTION`. Conversely, batdetect2 is CC-BY-NC-4.0 and fails the proposed commercial reuse. PM4Py resolves to `process-intelligence-solutions/pm4py` and is AGPL-3.0; copyleft is not automatically a commercial blocker, but the planned distribution/service must honor it. No full dependency or model/data audit was completed.

## Field coverage

| Field | Matching repositories reported by GitHub | Captured rows |
|---|---:|---:|
| geospatial | 376 | 50 |
| remote-sensing | 202 | 50 |
| weather-climate | 93 | 50 |
| bioinformatics | 675 | 50 |
| microscopy | 53 | 50 |
| computational-chemistry | 142 | 50 |
| robotics | 1083 | 50 |
| industrial-iot | 13 | 13 |
| cad-manufacturing | 200 | 50 |
| energy-power | 116 | 50 |
| water-hydrology | 57 | 50 |
| agriculture | 26 | 26 |
| astronomy | 188 | 50 |
| medical-imaging | 167 | 50 |
| transportation | 42 | 42 |
| operations-research | 615 | 50 |
| process-mining | 3 | 3 |
| formal-verification | 70 | 50 |
| cybersecurity | 3060 | 50 |
| privacy | 1171 | 50 |
| graph-databases | 115 | 50 |
| signal-processing | 146 | 50 |
| speech-audio | 1077 | 50 |
| document-processing | 518 | 50 |
| education | 561 | 50 |
| accessibility | 438 | 50 |
| finance | 482 | 50 |
| simulation | 842 | 50 |
| data-engineering | 265 | 50 |
| digital-preservation | 60 | 50 |

Some fields have few topic matches (process-mining: three; industrial: 13); this is a query-taxonomy limit, not proof that those industries have little open source. Fields with 50 captured rows are capped rather than exhaustive.

## Acceptance policy

The initial judgments use the same seven-dimension weighted rubric as the pipeline. Each dimension is scored 0–10, and the total is `sum(score × weight / 10)`, out of 100. Scores express reviewer judgment, not success probabilities.

| Dimension | Weight | Minimum score |
|---|---:|---:|
| novel_synergy | 20 | 9 |
| buyer_pain | 20 | 8 |
| willingness_to_pay | 15 | 8 |
| feasibility | 15 | 8 |
| defensibility | 10 | 7 |
| distribution | 10 | 7 |
| evidence | 10 | 8 |

Acceptance requires a weighted total of at least 85, every dimension meeting its floor, confidence of at least 0.8, at least two independent external demand/pricing source domains, verified demand/differentiation/integration/license compatibility, and no unresolved critical assumptions or fatal flaws. Licensing and data-access concerns remain explicit evidence gates and integration findings; they do not create a second score system.

No concept satisfies this policy. Confidence is 0.35 for JIG-001 and JIG-002, and 0.25 for the other concepts. Government documentation establishes problems, and vendor pages establish competing offers, but neither establishes willingness to buy this proposed product. Two domains containing general problem statements are not counted as two independent demand/pricing proofs. Vendor claims are not independently verified performance results. No invented prices, market sizes or promised profits are used.

## Ranked hypotheses and judgments

| Candidate | Components | Weighted score | Decision |
|---|---:|---:|---|
| JIG-001: Process-aware industrial energy savings assurance | 4 | 65/100 | Reject pending evidence |
| JIG-002: Deconstruction reuse bid and sequence optimizer | 4 | 64.5/100 | Reject pending evidence |
| JIG-003: Water repair prioritization using hydraulic consequence and actual crew friction | 4 | 62/100 | Reject pending evidence |
| JIG-006: Tailings inspection evidence triage | 4 | 58/100 | Reject pending evidence |
| JIG-007: Flood-aware accessible evacuation rehearsal | 4 | 56.5/100 | Reject pending evidence |
| JIG-005: Temperature-excursion salvage dispatch | 4 | 56/100 | Reject pending evidence |
| JIG-004: Ecology-aware wind dispatch | 3 | 54.5/100 | Reject pending evidence |

### JIG-001: Process-aware industrial energy savings assurance

**Buyer hypothesis:** Energy service companies and industrial energy managers with performance-based projects.

**Combination:** [ORNL-AMO/AMO-Tools-Desktop](https://github.com/ORNL-AMO/AMO-Tools-Desktop) — Engineering estimates of equipment/system savings; [process-intelligence-solutions/pm4py](https://github.com/process-intelligence-solutions/pm4py) — Infer production states and intervention timelines from event logs; [opendsm/opendsm](https://github.com/opendsm/opendsm) — Metered counterfactual and avoided-energy baseline; [docling-project/docling](https://github.com/docling-project/docling) — Extract intervention evidence from audit reports and commissioning documents.

Link production-event changes to physics-based audit assumptions, then flag savings claims that meter baselines cannot distinguish from production changes. Hypothesis: audit-ready exception packets reduce disputed payments and analyst time.

**Verified evidence and limits:**
- MEASUR identifies industrial-system efficiency savings opportunities. [DOE industrial software tools](https://www.energy.gov/cmei/ito/ito-software-tools)
- Avoided-energy methods compare metered usage with counterfactuals; primary use case includes procurement of energy savings. Whole-site methods do not establish process-level causal attribution. [CalTRACK methods](https://docs.caltrack.org/en/latest/methods.html)
- An established commercial process-mining competitor offers process optimization; not evidence that the proposed industrial measurement workflow is unique. [Celonis Process Excellence](https://www.celonis.com/solutions/process-excellence)
- Structured document conversion and JSON export exist; correctness on a buyer corpus is untested. [Docling document conversion](https://docling.ai/)
- Process-mining toolkit integrates event-data analysis with Python data-science libraries. [PM4Py research paper](https://arxiv.org/abs/1905.06169)

**Competitor check:** Celonis: Process analysis and optimization; specific combined M&V workflow not verified.; Existing M&V consultants and OpenDSM/CalTRACK workflows: Counterfactual savings estimation is already available.

**Integration hypothesis:** Convert reports to reviewed structured inputs; map CMMS/MES events to batch/equipment IDs; export PM4Py regimes into baseline covariates; compare measured and MEASUR-predicted savings. 4-8 engineer-weeks for an offline single-site study, excluding procurement, data cleaning and causal validation. This effort is a planning estimate, not a tested result.

**Principal difficulties:** MEASUR is a desktop application, not a guaranteed stable headless API. Process changes confound meter-based causal estimates; standard site models cannot simply be relabeled as process-level verification. No access to synchronized production and meter data yet.

**License finding:** Docling MIT and OpenDSM Apache-2.0; PM4Py AGPL-3.0 requires an intentionally compatible distribution/service design or separate commercial terms. MEASUR custom permissive license has notice/change-marking/trademark conditions. Third-party dependencies not exhaustively audited.

**Judgment: 65/100 weighted; rejected.** No buyer interview, paid pilot or measured analyst-hours reduction. Advantage over an experienced energy auditor using existing tools is unproven. Manufacturing confounders may invalidate savings attribution.

**Next falsification test:** Acquire one de-identified, synchronized 12-month meter/production dataset plus three historical retrofits from a consenting ESCO. Blindly compare disputed-claim detection and analyst time against its current workflow; stop if no incremental precision or time benefit. Obtain a paid pilot commitment before implementation beyond the study.

### JIG-002: Deconstruction reuse bid and sequence optimizer

**Buyer hypothesis:** Demolition contractors and reuse surveyors bidding on selective deconstruction.

**Combination:** [IfcOpenShell/IfcOpenShell](https://github.com/IfcOpenShell/IfcOpenShell) — Read BIM geometry, materials and object identifiers; [docling-project/docling](https://github.com/docling-project/docling) — Extract survey, contamination and salvage-offer records; [google/or-tools](https://github.com/google/or-tools) — Optimize disassembly sequence, crew capacity and shipment allocation; [brightway-lca/brightway2](https://github.com/brightway-lca/brightway2) — Estimate scenario lifecycle impacts with appropriately licensed inventory data.

Convert an imperfect material survey into a bid that chooses what to salvage, in what order, and for which confirmed buyer, showing uncertainty in recovery yield and net proceeds. Novelty hypothesis is an executable contractor bid, beyond a material passport.

**Verified evidence and limits:**
- Guidance identifies pre-demolition audits, hazardous materials, reuse potential, and waste logistics as practical needs. Guidance itself is not a purchase order or blanket legal obligation. [EU Construction and Demolition Waste Management Protocol 2024](https://build-up.ec.europa.eu/en/resources-and-tools/publications/eu-construction-demolition-waste-management-protocol-2024-updated)
- Commercial material inventory/passport platform already supports reuse-related workflows. [Madaster platform](https://madaster.com/platform/)
- IFC authoring and editing APIs exist. Does not prove that legacy buildings have reliable IFC files. [IfcOpenShell API documentation](https://docs.ifcopenshell.org/autoapi/ifcopenshell/api/index.html)
- Structured document conversion and JSON export exist; correctness on a buyer corpus is untested. [Docling document conversion](https://docling.ai/)

**Competitor check:** Madaster: Material records, quantities and reuse insights already exist.; Surveyors, demolition estimating and resale marketplaces: Existing workflow substitutes; feature-level comparative interviews not performed.

**Integration hypothesis:** Join IFC GlobalIds and reviewed survey rows to a dependency graph; attach signed-off contamination constraints; OR-Tools schedules crews and shipments; lifecycle module reports secondary impact. 6-10 engineer-weeks for a reviewed single-building scenario tool, excluding field surveys and integrations. This effort is a planning estimate, not a tested result.

**Principal difficulties:** Many older buildings lack trustworthy BIM; OCR cannot establish material condition. Buyer commitments, salvage prices and breakage yields are unavailable until site-specific fieldwork. A physics/engineering review must determine disassembly dependencies, not an LLM.

**License finding:** IfcOpenShell LGPL-3.0, Docling MIT, OR-Tools Apache-2.0, Brightway2 BSD-3-Clause. LGPL distribution obligations need appropriate packaging; lifecycle inventories can have separate commercial restrictions. No complete dependency or dataset audit.

**Judgment: 64.5/100 weighted; rejected.** No paid contractor demand or demonstrated margin improvement. Market liquidity and inspection costs may dominate software gains. Life-cycle datasets and real salvage inputs are not yet secured.

**Next falsification test:** Use a completed building project with survey, actual labor, breakage, disposal costs and sales outcomes. Have a contractor blind-score the generated bid against its original estimate. Require improved contribution margin after survey and handling costs; stop if gains depend on speculative buyers.

### JIG-003: Water repair prioritization using hydraulic consequence and actual crew friction

**Buyer hypothesis:** Small and medium water-utility asset managers or their engineering consultants.

**Combination:** [USEPA/WNTR](https://github.com/USEPA/WNTR) — Simulate network service consequences of failures and planned shutdowns; [process-intelligence-solutions/pm4py](https://github.com/process-intelligence-solutions/pm4py) — Extract repair delay and permit/parts bottlenecks from work orders; [pymc-devs/pymc](https://github.com/pymc-devs/pymc) — Represent uncertain repair durations and failure rates; [google/or-tools](https://github.com/google/or-tools) — Schedule repairs under crew, parts and service constraints.

Prioritize the repair portfolio by prevented service loss per realistic crew-hour, using actual organizational delays instead of ideal repair durations. Hypothesis: this outperforms age-only risk lists at utilities unable to maintain a broad digital-twin platform.

**Verified evidence and limits:**
- EPA identifies aging infrastructure, rising costs, and workforce challenges faced by utilities. [EPA effective water utility management](https://www.epa.gov/sustainable-water-infrastructure/effective-water-utility-management-practices)
- Commercial leak detection and real-time water-network digital twin capabilities exist. [Xylem Vue](https://www.xylem.com/en-uk/catalog/products--services/digital-water/xylem-vue/)
- Water network models can be constructed from EPANET INP files, subject to supported-feature limitations. [WNTR network model documentation](https://usepa.github.io/WNTR/waternetworkmodel.html)
- Process-mining toolkit integrates event-data analysis with Python data-science libraries. [PM4Py research paper](https://arxiv.org/abs/1905.06169)

**Competitor check:** Xylem Vue: Leak detection, network digital twin and operational analytics already exist.; Utility consultants and CMMS prioritization: Existing adoption channel and strong service substitute.

**Integration hypothesis:** Map work-order asset IDs onto EPANET INP links; derive event-log repair distributions; simulate candidate interventions; solve a rolling maintenance schedule. 6-12 engineer-weeks for advisory planning on a single calibrated utility network. This effort is a planning estimate, not a tested result.

**Principal difficulties:** Hydraulic calibration and consistent asset identifiers are prerequisites. Work-order timestamps are often administrative rather than physical work times. Failure and repair histories may be sparse; posterior confidence is not observed safety.

**License finding:** WNTR license text states Revised BSD with third-party notices; PyMC Apache-2.0 plus embedded MIT code; OR-Tools Apache-2.0. PM4Py AGPL service/distribution design needs review. No inference that public utility data are freely distributable.

**Judgment: 62/100 weighted; rejected.** Data access, calibration and purchasing cycle could overwhelm small-utility economics. Incumbent overlap is substantial. No retrospective intervention ranking tested.

**Next falsification test:** With a utility partner, replay 20 past repairs using only information available before each decision. Compare service-loss reduction and total crew-hours against its existing ranker; require a paid decision-support pilot, with utility engineer approval of every recommendation.

### JIG-004: Ecology-aware wind dispatch

**Buyer hypothesis:** Wind operators with wildlife curtailment obligations and colocated storage.

**Combination:** [macaodha/batdetect2](https://github.com/macaodha/batdetect2) — Detect/classify bat calls in ultrasonic audio; [wind-python/windpowerlib](https://github.com/wind-python/windpowerlib) — Estimate generation consequence of operating choices; [PyPSA/PyPSA](https://github.com/PyPSA/PyPSA) — Optimize curtailed output and storage dispatch.

Price wildlife-risk scenarios into storage and turbine decisions, producing an auditable tradeoff record. Hypothesis: coordinated dispatch recovers value under established wildlife constraints.

**Verified evidence and limits:**
- DOE describes an established DARC system, energy lost to blanket curtailment, and the mechanical, warranty, cybersecurity and permitting context of turbine integration. [DOE smart-curtailment technology](https://www.energy.gov/cmei/systems/articles/new-tool-protects-bats-while-increasing-energy-production)
- Acoustic monitoring and smart curtailment are established approaches; efficacy varies by site and species. [DOE birds and bats](https://www.energy.gov/cmei/systems/windexchange/birds-and-bats)

**Competitor check:** Natural Power DARC: DOE already describes real-time wildlife-aware curtailment and complex operational integration.; Vestas bat-protection systems: OEM-integrated control makes an external integration harder; not independently evaluated here.

**Integration hypothesis:** Time-align acoustic detections, weather and turbine output; estimate detection uncertainty; generate advisory curtailment/storage schedules. 8-16 engineer-weeks for retrospective analysis; live operation is a separate engineering project. This effort is a planning estimate, not a tested result.

**Principal difficulties:** Species/geography transfer is unvalidated. OEM interfaces, turbine warranties and safety constraints require site agreements. Only an offline advisory demonstrator is plausible without permissions.

**License finding:** batdetect2 LICENSE.md is Creative Commons Attribution-NonCommercial 4.0. It is publicly available but not an unrestricted commercial OSS building block. Separate permission or a genuinely suitable replacement is required. windpowerlib and PyPSA are MIT.

**Judgment: 54.5/100 weighted; rejected.** Commercial-use license blocker. Existing smart-curtailment systems already address the core benefit. No evidence that storage coupling adds net value after integration costs. windpowerlib last push 2024-02-20 also fails this catalogue activity cutoff; it was included only as an explicitly rejected deeper-screening component.

**Next falsification test:** Only reconsider after securing commercial rights or validating a permissible alternative. Then benchmark offline on partner-provided acoustic and SCADA history against the existing curtailment policy; do not control turbines as part of this research.

### JIG-005: Temperature-excursion salvage dispatch

**Buyer hypothesis:** Perishable-food distributors with independent product-quality validation.

**Combination:** [thingsboard/thingsboard](https://github.com/thingsboard/thingsboard) — Ingest sensor/device temperature histories; [bjodah/chempy](https://github.com/bjodah/chempy) — Compute product-specific reaction/degradation kinetics; [pymc-devs/pymc](https://github.com/pymc-devs/pymc) — Represent uncertain kinetic parameters and remaining quality; [google/or-tools](https://github.com/google/or-tools) — Optimize rerouting and sell-first allocations.

Use uncertainty-aware deterioration estimates to allocate at-risk lots to nearby customers before they spoil. Hypothesis: explicit abstention plus dispatch optimization improves realized recovered value beyond temperature alarms.

**Verified evidence and limits:**
- FAO and UNEP identify ineffective food refrigeration as a major cause of food losses and lost livelihoods. This establishes problem scale, not willingness to pay for this particular software. [FAO sustainable food cold chains](https://www.fao.org/newsroom/detail/amid-food-and-climate-crises-investing-in-sustainable-food-cold-chains-crucial/)
- Vaccine supply chains require product-appropriate temperature monitoring. This is evidence for the problem class, not evidence supporting a food shelf-life model or permission to release exposed vaccines. [WHO temperature monitoring guidance](https://www.who.int/publications/i/item/WHO-IVB-15.04)
- Commercial monitoring, connected devices, and facility/equipment monitoring already exist. [Sensitech cold-chain solutions](https://www.sensitech.com/en/solutions/cold-chain/)
- Supplier explicitly describes analysis of temperature impacts on quality and shelf life; claimed differentiation cannot simply be predictive shelf life. [Sensitech cold-chain logistical services](https://www.sensitech.com/en/media/FDCCLogisticalServicesEN0908_tcm878-132456.pdf)

**Competitor check:** Sensitech: Commercial cold-chain monitoring and time/temperature quality analysis already exist.; Existing FIFO/FEFO inventory and route planners: Operational baseline must be compared, not assumed inadequate.

**Integration hypothesis:** Ingest tagged time/temperature series; apply independently measured SKU kinetic models; generate conservative quality intervals; solve capacity-constrained redistribution. 4-8 engineer-weeks for offline routing with validated non-medical product data. This effort is a planning estimate, not a tested result.

**Principal difficulties:** Temperature does not determine safety/quality without product and pathogen-specific validation. Sensor placement, missing data and lot identity create bias. WHO evidence concerns vaccines and does not establish food-buyer demand or validate this product.

**License finding:** Check ThingsBoard community edition Apache-2.0 separately from commercial modules; ChemPy BSD-2-Clause, PyMC Apache-2.0/MIT and OR-Tools Apache-2.0. Product kinetic data and sensor-provider terms remain unaudited.

**Judgment: 56/100 weighted; rejected.** Data/model validation is the main product, not the OSS integration. Differentiation versus existing shelf-life analytics is unproven. No real recoverable-margin evidence.

**Next falsification test:** Run a blinded historical simulation for one food SKU with validated assays, traceable temperature data, actual orders and disposal costs. Require better net recovered value than FEFO with no increase in quality failures. Never use inferred shelf life to release vaccines or medicines.

### JIG-006: Tailings inspection evidence triage

**Buyer hypothesis:** Independent tailings engineers and mine-closure asset owners.

**Combination:** [insarlab/MintPy](https://github.com/insarlab/MintPy) — Estimate ground displacement time series from preprocessed interferograms; [gee-community/geemap](https://github.com/gee-community/geemap) — Join environmental imagery and site features; [pymc-devs/pymc](https://github.com/pymc-devs/pymc) — Quantify uncertain movement trends; [docling-project/docling](https://github.com/docling-project/docling) — Link inspection reports and action evidence to monitored zones.

Produce traceable inspection-priority packets linking motion changes to historical remedial actions and unresolved documentation gaps. Hypothesis: report-centric integration is cheaper to adopt for closure portfolios than a new monitoring/control stack.

**Verified evidence and limits:**
- Tailings governance, risk classification, environmental protection and disclosure are established needs; not a direct procurement commitment. [UNEP Global Industry Standard on Tailings Management](https://www.unep.org/resources/report/global-industry-standard-tailings-management)
- Incumbent already combines InSAR interpretation, geotechnical expertise, ground instruments and inspection scheduling. Vendor capabilities are self-reported. [SkyGeo mining InSAR](https://www.skygeo.com/insar-for-the-mining-industry)
- Structured document conversion and JSON export exist; correctness on a buyer corpus is untested. [Docling document conversion](https://docling.ai/)

**Competitor check:** SkyGeo: Already provides interpreted mining InSAR, ground-instrument integration and inspection scheduling support.

**Integration hypothesis:** Consume quality-controlled interferogram products into MintPy; attach zone IDs and reviewed report extractions; use uncertainty models to rank items for engineer investigation. 6-12 engineer-weeks for a retrospective engineer-reviewed report prototype; monitoring certification excluded. This effort is a planning estimate, not a tested result.

**Principal difficulties:** MintPy is not a complete raw-satellite-to-certified-warning pipeline. Atmospheric artifacts, radar geometry and decorrelation require specialist QA. Source imagery/commercial service terms and historical reports may be restricted.

**License finding:** MintPy GPL-3.0-or-later and geemap MIT; PyMC Apache-2.0/MIT and Docling MIT. GPL-compatible packaging and separate imagery/Earth Engine commercial-use terms must be checked; open code does not make hosted imagery free.

**Judgment: 58/100 weighted; rejected.** Strong incumbent overlap. No measured engineer-time or inspection-quality benefit. Data rights and scientific interpretation are unresolved.

**Next falsification test:** Have an independent qualified engineer blind-review ten historical inspection periods. Compare useful priority changes, false alarms and report preparation time against the existing workflow. Stop if the packet adds no actionable information; do not market collapse predictions.

### JIG-007: Flood-aware accessible evacuation rehearsal

**Buyer hypothesis:** Local emergency planners and paratransit operators conducting pre-event exercises.

**Combination:** [pyswmm/pyswmm](https://github.com/pyswmm/pyswmm) — Evaluate drainage-state scenarios; [valhalla/valhalla](https://github.com/valhalla/valhalla) — Construct road-routing costs with local accessibility attributes; [opentripplanner/OpenTripPlanner](https://github.com/opentripplanner/OpenTripPlanner) — Represent transit schedules and wheelchair-accessible itineraries; [google/or-tools](https://github.com/google/or-tools) — Allocate assisted-transport vehicles under capacity and shelter constraints.

Combine flood-sensitive access, accessible transit and wheelchair-vehicle capacity into rehearsal plans that expose who would be left without transport. Hypothesis: this identifies planning gaps missed by aggregate evacuation clearance times.

**Verified evidence and limits:**
- Accessible transportation and advance coordination with local government/paratransit are explicitly identified needs. [CDC sheltering and evacuating](https://cdc.gov/disability-emergency-preparedness/people-with-disabilities/sheltering-and-evacuating.html)
- Established public-sector decision support calculates evacuation timing using storm threats and clearance information. [HURREVAC key features](https://www.hurrevac.com/program-information/key-features/)
- Python interfaces can read node/link simulation states; this does not itself provide street-level flood depths or safe-route certification. [PySWMM quick start](https://pyswmm.github.io/pyswmm/quickstart.html)

**Competitor check:** HURREVAC: Established evacuation timing and storm-planning decision support; exact accessibility allocation features not audited.; Consultant-run tabletop exercises: Existing and potentially sufficient substitute.

**Integration hypothesis:** Use locally validated flood closures, not raw SWMM node overflow alone; modify routing graph; join GTFS accessibility fields and reviewed demand locations; optimize vehicle and shelter assignments. 8-12 engineer-weeks for synthetic/offline rehearsal in one locality; operational dispatch excluded. This effort is a planning estimate, not a tested result.

**Principal difficulties:** A drainage model does not directly produce validated street flood depth. Wheelchair access tags and real-time shelter/vehicle status can be incomplete. Personal assisted-transport demand is sensitive and often unavailable.

**License finding:** PySWMM BSD-2-Clause, Valhalla MIT, OpenTripPlanner LGPL-3.0-or-later and OR-Tools Apache-2.0 from primary license-text checks. OSM/GTFS/local flood and sensitive resident datasets carry separate obligations not audited here.

**Judgment: 56.5/100 weighted; rejected.** Social impact does not establish a purchasing budget. Missing accessibility and flood data can make the result misleading. Integration and operational acceptance not demonstrated.

**Next falsification test:** Use a municipality-approved synthetic demand set plus audited access/vehicle data for a tabletop exercise. Compare unserved wheelchair users and clearance constraints with the current plan; require planner acceptance and a defined procurement budget before product work.

## Recommended next research

The strongest follow-ups are JIG-001 and JIG-002, because a bounded historical project can test economic benefit before building a platform. This is a choice of research experiment, not an accepted business. Contact and data access should be explicit, consensual next steps; none were attempted here. A negative result should remain published in the rejection ledger.

## Files and reproducibility

- `catalogue.json`: the 1,320 topic-search records and query provenance.
- `search-log.json`: all 30 exact queries, result counts, timestamps and incomplete-result flags.
- `collector.py` and `fields.json`: reusable stdlib + authenticated `gh` collector; records public metadata only. Run `python3 collector.py --output ./capture`.
- `component-evidence.json`: 19 direct component records, license-source URLs and manual findings.
- `sources.json`: 22 external primary-source/vendor findings with URLs and retrieval time.
- `candidates.json`: seven explicit hypotheses, components, evidence, competitors, integration limits, license findings, scores, gates and kill tests.
- `metrics.json`: machine-readable scope counts.

Raw GitHub responses and downloaded license texts were used locally for inspection. Do not publish `raw-*.json`, `*--LICENSE.txt`, `*--COPYING.txt`, or the one-off drafting scripts. No source code or README text needs to be copied into the public research artifacts. Repository links and metadata are sufficient.
