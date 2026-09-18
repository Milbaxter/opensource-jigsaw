# Independent frozen ultrasonic review

Decision: **HOLD; original technical screen failed. No pursue-validation pass.** Recorded18 September2026 after frozen source execution. This is an implementation and evidence review, not a new performance study or a diagnosis of a FINUFFT defect.

Protocol SHA25639efd6e39d50c3a98ff57c2d27196b3f7175e9c8cd132ac2315b0f0a44d3a646 was published in commit4fc6057fb027cee066700076c6e39ef17622a57f. Executed prototype SHA256e1f9067cb7dbdba218ea3c0b9f26facf47dc1c3516b7780c727589d34a682e02; driver SHA256e7c61a428792df36c13c4b495653ddce4358a0e24bc456888ec1e40fb36bb863. Independent review identified four static issues before execution; the final frozen implementation corrected origin-phase placement, a vacuous translation control, native interpolation bounds, and disconnected-lobe width accounting. Earlier source snapshot remains explicitly unexecuted.

## Independent checks

Read the frozen implementation and finite driver. All159 author numerical/input/origin controls report success. Independently evaluated15 additional real-spectrum queries at three transmit wavenumbers by explicit centered-mode summation; relative errors were3.47e-6,2.00e-7,1.31e-7, within the preregistered1e-5 numerical tolerance. Reconstructed candidate, Arim-linear, native-linear2 and native-cubic2 at6400m/s using the unchanged source. Each image was bit-identical to the author's saved image. Own artifacts: `replay-selected.py`, `independent-replay.json`. This selected replay does not independently repeat every velocity or control, and provides no timing measurement.

| Method | Dominant depth at6400m/s | Error against nominal20mm |
|---|---:|---:|
| FINUFFT |20.864mm|0.864mm|
| Arim-linear |20.736mm|0.736mm|
| Native linear2 |20.992mm|0.992mm|
| Native cubic2 |20.992mm|0.992mm|

FINUFFT matches the canonical high-accuracy reconstruction numerically; its complex image error at6400m/s is3.12e-7. Its peak agrees with Arim within0.128mm, passing that relative check. It exceeds the preregistered0.5mm absolute tolerance. The driver correctly stopped before randomized repeated performance comparisons and retained native diagnostic images. Consequently no speed or memory advantage is established. Single quality-run elapsed times are not a substitute for the preregistered comparison.

## Stage semantics and comparator limits

Origin phases are applied on the sampled spectrum before masking/interpolation, matching the frozen canonical target. Type2 signs, centered coefficient order and units pass independent direct-sum checks. Native interpolation uses zero fill beyond sampled bounds while canonical interpolation is periodic. Per-transmit streaming avoids a gratuitous whole oversampled cube; setup, transforms, interpolation and accumulation are timed in stage records. Fresh-process `ru_maxrss` includes native memory. No peak-memory win can be inferred because the actual performance phase did not run. Arim also incurs transmit-FFT preparation in the shared acquisition class even though it does not use that preparation; do not interpret its total cold-process cost as an independently optimized TFM implementation.

Arim's complex-error failure against the selected DCWA interpolant is not evidence that TFM is physically wrong: the algorithms have different scaling, weighting and point-spread behavior. Both native and Arim diagnostics must remain visible. The numerical reference is a precise evaluation of a selected periodic polynomial, not independent physical truth.

## Is there a source-supported correction?

The original input contains `time` starting0, spacing40ns, `ph_velocity=6400`, probe geometry, waveform data,55 steering angles and a64×55 `delays` matrix. No scalar FMC instrument time-zero calibration is supplied in that schema. The steering-delay matrix is not evidence for a global time-origin correction. The primary acquisition paper and dataset title identify a1mm hole at20mm; no independently justified replacement depth, sound speed or timing correction was found in the inspected evidence.

Primary publication: https://doi.org/10.1098/rspa.2018.0451 ; author institution record https://research-information.bris.ac.uk/en/publications/strategies-for-data-acquisition-using-ultrasonic-phased-arrays/ ; dataset https://rs.figshare.com/articles/dataset/7178630 . My direct PMC retrieval encountered a browser check and the author-institution PDF returned403. Indexed primary excerpts and the researcher's section4(a) inspection support nominal geometry, but I cannot assert exhaustive absence of calibration from inaccessible full text. No waveform-derived or target-fitted correction was attempted.

The common positive depth offset is consistent with several possible causes, including acquisition calibration or model/pulse behavior. It does not distinguish them. The preregistered result is a failure; the physical root cause remains unresolved.

## What a future narrower study could establish

A separately preregistered numerical-equivalence/resource study could legitimately keep the unchanged polynomial, disclose this specimen's physical bias and test computational cost at fixed approximation error. That would answer a different mathematical engineering question. It must not relabel this failed experiment, silently remove its absolute gate, or treat Arim's disagreement with DCWA as an industrial-quality failure. Reusing this now-observed specimen is exploratory follow-up, not a new unseen validation case.

For a commercial pursuit decision, the missing bridge is still evidence that an independently calibrated or buyer-accepted reconstruction workload needs this tradeoff and benefits against practical alternatives. Obtain documented input calibration or a separate independently calibrated specimen, and retain strong native/TFM comparators. Otherwise further kernel timing risks demonstrating a fast answer to an unvalidated physical target. I recommend preserving the working numerical bridge as research evidence and holding the proposed service, rather than changing thresholds to obtain a pass.

The market sources support paid NDT analysis and retained-FMC postprocessing, but not an observed willingness to buy this narrow backend. NUFFT beamforming has direct2012 prior art; current analysis suppliers already offer automation. These facts do not independently kill a useful OSS integration, but the failed physical gate and absent completed resource comparison mean this prototype has not demonstrated its proposed practical advantage.
