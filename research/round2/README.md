# Round two: search in progress

The first research round and separate CLI validation produced eight rejected hypotheses. The user requested continued discovery until a defensible pursuit candidate is found, with transparent rubric improvements and ongoing repository updates.

The [prospectively frozen v2 rubric](../../docs/rubric-v2.md) evaluates whether a bounded validation experiment is justified. It uses an 80/100 threshold, dimension floors, and hard evidence, comparative benchmark, licensing, access, and experiment-budget gates. It does not establish profitability. Historical v1 results remain unchanged.

The three published broad metadata captures contain **2,246 distinct repository names** after case-insensitive deduplication; see [counts and source paths](broad-crawl-counts.json). This is discovery metadata, not 2,246 deep audits.

Two Astra research tracks are exploring additional components and recording rejected combinations:

- Document, geospatial, preservation, and public-data workflows.
- Developer operations, data engineering, verification, and scientific testing methods.

The [developer-workflow research](developer-workflows/README.md) records 569 repository candidates and 16 combinations. The [dbt prototype](../../experiments/incremental-fuzz/README.md) reproduces temporal failures through actual materializations, while documenting exact conceptual prior art and a corrected benchmark-classification bug. The [LiDAR prototype](../../experiments/lidar-delivery/README.md) failed independent false-positive/missed-check holdouts; corrected results and the invalid original positive label are preserved. [Geospatial/preservation discovery](geospatial-preservation/README.md) records another 444 repositories and 20 combinations. [Image-review prioritization](../../experiments/assay-qc/RESULTS.md) failed its held-out advantage gate: six corrected mistakes versus seven for simple margin ranking. [Independent Astra review](assay-independent-review/rejection.md) confirmed the rejection. [Cartonization regression discovery](../../experiments/carton-regression/RESULTS.md) generated five replayed counterexamples across three carton families. A second independent geometry implementation confirmed them; [Astra judged the business hypothesis WATCH, 76.5/100](carton-independent-review/REVIEW.md), below the threshold and defensibility floor. A passing synthetic prototype alone cannot establish a business case.

[Independent Astra judging](dbt-independent-review/judgement.md) reproduced the dbt bridge and returned **WATCH, 76/100**, below the frozen 80-point total.

Status: **researching; no v2 candidate accepted yet**. No external outreach or paid purchases have been made.
