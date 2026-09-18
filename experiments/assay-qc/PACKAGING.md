# Publication changes

`ORIGINAL-MANIFEST.json` describes the research handoff before publication. Original evaluated script bytes remain in `raw-evidence/*.txt`; `evaluation-freeze.json` refers to those original bytes. Executable copies are formatted and unused imports removed for repository CI. Runtime logs replace local workspace paths with placeholders. No result, model, ranking, or protocol content changed.

To preserve committed evidence, copy this directory to scratch before reproducing: scripts write their outputs beside themselves. Dataset downloads and predictions are deliberately excluded from Git; `fetch.py` verifies source archive hashes.

The parent reran calibration, ranking and evaluation with formatted scripts against the original cached image predictions and source archives. All result fields reproduced exactly except the expected timestamp and source-code-derived ranking hash. The image segmentation stage was not rerun during packaging.
