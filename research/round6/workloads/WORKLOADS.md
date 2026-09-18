# Public scientific-array workloads: feasibility screen

**Decision: HOLD the present optimizer experiment.** Authentic complementary requests exist, public ERA5 source access is feasible, and code/data rights can be separated. This collection does not establish a consequential shared-budget choice. No performance evaluation, workload replay, candidate implementation, or scientific-array payload download occurred in this screen. The 512 MB limit was a prospective source-download allowance, not evidence of a customer storage budget.

## Authentic requests and their limits

The pinned sources and exact code licenses are in `workload-ledger.json` and `source-pins.json`. All are public programs/tutorials, not production telemetry. Code inspection makes them inspected case studies, not blind historical workloads.

- [Geoscience Australia's climate-data notebook](https://github.com/GeoscienceAustralia/dea-notebooks/blob/a6648997c16e240aa82f3e5b500f814d457994fc/How_to_guides/External_data_Climate.ipynb) requests a Victoria bounding box of hourly ERA5 precipitation for 2020, then produces an annual map. It already uses anonymous ARCO. The requested cube is small, but the source stores each hour as a global chunk; replaying the original entire year would exceed the proposed download cap.
- [AtmosCol's ERA5 lesson](https://github.com/ProjectPythia/AtmosCol-2023/blob/9742801d5674b9ec15691e698b4ecef9db43a6de/notebooks/3.Aplicaciones/3.3.ERA5.ipynb) requests a global temperature map, a Colombia daily regional mean, and a Bogotá annual point series. It explicitly selects spatial versus temporal Arraylake layouts. A two-layout baseline is therefore demonstrated incumbent practice, not an optional weak alternative.
- [Earthmover's risk workshop](https://github.com/earth-mover/risk-analysis-workshop/blob/ece787dc5add9f9764f859df55d1bc2b119439ce/era5.py) requests a global precipitation map, three-variable Indian heat-wave snapshot, and NYC temperature/dewpoint history. It explicitly logs in and uses both layouts. Anonymous ARCO substitution is feasible in principle but is an adaptation requiring coordinate/variable/unit checks, not an unchanged replay. AtmosCol and this workshop are different repositories but share the same vendor data service; project separation alone would exaggerate independence.
- NOAA's OISST notebook is an authentic agency source, but includes full-map, Arctic reduction, and eager whole-file download operations. Xarray's ERSST tutorial eagerly loads the entire source before its point selections. Neither supports an unchanged remote point-read trace. WeatherBench global scoring, native Gaussian-grid ARCO examples, and the Pangeo fullscan example do not strengthen a sparse regular-array benchmark.

Shortening a year or changing the dataset grid/cadence must be disclosed before execution. Such tests could be operator-preserving infrastructure case studies, but cannot validate the original scientific outputs or a production workload distribution. No arbitrary frequency multipliers, random regions, or repetition counts have been inferred from these examples.

## Dataset access, layout, and rights

[ARCO's primary README](https://github.com/google-research/arco-era5/blob/8fb5e9b982f489ba91af3ced9ce0b0a8ade8dd7d/README.md) provides anonymous access and explains commercial/research use under the Copernicus license. Its Apache license applies to repository code; it is not the dataset license. Monthly updates mean the archive is not immutable merely because old dates are selected. A future experiment must pin fetched object generations/content, metadata, and validity ranges.

The exact regular-grid `.zmetadata` was fetched from `https://storage.googleapis.com/gcp-public-data-arco-era5/ar/full_37-1h-0p25deg-chunk-1.zarr-v3/.zmetadata`. Despite the suffix, metadata specifies Zarr format 2. Surface variables use float32, dimensions time/latitude/longitude, shape 1,323,648×721×1440, and chunks 1×721×1440: 4,152,960 decoded bytes per hour. A sample existing temperature object is 2,312,993 compressed bytes by HEAD. Its scientific date was not decoded; the exploratory numeric chunk index must not be assigned a date. No payload was fetched. The larger 154 MB chunk noted in the README includes pressure levels and does not describe these surface variables.

The public [WB2 ERA5 store](https://storage.googleapis.com/weatherbench2/datasets/era5/1959-2022-6h-64x32_equiangular_conservative.zarr/.zmetadata) offers a smaller footprint: 92,044×64×32, float32, **time/longitude/latitude**, chunks 100×64×32. One actual chunk is 580,059 bytes by HEAD. This 6-hour, 5.625-degree source is not scientifically interchangeable with hourly 0.25-degree queries; its time coverage also excludes the 2024 examples. Changing source would require explicit date and resolution adaptations.

The exact [WB2 ERA5 dataset LICENSE](https://storage.googleapis.com/weatherbench2/datasets/era5/LICENSE) was retrieved and hashed (`wb2-era5-license.txt`): ECMWF Copernicus License v1.2, November 2019. It permits lawful reproduction/adaptation/distribution with acknowledgement and modified-data notices. This file is source-specific evidence; do not assume WB2's Apache code license licenses all forecast datasets. ARCO's bucket-root `/LICENSE` returned 404, retained in access records; its own README supplies the primary link and terms statement. NOAA CDR's [use agreement](https://www.ncei.noaa.gov/pub/data/sds/cdr/CDRs/Sea_Surface_Temperature_Optimum_Interpolation/UseAgreement_01B-09.pdf) allows data use separately from production software. No scientific payloads are included in this publication packet.

## Read-only retained-storage estimate

`storage-feasibility-estimates.json` calculates float32 logical sizes directly from source operators and ARCO grid metadata. It is not a compression, runtime, request-count, egress, or cloud-cost measurement. Victoria bounds come from the pinned polygon; the estimate includes the bounding cube before masking. NYC conservatively uses the entire allocated ARCO time axis, exceeding valid data coverage.

| ERA5 request materialization | Logical bytes |
|---|---:|
| Victoria 2020 precipitation cube, 21×36×8784 | 26,562,816 |
| Global temperature map | 4,152,960 |
| Colombia 24-hour temperature cube, 69×101 | 669,024 |
| Bogotá 2024 temperature point series | 35,136 |
| Global convective-precipitation map | 4,152,960 |
| India 131×129 snapshot, three variables | 202,788 |
| NYC entire allocated axis, two variables | 10,589,184 |
| **All seven** | **46,364,868 (~44.2 MiB)** |

Regional/point requests alone total 38,058,948 bytes (~36.3 MiB). Coordinate arrays and container overhead are excluded, but these would not plausibly transform this collection into a demanding storage-allocation problem at a modest ordinary budget. This is limited to the seven eligible ERA5 requests: it does not assert that every inspected NOAA/fullscan program's raw cube fits. Cached final annual/daily reductions can be smaller still, although retaining only outputs cannot answer changed future parameters.

The real source scans required to construct these views can be much larger than retained storage. A fixed-example speedup after scanning years of global source chunks could merely move the cost to setup. Build reads, write bytes, request overhead, cold and warm caches, and useful lifetime must all be included. No claimed byte reduction or business benefit has been measured here.

## What would warrant reopening

A public or consented workload with genuine independently varying regions, dates, and repeated analyses could make reusable tiles share budget meaningfully. It would need to establish why direct materialization of all observed requests, cached final results, tuned single/two-layout stores, and greedy placement are insufficient at an independently justified storage constraint. The existing examples are sufficient to test adapter correctness, but do not establish that OR-Tools adds a useful bridge. Do not choose an artificially tiny budget simply to make the solver matter.

If reopened, freeze project-level separation and actual query operators before selecting plans; do not claim project-level independence when sources derive from the same vendor lesson. Freeze source/version/coordinate/units equivalence and the exact accounting contract. Compare per-request views, output memoization, LRU/LFU, greedy coverage, best single partial replica, tuned single/sharded and complementary full layouts. No protocol or threshold is proposed in this screen because the necessary workload mechanism remains unsubstantiated.
