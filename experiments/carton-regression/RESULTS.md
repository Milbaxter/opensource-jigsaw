# C07 observed results: five constructive packing-regression witnesses

**The preregistered technical bridge succeeded on synthetic cuboids. No business pass or real invoice savings are established.** The unchanged py3dbp 1.1.2 engine produced five retained transitions, across carton families A, B and C, where shrinking an item makes both supported sorting modes miss the cheap carton. All five have an independently valid cheaper placement inherited from the larger-item run. All replayed in separate processes. The code was frozen before engine execution; parent published protocol commit `ee5b14c` first.

## What ran

Python 3.14.6 on macOS 15 arm64; py3dbp 1.1.2, Hypothesis 6.168.0, sortedcontainers 2.4.0. Implementation SHA-256: `aefd721b10c73ad1907b52f27c6a6edd01feb798c050247f1ba0a39707ad9388`. Exact versions and provenance are in `requirements-executed.txt`, `implementation-freeze.json`, and `execution-provenance.json`. No implementation correction or search-domain amendment occurred after freezing. **Provenance correction/protocol deviation:** the required fetched PDF checksum is unavailable. A post-run script initially mislabeled an HTTP 200 HTML response as the carrier PDF; the parent caught its 1,770-byte size. Content-type and magic-byte inspection confirmed HTML. The corrected provenance retains that failed response hash and the error record. Primary tariff text was independently inspected through the web tool; no locally hash-pinned PDF is claimed.

| Search arm | Generated evaluations | Postdiscovery/shrink evaluations | Seeds with witnesses | Elapsed search |
|---|---:|---:|---:|---:|
| Hypothesis | 8,037 | 3,000 | 3/10 | 30.39 s |
| Standard-library random | 8,252 | 0 | 2/10 | 10.94 s |

There are 19,289 retained trace rows and 19,161 unique serialized case hashes, including excluded cases and unsuccessful searches. The 489 successful predicate evaluations include related shrinking trials; **they are not 489 independent discoveries**. Five final distinct fixtures are retained. All three Hypothesis runs that found witnesses exhausted their 1,000-evaluation postdiscovery cap. Their selected fixtures have smaller aggregate dimensions, but the search did not finish shrinking; no minimality claim is made. The input distributions differ, sample sizes are small, and the arms stop a seed on discovery. These figures do not establish a Hypothesis speed or success-rate advantage. Random testing found useful witnesses too.

48 predeclared tariff/geometry controls passed. There were zero engine or geometry exceptions. The three Hypothesis reductions changed total dimension ticks 558→431, 677→532, and 438→375, retaining 4, 5 and 3 items respectively. The two random fixtures contain 7 and 6 items and were not shrunk. All seeds, including fifteen with no final witness, are in `execution/summary.json` and compressed traces. Nothing was rerun with altered seeds to improve the outcome.

## A small, exact example

Fixture `execution/witness-H-7009.json`, family A, uses these synthetic source dimensions in inches:

| Item | Larger-item case L | Smaller-item case S |
|---|---|---|
| 0 | 3.25 × 39.50 × 3.25 | 3.00 × 39.50 × 3.25 |
| 1 | 8.50 × 9.25 × 9.25 | unchanged |
| 2 | 10.00 × 8.75 × 2.00 | unchanged |

Cheap carton outer dimensions are 48 × 12 × 12, with synthetic inner dimensions 47.75 × 11.75 × 11.75. Larger outer carton is 49 × 12 × 12. L fits the cheap carton in ascending-volume mode. S fails cheap in **both** ascending and descending modes; descending mode fits S in the larger carton.

The independent constructive witness for S uses the cheap carton with the following **oriented dimensions and positions**, in inches:

| Item | Oriented dimensions | Lower-corner position |
|---|---|---|
| 2 | 10.00 × 8.75 × 2.00 | 0 × 0 × 0 |
| 0 | 39.50 × 3.00 × 3.25 | 0 × 0 × 2.00 |
| 1 | 9.25 × 8.50 × 9.25 | 0 × 3.25 × 2.00 |

Containment and disjoint intervals can be checked directly. Item 2 ends at height 2; the others start there. Item 0 ends at width 3; item 1 starts at width 3.25. Item 1 ends at width 11.75 and height 11.25. No engine collision helper is used in the checker. This is a valid witness for the modeled cuboids, not a proof that fragile physical products can safely be packed this way.

Under the scoped official rule, cheap versus larger carton yields a dimension-AHS component of $0 versus $29.50 and modeled billable weight of 50 versus 51 lb. **Neither value is a complete invoice or observed saving.** The fee source is the [FedEx 2026 Service Guide updated September 11](https://www.fedex.com/content/dam/fedex/us-united-states/services/Service_Guide_2026.pdf), verified through the web tool and independently by the parent. The direct URL fetch returned a 1,770-byte HTML response despite HTTP 200; its checksum is not a PDF checksum. Actual contracts, other charges, material cost and packing constraints remain outside this synthetic test.

## Failure checks, neighboring cases and baselines

Clean-process replay enumerated every legal 1–4 quarter-inch shrink of every source axis around the five retained L fixtures: 279 local cases, of which 31 satisfy the witness predicate, 247 still fit cheap, and one fails to fit the larger carton. That last case is explicitly classified `S_no_large_fit`, not an invented expensive shipment. Detailed neighborhoods are retained in each `*-replay.json`.

Ordinary validity checking accepts the valid larger-carton placement; it establishes fit, not the absence of a cheaper feasible placement. The inherited-placement endpoint argument correctly certifies the cheaper solution. The fee calculator correctly prices both cartons. Their combination with generated paired engine executions creates the replayable regression artifact; none of those individual capabilities is claimed to be novel. No Paccurate/Packvium commercial-service comparison was executed.

## Commercial evidence and substantial counterevidence

Parent independently located Kodaris release notes recording a real cartonization defect and its regression tests, including an order whose calculated carton count was too high. This is stronger evidence of the target workflow than generic shipping market size, but does not establish our tested phenomenon's incidence. [Kodaris KOR-154](https://www.kodaris.com/content/releases/kor-154-release). Cycle Labs discusses cartonization-rule testing in commercial WMS QA, and Veridian offers system optimization services: there are existing paid suppliers and possible partners, as well as competition. [Cycle Labs](https://cyclelabs.io/blog/off-the-shelf-testing-for-complex-wms-landscapes/), [Veridian](https://veridian.info/services/system-optimization/).

Crucial prior art: Murphy and Kaiser already studied metamorphic runtime checking using the GAFFitter bin-packing application. Applying metamorphic testing to packing is **not new**. The only proposed narrow addition is economically prioritized constructive witnesses packaged into a practical assurance workflow. [Columbia technical report](https://mice.cs.columbia.edu/getTechreport.php?format=pdf&techreportID=1550). Paccurate already offers cost-aware packing and simulation; Packvium already documents independent validation and fixtures. Further distinctions and exact primary links are in `c07-evidence.md`.

The code is readily copied; durable service value is unproven. This old py3dbp release is an accessible test target, not evidence modern production engines share these failures. Public/synthetic data suffice for this reproducible proof. Access to actual catalogs, contracts and order histories must be separately obtained with consent before a customer-data pilot. Recruiting that access can be a bounded next experiment; it must not be represented as existing access. No outreach occurred. The independent judge must decide whether the evidence supports a narrowly budgeted validation experiment under rubric v2; this researcher does not score their own proposal.

## Replay and publication

From the experiment root, create a Python≥3.10 environment, install `requirements-executed.txt`, then run:

```sh
python prototype.py replay execution/witness-H-7009.json
```

This reruns the unmodified packing engine and all 36 legal local perturbations around that example. `python prototype.py search` repeats the full finite search and overwrites same-named execution outputs; use a fresh copy when preserving the original record. It verifies its own implementation hash against the pre-execution freeze. The publication launcher loads a byte-identical `prototype-original.py.txt`, whose hash is unchanged; the original remains at the experiment root for correct artifact paths.

Publish files listed in `publish-manifest.json`; exclude `.venv`, `__pycache__`, `.hypothesis`, and individual `candidate-*.json` files because every such placement record is retained in `execution/all-candidate-placements.jsonl.gz`. No raw third-party README, license, paper, or carrier PDF is included. `artifact-manifest.json` hashes the original execution evidence; publication renaming is explicitly mapped rather than silently modifying the frozen code.
