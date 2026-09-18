# Thermoset calibration-to-material-card: deeper feasibility audit

**Decision: a rigorous, narrow material-response and export-verification test is possible with public files now; the proposed manufacturing-stress or economically superior handoff claim is not yet testable from these files alone. HOLD as a pursuit candidate. No performance evaluation, fit, model selection, or comparison was run.**

This corrects the earlier overly broad data objection. Multiple independent temperature schedules really are available. Established physics is entirely acceptable for a commercial engineering service. The unresolved issue is a measurable integration advantage over a competent existing workflow, rather than a need to invent another cure model.

## 1. Exact input access and rights

Original DOI **10.17862/cranfield.rd.22890563** is valid. DataCite resolves it to `https://dspace.lib.cranfield.ac.uk/handle/1826/22017`, following a repository migration. The old Figshare article API returns404; the current DSpace web/API endpoints return403 in this environment. These are access observations, not proof of withdrawn data. `datacite-original.json` preserves metadata, attribution and explicit **CC BY4.0** rights. Its description names:

- DGEBA/4-APDS cure: four dynamic DSC schedules,1.25/2.5/5/10°C/min; seven isothermal schedules,140–200°C at10°C increments.
- Viscosity: five isothermal experiments,80–120°C.
- Stress relaxation: five isothermal experiments,180–220°C, recording time,temperature,stress,strain and modulus.
- Eighteen Tg scans after different partial-cure histories, including several ramps and150°C holds.

The metadata establish scope and reuse rights, but the original measurement bytes could not be inspected. Do not claim those files are locally runnable.

Two related primary studies provide accessible alternatives. All eight workbooks have been downloaded; file hashes, worksheet names, first header/data rows and worksheet dimensions are recorded in `schema-inspection.json`. This was schema inspection only, not outcome analysis.

| Formulation | Primary dataset and rights | Locally inspected content |
|---|---|---|
| Aerospace benzoxazine DHPDS-a | https://doi.org/10.6084/m9.figshare.28105523 ; Figshare explicitCC BY4.0 |8 cure sheets:2.5/5/10°C/min and150/160/170/180/190°C;4 low-conversion viscosity sheets100/110/120/130°C;2 additional high-viscosity cure-rheology sheets130/150°C;11 Tg scans. Four files,~5.3MB. |
| Coating DGEBA/MHHPA/TEOA | https://doi.org/10.6084/m9.figshare.29053802 ; Figshare explicitCC BY4.0 |9 cure sheets:1/1.5/2/2.5/3°C/min and100/110/120/130°C;4 viscosity sheets80/90/100/110°C;4 stress-relaxation sheets190/200/210/220°C;10 Tg scans. Four files,~372kB. |

The cure data are **processed time/temperature/conversion/rate data**, not raw heat-flow traces for independently redoing the cure integration/baseline correction. The Tg data contain heat-flow scans. The benzoxazine viscosity files use seconds; the coating viscosity files use minutes. Coating relaxation sheets contain MPa stress/modulus and percent strain, plus a normalized modulus column. These are realistic adapter requirements, not evidence that existing software cannot handle units.

Important boundary observations from headers/first rows: benzoxazine isothermal traces begin at differing, already substantial conversion (e.g.190°C starts near0.50); a fair replay must state its initialization assumption and offer identical initial-state information to both methods. One must not falsely claim prediction from uncured resin when using measured initial conversion. Coating relaxation applies about3% strain; the study did not provide a strain-amplitude sweep establishing the full linear-viscoelastic domain. Dataset descriptions contain occasional count/name inconsistencies, so inventory should derive from actual worksheet manifests.

## 2. What constitutes independent validation here

An entire temperature/ramp experiment can be withheld from fitting. Different time samples of one experiment cannot be split randomly: that would be severe leakage. Two different formulations can test whether the automation repeats, but their parameters must be fit separately. They are not interchangeable calibration/validation specimens.

The articles fitted their reported equations to their experimental sets. Their published parameter tables therefore encode all schedules and cannot be used as a leakage-free baseline for a new held-out fit. They can serve as a labelled reproduction reference. Public plots and reported outcomes have already been read; this is prospective held-out evaluation of new code, not a claim of researcher blindness.

The independent relaxation temperatures support testing **fully cured specimen relaxation**. They do not validate residual stresses developing during cure. These vitrimers exhibit dynamic bond exchange; treating them automatically as an ordinary thermoset with fixed irreversible gel behavior is unsound. No measured through-thickness manufacturing temperatures, independently measured part warpage/residual stress, simultaneous evolving modulus/cure shrinkage, or thermal conductivity/heat-capacity measurements for these exact batches were found in the audited releases. Assigning those quantities from another resin to manufacture an FE result would create assumptions, not experimental validation.

A FE solver could consume a material card and establish numerical verification. In a homogeneous prescribed-temperature DSC replay, an ODE is already sufficient. Adding FE merely to solve that problem would not make it an essential cross-field component. The NIST packaging dataset from the earlier screen is a different material and cannot close this gap.

## 3. Actual OSS bridge rather than decorative libraries

A substantially better fitting component than the initial pkynetics guess was found: **alan-tabore/KinOpt**, BSD3, JOSS2026, commit `059bc7ba633a2fc53e5e4575ea4f11fffa02ad01`. Its inspected source has Kamal kinetics, vitrification/WLF terms, DiBenedetto Tg, coupling laws, global/local optimization and integration. It already supplies derivatives of its ordinary Kamal model. Thus merely adding a symbolic derivative of that same built-in model is not a useful new bridge.

The Cranfield published models have an extended autocatalytic rate with diffusion/logistic terms and different exponents; those exact equations are not equivalent to assuming stock Kamal. KinOpt accepts added rate functions, so an adapter is feasible, but needs implementation and validation. Source and BSD license saved. No installation/performance claim is made.

**NatLabRockies/pyvisco**, BSD3 directlicense, commit `b61b5a0c6a2939927c87189972ea5619503bd813`, fits generalized-Maxwell Prony series and time-temperature shifts. This is a genuine candidate for the fully cured relaxation part. It is not a ready-made constitutive model for an evolving vitrimer during cure. The four coating relaxation temperatures provide a small but real held-out check, subject to the linearity/domain limitation.

**sympy/sympy** could compile a single checked mathematical rate expression and its state/temperature derivatives into Python and C/Fortran callback artifacts. The commercial Abaqus UCURE interface publicly requires rate plus both derivatives. Such a compiler is more than copying a coefficient table, but the API is already documented and manual implementation is a strong practical comparator. SfePy/BSD3 can be an open numerical host if a useful thermo-mechanical problem and inputs are subsequently obtained. Full Abaqus execution is unavailable without a license; a compiled standalone UCURE-signature harness is not an Abaqus integration certification.

**OpenTURNS or PyMC** could carry uncertainty into predictions, but simply adding them is insufficient differentiation. The2026 primary paper below already treats multi-step calibration uncertainty and finite-element propagation using FOSM versus Monte Carlo. Whole-experiment resampling/parameter covariance are necessary practical baselines. The small number of independent schedules cannot support a precise universal uncertainty-coverage guarantee. OpenTURNS has bothCOPYING and a licensing context requiring further audit; do not mislabel it from theGPL text alone. Exact dependency/release audits remain a preimplementation gate.

A separate real OSS process solver, **FAST-LB/of-rtm-6**, has resin-transfer-molding examples and cure/viscosity coupling. Its model conventions, solver inputs, license context and build have not been fully audited. No assumption that it accepts the Cranfield model directly is warranted. Its inspected cure transport file alone does not establish the complete constitutive pathway.

## 4. Buyer artifact and paid category

Proposed deliverable to an independent composite-process engineering consultancy or resin-formulation lab: a versioned calibration package per formulation/batch consisting of original measurement hashes; units and preprocessing ledger; fit-domain report; parameter card and covariance/ensemble; solver-ready rate/derivative callback; representative replay cases; independent-schedule errors; explicit unsupported parameters; and signed-off material-model revision history. Repeated formulation changes or new batches can make this repeat work. A customer still needs to supply or commission the physical measurements.

Direct suppliers demonstrate a paid category, not an entrant conversion rate:

- NETZSCH Kinetics as a Service explicitly delivers laboratory measurements if needed, model creation, predictions, and optimized temperature programs: https://kinetics.netzsch.com/en/kinetics-as-a-service . Quote only.
- Convergent explicitly sells characterization and material models for thermo-chemical, flow, and stress/deformation analysis. Its full viscoelastic stress package requires the thermo-chemical model: https://www.convergent.ca/node/25 . Quote only.
- Intertek provides composite development programs including cure-time optimization and processing defects: https://www.intertek.com/polymers-plastics/composite-development/ . Quote only.

No exact comparable model-handoff price, buyer-origin purchase order, entrant willingness-to-pay, or measured engineering labor saving was established. A low-price standalone DSC test is not a defensible price proxy for a validated multi-physics material card. Any proposed fixed-fee service price is a hypothesis. Supplier marketing estimates of industry loss must not be presented as observed customer economics.

Close practical alternatives are substantial. NETZSCH already exports model equations and parameters toASCII, supports external-instrumentASCII inputs, and connects Kinetics Neo models to Termica Neo simulation. Convergent uses common material databases across its software and offers full characterization. Abaqus has built-in Kamal/Grindling cure models and a documented user model interface. Veryst/MCalibration already automatically exports calibrated parameters into Abaqus/CAE and ANSYS Workbench; Axel Products sells native-model calibration and sometimes teaches customers to fit future datasets; Huntsman provides resin characterization and process simulation assistance. These further support the paid category and strengthen the practical comparator. The correct competitive claim is therefore an independently checked, portable engineering handoff with measured lower setup/review effort, not “incumbents cannot export” or “nobody combines these measurements.”

## 5. Is a rigorous test possible?

**Yes for predictive validity and export correctness.** A protocol can withhold entire temperatures/ramp schedules, fit only the remaining experiments, generate a card, and replay it in an independently compiled implementation. Strong baselines: KinOpt/competent multistart fitting of the same model with the same data, ordinary Arrhenius-shift/Prony fitting for relaxation, and an engineer's manually authored solver card. Both methods receive the same initial conversion, preprocessing, temperature interpolation and data weights. The paper's all-data coefficients are reproduction references only.

**Not yet for the required practical advantage.** Identical equations and parameters exported correctly should predict the same result. Numerical equality is valuable verification but is not an improvement over a competent handoff. A defensible improvement would be less measured engineer setup/review time at equal accuracy and artifact completeness, or better held-out prediction/calibrated decision coverage from a specified mechanism that beats the strong same-input comparator. No such measured benefit has been established. The current evidence does not justify inventing an expectedaccuracy advantage or testing against a deliberately wrong unit conversion.

A capped future workflow experiment could compare manual KinOpt+documentedsolverhandoff versus the integrated package on the two datasets, with independent engineers or genuinely timed analyst runs, predeclaredtaskorder and reviewchecklist. However, building the prototype and then timing oneself on the already-known files creates an experience advantage. A meaningful human-effort experiment needs a predeclared crossover or separate unfamiliar analysts and another untouched input package. No outreach occurred and no analyst population has agreed to participate.

**Recommendation to parent:** preserve this as an improved, technically plausible service lead rather than claim a failed scientific idea. We have removed the “no multi-schedule data” blocker. The next decision should be whether to secure a concrete repeat handoff task and comparative work-effort test, or find public independent part-level thermomechanical data for a more ambitious mechanism. Do not spend a long prototype merely to obtain equal curve predictions and call that pursuit-grade advantage.

No scored PursuitReview or performance preregistration is issued: the current bounded task was feasibility, and an honest practical-advantage endpoint is still missing. `TEST-DESIGN.md` records a prospective design skeleton explicitly NOT frozen and NOT executed.
