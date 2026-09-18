# Real-image test of decision-aware segmentation review

This is a research-only experimental prototype with a preregistered success/failure gate. Outcome: failed advantage gate. Read RESULTS.md, PROTOCOL.md and DOSSIER.md before interpreting results. The three decisions concern nuclear count/median area relative to fixed training quantiles; they are not biological hit labels or clinical decisions.

## Reproduce

Tested with Python 3.14 on Apple Silicon. From this directory:

```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements-lock.txt
.venv/bin/python fetch.py
PYTHONWARNINGS=ignore .venv/bin/python prepare_calibration.py
PYTHONWARNINGS=ignore .venv/bin/python segment.py --images data/images --out predictions
.venv/bin/python calibrate.py
.venv/bin/python rank.py
# Only this final command decodes held-out annotation masks:
PYTHONWARNINGS=ignore .venv/bin/python evaluate.py
```

`fetch.py` checks pinned source hashes. It retrieves about 81 MB of official public data. Four parallel byte ranges work around unreliable long connections. It never decodes masks. `prepare_calibration.py` opens only train/validation entries. `segment.py` takes image paths and never reads masks. `rank.py` receives frozen calibration outputs and image-derived features and saves all rankings before `evaluate.py` opens any test annotation. The code uses original published splits (100/50/50). No test image was manually selected or corrupted to favor the candidate.

`model.json` records all 24 training parameter scores, selected settings, thresholds, and validation-only baseline selection. `rankings.json` includes all randomized/stratified orders and input hashes. `results.json` is the first held-out result, including failed conditions; there is no tuned second attempt. Some dependencies emit deprecation warnings, hence the environment warning suppression in reproduction. This does not hide assertion/runtime failures.

## Rights and attribution

BBBC039v1 is CC0 as specified on https://bbbc.broadinstitute.org/BBBC039. Dataset citation: Caicedo et al. 2018, BBBC039v1, Broad Bioimage Benchmark Collection; collection described by Ljosa et al., Nature Methods 2012. Data URLs/hashes: data-provenance.json. Ground-truth decoding follows the representation documented by the dataset authors: connected components of the first PNG channel. No unlicensed example source code was copied.

Runtime source licenses checked: NumPy BSD-3 (manual review; GitHub API NOASSERTION); SciPy BSD-3; scikit-image default BSD-3, selected BSD-2 thresholding and MIT helpers. components.json stores exact source license URLs and hashes. Binary wheels include their own dependency notices; preserve them if distributing binaries. We publish scripts and dependency pins rather than vendoring libraries or dataset archives. This is a compatibility screening, not a claim to own upstream code or data.

## Attempt log

- Before inference, protocol SHA256 frozen as `544e5b99a44ea2b6c37b76962f2c827881b231d3ea3baa91a9ed87c5a007161b`; parent published the preregistration.
- Initial source download truncated at 30.7/77.9 MB; a single resumed connection later stalled. Parallel verified byte ranges completed the identical official archive; no dataset substitution.
- First segmentation attempted Apple's `__MACOSX` resource forks accidentally included by a broad TIFF glob. It failed before predictions were written. `attempt-01-resource-fork-error.log` preserves the error. Filtering nonimages fixed file enumeration, with no algorithm changes.
- Before any held-out mask decoding, quantiles were corrected to use raw training measurements instead of a floating-point log/exponential roundtrip. Initial pre-evaluation model/rankings are retained as attempt-02-float-*.json. The official decoder is https://gist.github.com/jccaicedo/15e811722fca51e3ae90e8b43057f075 .
- Calibration and segmentation parameters remain those preregistered. Any future changes after results must be separately labeled exploratory.

No external messages, customer contacts, dataset uploads, commits or pushes were performed by this subagent.
