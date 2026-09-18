# A02 — Spreadsheet migration acceptance for archives

**Decision: HOLD / not a pursuit pass.** Real preservation pain and paid category exist; current evidence does not establish enough novelty, practical buyer access or a tested essential integration. This is not a generic spreadsheet formula auditor or a new preservation platform.

## Buyer, pain and output

An archive's digital preservation lead needs to decide whether a migrated spreadsheet preserves the properties their collection actually values. A PDF/TIFF preview can preserve visible numbers while losing formulas, hidden sheets, links and behavior. The output would be a per-workbook source-to-target property diff, policy-based acceptance queue and evidence bundle for the existing preservation platform.

Primary evidence is unusually direct: the [National Archives spreadsheet preservation description](https://www.archives.gov/preservation/digital-preservation/linked-data/spreadsheets) says spreadsheets can contain cross-sheet/external calculations and that significant properties can form test criteria for transformation tools. The [OPF spreadsheet preservation specification](https://github.com/openpreserve/sheets-preservation-spec/blob/main/Draft%20v1.0/Specification.md) explicitly calls for automated conversion and validation support and distinguishes syntactic validation from institution-chosen policy. It also says analysis/appraisal should precede migration. This supports an institution-specific acceptance workflow, not a universal fidelity score.

## Proposed 4-repo combination and exact bridge

1. [apache/poi](https://github.com/apache/poi): read XLS/XLSX source structure and cached values; emit canonical properties keyed by sheet/cell. Apache-2.0, verified from actual `legal/LICENSE` (saved locally as `apache--poi--legal_LICENSE`); preserve release notices when shipping.
2. [LibreOffice/core](https://github.com/LibreOffice/core): run a separately installed conversion subprocess to produce ODS and a visual access copy. LibreOffice source licensing is mixed and cannot safely be reduced to GitHub's top-level GPL detection; official project commonly uses MPL-2.0/LGPL terms, with file-specific and dependency obligations. We fetched the actual COPYING.MPL and repository copying file. A packaging/license review remains required; avoid embedding or relabeling its code.
3. [RvanVeenendaal/Spreadsheet-Complexity-Analyser](https://github.com/RvanVeenendaal/Spreadsheet-Complexity-Analyser): source property extraction/complexity features used to prioritize manual review. [OPF's announcement](https://openpreservation.org/blogs/shoulder-to-shoulder-studying-significant-properties-of-spreadsheets-with-the-opf-archives-interest-group/) states CC0 publication. Direct repo root license discovery did not immediately identify a standalone LICENSE file, so the original declaration must be retained and checked rather than inventing a SPDX result.
4. [richardlehane/siegfried](https://github.com/richardlehane/siegfried): file format identification for source/target and evidence manifest, Apache-2.0 actual license checked.

Input-output bridge: identify format → extract source properties/cached results → convert without opening live external data connections → extract target properties → compare only curator-selected properties → produce a structured report plus hashes attached to the original and derivative. Original workbook is always retained. Formula equality cannot be established by string comparison across Excel/ODF formula dialects; unsupported constructs must be marked unverified, not passed.

## Paid category and competition

[Preservica pricing](https://preservica.com/pricing) lists Starter Plus at £171/month billed annually, excluding sales tax; the same multi-currency page displays $310/$230/$300 for other currencies, so this dossier does not guess which dollar region is selected. Its free tier already transforms files for preservation/access, and Professional supports ongoing transformation. A narrow tool therefore must show value as independent QA of chosen significant properties, not sell commodity conversion.

The [UK Government supplier listing for Preserve365 Professional](https://www.applytosupply.digitalmarketplace.service.gov.uk/g-cloud/services/733747568318802) gives £25,750 per licence. This is concrete budget in the larger category, not evidence that a small archive will buy an additional checker. Enterprise systems such as Rosetta already model significant properties; [Rosetta documentation](https://knowledge.exlibrisgroup.com/Rosetta/Product_Documentation/Rosetta_Preservation_Guide/Preservation_Libraries/003_Significant_Properties) is a direct competitor warning.

The OPF specification and SCA are particularly strong open substitutes and channels. Existing conversion suites, institution scripts, Excel auditing tools and manual spreadsheet review also compete. Paid formula-auditing tools solve part of the problem but do not establish a differentiated archival migration offer. “No exact product found” would not prove absence.

## Novelty, defensibility and distribution

Possible practical novelty: make preservation intent explicit, comparing source versus converted derivative while preserving review decisions in a platform-independent evidence package. This is integration/workflow novelty; the underlying concepts and many components already exist. Maintaining tested migration-path/property profiles could become an asset. Today there is no moat or unique data.

Potential distribution: OPF/Digital Preservation Coalition practitioner communities and preservation service integrators; participating institutions in the spreadsheet specification identify a validation population (Danish, Dutch and Estonian national archives). These are accessible as public communities but national archives are not assumed to be fast buyers. No one was messaged. A more plausible first buyer might be a commercial migration contractor with repeated spreadsheet batches, but none was verified as willing to participate here.

Test-price hypothesis: £500 fixed-scope retrospective migration audit of 100 workbooks. Not an observed sale. The archive would supply a preservation-intent checklist, not merely files. Future subscription pricing is premature.

## Concrete proof recipe for a later validation

This recipe was NOT run and is not a completed technical hard gate. Pre-register 12 source workbooks with curator-selected properties, including hidden worksheets, named ranges, external references with cached values, cross-sheet formulas, date-serial differences, charts and unsupported macros. Generate safe synthetic files or use a licensed public test corpus; never execute arbitrary macros or refresh network links.

Run unchanged LibreOffice conversion as baseline. A format-identifier/ODS syntactic validator baseline can pass a structurally valid output even when significant properties differ. The candidate compares paired source/target extractions and emits exact cell/property losses. Include clean controls where an allowed loss (such as removing macros under the institutional policy) is correctly treated as policy-approved, and a negative control where a visually identical preview has lost a hidden analytical sheet. Success requires ≥90% detection of curator-labelled unacceptable loss, ≤5% false alarms and an explicit “unverified” outcome on unsupported semantics. Compare analyst review time against the institution's actual current workflow, not only a format parser.

Stop if ordinary platform configuration can provide equivalent acceptance evidence with no meaningful extra work. A real trial needs three preservation leads to label properties and one paid contractor pilot. A formula audit alone cannot establish archival semantic equivalence.

## Preliminary rubric assessment

Novelty 6, pain 8, payment 7, feasibility 7, defensibility 5, distribution 6, evidence 7 → **67/100**. Novelty, feasibility, defensibility, distribution and evidence floors fail; the essential bridge has not been demonstrated. Licensing route for LibreOffice/SCA and post-conversion feature coverage also need closure. The purpose of this dossier is to document a substantive candidate and why it should not be promoted merely because the paid category exists.
