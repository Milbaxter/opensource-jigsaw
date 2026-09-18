# Independent ultrasonic review before execution

18 September2026. Reviewer: Astra agentA, not the proposer. No reconstruction, numerical transform comparison, runtime evaluation or score was executed. This review reads the unfrozen proposal, upstream source, primary references, exact input metadata and package bytes.

**Recommendation: a bounded numerical benchmark is worth freezing after target/fairness corrections. This is not a validation-ready or commercial pass.** The proposed advantage is falsifiable and materially different from merely demonstrating that libraries connect: evaluate the same complex interpolation target within an error budget while reducing end-to-end time or peak resident memory against a competent padded-FFT implementation. Whether that benefit exists is unknown.

## Actual input and access

Independently obtained Figshare article7178630 metadata: CC BY4.0, file13206053,1,869,782bytes. Existing local bytes match the source MD5, `b01187a329f13350531c19ec5388dbf2`; SHA256 `b244d0e800087590da0664ef97473494dc6ef38a683ec80f262af307c8c37b89`.

Independent structural inspection confirms512×4096 finite measurements, all4096 unique transmit/receive pairs with IDs1–64, uniform40ns sampling and uniform0.6mm element-center spacing. Saved in independent-input-inspection.json. I did not inspect a reconstructed image or calculate signal quality.

This is one laboratory specimen/capture. Parameter sweeps, shifted coordinate controls, synthetic impulses and repeated timings do not create independent flaw observations. Data access is real for this experiment; access to a customer's retained raw FMC is a separate commercial hypothesis. The supplied fields include explicit tx/rx ordering, so reshaping without respecting those IDs is an avoidable implementation error.

## Mathematical target must be fixed

The upstream DCWA source applies temporal-origin phases, spatial transforms, evanescent masking and optional angular masking before its bilinear interpolation. It then applies a migration correction with a hard0.007 cap and additional nonphysical-region handling. Consequently, evaluating an unmasked raw-data DTFT and masking only query locations is not generally identical to interpolating the already-masked sampled spectrum.

The proposer acknowledged this before freeze and plans a canonical masked-spectrum interpolant: fix the base DCWA grid/mask, inverse-transform that spectrum into coefficients, and compare FINUFFT against padded FFT/interpolation of those same coefficients. That is mathematically legitimate. It is a selected periodic numerical interpolant, not independently proven physical truth. Near a discontinuous mask it can ring. Retaining a faithful upstream-order DCWA image and Arim TFM as separate practical/physical checks is therefore important.

Spatial padding in the original source also changes the transmit-wavenumber quadrature, output image extent, and interpolation grid. Common image coordinates, transmit quadrature, mask convention, weights and normalization must remain fixed when attributing a gain to the interpolation kernel. Increasing both FFT axes is a valid accuracy strategy, but its cost must be compared with optimized separable/streamed alternatives rather than a needlessly allocated full tensor.

FINUFFT type2 evaluates a specified Fourier polynomial. It does not invert an arbitrary nonuniform transform, recover missing measurements, improve the propagation approximation or guarantee physical resolution. The requested tolerance is an algorithm setting, not an observed error bound; direct-sum and tolerance-convergence checks remain necessary.

## Practical baselines and resource accounting

The strongest accessible comparisons include:

- Published DCWA/WA with native masking and temporal-origin handling.
- Linear and competent cubic interpolation, several padding levels, same arithmetic precision and input information.
- Streamed per-transmit-slice FFT processing; reusing invariant FFTs/coefficient preparation across a velocity batch when equally available to both methods.
- Arim's compiled TFM for the same homogeneous contact problem, with supported interpolation modes. This checks practical imaging; it is not the sole kernel comparator.
- Small direct complex sums as a numerical oracle, never as the main speed competitor.

Report complete batch latency, setup, FFT/prefilter/plan construction, loading and image assembly. A warm kernel gain can disappear in preparation. Equal thread counts and fresh-process peak RSS are appropriate. Capture resident memory from native allocations, not merely Python tracemalloc. One catastrophic full-cube allocation is not evidence that padding intrinsically requires that much RAM.

The proposal's criterion of comparing against the fastest accuracy-passing baseline is appropriate; retain the whole error/time/memory frontier. No passing baseline means inconclusive, not victory. Synthetic enlarged arrays are not independent measured industrial data; no such enlargement is necessary to make the current trial valid.

## Prior art and the actual cross-field contribution

The transfer is genuine at the software/mechanism level: a mature general-purpose NUFFT implementation replaces a specific complex-spectrum interpolation step in a domain-specific migration implementation, while Arim provides acquisition/TFM context. This can be practically valuable even when mathematically established.

It is not new scientific territory. The2008 ultrasonic wavenumber work already drew on radar/sonar reconstruction. A2025 primary paper uses FINUFFT in millimeter-wave near-field imaging to replace Stolt interpolation plus an inverse transform, with real-data experiments. This is close algorithmic precedent, although its type1/quasi-monostatic formulation is not the proposed type2 FMC/DCWA integration. Related ultrasonic migration literature also discusses interpolation/padding limitations. Do not claim novelty from the absence of this exact repository combination.

Durable value could plausibly come from validated instrument adapters, qualified-user regression datasets and integration/support for a recurring method-development workflow. None has yet been acquired. The public kernel alone is readily reproducible and therefore offers weak standalone defensibility. No score is assigned before actual evidence.

## Buyer and economics

The credible initial user is a method-development engineer or specialist NDT reanalysis service already retaining elementary data and using programmable workflows, not every field inspector. The likely budget owner is the technical lead responsible for inspection procedure development or analysis throughput.

Eddyfi's primary description substantiates why retained data are reprocessed: ROI, pixel count, modes, geometry and material properties. It also documents existing fast CIVA processing and a vendor-provided access library, while noting that raw FMC is often discarded. Thus the useful gap is a demonstrated accuracy/resource improvement on a concrete repeat batch, not a claim that current tools cannot reprocess or that all TFM remains slow. CPU seconds do not automatically save analyst labor. The original public file is much smaller than a real scan archive; linear extrapolation should not be sold as an observed industrial result.

TWI advertises FMC services and optimized real-time TFM. Parent's primary NASA2023 maintenance notice supports a paid CIVA category, not a2026 entrant budget. No narrow kernel price or committed customer was found. A future qualified-user study must ask whether the actual wait/memory limit matters enough to outweigh import, validation and support effort. Available paths include the documented public technical communities and service organizations; a named company is not an agreed pilot participant or authorization to contact anyone.

## Exact binary rights finding

FINUFFT2.5.1 source is Apache2.0, but its release NOTICE expressly distinguishes optional FFTW GPLv2-or-later from DUCC's dual BSD3/GPL FFT components. The exact macOSarm64 wheel named in the proposal contains no standalone LICENSE/NOTICE. Its libfinufft.dylib has many FFTW-named symbols/strings, no observed ducc strings, and no external FFTW dependency in `otool -L`; this strongly suggests bundled/static FFTW. Saved evidence is in binary-rights-inspection.json, finufft-wheel-METADATA.txt and the release LICENSE/NOTICE source records.

Do not describe this binary as Apache-only. Internal execution does not require publishing the binary; commercial use is not prohibited by the GPL. A distributable product must satisfy the actual bundled obligations, or establish a tested DUCC build with suitable notices. This is not a reason to stop a local benchmark, but it is an essential delivery-boundary disclosure. Arim MIT and upstream DCWA BSD3 can be combined subject to preserving notices. Exact adapted files and dependencies should accompany final execution evidence.

## Independent checking plan

See TECHNICAL-CHECKS.md. I will check the frozen protocol/source/results hashes; inspect the target definition and mask ordering; independently verify numerical indexing on bounded controls; inspect all baseline observations and resource accounting; and judge only the claimed scope. No desired verdict is assumed.
