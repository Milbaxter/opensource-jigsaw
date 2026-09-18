# Ultrasonic FMC reconstruction experiment

**HOLD: the frozen physical-location gate failed. No repeated performance comparison ran and no pursuit pass was awarded.**

[Results](RESULTS.md) · [independent review](../../research/round4/ultrasonic-independent-review/POST-RESULT-REVIEW.md) · [protocol](preregistration.md) · [packaging and replay](PACKAGING.md)

FINUFFT + Arim + published Fourier beamforming successfully evaluated the selected numerical interpolant:159controls and9canonical image comparisons passed. At the declared6,400m/s, the target appeared at20.864mm instead of nominal20mm, beyond the frozen0.5mm tolerance. Arim also had an offset(20.736mm). No independently supported calibration correction was found. The cause remains unresolved; this is not a demonstrated FINUFFT defect.

All54diagnostic images, the original failure, source snapshots, dependency provenance and independent selected replay are retained. Nine velocity conditions represent one measured specimen. Timing observations from quality diagnostics are not a speed benchmark.

![Physical precheck](physical-precheck.png)

Benchmark source is GPL-3.0-or-later with applicable notices, overriding the repository's MIT default for that source. No third-party binaries are included. The measured FINUFFT wheel includes GPL2+FFTW and is not Apache-only. Input and derived-data attribution: Alexander Velichko and Anthony Croxford,2018, DOI10.6084/m9.figshare.7178630, [CC BY4.0](https://creativecommons.org/licenses/by/4.0/). Derived reconstructions and plots are modified analyses; authors do not endorse the conclusions.
