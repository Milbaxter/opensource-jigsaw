# C07 evidence and strongest objections

Research by Astra, 2026-09-18. No prototype results, customer contact, business pass, or profitability claim. This supplements the prospective `preregistration.md`; it does not change its criteria.

## Narrow proposition and buyer

Hypothesis: WMS/cartonization integration teams could use an offline, engine-independent regression service that discovers a smaller-item / more-expensive-carton transition, attaches a cheaper constructive placement, and prioritizes the fixture using the buyer's carrier rules. The probable budget owner is shipping systems engineering or fulfillment operations. Its expensive workflow is testing packing configuration, item-master changes and engine upgrades before releasing them. Public evidence below establishes packing and shipping-cost workflows; **it does not establish that this particular regression category is frequent, currently costly, or purchased separately**.

Paccurate's Hunter Douglas case study attributes a description of SAP-to-factory packing integration and replacing manual carton sizing to Rahul Garg, Senior Director IT, ERP Applications & Strategy. That is a named buyer statement hosted and selected by its vendor, not an independently audited case. [Case study](https://paccurate.io/case-studies/hunter-douglas-from-best-guess-to-dynamic-optimized-shipping).

A current Paccurate offer starts at $249/month for 5,000 shipments, supporting an offered paid cartonization category. It also advertises carton analysis/simulation: a direct competitive threat to a generic packing-audit service. Posted pricing is not evidence our candidate has buyers. [Pricing](https://paccurate.io/pricing).

FedEx's dated 2026 service guide supplies a primary, actual charge schedule that makes carton dimensions financially consequential. The planned fee component follows the scoped protocol, rather than treating every nominal fit as the cheapest shipment. Actual negotiated carrier terms may differ. [Service guide, updated September 11](https://www.fedex.com/content/dam/fedex/us-united-states/services/Service_Guide_2026.pdf).

Shipware independently offers parcel invoice audits covering dimensions, weights, surcharges and negotiated-rate errors. Its main service describes gainshare payment; another page offers free Audit and Pay to qualifying shippers above $100,000 annual parcel spend. This confirms a nearby commercial workflow and **weakens a generic paid-audit pitch**. These are postshipment billing checks; the proposed predeployment heuristic witness is different, but the distinction alone does not establish additional willingness to pay. [Audit service](https://shipware.com/solutions/invoice-audit-recovery/), [free qualifying offer](https://get.shipware.com/demo-audit-pay/).

## Near competitors and meaningful baseline

| Alternative | Verified relevant capability | Consequence for this proposal |
|---|---|---|
| Paccurate | Cost-aware cartonization includes thresholds; API resource types allow item-dimension transformations. Pricing includes advanced simulation/carton analysis. | Ordinary fee-aware packing or dimension sensitivity is not distinctive. Incumbent may already catch these cases. No Paccurate comparison is run or claimed. |
| Packvium | Public docs describe exact-integer geometry, independently recomputed placements/objectives, versioned rules, seeded bounded search, and fixture corpora. | Independent validity checking, determinism and regression fixtures are existing capabilities. Its new repository/low adoption do not erase technical prior art. Claims were inspected, not independently benchmarked here. |
| Simple endpoint bounds | A smaller cuboid still fits an inherited valid placement in a fixed carton. A carton fee calculator directly prices fixed outer dimensions. | A generic worst-case tolerance demonstration adds little. Our proposed search must find a real algorithm decision regression; the cheap inherited placement is precisely the analytic witness. |
| Both py3dbp sorting modes | The engine supports ascending/descending volume ordering. | Both must fail the cheap carton for S, while an independent valid cheap witness exists. Default-mode failure alone is not the desired finding. |
| Random metamorphic script | Can generate L/S pairs and check identical invariants. | Hypothesis contributes generation/shrinking, but may not outperform this cheap baseline. No speed or discovery-rate advantage is assumed. |

Primary feature links: [Paccurate on-demand cartonization](https://docs.paccurate.io/docs/on-demand-cartonization), [Paccurate resource types](https://docs.paccurate.io/resource-types), [Packvium](https://packvium.com/), [Packvium Python](https://github.com/toxakara/packvium-python), [py3dbp](https://github.com/enzoruiz/3dbinpacking), [Hypothesis](https://hypothesis.readthedocs.io/en/latest/).

## Acquisition, inputs, and rights

Paccurate publishes an actual WMS/automation/shipping partner directory, and Deposco separately lists its Paccurate integration. These provide a concrete way to identify relevant integration firms and use their public business inquiry routes, subject to authorization. They do not establish a relationship or recruitment conversion. ISTA's laboratory/services directory is an adjacent packaging-consultant channel; it is less directly relevant than WMS integrators for a software-regression service. [Partner directory](https://paccurate.io/partners/), [Deposco integration](https://deposco.com/platform/software-integrations/paccurate/), [ISTA directory](https://www.ista.org/find_a_lab_or_services.php).

The local proof uses synthetic cuboids, original rules code, MIT py3dbp and MPL-2.0 Hypothesis. Exact distribution hashes are in `c07-package-pins.json`; inspected primary license provenance is in that file and `shortlist-license-evidence.json`. Proposed delivery is an offline audit harness running unmodified dependencies, with notices preserved; modifying/distributing MPL-covered files requires appropriate source availability. Do not copy README or tariff PDF text into published research. Before a commercial-data pilot, the participating teams must authorize the deidentified order/catalog exports and applicable contract rules. Availability is a recruitment hypothesis, not established access.

Durable value is currently weak: the useful code could be copied or added upstream. A maintained, permissioned corpus of real integration regressions plus adapters and rule maintenance might create recurring service value, but no such corpus, access, or retention evidence exists. A single old-engine bug is especially weak evidence of a sustained buyer problem. The independent judge must explicitly account for this, and may reject even a successful technical proof.
