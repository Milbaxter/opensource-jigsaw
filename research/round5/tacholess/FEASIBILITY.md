# Tacholess speed recovery: bounded feasibility screen

**Decision: HOLD, despite usable primary data.** A librosa/Astropy integration is technically plausible, but no differentiated buyer-relevant benefit was established over competent multi-order tracking and existing reviewed workflows. No estimator, RPM decoding, prototype, benchmark or performance evaluation was run. Schema inspection alone is not an executed essential bridge.

## Verified primary input and ground-truth boundary

The [Ottawa v2 dataset](https://data.mendeley.com/datasets/v43hmbwxpm/2), DOI `10.17632/v43hmbwxpm.2`, is released by Huan Huang and Natalie Baddour under **CC BY4.0**. Its publisher describes 60 ten-second trials at 200kHz: five bearing conditions, four speed profiles, three repetitions. `Channel_1` is accelerometer data; `Channel_2` is encoder data, with 1,024 cycles/revolution. Version1 has only36 trials; do not mix version descriptions.

Normal public metadata/file API attempts were partly blocked (403), and this agent's computer-use tool had no browser. The parent accessed the ordinary public v2 interface without login/CAPTCHA and supplied its visible download link. That exact primary link downloaded successfully:

- `H-A-1.mat`, **11,909,642 bytes**.
- SHA256 `a113089dac7969eaf3e2adc563aa724a523f5d7ef4b3dd957bdf111ac1d84257`.
- MATLAB5 file with `Channel_1` and `Channel_2`, each `float64` shape `(2000000,1)`, all finite.
- Channel2 range about−0.083 to4.421 and inspected leading values are pulse-like voltage levels, **not already an RPM vector**. This interpretation still needs a frozen decoder before evaluation.

`schema-inspection.json` records these observations and its exact inspection-script hash. No signal-derived speed, order spectrum or prediction was computed. Only this primary trial was downloaded; full-dataset availability has not been exhaustively verified.

A separately attributed GitHub mirror `H-C-1.mat` was downloaded before primary access was resolved. It has compatible schema, but its identity against an official v2 file was not checked. It is excluded from the proposed benchmark input path and publication payload. Its repository MIT license does not replace the original data's CC BY4.0 terms.

Future truth extraction must freeze pulse polarity/threshold or hysteresis, 1,024-cycle interpretation, interpolation, timestamp alignment, edge trimming and invalid-pulse rejection. Counting both edges without adjusting the denominator would create a factor-two error; assuming quadrature decoding from a single recorded channel would be unjustified. [MATLAB tachorpm](https://www.mathworks.com/help/signal/ref/tachorpm.html) provides a useful independent decoder specification and explicitly warns that pairing pulse edges incorrectly can distort RPM. The encoder must remain inaccessible to the estimator, window selection and test-time tuning. Entire trials/conditions should be split, not overlapping windows from one record. H-A-1 is now inspected development material, not untouched holdout data.

## Strong alternatives

| Alternative | Primary evidence and consequence |
|---|---|
| Dewesoft signal tracking | [Current manual](https://manual.dewesoft.com/x/setupmodule/modules/machinery/ordertracking) includes multiple dominant orders, acceleration constraints, adjustable windows and automatic initial RPM. The simple strongest-FFT-peak tutorial is an inadequate comparison. Licensed module/hardware requirements establish a commercial offering, not an entrant-specific price or unserved workflow. |
| MATLAB rpmtrack | [Official implementation description](https://www.mathworks.com/help/signal/ref/rpmtrack.html) combines user-guided ridge points, STFT or synchrosqueezing, crossing/jump penalties and Vold–Kalman refinement; it exports generated scripts. A reviewed batch workflow is not new merely because it is implemented in Python. |
| Ottawa MTFCE | [Authors' 2019 MethodsX paper](https://www.sciencedirect.com/science/article/pii/S2215016119301402) supplies MATLAB dynamic-path multi-curve code, raw/envelope branches, and frequency-ratio consistency for identifying speed and fault components. It was tested on the original36-trial release. Supplementary code rights were not independently cleared; do not silently bundle it as permissive OSS. |
| Weighted multi-order Viterbi | [WMOVA2024](https://doi.org/10.1016/j.ymssp.2024.111187) specifically addresses fading/crossing harmonics, strong noise and speed variation. Harmonic weighting followed by temporal decoding is close prior art to the proposed music transfer. |
| Adaptive multi-order methods | [Adaptive MOPA2025 publisher article](https://www.sciencedirect.com/science/article/pii/S0888327025000238) and [author preprint](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4956437). These describe adapting frequency bands to reduce interfering neighboring harmonics. No executable repository/license was verified. |

A future numerical comparison needs a faithful multi-order probabilistic/dynamic-ridge implementation, tuned within the same development budget, plus the simpler fixed/multi-order ridge baseline. Inaccessible commercial software can be documented and a proxy labeled; absence of a direct run cannot become superiority over the product. A GitHub repository-name search returning zero for “tacholess” does not establish absence of OSS.

## Concrete transfer and why it does not yet earn a build

A plausible bridge is: original time-stamped vibration → short local frames → **Astropy multiharmonic least-squares scores** across physically admitted rotational frequencies → normalized candidate-emission matrix → **librosa Viterbi sequence decoding** with physically declared transition constraints → a reviewed RPM/validity trace and an order-domain report. pYIN could instead supply a periodicity candidate branch, using raw or envelope signals. Its music-specific frequency limits, transition rates and periodicity priors cannot be used uncritically.

This has exact interface compatibility: Astropy supplies per-frame frequency scores and librosa consumes state-by-time observation likelihoods. However, normalized spectral fit scores are not automatically statistically valid likelihoods, and adding the two libraries does not create a new capability if ordinary harmonic regression plus dynamic programming provides the same result. The astronomy advantage for uneven sampling is not exercised by Ottawa's regularly sampled records. Artificially dropping samples would test a synthetic corruption, not establish an observed customer problem.

Two important source-level limits:

- [Astropy documentation](https://docs.astropy.org/en/stable/timeseries/lombscargle.html) distinguishes noise-only false-alarm probability from correctness of the chosen peak. Exact pinned source additionally **raises NotImplementedError for false-alarm probability when `nterms != 1`**. Thus a multiharmonic fitter plus built-in FAP is not an available calibrated harmonic-identity estimator.
- [librosa pYIN](https://librosa.org/doc/0.9.2/generated/librosa.pyin.html) estimates periodic fundamental candidates and voicing state using Viterbi. A high voiced probability is not a probability that the inferred frequency is the physical shaft fundamental. Consistent wrong harmonics can remain confidently periodic. Exact current source was inspected separately from this versioned API documentation.

No celerite dependency is justified here. Smoothing alone cannot identify the correct shaft harmonic, and a third library would add maintenance without an established essential contribution.

The strongest surviving **hypothesis**, not demonstrated differentiation, is an offline recovery/review package for vibration-service analysts handling archived records with missing or unreliable tachometer channels: expose competing harmonic interpretations, abstain on ambiguity and export a reviewed trace to their existing analysis stack. Its possible benefit is fewer manual ridge corrections at fixed accepted-trace error and usable coverage. The current sources do not show how often this work recurs, how much time it costs, whether existing automatic modes already suffice, or willingness to pay for a separate tool. No calibration guarantee, diagnostic reliability or labor-saving claim is made.

Before any protocol, require a concrete prospective buyer workflow and a same-input baseline task. If the benefit is operator effort, measure operator corrections/time against their competent existing workflow. For accuracy/abstention, freeze equal-coverage or coverage-risk metrics, compare calibration on whole unseen trials, and count wrong-harmonic acceptance. A beautiful trace or lower synthetic RMSE alone would not test the proposed purchase. No protocol is frozen because this claim-to-test link remains unsupported.

## Rights and pins

- librosa: ISC, commit `6d6c380687a27aaef2d77842c0d3356d598d44f8`; `core/pitch.py` and `sequence.py` inspected.
- Astropy: BSD3-Clause, commit `61b2d9c01ef7f9a9b32d138b669a2d7636fc5d18`; LombScargle `core.py` inspected.
- These are research source pins, not installed/executed dependency versions. Exact license files were fetched at those commits. A future executable lockfile requires separate rights/dependency review.
- Primary Ottawa data: credit Huang/Baddour, dataset title, v2 DOI and CC BY4.0 link; identify any derived/modified outputs and avoid implying author endorsement. Publication manifest excludes the raw MAT payload; provenance contains its official redownload link and hash.

## Better adjacent reserve lead

[MOIRA-UNIMORE independent-cart data](https://zenodo.org/records/14753683) is a more specific industrial setting: stationary vibration sensors, recorded positions/speeds/current for individual moving carts, and physically introduced bearing faults. Its API confirms **CC BY4.0**. Tetra Pak coauthors establish industrial participation, not purchase intent. One possible narrower problem is assigning suspicious vibration to the cart that should be inspected. Position-conditioned source separation from acoustics could be relevant where passages overlap; a nearest-cart or windowed passage-gating baseline may already solve it. The exact multi-cart fault identities and overlap cases must be inspected before claiming a gap.

This adjacent lead is **metadata-screened only**: the first official record contains10.8GB and27.6GB archives, not a conveniently verified small benchmark. No large archive was downloaded and no signal was evaluated. Separate bounded description/archive inspection is the next step. The Lenze-MB alternative has industrial author evidence and existing-drive signals, but its exact dataset license is CC BY-NC4.0; it is excluded from a presumed commercially usable data path. A second USP rotor dataset has CC BY4.0 and an optical reference, but is less distinctive than cart attribution.
