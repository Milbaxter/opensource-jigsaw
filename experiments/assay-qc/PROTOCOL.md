# BBBC039 decision-aware segmentation review: preregistration v1

Frozen 2026-09-18 before downloading images, masks, metadata, or running any segmentation. Research workflow proxy only: neither a biological hit-validation test nor a clinical-use experiment.

## Hypothesis and implementation bridge
An equally costly manual image review is more useful when correcting that image's segmentation is likely to change a specified downstream count/morphology decision. Use scikit-image segmentation and feature extraction, SciPy uncertainty propagation and numerical ranking to estimate expected decision errors removed. Contrast this with choosing images that merely have uncertain segmentations. No held-out annotation may enter selection.

## Data and fixed split
Use BBBC039v1, official images.zip, masks.zip, metadata.zip. Respect the supplied train/validation/test partitions without moving images. Dataset is CC0 per https://bbbc.broadinstitute.org/BBBC039. Download raw images and metadata first. Extract train and validation masks into a calibration-only directory; leave test masks in a separate evaluator-only archive/directory. The inference/selection script has no mask-directory argument and does not import evaluator functions. It outputs all rankings before evaluator reads any test mask. Save SHA256 of protocol, scripts, archive inputs and rankings. A later independent rerun may verify these boundaries; filesystem separation is procedural, not a cryptographic enclave.

## Decisions fixed before inspection
Extract count of nonzero nucleus instances and median instance area in pixels. Define three binary scientific-QC proxy decisions: count below training-ground-truth 25th percentile, count above training-ground-truth 75th percentile, median area above training-ground-truth 75th percentile. Quantile thresholds fixed from training masks only (NumPy default linear interpolation); no threshold choice using validation/test performance. These are intentionally transparent proxies for nuclear density/morphology flags, not validated compound hit labels. Correct manual review reveals all three reference decisions for that image. Review cost = one complete image, equal across methods; this ignores real density-dependent labor and must not be converted into claimed staff time savings.

## Segmentation and calibration, fixed search space
Normalize each image with 1st and 99th percentile intensities. Gaussian smooth sigma 1.0; foreground via Otsu threshold times {0.75, 1.0, 1.25}; remove foreground components smaller than 20 pixels and fill holes up to 20 pixels. Watershed on negative distance transform, markers from peak_local_max with minimum distance {5, 8, 12, 16}, exclude_border=False; no minimum peak height beyond foreground. Discard final labeled objects below {20, 50} pixels. This gives 24 deterministic parameter sets. Score each on training images by mean absolute log1p count error plus mean absolute log1p median-area error; select best single configuration and top nine configurations for ensemble. Ties by lexicographic tuple. No hand-injected segmentation defects, no deep model training, no modification after test results.

For each of the two log1p features, bias-correct the selected configuration by the median training residual (truth minus selected prediction). Uncertainty uses the nine configuration deviations around their per-image median, plus training residual pairs after centering. For each test image form all 9 x N_train draws: corrected selected feature vector + ensemble deviation vector + centered training residual pair. This preserves paired residual structure; it is an empirical sensitivity distribution, not a claimed calibrated Bayesian posterior. Classify the corrected selected prediction at the fixed thresholds. The candidate ranking score is the expected number (0–3) of these decisions changed across draws. Ties: larger summed normalized ensemble spread, then filename. No adaptive re-ranking using review annotations.

## Baselines and budgets
Budget = floor(0.20 * number of test images), primary. Also report 10% and 30% as descriptive, never substitute them for primary.
1. Strong uncertainty: rank by sum of sample standard deviations of log1p ensemble features divided by training feature IQR (zero IQR replaced with 1). Also test max spread and foreground-mask pixel disagreement. Select the strongest of these three on validation correction count at the same 20% budget; freeze chosen variant before test. This is an ensemble sensitivity baseline, not a direct run of deepflash2.
2. Simple decision margin: rank by minimum distance of corrected log1p features from any applicable threshold, divided by training feature IQR. Smaller first; tie filename.
3. Stratified review: partition test images into 4 x 4 quantile bins by unlabelled predicted count and median area. Allocate reviews round-robin among nonempty bins in sorted bin order, randomizing within bins with seeds 0–999. Report mean and 95th percentile corrected-error counts (strong baseline comparator uses 95th percentile).
4. Uniform random review with seeds 0–999; report mean and 95th percentile (strong comparator uses 95th percentile).
All deterministic ties use filenames except candidate secondary tie defined above. An oracle selecting true decision errors is only an upper bound reported by evaluator and never a competitor/algorithm input.

## Preregistered primary gate
Let E0 be number of wrong proxy decisions before review and Em remaining wrong decisions after budgeted review. A successful essential-bridge demonstration requires:
- E0 >= 10 and oracle can correct at least 5; otherwise inconclusive due to insufficient error opportunity.
- Candidate Em <= 0.80 times Em of EVERY baseline, using the selected uncertainty variant, deterministic margin, random 95th-percentile benefit, and stratified 95th-percentile benefit. If a baseline achieves Em=0, candidate must also achieve 0 but this counts as no distinctive benefit and fails the advantage gate.
- Candidate corrects at least 3 more decisions than each deterministic baseline and the mean stochastic baselines.
Report per-task results, all ranking lists, calibration thresholds, selected segmentation configuration, number of images, and parameter-search scores. A pass indicates value for this one nuclear QC proxy under perfect equal-cost review, not general biological or commercial validity. Failure remains failure: no retuning or replacing test set. Further experiments must be explicitly exploratory with a new protocol.

## Robustness and limits fixed in advance
Report candidate performance among the densest test quartile and images whose ground-truth decisions are wrong despite low ensemble uncertainty (bottom uncertainty half). These are descriptive adversarial subgroups defined by evaluator after rankings, not separate gates. Report count and median-area extraction errors. No actual staff reviews, batch replication, biological ground truth, or customer commitments are available. Counteracting segmentation errors requires user correction rather than simply excluding phenotypically unusual cells. Baseline search also includes coSMicQC, CellProfiler Analyst, SPACe, deepflash2; no novelty claim over all active learning research.

## Publication
Publish protocol, code, metadata/provenance, aggregate and per-image results, rankings, and reproduction instructions. Do not publish local virtualenvs or downloaded datasets by default; link original CC0 source. No external communication is performed.
