# Review packaging and parent replay

`ORIGINAL-MANIFEST.json` records the reviewer's supplied files before formatting. Source copies in `raw-evidence/` preserve supplied bytes. Runnable Python copies are formatted, with an ambiguous local variable renamed and equivalent string wrapping. The parent executed both formatted scripts against the published experiment in a separate scratch directory. `parent-packaged-verification.json` verifies all 71 result/graph pairs; `parent-packaged-input-probe.json` reproduces the omitted-wall and nonfinite-cost failures. Their source hashes bind to the formatted scripts.

The probe's `source_sha256` refers to the published launcher; the evaluated original implementation is `experiments/mep-access/prototype-original.py.txt`, whose hash is fixed by `implementation-freeze.json`. The two duplicate graph replays are included in verification coverage, but excluded from the experiment's economic comparison counts.

The original verifier output was generated before a portable-path edit. The reviewer retained it as `verification-before-portable-path.json` and disclosed that exact earlier source bytes were unavailable. `verification.json` is a fresh run of the preserved final raw verifier (hash `f20637fc…`); the parent packaged replay separately binds to the formatted copy. The old result is historical, not a reproducibility claim for the final source.
