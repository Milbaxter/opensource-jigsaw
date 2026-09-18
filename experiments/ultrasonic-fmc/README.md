# Ultrasonic FMC reconstruction experiment

Status: prospective protocol and immutable source published; numerical controls are running under independent review. **No pursuit pass or measured advantage yet.**

[Protocol](preregistration.md) · [input access/hash](input-access.json) · [exact dependency rights](rights-notes.md) · [commercial context](../../research/round4/parent-sources/ultrasonic-commercial-evidence.md)

The proposed combination is FINUFFT + Arim + a published Fourier beamforming method. It tests a specific accuracy/runtime/memory trade-off on one measured specimen, against streamed and oversampled FFT alternatives and Arim TFM. Nine velocity runs remain one specimen.

The protocol and notes are original project research. The byte-preserved benchmark source carries GPL-3.0-or-later and applicable third-party notices, overriding the repository's MIT default for that source. See [packaging/replay notes](PACKAGING.md). No third-party binaries are bundled. The selected FINUFFT wheel contains FFTW; it is not represented as Apache-only. The input is retrieved separately under CC BY 4.0, with attribution to Alexander Velichko and Anthony Croxford and DOI 10.6084/m9.figshare.7178630.
