# Preregistered outcome: failed advantage gate

The candidate did not earn a technical-validation pass. The first held-out evaluation used all 50 official test images after the review rankings were frozen. There were 18 wrong nuclear-QC proxy decisions initially, so error opportunity was sufficient. At the fixed 20% review budget (10 images):

| Method | Wrong decisions corrected | Wrong decisions remaining |
|---|---:|---:|
| Decision-risk candidate | 6 | 12 |
| Validation-selected uncertainty baseline | 2 | 16 |
| Simple decision-margin baseline | 7 | 11 |
| Random review, mean of 1,000 seeds | 3.594 | 14.406 |
| Random review, 95th-percentile benefit | 6.05 | 11.95 |
| Stratified review, mean of 1,000 seeds | 3.532 | 14.468 |
| Stratified review, 95th-percentile benefit | 6 | 12 |
| Oracle, evaluator-only upper bound | 13 | 5 |

The candidate reduced remaining mistakes 25% relative to the uncertainty baseline, but a simple threshold-margin rule corrected one more mistake. It also failed the preregistered comparison with strong stochastic baselines and the absolute-advantage requirement. This is a substantive negative finding: integrating uncertainty propagation did not establish value beyond a simpler rule at the chosen budget. The 30% budget was descriptive and is not substituted for the primary outcome.

The error mix was 3 low-count flags, 2 high-count flags and 13 large-median-area flags. The candidate corrected 1, 2 and 3 respectively. Among seven wrong images in the lower half of ensemble uncertainty, it corrected two of ten wrong decisions. On the thirteen densest test images it corrected one of three mistakes. These descriptive slices do not establish robustness.

This experiment used real microscopy images and independent annotation masks; no artificial segmentation defects or selected favorable images were inserted. Perfect equal-cost review was simulated, not performed by staff. Count/area thresholds are scientific-QC proxies derived from training quartiles, not biological hit labels. The watershed sensitivity ensemble is not a direct implementation of deepflash2 or a comparison with all modern segmenters.

`results.json` and `evaluation.log` preserve the first held-out results. `evaluation-freeze.json` records pre-evaluation hashes. The final ranking SHA256 was `e9bac94c707544492512ac3d0d28ababe653f9495cdaae3d88f4efd77515dbc0`. The protocol hash remained `544e5b99a44ea2b6c37b76962f2c827881b231d3ea3baa91a9ed87c5a007161b`.

Before decoding any test annotations, a numeric implementation correction computed training quantiles directly from raw measurements instead of roundtripping through log1p/expm1. The original pre-evaluation model and rankings are preserved as attempt-02-float-*.json. This corrected the area threshold from 655.9999999999997 to656; it did not change the protocol or use test performance. Earlier resource-fork file enumeration failure is also preserved. The official ground-truth decoder explicitly uses the first PNG channel and connected components: https://gist.github.com/jccaicedo/15e811722fca51e3ae90e8b43057f075 . No decoder change was made.

Business conclusion: reject this implementation for pursuit. Paid image-analysis work exists, but the current mechanism fails its own advantage test, general decision-aware deferral has substantial prior art, and standalone payment/distribution/defensibility remain unproven. No score increase is warranted from a runnable bridge alone. Do not retune this test set to manufacture a pass.
