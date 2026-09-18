# LiDAR delivery reconciliation: below pursuit threshold

Actual PDF contracts/reports, LAS point clouds and GeoJSON tile indexes were integrated using pdfplumber, Pydantic, laspy, pyproj and Shapely. All data is synthetic. The preliminary score is 76.5/100; no candidate has been accepted on this evidence.

The original benchmark reported 8/8 seeded errors and 0/2 clean false alarms against a narrow per-file parser baseline. Independent preregistered holdouts exposed **one false positive and three missed contradictions**. Corrected code passes these holdouts, but an invalid original positive label was retired: **the original preregistered 8/8 gate did not pass**. Read [the full correction record](benchmark-changelog.md). There is no measured advantage over a complete commercial QC workflow.

## Reproduce

Use a fresh Python 3.11+ virtual environment, install `requirements.lock`, then run `benchmark.py`, `run-holdouts.py`, `benchmark-v2.py`, and `run-holdouts-v2.py` in that order. These commands replace generated fixtures/results in their corresponding directories. Copy the folder to a scratch directory first to preserve committed evidence. Fixture PDF creation timestamps vary.

Published runnable scripts were formatted, unused imports removed, and corresponding source-splitting delimiters updated for packaging. The exact originally executed scripts are retained in `original-source/*.py.txt`. Results were preserved before packaging; a scratch rerun verified the same classification outcomes.

Research evidence and rejected alternatives are in [round-two geospatial research](../../research/round2/geospatial-preservation/README.md). Protocols: [initial](PREREGISTRATION.md) and [independent holdouts](HOLDOUTS.md). Exact versions: [runtime inventory](runtime-versions.json). No external communication or paid service was used.
