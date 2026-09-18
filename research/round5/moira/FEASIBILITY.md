# MOIRA cart attribution: hold before experiment

Decision: **HOLD** the position-conditioned source-separation lead. No estimator, performance evaluation, or archive download was run. This is a data/claim compatibility screen, not a judgment that the industrial problem is solved or commercially unimportant.

## Decisive identification problem

The [dataset paper](https://doi.org/10.3390/app15073691), Remark 3, specifies that the faulty cart is always the middle cart M2 in the three-cart experiments, with only one bearing fault at a time. The dataset contains synchronized positions and vibration, controlled defects, several separations and speeds, and healthy recordings. It does not vary faulty cart identity. Consequently, an attribution score among faulty runs can be saturated by a constant-middle rule. Renaming channels cannot remove that physical shortcut. The reported data description also does not establish isolated, simultaneous source waveforms as separation ground truth.

This is a mismatch between the proposed claim and available variation, not a claim that position gating certainly solves real industrial attribution. Healthy-versus-faulted detection remains possible, but would be a new, narrower experiment requiring its own buyer claim and protocol. No forced classifier proposal is advanced here.

## Practical problem and paid category

The [ISMA 2024 authors](https://past.isma-isaac.be/downloads/isma2024/proceedings/Contribution_573_proceeding_3.pdf) describe interference from nearby carts and other mechanical activity, and motivate localization across large fleets. Their own reported experiment is single-cart anomaly detection, not demonstrated fleet attribution. The primary PDF was downloaded and verified as a 14-page PDF; its hash appears in research-provenance.json.

[Tetra Pak sells asset-health monitoring services](https://www.tetrapak.com/en-gb/solutions/services/service-offerings/asset-health-monitoring), including sensor/network setup, OEM interpretation, dashboards and actionable notifications. This establishes a paid maintenance category. Its [separator case](https://www.tetrapak.com/content/dam/tetrapak/media-box/global/en/services/maintenance-service-packaging/predictive-maintenance-packaging/documents/Case%20Predictive%20Maintenance%20Seperators.pdf) is an adjacent supplier-reported example, not cart-specific willingness to pay, avoided loss or obtainable margin. Tetra Pak employees coauthoring the dataset is not independent customer demand.

Possible user: a packaging OEM condition-monitoring engineer preparing a reviewed suspect-mover list for service. Acquisition would require synchronized stationary vibration and controller positions, permission to export production data, and actual maintenance confirmation. The public laboratory data does not establish an accessible paying validation population.

[Beckhoff's XTS software](https://www.beckhoff.com/en-us/products/motion/xts-linear-product-transport/xts-software/) already supplies extensive diagnostics and motion variables. [Leave/Arrive](https://infosys.beckhoff.com/content/1033/xts_software/14320620811.html) supports removal and return of movers for service. These support a plausible maintenance integration path; neither source establishes an unmet bearing-attribution purchase.

## Necessary bridge considered, but not executed

A real cross-field bridge could combine SciPy position-conditioned vibration features, librosa nonnegative spectrogram decomposition or constrained NMF, and state/path association to assign residual energy to moving sources. Unlike an arbitrary smoother, position-conditioned mixing coefficients would connect the source-separation representation to the maintenance object. However, independent cart motion, structural transfer functions, intermittent impacts and correlated healthy sources make the mixing model an empirical assumption. The current labels cannot validate its central identity claim. Selecting repositories and pinning runtime versions is deferred; no compatibility or implementation claim is made.

Strong baselines would include a constant-middle predictor, per-cart position/speed passage windows with conventional band/envelope features, nearest-sensor energy association, and the same feature detector without separation. Features and file names must not expose fault labels; neighboring windows of a recording cannot straddle train/test. Training healthy-only should not quietly be replaced by fitting a transform separately to each known test class.

The [2025 IEEE IWCCT paper](https://doi.org/10.1109/ACCESS.2025.3636190) explicitly discusses source attribution but evaluates position-gated single-cart Type 2 data and feature-distribution reshaping, not a demonstrated three-cart identity solver. It is a strong detection baseline, not evidence that attribution is solved. Its class-wise operating assumption and published split warrant attention in a prospective reproduction.

The [2026 adaptive transformation paper](https://doi.org/10.1016/j.isatra.2026.06.005) adds distribution-aware feature processing and reports fault-detection results. This further raises the baseline for a replacement detection claim. No public reproduction code or exact usable code license was established in this bounded screen; paper access does not license an unknown implementation.

## Access and rights

Primary Zenodo metadata is preserved locally. The relevant three-cart records are [Types 5–6](https://zenodo.org/records/14761243), [Type 7](https://zenodo.org/records/14764717), and [Type 8](https://zenodo.org/records/14765815). data-access.json reports exact API responses, file sizes/checksums, and licenses where retrieval succeeded. These are archive metadata, not hashes of locally validated data contents. No multi-gigabyte archive was downloaded because the identity limitation already defeats the intended benchmark. CC BY 4.0 permits commercial reuse with attribution, but does not confer equipment warranties or customer-data access.

The university dataset-paper URL returned HTML rather than a PDF; that failed response is recorded and excluded from publication. Publisher search text and the primary bibliographic page were consulted; no access controls were bypassed.

## Reconsideration condition

A worthwhile attribution protocol would need genuine measurements with faulty identities varied independently of position/order, and an actionable output evaluated against strong passage-gating baselines. Clean-source separation truth would be desirable, but maintenance-confirmed identity labels plus a blinded reviewed-output task could suffice. Buying that evidence may eventually be rational after buyer discovery; it is not presently a ready public-data experiment. Do not rescue the lead by synthetic superposition presented as measured industrial truth, label permutation, or tuning an unrelated detection score.
