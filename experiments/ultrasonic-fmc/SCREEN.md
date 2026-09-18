# Round 4 C: real-data, transferable-primitives screen

Manual Astra research, 18 September 2026. Eight concepts screened; no reconstruction, diagnostic, or comparative performance evaluation has run. These are screening decisions, not independent rubric verdicts. A paid category is evidence of a workflow budget, not willingness to buy the proposed product. Repository metadata is in `repo-metadata.json`; errors and missing license classifications are retained, not converted into asserted permissions.

## 1. Error-controlled Fourier reconstruction for ultrasonic reanalysis — shortlist

**Buyer/workflow:** NDT method-development teams and inspection service providers reprocess saved full-matrix captures across imaging regions and wave speeds. Existing commercial tools already do this well. The narrowly testable gap is avoiding large FFT padding and its memory/time cost when accurate complex-spectrum interpolation is needed in Fourier reconstruction, while retaining a Python/Arim workflow.

**Combination:** [FINUFFT](https://github.com/flatironinstitute/finufft) nonuniform Fourier evaluation, a mature primitive used in astronomy and inverse imaging, plus [Arim](https://github.com/ndtatbristol/arim) ultrasonic acquisition/TFM and the independently published [DCWA/WA implementation](https://github.com/sufayanm/Fourier_beamforming). FINUFFT has 444 GitHub stars, not thousands; domain impact and independent application adoption matter more here than pretending it is a hugely starred project. Arim has 52 stars and last pushed June 2025.

**Actual input:** Velichko/Croxford [2018 experimental FMC data](https://rs.figshare.com/articles/dataset/Experimental_array_data_1_mm_hole_at_20_mm_depth_Full_Matrix_Capture_from_Strategies_for_data_acquisition_using_ultrasonic_phased_arrays/7178630), CC BY 4.0 confirmed by publisher and Figshare API. One 1 mm hole at 20 mm depth; 1,869,782-byte MAT file. Collection has three companion plane-wave acquisitions of the same specimen, not four independent defects. No clinical data or customer archive assumed.

**Strong baseline:** Current DCWA and WA source, including temporal/spatial zero padding and bilinear interpolation; Arim accelerated TFM; direct Fourier sum only a small numerical oracle, never the sole runtime comparator. [Hunter 2008](https://pubmed.ncbi.nlm.nih.gov/19049924/) already transferred radar/sonar methods into full-matrix ultrasound. [TPAC 2015](https://aos-ndt.com/wp-content/uploads/2016/09/EC_IUS15_fullPaper.pdf) already compared migration and GPU TFM. [NUFFT ultrasound research](https://www.sciencedirect.com/science/article/pii/S0041624X21001992) also exists. The contribution must be a useful, deployable accuracy/memory/runtime trade-off, not algorithmic priority.

**Paid/access evidence:** [EXTENDE](https://www.extende.com/) sells CIVA and consulting. [Eddyfi](https://blog.eddyfi.com/en/data-analysis-and-postprocessing-of-plane-wave-imaging-total-focusing-method-data) describes retained elementary data, custom Python access by requested library, and existing batch reprocessing. The input path is conditional: many operators discard raw FMC because of size. Parent's primary procurement/commercial notes are `work/round4-parent/ultrasonic-commercial-evidence.md`.

**Decision:** Highest-priority bounded feasibility protocol, only if an exact mathematical bridge and credible Fourier comparator can be preregistered. A single-hole accuracy/runtime result would not establish real inspection qualification, buyer access, or profitability.

## 2. Tacholess speed recovery using music/astronomy periodic-signal tools — reserve

**Buyer/workflow:** Machinery test engineers need order tracking when fitting an encoder is impractical. Combine [librosa](https://github.com/librosa/librosa) probabilistic fundamental/harmonic tracking with [Astropy](https://github.com/astropy/astropy) multiharmonic periodic fitting; astronomical [celerite2](https://github.com/exoplanet-dev/celerite2) is an optional noise/uncertainty primitive only if it contributes beyond a generic smoother. Do not add it for appearance.

**Actual input:** [Ottawa variable-speed bearing data v2](https://data.mendeley.com/datasets/v43hmbwxpm/2): CC BY 4.0, 60 experimental records, accelerometer and 1,024-cycle/revolution encoder, 10 seconds at 200 kHz. Encoder is evaluation truth and cannot leak into the estimator. Public page verified; direct metadata endpoint returned 403, so no claim of successful download.

**Benefit to measure:** Held-out speed error, harmonic/octave confusion, order-line concentration, abstention calibration and runtime. Split entire trials/conditions, not overlapping windows. Strong multi-order ridge tracking and regularized dynamic programming are essential baselines.

**Paid comparator:** [Dewesoft documentation](https://manual.dewesoft.com/x/setupmodule/modules/machinery/ordertracking) already supports multiple dominant orders, acceleration constraints, automatic initial speed and signal-only speed estimation. Its [simple example](https://support.dewesoft.com/en/support/solutions/articles/14000096008-order-tracking-without-rpm-sensor) using a dominant FFT peak is not the strongest current comparator. [Original dataset-associated method](https://www.sciencedirect.com/science/article/pii/S0022460X17307678) already extracts multiple time-frequency curves.

**Decision:** Good reusable ground truth and testability; no demonstrated practical gap over competent multi-order tracking yet. Reserve after FMC, not a claimed new product.

## 3. Astronomy cosmic-ray rejection for heterogeneous Raman maps — hold

**Buyer/workflow:** Materials-analysis labs remove detector spikes without erasing genuine narrow peaks. Combine [Astro-SCRAPPY](https://github.com/astropy/astroscrappy) spatial cosmic-ray morphology with Raman preprocessing and local spectral-neighbor consensus. Measurable outcome would be spike recall at a fixed real-peak false-removal rate, against repeat-acquisition truth.

**Comparator:** [Renishaw WiRE](https://www.renishaw.com/nl/cosmic-ray-removal--25933) already automates removal and uses matching neighboring spectra, while its [current software](https://www.renishaw.com/en/raman-software--9450) supports large Raman images. A 2-D astronomical CCD algorithm on a spectral-image matrix can misinterpret real material boundaries; reformatting axes is not a valid physics transfer.

**Data/access gap:** Public Raman studies exist, but no exact openly licensed paired raw/clean spike labels were verified in this bounded screen. Merely injecting synthetic spikes would not establish protection of naturally sharp Raman bands. A mistyped RamanSPy repository URL returned 404 and is retained in metadata.

**Decision:** Hold for suitable data and mechanism evidence; no prototype.

## 4. Robotics factor-graph repair of motion-capture dropout — hold on access and baseline

**Buyer/workflow:** Biomechanics and animation processing teams repair missing markers. Combine [GTSAM](https://github.com/borglab/gtsam) rigid-motion/factor-graph smoothing with [ezc3d](https://github.com/pyomeca/ezc3d) trajectory IO and marker topology. Measure hidden-marker error and abstention under naturally occurring missingness, not only easy random deletion.

**Comparator:** [Vicon Nexus](https://www.vicon.com/support/faqs/what-gap-filling-algorithms-are-used-nexus-2/) already has spline, donor-pattern and rigid-body methods; its [2025 guide](https://help.vicon.com/download/attachments/406490967/Vicon%20Nexus%20User%20Guide.pdf) also describes kinematic and cyclic fills. Factor graphs must outperform these on sustained multi-marker dropout without confidently inventing motion.

**Rights correction:** The MoVi *paper* is open access, but the [actual BML-MoVi data license](https://www.yorku.ca/research/biomotionlab/2025/09/14/bml-movi/) restricts commercial use and redistribution. Do not infer data rights from article rights. No data downloaded.

**Decision:** Proposed accessible data path fails this commercial experiment; replacement dataset and measurable baseline advantage required.

## 5. Low-rank/astronomical uncertainty tools for short NMR acquisitions — hold

**Buyer/workflow:** Analytical chemistry teams quantify weak components from limited acquisitions. Combine [nmrglue](https://github.com/jjhelmus/nmrglue), [TensorLy](https://github.com/tensorly/tensorly) low-rank structure, and FINUFFT or celerite2 only where the acquisition model warrants them. Proposed measure is concentration bias/coverage at fixed acquisition length, not prettier spectra.

**Paid category:** [Mestrelab](https://mestrelab.com/main-product/mnova) lists industrial Mnova packages beginning at USD 2,813 and already offers quantitative/advanced processing. [nmrXiv](https://docs.nmrxiv.org/introduction/data/formats.html) preserves raw FIDs and [public metadata APIs](https://docs.nmrxiv.org/developer-guides/api.html), but an exact licensed mixture series with independently known concentrations was not selected.

**Strong baseline:** Vendor quantitative processing, established compressed-sensing/NUS reconstruction, well-tuned time-domain line fitting, and ordinary longer acquisition. Nonuniform Fourier evaluation is not by itself an inverse reconstruction algorithm or an uncertainty guarantee.

**Decision:** Hold: useful output specified, but no sufficiently narrow, substantiated advantage/data pair. Do not prototype generic NMR denoising.

## 6. Bioinformatics alignment for metadata-free audio reconform — hold on practical differentiation

**Buyer/workflow:** Post-production teams rebuild edits after a new picture cut when source metadata is absent. Combine [Chromaprint](https://github.com/acoustid/chromaprint) fingerprints, [Parasail](https://github.com/jeffdaily/parasail) SIMD local/affine-gap sequence alignment, and editorial interchange. Local matches can represent inserted or removed spans; repeated/reordered scenes require explicit ambiguity handling beyond one monotone alignment.

**Actual input path:** [Elephants Dream](https://orange.blender.org/download/) film/production material is released for remix under Creative Commons; [Creative Commons' project account](https://wiki.creativecommons.org/wiki/Blender_Foundation) confirms commercial reuse. Artificial recuts of real media would be clearly labeled synthetic edits. Exact media-file license/hash would be pinned before use.

**Measurable outcome:** Correct source interval/cut boundary recall at fixed false-match rate, on preregistered repeats, reordered scenes, alternate mixes and inserted dialogue. Baselines: fingerprint seed-chain plus DTW, not just naïve waveform correlation.

**Paid comparator:** [Matchbox](https://www.thecargocult.nz/products/matchbox/) already works directly from reference video and guide audio, performs source match-back and updates edits. [Posted price](https://www.thecargocult.nz/store/) is USD 699. [EdiLoad](https://www.soundsinsync.com/products/ediload) handles related editorial handoffs.

**Decision:** Strong paid pain and input availability, but no identified accuracy/setup gap over existing competent tools. Hold rather than build an OSS clone and call it differentiation.

## 7. Genomic seed chaining for repeat pipeline-inspection alignment — hold on data

**Buyer/workflow:** Integrity analysts match physical indications across successive inline inspections despite odometer distortion. Combine [minimap2](https://github.com/lh3/minimap2) seed-chain concepts or Parasail local alignment with change-point segmentation and physical weld landmarks. A numeric feature alphabet would need stability/aliasing analysis; raw nucleotide encodings are not automatically appropriate.

**Comparator:** [UPP OMNI](https://uppipeline.com/inline-inspection-software-data-analysis/) already compares MFL, IMU and caliper runs at signal and box levels; [Cenosco](https://ims-handbook.cenosco.com/docs/pl-ili-comparison-match-defects-and-corrosion-rates-tables) supports defect matching and corrosion calculations. Ground-truth pair matching and lower analyst review load are relevant metrics, not a generic image classifier score.

**Data failure:** [PipeMFL-240K](https://huggingface.co/datasets/PipeMFL/PipeMFL-240K/blob/main/README.md?code=true) is CC BY-NC 4.0. It also provides cropped detection images, not verified paired longitudinal runs. Open download does not solve either commercial rights or task-ground-truth requirements.

**Decision:** Hold. Real paired data and a defensible transfer are missing; no diagnostic/corrosion-growth claim.

## 8. Astronomical background modeling for solar thermography normalization — hold on mismatched data

**Buyer/workflow:** Drone inspection teams distinguish real module hotspots from changing background/illumination and mosaicking artifacts. Combine [Photutils](https://github.com/astropy/photutils) robust spatial-background estimation with radiometric image processing and module geometry.

**Comparator:** Raptor Maps, Sitemark and existing radiometric processing are the practical class. [Raptor Maps flight guidance](https://pages.raptormaps.com/raptor-maps-knowledge-hub/solar-pv-inspection-drone-flight-guidelines) makes acquisition conditions part of the workflow; software cannot manufacture missing thermal calibration.

**Real data:** [RaptorMaps/InfraredSolarModules](https://github.com/RaptorMaps/InfraredSolarModules) is MIT-licensed and contains 20,000 labeled 24×40 module images. That is usable classification data, but lacks the raw overlapping radiometric flight data/calibration needed to validate the proposed background-normalization mechanism. A classification gain would answer a different question.

**Decision:** Hold for correctly matched real data. No thermal measurement or ROI claims from low-resolution normalized crops.

## Priority

Focus next on the exact numerical/physical FMC bridge and a prospective test against the current DCWA/WA interpolation implementation. Reserve tacholess tracking because it has real encoder truth, but insist on multi-order baselines. The other six screen results remain visible; neither research prior art nor incumbent existence is treated as an automatic rejection.
