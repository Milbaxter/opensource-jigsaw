# Prospective experiment: error-controlled Fourier interpolation for saved ultrasonic FMC

Status: awaiting publication/freeze before implementation and performance evaluation. Prepared 18 September 2026 by Astra researcher. This is a finite technical screen under the already frozen v2 rubric, not a change to that rubric and not an inspection qualification.

## Decision and claim

Test whether FINUFFT can improve the accuracy/resource trade-off of a current Fourier-domain ultrasonic imager inside a Python/Arim workflow. The candidate changes **complex-spectrum interpolation**, retaining the published delay-and-sum-consistent wavenumber algorithm (DCWA) propagation and amplitude weighting. The transfer is from a mature nonuniform Fourier primitive used in astronomy/inverse imaging into a specific NDT reanalysis step.

The paid workflow is offline reconstruction of retained elementary full-matrix data while varying homogeneous material velocity or image settings. Existing Eddyfi/CIVA products already support this and commercial TFM can be real time. This experiment does not claim that the category lacks fast processing, that a published NUFFT method is new, or that a speed-up in this tiny specimen proves a commercial opportunity.

Potential deployment: a transparent numerical backend for an existing Python method-development/reanalysis workflow. Buyer access, real job sizes, supported instrument export and actual paid adoption remain separately testable. No customer data, procurement, outreach or paid use is assumed.

## Claim-to-test declaration

- **Proposed purchased deliverable:** an installed, documented offline Python backend and one reproducible batch-reconstruction workflow for a qualified NDT method-development team with retained homogeneous-planar FMC data; not a defect-acceptance service.
- **Primary practical benefit:** accurate batch reconstruction on the buyer's existing CPU with less end-to-end waiting or materially less memory. This is the declared value claim; raw Fourier-query error alone cannot satisfy it.
- **Fair same-information baseline:** the same measured traces, geometry, velocity list, image grid and mask conventions, processed by streamed FFT-interpolation migration; also the original DCWA processing order and accelerated Arim TFM. All methods can cache the same invariant quantities and incur their real preprocessing/plan costs.
- **Exactly measured outcomes:** numerical error, target localization/profile changes, new artifacts, complete cold/warm batch latency and process peak RSS. No human labor or instrument acquisition-time savings are measured.
- **Decision-critical buyer uncertainty remaining:** whether real retained-FMC work actually waits on this numerical step, whether customers can export the needed elementary data, whether their incumbent is equally efficient, whether the restricted physics is relevant, and whether a maintained integration earns paid repeat use.

## Inputs, rights and scope

Use the **single original measured** Velichko/Croxford FMC file, Figshare article 7178630, file 13206053, DOI 10.6084/m9.figshare.7178630, CC BY 4.0. `input-access.json` records successful direct retrieval, original bytes/hash and schema. File: 1,869,782 bytes, 64 uniformly spaced elements at 0.6 mm pitch, 512 samples per trace at 25 MHz, all 4,096 transmit/receive pairs, stated longitudinal velocity 6,400 m/s and nominal 5 MHz probe; specimen contains a 1 mm side-drilled hole at 20 mm depth. Only schema and metadata were inspected before registration; no reconstructions/timings were evaluated.

Only this original measured capture is the primary real-data input. Nine velocity reprocessings are repeated computational conditions on **one specimen**, never nine independent experiments. Supplementary same-specimen plane-wave files and immersion/multiview Bristol datasets are excluded: their acquisition/propagation models are different. No extra specimen may be silently added after outcomes.

Homogeneous, flat contact geometry and single longitudinal mode only. No curved surface, refraction, anisotropic weld, multiple scattering qualification, defect acceptance decision, medical use or certification. Output is research/preplanning numerical evidence for a qualified analyst.

Pins: Python 3.12.14; NumPy 2.2.6; SciPy 1.16.2; Numba 0.61.2; FINUFFT 2.5.1; Arim source commit `0cee9de26ae995ca80e00bc67801ffb3b1188e44`; published DCWA/WA reference commit `246d97a9ff19983e0b047cd259e3ac62c6b3b88a`. Source and wheel rights must be completed and recorded before execution. Arim is MIT; DCWA code BSD-3-Clause. FINUFFT exact wheel omits standalone license files: its metadata and v2.5.1 source license identify Apache-2.0, while bundled FFTW archives are GPL-2.0-or-later per the release NOTICE. This experiment must use a GPL-compatible source distribution; no third-party binary is published. No claim is made that this wheel is suitable for closed-source redistribution. A differently built DUCC backend is outside this run. Exact release/wheel evidence is in rights-inspection.json and rights-notes.md.

## Exact essential bridge

1. Load real acquisition through Arim's Bristol MATLAB reader or construct an Arim Frame from the original explicit element/pair/time arrays after validating every required field. Record which interface is used. All pair IDs must occur exactly once; reject missing/duplicate pairs, nonfinite values, nonuniform time/pitch, nonpositive velocity or incompatible dimensions.
2. Let `s[n,r,t]` denote the finite recorded samples and `x_r,x_t` actual centered element coordinates. Form the uniform transmit transform with 2× spatial padding shared by every method. For each transmit wavenumber and velocity, form a **canonical complex spectrum** with temporal padding 2× (1,024 samples) and receiver spatial padding 2× (128 samples), including the actual time/element-origin phases. Apply the original DCWA evanescent mask on this sampled frequency grid *before interpolation*. No optional angular taper is applied. This fixed sampled masked spectrum defines the canonical reconstruction target.
3. Inverse-transform the canonical masked spectrum into its finite centered Fourier-polynomial coefficients. **Candidate:** FINUFFT type 2 evaluates that polynomial at migrated `(omega,kv)` query points with requested tolerance 1e-6. **Matched-target baselines:** zero-pad those identical coefficients by factors 1,2,4,8 on both polynomial axes, FFT, then bilinear or bicubic interpolation at the same query points. Include this inverse transform and all oversampling work in end-to-end cost. The original raw-data DTFT with a mask applied only at target query points is explicitly **not** the same target and is not substituted. Spatial padding defining the transmit quadrature/image target is held fixed; coefficient oversampling changes interpolation resolution only. For the exact numerical sum controls, the coefficients are those of this masked-spectrum polynomial, not the unmasked original time traces.
4. For each Cartesian image wavenumber `(kx,kz)` and transmit `ku`, use the published migration relation `kv=kx-ku`, `k = sqrt(kz^4+2*(ku^2+kv^2)*kz^2+(ku^2-kv^2)^2)/(2*kz)`, `omega=c*k`, with zero/evanescent/nonphysical/Nyquist queries explicitly masked. Retain DCWA published weighting `k/[sqrt(sqrt(k^2-ku^2)*sqrt(k^2-kv^2))*kz]`, its finite-value handling and 0.007 magnitude cap identically for every Fourier method; sum transmit components, inverse transform and multiply by depth as in DCWA. Document angular/normalization conventions and any adaptation. No per-method fitted physics parameters.
5. Arim's accelerated delay-and-sum TFM supplies a separate established physical-image comparator. It is not the sole speed comparator. Use both nearest and linear interpolation if the pinned API supports them, and report the fastest accurate result. If a necessary API cannot be used, record failure rather than silently replacing Arim with our own code.

## Fixed computation domain and fair baselines

Image grid: 128 lateral samples at 0.3 mm spacing centered at zero, 256 depth samples at 0.128 mm spacing starting at zero. Evaluate image-quality metrics only at positive depths and in the fixed region |x|<=15 mm, 5<=z<=30 mm. Target region is |x|<=2 mm, 18<=z<=22 mm; background is the evaluation region outside that target box. Report any strong interface response separately without relabeling it as a defect. No arbitrary upsampled image-size inflation to manufacture a cost advantage.

Velocity batch, in this order: 6,272, 6,304, 6,336, 6,368, 6,400, 6,432, 6,464, 6,496, 6,528 m/s. These are parameter sensitivity calculations on the original data; the stated 6,400 m/s is the physical-location check. Do not tune velocity to maximize a candidate's result.

Matched-target migration baselines: linear and cubic interpolation each with coefficient oversampling factors 1,2,4,8 on both polynomial axes; the canonical mask and transmit quadrature stay fixed. In addition, retain the **faithful upstream-order practical baseline**: original raw-data temporal padding 1,2,4,8, receiver/transmit spatial padding 2×, evanescent masking before interpolation and linear/cubic interpolation. These upstream-order variants differ slightly in masked-spectrum discretization; report this openly and require physical/image agreement, rather than silently treating their mathematical target as identical. The candidate must improve over the fastest accuracy-passing member of either family, not just the canonical family. For the cubic baseline use regular-grid cubic B-spline interpolation of real/imaginary components with the corresponding prefilter cost included, never a slow general scattered interpolator. FFTs use SciPy's established backend. Stream independent transmit slices to avoid gratuitous full padded-cube allocations. Reuse invariant coefficients/coordinates/FFT plans when legitimately reusable; both candidate and baseline receive the same opportunities. No caching of completed images.

FINUFFT requested tolerance 1e-6 is the candidate; tolerance 1e-12 is a high-accuracy internal numerical reference, not a runtime competitor. The latter must first pass independent small direct-sum checks. Also report conventional WA if useful for explaining physics, but it cannot replace the fixed DCWA baseline or create a new success gate.

## Correctness controls before timed performance

Freeze source hashes before any control/evaluation execution. Controls:

- Compare the Fourier query evaluators to direct complex sums for eight evenly spaced transmit wavenumber indices and 16 valid migrated query indices per velocity, fixed selection RNG seed 9400. A zero or tiny-energy slice uses an absolute floor scaled to the input l1 norm; do not divide by nearly zero values or discard it silently. FINUFFT relative l2 error must be <=1e-5, with reference tolerance 1e-12 error <=1e-9.
- Analytic impulses, all-zero input, translated element/time origins, a one-pair missing/duplicate mutation and NaN/+infinity velocity/data must have expected finite transforms or explicit rejection. Controls are synthetic and labeled separately.
- On the original input at 6,400 m/s, the reconstructed dominant target must lie within 0.5 mm of the stated hole location `(x=0,z=20 mm)`, and candidate versus Arim TFM peak difference must be <=0.5 mm. The source paper section 4(a) explicitly states the array was positioned above the 20 mm-deep defect (https://pmc.ncbi.nlm.nih.gov/articles/PMC6237505/); the later multiple-hole experiment is distinct. Never infer target position from a candidate image.
- Relative complex-image l2 error against the high-accuracy same-physics reference <=1%; candidate peak amplitude error <=1%, peak displacement <=one grid cell. All baseline qualities are measured identically. DCWA/Arim comparison reports normalized target profiles, -6 dB axial/lateral widths and off-target sidelobes; raw inter-method scaling also reported. Do not conflate different physical weighting units with calibrated defect amplitude.
- No new off-target local maximum above -6 dB of target that is absent in the high-accuracy DCWA reference. A disagreement with Arim is retained and discussed, not automatically called a newly detected flaw.

Missing controls, invalid reference, implementation errors or unresolved coordinate/sign errors make the screen fail/inconclusive. Do not run through them to claim a performance win.

## Timing, memory and bounded execution

Run each method in a fresh process with one computational thread (including BLAS/Numba/FINUFFT); record CPU, OS, dependencies, command, process status and peak resident memory. Explicitly time file loading, coefficient preparation, baseline prefilter/FFT, FINUFFT plan/set-points construction, evaluation and image assembly. Both cold full-process and warm nine-velocity batch are reported. Numba JIT is recorded separately and in the cold process. A warm kernel-only number is never presented as job time.

For each method, one warm-up batch then three timed nine-velocity batches, retain all observations, median primary. Randomize method order with seed 9401 once and preserve it. Resource cap per process: 120 seconds per nine-image batch and 2 GiB resident-memory target, terminate at 180 seconds or observed >2.5 GiB; record censored/error results as failures, not zero timings. Overall performance execution capped at 30 minutes. A resource-reducing substantive algorithm/domain amendment requires a new prospective version before affected runs.

## Predeclared technical success and stopping

Must satisfy every correctness requirement and have at least one accuracy-passing strong migration baseline. Against the **fastest** passing baseline, candidate must achieve either:

- >=2× median complete warm-batch speed-up, with >=1 second absolute saving per nine-image batch, no increase in peak memory >10%; or
- >=50% peak-memory reduction and >=128 MiB absolute reduction, with median complete warm-batch runtime <=1.1× the fastest passing baseline.

Also report the complete time/error/memory Pareto table for every method. An inaccurate baseline cannot be used to claim matched-quality speed-up; absence of any passing baseline makes the comparison inconclusive, not an automatic pass. Arim physical-image check remains mandatory. A single successful point does not establish universal speed/accuracy advantage.

If either outcome fails, preserve all evidence and HOLD this candidate. Do not adjust accuracy targets/padding/grid after observing results to produce a win. A separate implementation repair may be preregistered, but original outcomes remain visible.

## Subsequent paid validation, only if technical result warrants it

Proposed, not executed: three independent NDT method-development/service organizations, three weeks, max 24 engineer-hours plus EUR 600 compute/acquisition allowance (EUR 3,000 at EUR 100/hour). Obtain two authorized retained-FMC exports covering this exact homogeneous planar scope, compare against each customer's existing tool on their real parameter-sweep workload with setup/import/review time included, and seek one paid follow-up of >=EUR 500. Kill if exports are unavailable, physics outside scope, incumbent is equally quick after configuration, integration takes >8 hours per archive, or no buyer values the measured improvement. Human-labor savings cannot be inferred from CPU seconds. No operation/acceptance decisions are automated.

## Publication

Preserve input attribution/hash, protocol, original source hashes, numerical/physical controls, every baseline including failed/censored runs, stage-level timing, memory, images/profiles and reproducible commands. Publish the small CC-BY input only with attribution if repository policy permits; otherwise include verified downloader. Third-party license obligations must accompany any adapted reference code. No proprietary CIVA/Eddyfi data, code or customer material is copied.
