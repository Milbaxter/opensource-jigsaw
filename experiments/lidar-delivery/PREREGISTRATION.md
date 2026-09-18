# LiDAR cross-artifact acceptance benchmark: preregistered before execution

2026-09-18. Purpose: test essential bridge, NOT market validation or superiority to commercial QC.

Inputs: a contract PDF with deterministic labelled fields (CRS, tile names, expected point count, AOI); two real LAS 1.4 files containing generated non-sensitive points; an independently authored GeoJSON tile index; and a delivery report PDF. These synthetic bundles model official USGS error classes (https://www.usgs.gov/ngp-standards-and-specifications/lidar-error-dictionary-part-2). No claim that generated data are a customer corpus.

Cross-field stack: pdfplumber (PDF evidence extraction) → Pydantic contract schema → laspy (LAS artifact properties) + pyproj (semantic CRS comparison) + Shapely (geometry predicates) → evidence JSON. reportlab creates fixture PDFs only, not product component.

Precommitted baseline: each file parses; LAS contains points with a resolvable CRS and finite coordinates; GeoJSON has valid polygons and resolvable CRS; PDF labelled fields parse. The baseline checks the exact same inputs but does not reconcile assertions across artifacts. It is a per-artifact validation baseline, not a proxy for everything LP360/Global Mapper can do.

Ten independently generated fixtures: two clean cases (EPSG name and equivalent WKT in tile index), plus eight adversarial cases: LAS CRS differs from contract; tile absent; index geometry translated; delivery report wrong point count; delivery report CRS wrong; tile index references nonexistent tile; actual tile filename does not match index; second tile only covers half the expected footprint.

Success preregistered: 8/8 adversarial bundles flagged, 0/2 clean false alarms, baseline accepts >=6/8 adversarial bundles. Every flag must list the actual artifact and evidence, never assert formal USGS compliance. No changes to thresholds after results. Runtime reported but not a pass threshold.

Hard limits: contract parsing is deliberately deterministic; arbitrary contracts, 3D/vertical CRS, measurement accuracy, DEM matching, point classification, visual anomalies and scanning costs are NOT evaluated. Expected buyer experiment: 3 mapping firms independently review 10 historical delivered packages; >=80% of machine alerts judged actionable, >=50% reduction in review time against current workflow, and 2 paid $250 pilots before product build.
