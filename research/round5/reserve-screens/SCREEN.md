# Three reserve combinations, screened before performance

No protocol or performance experiment was run. These are three distinct hypotheses with explicit data and incumbent checks, not pursuit passes. Only the 3.4 MB Andasol CSV was downloaded and inspected for schema; no target distribution or predictive model was computed.

## 1. Resurvey-route triage for mobile mapping

**Combination:** RTKLIB residual/solution parsing + ruptures change-point segmentation + OR-Tools route/interval selection. Necessary transfer: turn correlated navigation-quality failures into contiguous, operationally usable reacquisition segments, rather than sending surveyors a long list of suspect epochs. Candidate benefit: fewer route meters requiring reacquisition at a fixed rate of missed out-of-tolerance segments. This is a planning/review claim, not a new GNSS estimator.

**Measured reference first:** [UrbanNav](https://github.com/IPNL-POLYU/UrbanNavDataset) provides raw RINEX, motion sensors and a separate SPAN-CPT postprocessed reference. Its published License heading currently contains contact details rather than a clear reuse grant. Moreover, another GNSS/INS device is not perfectly independent truth in the same multipath environment. The [Hilti-Oxford benchmark](https://huggingface.co/datasets/Hilti-Research/hilti-slam-challenge-2022) has independently surveyed reference positions, but explicitly restricts use to noncommercial purposes. Neither clears the proposed commercial demonstration gate without further rights/data work.

**Paid workflow and strongest alternatives:** [Trimble POSPac](https://applanix.trimble.com/en/software/applanix-pospac-complete), [POSPac Assure](https://applanix.trimble.com/en/services/applanix-pospac-assure) and [LiDAR QC](https://applanix.trimble.com/en/software/applanix-lidar-qc-tools) already offer processing, quality reports and trajectory improvements. Candidate must beat existing quality flags followed by contiguous-interval merging and route planning, on identical inputs. A separate tool must justify an actual handoff gap. No measured review burden or absent incumbent feature was established.

**Screen:** HOLD. Data rights and reference independence are unresolved; a generic automatic QC report is already sold. No large sensor bags downloaded. Exact component integration and licenses remain unverified because this screen failed first.

## 2. Fewer manual mirror-gloss inspections for a solar thermal O&M crew

**Combination:** pandas ingestion + scikit-learn spatial/operational regression + CVXPY decision-focused inspection allocation, with a route constraint only if true access geometry exists. Necessary transfer: use finite-population sampling and decision uncertainty to choose which collectors need physical measurement before accepting a field-cleaning decision. It would produce a reviewable inspection list, not directly automate washing.

**Measured reference first:** [Andasol-3](https://zenodo.org/records/7061913) has actual gloss-meter readings, collector positions, cleaning age and operational/weather features. API confirms CC BY 4.0. Downloaded CSV: 8,116 rows, 3,418,752 bytes; publisher MD5 matches. Exact hash and schema in soiling-schema.json. The [authors’ paper](https://publikationen.bibliothek.kit.edu/1000159386/150926096) describes recurring physical measurements at 40 predefined locations per subfield, approximately every two days. Gloss is explicitly a surrogate for soiling, not direct specular reflectance or realized energy recovery.

**Concrete benefit and blockers:** Compare manual readings required to estimate a prespecified field-level gloss quantity/decision at fixed error against stratified random sampling, spatial coverage and ordinary uncertainty sampling. This could measure a real physical-inspection count, without invented labor minutes. However, the public CSV drops absolute dates/year despite covering 2015–2017. A defensible same-day sampling frame and future-date holdout cannot currently be reconstructed from documented columns. Do not infer dates from row order or repeated seasonal encodings.

**Paid category and alternatives:** [Solar Unsoiled](https://www.solarunsoiled.com/) and [Suncast](https://www.suncast.cl/servicios?lang=en) sell PV soiling/cleaning analysis; this is adjacent commercial evidence, not proof of demand for solar-thermal gloss inspection. Existing Andasol operational-data regression is a direct baseline. PV [RdTools](https://rdtools.readthedocs.io/en/stable/generated/rdtools.soiling.soiling_srr.html) already estimates soiling with stochastic uncertainty. PV economics cannot be imported into CSP without validation.

**Screen:** Most concrete measured inspection workflow of the three, but HOLD pending dated sampling frames and buyer confirmation that fewer gloss readings are an acceptable deliverable. No model fitted, no retrospective threshold selected, no cleaning savings claimed.

## 3. Measurement planning for professional acoustic calibration

**Combination:** pyfar response processing + a Gaussian-process acoustic field model + OR-Tools measurement-order planning. Necessary transfer: optimize acquisition count and movement under a reconstruction-error target. Candidate practical output is the next microphone position and a coverage report; an open-loop fixed mic grid is the basic alternative.

**Measured reference first:** [MeshRIR](https://www.sh01.org/MeshRIR/) supplies CC BY 4.0 impulse responses measured by a Cartesian robot on dense grids, with true positions and NumPy/MATLAB data. The spatial field is independently measured rather than generated by the proposed model. Its regions are only about one meter across, inside a room. That can validate interpolation on a compact area, not room-wide commissioning travel savings.

**Paid workflow and existing mechanism:** [Smaart Suite](https://www.rationalacoustics.com/products/smaart-suite-v9-subscription) costs $399/year and supports professional sound-system alignment and measurement. But MeshRIR already ships GP/MSE-based sensor selection, and [optimal sensor placement](https://doi.org/10.1186/s13636-024-00364-4) is established. The strongest baseline must include that selection method, not merely a uniform grid. [Multi-Sub Optimizer](https://www.andyc.diy-audio-engineering.org/mso/html/) and [miniDSP’s workflow](https://www.minidsp.com/applications/subwoofer-tuning/minidsp-multi-sub-optimizer) already turn multiseat measurements into optimized filters. Selling another response optimizer is not the proposed gap.

**Screen:** HOLD as a business experiment. Dense measured truth and permissive rights are good, but route savings in a one-meter robotic patch are not a credible stand-in for a professional calibration visit. A specific acquisition workflow and representative measured region would be necessary. No archive downloaded or signal processed.

## Next choice

Resolve the Andasol date/sampling-frame provenance only if a source already exposes it; otherwise move on. The narrow inspection-count claim is more testable than pretending the public data gives cleaning profit counterfactuals. None of these screens warrants retroactive threshold changes, a forced numeric score, or immediate performance execution.
