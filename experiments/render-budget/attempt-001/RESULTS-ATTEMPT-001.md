# Attempt 001: stopped at strict original-roundtrip control

Frozen commit: `1a842b49a92b0723f810bec70d9c05daf7cb78a7`. The unmodified frozen runner exited1 after581.824 seconds. All12 executed source hashes matched the implementation freeze. This attempt provides **no allocation-comparison result and no technical support for the proposed mechanism**.

The9 authored color/data/normal × WebP/ETC1S/UASTC controls passed their frozen bound (worst sampled normalized channel error0.023529, threshold0.12). Missing PNG and invalid KTX inputs were rejected. The browser actually used compressed formats for ETC1S/UASTC, while WebP decoded to RGBA. All279 real-image codec/resolution options completed the common preparation stage.

The first real-asset control then failed. FlightHelmet repeated original GLB renders had exactly zero differing raw RGBA bytes in all six views. Loading the original source glTF versus its unchanged glTF Transform GLB produced raw differing-channel counts **[10,8,0,0,0,21]**. Maximum foreground normalized MAE was0.000008920258464489009. Although numerically small, these differences violate the prospectively frozen exact-equality gate. They are not assumed harmless or used to relax the gate.

No allocation search, SpatialPack recipe search, selection seal or held-out evaluation ran. No failed control was silently retried. `execution/failure.json` and `execution/FlightHelmet-setup.json` preserve the observed failure; raw logs and original frozen source were copied to `attempts/attempt-001`. All780 generated artifacts (598,933,363 bytes including intermediates) remain locally retained and are individually hashed in the attempt's generated-artifact manifest.

`outcomes-publish-manifest.json` lists only publication-safe evidence, including the tiny authored controls and model metadata. Public JSON/JSONL copies replace the local absolute experiment root with `<EXPERIMENT_ROOT>`; each entry records both raw and transformed hashes. No competitor implementation, npm dependency tree, original large model payload or arbitrary scratch file is included. The source data and generated artifact provenance remain available through the pinned manifests.

A separately authorized diagnostic may now investigate source-versus-GLB transforms or draw-order differences. That is not a continuation or pass of this failed experiment. Any amended experiment requires preserved failure evidence and a new prospective freeze before execution. No diagnosis is established by the failure counts alone.
