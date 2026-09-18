# Sewer handover acceptance — follow-up screen

Status: HOLD, no prototype. Strong public buyer need is real; immediate benchmark/data-rights gate unresolved. Generic file-count checking would not establish useful cross-field advantage.

The narrow proposal is an independent acceptance packet for a contractor or utility, bridging Access data extraction (mdbtools), multimedia validation/alignment (FFmpeg/OpenCV) and GIS reconciliation (GeoPandas/DuckDB). It would check that inspection observations, surveyed pipe assets, timestamp/distance records and submitted video describe the same work, and preserve source-to-target evidence during migration. It would not replace NASSCO-certified defect grading.

## Evidence that improved the screen

- Lee's Summit's 2026 ITpipes renewal documents costly/laborious database conversion and $92,000 first-year annual license. This validates lock-in/pain and paid category; not a separate QA budget. https://lsmo.legistar.com/LegislationDetail.aspx?From=RSS&FullText=1&GUID=120601C3-F298-4F82-AA56-004374F155FC&ID=7797166
- Fairfax County buyer RFP requires cumulative inspection database, video, photos and tracking log, cross-referenced photographs/logs, and redlined GIS maps. This is a recurring multi-artifact handover contract, not an invented checklist. https://www.fairfaxcounty.gov/cregister/DownloadPDF.aspx?AttachmentID=d5785dcc-d048-4ea6-9769-e1f2fb189a01
- Monterey publishes actual workflow: field export, WinCan import and postprocessing, GIS update, archive video/PDF/database, then enter Hansen log. https://files.monterey.gov/Document%20Center/Public%20Works/Engineering/Environmental%20Regulations/Sanitary%20Sewer%20Program/SSMP-Plan.pdf
- Autodesk support Jan23,2026 documents a concrete failure: certain InfoAsset Manager PACP7 exports leave PACP_Ratings blank and a calculated likelihood-of-failure value is incorrect. Their supplied Ruby workaround also depends on display units being MGD and at least lengths being ft. This is an observed vendor defect, but the vendor already supplies its fix, so reproducing it alone is not a product wedge. https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Exporting-PACP7-survey-data-including-the-PACP-Ratings-table-from-InfoAsset-Manager.html
- SewerAI's actual import contract accepts NASSCO Exchange MDBv6/v7 plus videos and optional distance text files. https://help.sewerai.com/articles/4412760428-uploading-inspections
- SewerAI and WinCan already sell migration/integration services. An independent acceptance subcontract could still sell, but cannot pretend migration is an unserved concept. https://www.esri.com/partners/sewerai-a2T5x000008VXJ0EAO ; https://blog.wincan.com/topic/wincan-vx/page/4

## Immediate blocker to a rigorous local test

Search found public specifications, report examples and software instructions, but no clearly reusable realistic multi-artifact handover package with original MDB, video and distance/GIS truth. NASSCO explicitly reserves rights in the codes, exchange template and data dictionary and describes licensing for import/export vendors. The public license terms need resolving before a protocol that depends on reproducing that template or coding rules; an OSS parser's permissive license does not solve schema rights.

Primary terms: https://nassco.org/education-and-training/pacp-lacp-macp/pacp-software/ ; https://www.nassco.org/wp-content/uploads/2023/08/LICENSE-AGREEMENT-FOR-DATA-IMPORT-AND-EXPORT-SOFTWARE-4-14-2021-FILLABLE.pdf . This is not a legal conclusion about generic read-only customer-data reconciliation; it is an unresolved scope/license question for the proposed commercial standards-aware product.

A generic customer-authorized file/hash/row reconciliation service could avoid grading/standard implementation. Its immediate comparator is equally generic database/media/GIS export validation; no measured extra benefit is currently established. Therefore do not spend hours manufacturing a PACP fixture or declare a pass based on a toy missing-file detector. Reopen with licensed sample deliverables or a customer-provided pilot, a precise independent acceptance scope, and the incumbent's real acceptance checklist.
