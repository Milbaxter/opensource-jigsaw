# LiDAR benchmark adversarial review and correction

The original result remains in `benchmark/results.json` and `first-run.txt`; original code remains `benchmark.py`. Nothing was overwritten.

After reading the code, the parent independently specified four holdouts; protocol was frozen in commit `5396383`. Unchanged code produced **1/1 false positive on a valid interior-point control and detected 0/3 true contradictions**. Raw outputs: `holdouts-first-run.txt` and `holdouts-v1/results.json`.

This exposed two distinct issues: exact equality between observed point bounds and nominal tile boundary was an unjustified assumption; and the integration ignored contract count/AOI and did not check the reverse inventory direction. These are substantial weaknesses, not merely edge-case cosmetic failures.

Correction in `benchmark-v2.py`:

- Replace equal bounds with nominal tile containment of observed bounds. A point cloud can legitimately have no observation at tile corners; this check now catches points outside the declared tile but does not claim to detect all missing observations.
- Reconcile contract-declared exact point count against actual LAS count, separately from report count.
- Require the declared project AOI to be covered by the nominal index union. This only checks nominal delivered coverage. It is not a point-density or survey-completeness test. Real clipped/rotated/irregular tiles need richer geometry rules; this fixture contract deliberately specifies axis-aligned rectangular nominal tile footprints.
- Require every actual tile to appear in the index, in addition to requiring every index reference to exist.

Corrected code passes the valid interior-point holdout and detects all three parent-specified contradictions. Raw outputs: `holdouts-corrected-run.txt`, `holdouts-v2/results.json`. On the original case set, corrected code flags **7/8**, because the original `half_coverage` seeded case only has points in half a nominal tile and is not provably a delivery error under this contract. It now correctly remains unflagged/undetermined. We explicitly retire it as a valid positive label; we do not redefine the original 8/8 preregistered gate as passed. Core runtime ~0.126s on tiny fixtures; not a scale benchmark.

This challenge makes the evidence more honest but still does not establish an advantage over existing full QC workflows. The correction demonstrates reconciliation among actual PDFs/LAS/GeoJSON under a declared simple contract. No commercial product comparison or manual reviewer time-saving test ran. Dossier remains below pursuit threshold and requires a real workflow/baseline pilot to establish incremental value.

Rerun in this folder:

```sh
venv/bin/python benchmark.py
venv/bin/python run-holdouts.py
venv/bin/python benchmark-v2.py
venv/bin/python run-holdouts-v2.py
```

Repeated runs replace the result files for that specific version; first-run logs remain saved separately. PDF creation timestamps may change the input hashes, so byte-identical fixture regeneration is not claimed; geometric/textual case semantics are stable.

Primary specification context: [USGS Deliverables](https://www.usgs.gov/ngp-standards-and-specifications/lidar-base-specification-deliverables) distinguishes the project tiling scheme from actual acquisition/swath boundaries and notes that minimum bounding rectangles are not acceptable substitutes for swath shape. [USGS FY26 project-area/tile instructions](https://d9-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/s3fs-public/media/files/FY26%20DCA%203DEP-B%20-%20Instructions%20for%20Creating%203DEP%20Defined%20Project%20Area%20and%20Tile%20Delivery%20Scheme.pdf) distinguish AOI and buffered defined project area. Therefore the benchmark's simple contract AOI and nominal tile assumptions are fixture rules, not universal USGS checks. A real adapter must model DPA/AOI buffers and approved delivery scheme explicitly.
