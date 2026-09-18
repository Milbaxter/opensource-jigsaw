# Frozen source packaging

The evaluated source is preserved byte-for-byte as `frozen/prototype.py.txt` and `frozen/run_frozen.py.txt`. These are Python source files stored with a text suffix so repository formatting does not change the evaluated program. `source-publication-manifest.json` maps original names to published paths and verifies identical SHA256 values. The frozen driver verifies both source hashes before execution.

To recreate the run directory, copy those two text files to `prototype.py` and `run_frozen.py` in a separate scratch directory, copy `implementation-freeze.json`, place the verified original input at `fmc-input.mat`, and create the declared dependency environment at `.venv/` there. Invoke `.venv/bin/python run_frozen.py` in that directory. All outputs are written to `execution/`. Exact installed dependency provenance and executed outcomes will be added when the run completes; the protocol records requested versions.

The initial unexecuted source snapshot is explicitly historical. Independent review corrected it before any control or benchmark execution. It must not be represented as evaluated code.

Benchmark source, including the text-suffixed files, is GPL-3.0-or-later; see its SPDX headers, LICENSE-GPL-3.0.txt and THIRD-PARTY-NOTICES.md. This does not relicense the Jigsaw application. No dependency binaries or raw dataset are included.
