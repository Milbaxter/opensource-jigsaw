# BAS service lead — preserved, no prototype performance run

Decision at 2026-09-18: promising paid workflow and public data, but no adequate differentiated mechanism selected. Do not treat this as a pursuit pass. No preregistration has been frozen and no classifier performance comparison has run.

## Verified buyer work

The public Virginia Tech VTS-913-2018 contract packet contains a 2018 U&S Services quote. Printed slide16, “Pricing Review Continued,” specifies Task1 point mapping from Siemens Apogee, Tracer ES and AiM asset data into ICONICS using BAC sheets: 25.8 hours, $3,900. Virtual points are included. Task5 BAC-sheet generation:8.6h/$1,300, and the supplier expects automation. Total172h/$26,000 includes graphics, asset classes and FDD rules, so it must not be represented as the mapping budget. Slide16 says the example is a single/initial500asset-point building. Slide15 has a different volume pricing premise: minimum10buildings/year, average1,100points. Historic quote is evidence of an established paid service, not present willingness to pay for this entrant.

Source: https://www.procurement.vt.edu/content/dam/procurement_vt_edu/contracts/documents/VTS-913-2018.pdf . Local source PDF/text live in the parent directory. The packet's later renewals do not make the original quote a2026price.

## Public data verified

Official raw dataset v3 DOI https://doi.org/10.6084/m9.figshare.28705559 (2025-04-03), CC BY4.0, attribution to Arian Prabowo, Xiachong Lin, Imran Razzak, Hao Xue, Emily Wern Jien Yap, Matthew Amos, Flora D. Salim. Exact Figshare metadata with download URLs/checksums preserved in figshare.json. Current raw access supersedes old README sentences about training-only embargo.

Downloaded all three site metadata CSVs and Brick1.2.1 graphs, about12MB. Raw zipped timeseries total18.97GB; none downloaded. CSVs contain whole-period measured summaries (count, mean, std, quartiles, range, unique count), Brick target class and UUID. No original BAS point names remain. An honest experiment could evaluate retrospective name-free assistance with an existing equipment inventory; it cannot evaluate naming accuracy or a short-window cold start. Original dataset annotations were expert-created but datacard says not independently validated.

Schema inspection only (script and JSON preserved): A8374rows/8349positive counts; B851/851; C10440/5347. C has2392metadata rows without an equipment type; do not exclude these simply to improve performance. Graphs retain isPointOf and equipment/location classes. A contains FCU while B contains Fan_Coil_Unit; aliases/ontology normalization can be useful, but a strong baseline must receive the same canonicalized features. Source point rdf:type and annotated power/units properties risk target leakage if treated as free deployment inputs. Masking must precede any future model use, with a documented allowed-input contract.

## Why no forced prototype

A candidate was considered: Brick ontology parsing + time-series classifier + calibrated abstention + SHACL-validated reviewed import. Published BTS summary-stat RF, nearest-neighbor and strong multimodal RF would be same-input baselines; building-level holdout prevents time-series/name leakage. But the graph supplies no justified restrictive cardinality constraints for a global assignment solver. The proposed ontology filter largely duplicates equipment features the baseline can use. Adding OR-Tools or calling a different RF probability weighting a cross-field breakthrough would not strengthen the business case.

There may still be a commercially useful portable onboarding subcontract/service with a reviewable import packet. The current research has not demonstrated its specific coverage, installation, or workflow-cost advantage. No claim of human minutes saved is supported. A future pilot would need actual original-name exports, engineering-unit inputs acquired independently of target labels, deployment constraints, and timed reviewer tasks.

## Strong prior art, not automatic disqualification

- Clockworks explicitly combines nearest-neighbor point-name classification with ontology-allowed types, and uses LLMs on building documents: https://clockworksanalytics.com/ontologies-ai-building-metadata-mapping/ . Current onboarding bulk QA: https://clockworksanalytics.com/onboarding-design-updates/ .
- Plaster is an OSS framework for names/time-series tagging, confidence and human feedback: https://github.com/plastering/plastering .
- Unified Architecture combines BAS names/time series: https://arxiv.org/abs/2003.07690 .
- Brick-DICL June2026 includes low-confidence human review: https://arxiv.org/html/2606.17637v1 .
- Independent commercial review: work/bas-independent-review/PRE-RESULT-REVIEW.md (workspace-relative, outside this folder).

The above establish a strong existing baseline. They do not rule out a focused integration or service. A future proposal must identify and measure a different practical outcome.
