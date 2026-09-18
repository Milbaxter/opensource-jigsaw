# A01 — LiDAR delivery contradiction preflight

**Decision proposed:** a technically demonstrated, tightly bounded validation candidate; not a validated business and not automatically an 80-point pursuit pass. The strongest unresolved objections are commodity GIS checks, buyer access without an existing channel, and easy replication by incumbents.

## Workflow and buyer

A survey/mapping firm's delivery QA lead uploads the contract's confirmed requirements, the project report, LAS tiles and tile index before sending a milestone package. The service returns artifact-specific contradictions and hashes for review: wrong CRS compared with the contract, a report count inconsistent with the files, index references to missing tiles, and footprint disagreements. First scope is one known delivery template and horizontal CRS, with an analyst confirming parsed fields. Output is an exception pack the firm's existing QA lead can use; it does not approve a survey, establish positional accuracy or certify USGS compliance.

Real public pain: USGS maintains a dictionary of commonly encountered delivery errors that includes inaccurate reports/metadata, wrong contractual CRS, geometry errors and extent mismatches. These are actual error classes, not invented generic risks. [USGS Error Dictionary](https://www.usgs.gov/ngp-standards-and-specifications/lidar-error-dictionary-part-2). A public third-party QA report also documents completeness, projection, coverage, naming and format checks performed by a mix of commercial tools and proprietary scripts. This both supports the work's existence and challenges novelty. [Calvert County QA report](https://noaa-nos-coastal-lidar-pds.s3.amazonaws.com/laz/geoid18/8493/supplemental/Final_Calvert_LiDAR_QA_Report.pdf).

## Exact OSS bridge and licensing

Five product repos bridge PDF extraction, typed contractual assertions, point-cloud formats, geodesy and computational geometry:

| Repository | Actual license | Tested version | Input → output |
|---|---|---|---|
| [jsvine/pdfplumber](https://github.com/jsvine/pdfplumber) | MIT | 0.11.10 | contract/report PDF → labelled textual facts |
| [pydantic/pydantic](https://github.com/pydantic/pydantic) | MIT | 2.13.5 | extracted facts → validated requirement schema |
| [laspy/laspy](https://github.com/laspy/laspy) | BSD-2-Clause, confirmed from actual license and installed metadata despite GitHub NOASSERTION | 2.7.0 | LAS 1.4 → CRS, point count and actual coordinate bounds |
| [pyproj4/pyproj](https://github.com/pyproj4/pyproj) | MIT | 3.8.0 | EPSG/WKT → semantic CRS equivalence |
| [shapely/shapely](https://github.com/shapely/shapely) | BSD-3-Clause | 2.1.2 | tile-index geometry + LAS bounds → spatial contradictions |

Python is 3.14 in this run. NumPy is transitive data tooling. ReportLab 5.0.1 is used only to generate fixture PDFs. Actual license text and repository metadata are saved in `licenses-decoded.json` and `selected_repos.json`; wheel metadata in `runtime-versions.json`; all exact pip packages in `requirements.lock`. These permissive core licenses allow commercial combination with notice obligations. Shapely's binary GEOS dependency has LGPL obligations; preserve its license/notices and dynamic-library rights in binary distribution. No GPL/AGPL dependency is knowingly incorporated into product code. This is a checked practical licensing route, not legal advice or a full dependency SBOM audit.

## What ran and what did not

**Adversarial review changed the conclusion.** Parent-specified holdouts found a false alarm on a valid sparse/interior point cloud and 0/3 detection of untested contract-count, required-AOI and missing-index-entry contradictions. Corrected code detects all three and accepts the clean interior-point case. It now flags 7/8 original seeds because the original half-tile-points case is not valid evidence of missing coverage; that eighth positive label is retired. The original 8/8 preregistered success is historical and does not survive the semantic audit as a meaningful complete gate. See `benchmark-changelog.md`, preserved `holdouts-v1/results.json`, corrected `holdouts-v2/results.json` and `benchmark-v2/results.json`. No thresholds were silently changed.


Preregistration was written before execution and parent committed it as `b90759b` at `experiments/lidar-delivery/PREREGISTRATION.md`. All eight adversarial bundles were flagged; both clean controls passed; per-artifact parse/validity checks flagged zero adversarial bundles. The clean control using equivalent WKT/EPSG descriptions confirms comparison is semantic, rather than a string mismatch. First run core elapsed time was 0.125 seconds; total fresh process startup was about 9 seconds on this host. These are tiny generated files, not throughput benchmarks.

**Actual files**, not mocked parser responses: PDFs, LAS 1.4 point files and GeoJSON index, with SHA-256 input manifests and per-alert expected/actual evidence in `benchmark/results.json`. The eight seeded problems were LAS CRS contradiction, missing tile, shifted index geometry, incorrect report point count, incorrect report CRS, nonexistent indexed tile, renamed tile, and partial tile extent. First-run output is preserved unchanged as `first-run.txt`. Criteria were not revised after the result.

This proves only that the essential bridge catches cross-artifact errors missed by the restricted per-file baseline in these fixtures. It does **not** prove superiority to full LP360, Global Mapper, GeoCue, a competent QA analyst or existing mapping-firm scripts. Existing normal workflows can catch all these errors. The hypothetical advantage is faster repeatable packaging and fewer manual reconciliation steps, to be measured in a real pilot.

Data rights: benchmark inputs are generated de novo with fictional project geometry; no customer, patient or personal data and no third-party survey observations. The fixture PDFs are plain labeled documents generated for this experiment. CRS definitions come via the licensed pyproj/PROJ/EPSG stack. A future real public-data control is the [OpenTopography Meteor Crater collection](https://portal.opentopography.org/datasetMetadata?otCollectionID=OT.112011.26912.3), which explicitly publishes CC BY 4.0 licensing and supplies survey report, LAS validation report, boundary and tile index. It was discovered, not downloaded or benchmarked here.

Reproduce from this directory:

```sh
python3 -m venv venv
venv/bin/pip install -r requirements.lock
venv/bin/python benchmark.py
```

Implementation limits: fixed-label contract parser; no arbitrary contractual language, vertical datum/epoch reconciliation, point accuracy/classification, scan OCR, multi-gigabyte streaming, clipped edge-tile tolerance or spatial reprojection in mismatch cases. Original footprint comparison was exact and failed the interior-point holdout. Corrected v2 checks containment, bidirectional inventory, count and required-AOI coverage under the simple fixture contract. It still cannot establish observation density or full survey completeness. This is a material limit before pilot conclusions.

## Paid category and nearest substitutes

[Global Mapper vendor pricing](https://www.bluemarblegeo.com/purchase-global-mapper/) currently lists Standard $700 and Pro $1,750 for a single-user node-locked purchase, with Pro maintenance/support $610 per 12 months. This proves a paid geospatial processing category, not incremental willingness to pay for this product. Its Pro suite includes control-point QC, point-cloud comparison, scripting and reports; it can likely implement many checks via existing workflows. [Global Mapper capabilities](https://www.bluemarblegeo.com/docs/guides/global-mapper-24-getting-started-guide-en.pdf).

LP360's documented header QA extraction requires a paid license and assumes headers are correctly populated. [LP360 header extraction](https://support.lp360.com/hc/en-us/articles/31877218124819-QA-QC-on-LIDAR-data-using-either-LP360-Command-line-executables-or-the-Point-Cloud-Statistics-Extractor). Its broader QA tooling has custom issue lists, review navigation and exported issue layers; its 2025 training covers statistics, accuracy checks and reports. Thus lack of one feature on a marketing page is **not** evidence of absence. [LP360 QA workflow](https://support.lp360.com/hc/en-us/articles/31853465568275-Tips-for-Quality-Assurance-and-Quality-Control-QA-QC-for-LiDAR-data), [LP360 2025 QA training](https://support.lp360.com/hc/en-us/articles/47214443170835-How-to-QA-QC-in-LP360).

[lasvalidate](https://downloads.rapidlasso.de/html/lasvalidate_README.html) validates LAS-format conformance; PDAL/GDAL scripts are a strong low-cost substitute for cross-artifact spatial checks. This candidate must outperform setup/review labor for a particular delivery template, not merely beat a narrow file parser.

## Wedge, distribution and bounded next test

Potential wedge: a downloadable, local preflight for one repeat USGS/agency delivery template, emitting the customer's existing QA evidence format and handling reporter-approved contract facts. Hypothesized price: **$250 per historical-package pilot**, or $99–299/month only after repeated use is shown. These are test prices, not observed sales or validated budget.

Reachable validation population is identifiable mapping QA specialists via the public [ASPRS professional directory](https://my.asprs.org/), firms describing LiDAR delivery such as [Angell Surveys](https://angellsurveys.com/services/lidar/), and [Dewberry](https://www.dewberry.com/services/geospatial-mapping-and-survey). The latter is a large sophisticated firm and more useful as a workflow expert than an easy initial sales target. No contacts were harvested or messaged. Public directory access is a possible discovery channel, not proof of affordable acquisition. A free local checker plus a reproducible rule pack could be distributed to this professional audience, subject to community rules.

Next experiment: obtain permission from three mapping QA leads to replay ten historical packages with analyst-confirmed contract facts. Randomize package order for their normal review versus assisted review. Precommit ≥80% actionable alerts, ≥50% median review-time reduction, no missed critical contract contradiction already found by the reviewer, and two paid $250 pilots. Kill if the same effort can be reproduced in existing software without meaningful setup cost. A customer-specific rule pack and regression corpus could become useful accumulated assets, but there is no current moat.

## Preliminary score, not independent judgment

Novelty 7, pain 8, payment 8, feasibility 9, defensibility 6, distribution 7, evidence 8 → **76.5/100** under the prospective weights. Confidence about bounded technical feasibility is ~0.8; confidence of commercial differentiation is lower. All numeric floors can be met, but total misses 80. Novel workflow packaging is plausible; an independent reviewer should not inflate novelty/distribution to force a pass. If parent judge applies a different score, it should cite new evidence or a plainly stated interpretation.
