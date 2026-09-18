# Frozen source packaging

The evaluated source is preserved byte-for-byte as `frozen/prototype.py.txt` and `frozen/run_frozen.py.txt`. These are Python source files stored with a text suffix so repository formatting does not change the evaluated program. `source-publication-manifest.json` maps original names to published paths and verifies identical SHA256 values. The frozen driver verifies both source hashes before execution.

To recreate the run directory, copy those two text files to `prototype.py` and `run_frozen.py` in a separate scratch directory, copy `implementation-freeze.json`, place the verified original input at `fmc-input.mat`, and create the declared dependency environment at `.venv/` there. Invoke `.venv/bin/python run_frozen.py` in that directory. All outputs are written to `execution/`. Exact installed dependency provenance and executed outcomes will be added when the run completes; the protocol records requested versions.

The initial unexecuted source snapshot is explicitly historical. Independent review corrected it before any control or benchmark execution. It must not be represented as evaluated code.

Benchmark source, including the text-suffixed files, is GPL-3.0-or-later; see its SPDX headers, LICENSE-GPL-3.0.txt and THIRD-PARTY-NOTICES.md. This does not relicense the Jigsaw application. No dependency binaries or raw dataset are included.

## Complete result packet

The final 49-file source/result selection is recorded in `result-publication-manifest.json`. Original source suffixes map to `frozen/*.py.txt`; all listed hashes refer to identical original bytes. Formatted conveniences `fetch-input.py` and `render_results.py` have separate bytes and do not replace frozen evidence. `publication-transformations.json` records redaction of workstation path prefixes from two command logs; the independent review hashes the original driver log, while the public redacted file has its own manifest hash.

The original proposer report's `work/...` review reference resolves publicly to [the independent post-result review](../../research/round4/ultrasonic-independent-review/POST-RESULT-REVIEW.md). Its reproduction commands assume reconstructed original filenames in scratch. The original report and output bytes remain unchanged. For replay, copy the published `execution/` directory to scratch before running the independent checker; never overwrite the published historical results.

The original input and all derived reconstructions credit Alexander Velichko and Anthony Croxford, DOI10.6084/m9.figshare.7178630, CC BY4.0. The arrays and plots are modified analyses, not endorsed source measurements.
