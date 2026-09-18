# Prospective test skeleton — not preregistered or executed

This is an implementability proposal. Exact models, budgets, numerical thresholds and a practical advantage endpoint must be fixed before comparative fitting. It is deliberately not a preregistration: the service benefit is still underspecified.

## Available inputs and possible split

Eight local XLSX files have verified source MD5 checksums and recorded SHA256 hashes in download-manifest.json. Both datasets use CC BY4.0. The inaccessible original2023 dataset is excluded.

Use the two accessible formulations independently. A possible split, selected only from named conditions:

- Benzoxazine cure: hold out5°C/min,160°C and180°C; fit2.5/10°C/min and150/170/190°C.
- Coating cure: hold out2°C/min and110°C; fit1/1.5/2.5/3°C/min and100/120/130°C.
- Coating fully cured relaxation: hold out210°C; fit190/200/220°C. One curve cannot establish general uncertainty coverage.

Do not add chemoviscosity or Tg to a coupled predictor without a physical dependency specified before fitting. Their availability alone does not justify coupling. No curves were plotted; paper summaries and worksheet headers/first rows were inspected. This can be a prospective code evaluation, not a claim of researcher blindness.

## Strong practical comparison

Baseline: competent multistart fitting of the established extended autocatalytic/diffusion model using KinOpt or an equivalent correct implementation, with identical units, preprocessing, weights, temperature interpolation and initial conversion information. The articles' all-data parameter tables are reproduction references, not leakage-free held-out fits.

Candidate: the same calibrated physics packaged into a checked material card, compiled rate/derivative callback, and fit-domain/provenance report. If a different fitting or uncertainty mechanism is proposed, specify it prospectively and include an ablation. Without one, accuracy superiority should not be expected.

Relaxation baseline: a conventional temperature-shifted Prony model and simpler Arrhenius single-relaxation-time model, selected on calibration data. Candidate pyvisco receives the same observations and initial-modulus information. State the absence of an independent strain-amplitude linearity check.

Export baseline: a correctly authored manual card or native export. Corrupted coefficients or wrong time units are fault-injection cases, not representative competitor quality.

## Supported measurements

1. Whole-experiment conversion MAE, evaluated at uniform time points and averaged equally across experiments; reaction-rate error reported separately with fixed normalization.
2. Time-to-conversion error only where the measured trace actually crosses the selected conversion; report censored cases explicitly.
3. Normalized relaxation-modulus error; report absolute amplitude error if amplitude is predicted. Do not relabel bending modulus as shear modulus.
4. Independent compiled callback agreement with the reference equation over a declared state/temperature domain, including derivative checks and singular/out-of-domain cases.
5. Artifact completeness: source hashes, unit conversions, model identity, coefficients, domain, initial state, uncertainty assumptions, interface version, replay cases, missing properties and approval status.

A partial-cure Tg cross-check requires independently inferred conversion and prospectively fixed Tg extraction. It cannot generate its label from the kinetic model being tested.

## Missing practical advantage endpoint

A useful handoff test could measure equal predictive accuracy with less engineer setup/review work. It requires representative tasks, an independent reviewer, fixed completion criteria, counterbalanced order and active-work timing. Compare against existing KinOpt/native-export/templates, not blank-page coding. No participants or customer inputs are arranged.

An alternative technical endpoint is greater accepted prediction coverage at a fixed decision-error budget. That requires an explicit buyer-grounded decision threshold and enough independent schedules. Neither is established here. Arbitrary synthetic limits would not establish buyer utility.

## Limits and next gate

No part-level manufacturing-stress, temperature-gradient, warpage, flow-front or defect claim. A standalone UCURE-signature harness does not certify execution in Abaqus. No scrap, cycle-time or revenue claim.

A future40-hour/14-day/<$1000 trial could cover a narrow adapter and comparative handoff exercise with already-owned lab files. It cannot cover new material characterization or industrial certification. Before starting: obtain a concrete task and participant access; fix the advantage endpoint; pin dependencies and licenses; freeze the protocol; then implement and evaluate. No spend, outreach or evaluation occurred.
