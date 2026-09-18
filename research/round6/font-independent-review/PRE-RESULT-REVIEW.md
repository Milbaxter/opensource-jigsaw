# Independent font-witness pre-result review

Recorded 2026-09-18T10:52:45.178303+00:00. Reviewer: Astra, independent of proposal author. Reviewed draft SHA256 `d0bcee063588bf49301411039fc34963975fbe2fe463da1a8241af7d9ec3ca8a`. The draft remains unfrozen; this is a prospective checking plan, not experiment authorization, a score or a pursuit verdict. No font shaping, witness generation, model execution or comparative evaluation was performed in this review. Metadata-only FontTools inspection is retained in `structural-root-inspection.json`.

## Decision before results

The bounded lookup-effect coverage endpoint is coherent if its oracle and equal-budget baseline are implemented correctly. A compiler/model-checking to font-engineering transfer is concrete: parse the actual GSUB program, solve interacting substitutions, then validate real strings with the native shaper. It is not enough to enumerate table contexts and import Z3. Native-confirmed additional coverage would be a technical result, not evidence of defects found, minutes saved or willingness to pay.

A baseline-only Stage 0 is a useful prospective economy: after oracle controls, compute coverage of an eligible retained project/practical corpus. If fewer than 10 accepted targets remain on both primary fonts, the proposed absolute improvement is mathematically impossible and the expensive symbolic implementation can stop. This bound is valid only for the baseline actually retained within the frozen runtime and 128-string cap; unlimited corpus union coverage is insufficient. Freeze this staging and implementation before execution. Preserve a stopped test as a negative screen, without claiming a working symbolic bridge.

## Validity checks before the final freeze

1. Resolve the active `calt` feature through the selected Script/LangSys, not every FeatureRecord tagged `calt`. Structural inspection found 16 such records in Fira Code 5.2, each with 103 root indices, versus one record with 101 roots in 6.x. The prior 198/286 counts describe transitive reachable lookup closures, not the proposed top-level denominator. Confirm actual native scheduled roots and preserve the complete local target set. IDs are exact-font-local; a recompiled lookup index is not a cross-version identity.
2. Native coverage must compare the glyph buffer before and after the outer scheduled lookup, maintaining a nested lookup stack. A matched zero-action context, a nested intermediate change restored before exit, and a lookup merely entered must not count as a net effect. Root coverage does not mean all branches, subtables or substitution sites were tested. Keep separate descriptive subtable counts if available, without changing the primary endpoint.
3. The trace callback must return True explicitly. uharfbuzz documents that returning False can skip a shaping step. Copy glyph IDs/clusters while the buffer state exists; do not request glyph positions mid-GSUB. Compare final traced and untraced glyphs and positions. A silent tracing-induced change invalidates the oracle.
4. Fix script, direction and language without process-locale defaults. `dflt` is an OpenType language-system convention; document its actual HarfBuzz configuration rather than assuming a BCP47 string and an OT tag are interchangeable. Confirm the executed feature plan matches the modeled one. Disabling other present features is part of this narrow configured-workflow claim, not typical unconstrained editor behavior.
5. Include native synthetic controls for type6 formats1/2/3, class0, reverse-order backtrack arrays, first matching rule, matching zero-record rules that block a later rule, nested substitutions seeing earlier modifications, and cursor advancement after an application. Every reachable unsupported lookup must reject unless a recorded conservative closure proves its input impossible. Full GSUB semantics cannot be inferred from a few successful ligatures.
6. Main candidate and combined baseline must ingest the same pre-existing corpus and share one total budget each. Recursive enumeration must retain class alternatives, preimages and nested contexts; do not reduce it to one easy representative. Use the same deduplication, native oracle and greedy set-cover in both pipelines. Account for corpus extraction/replay and final selection in totals, and report coverage-versus-corpus-size curves alongside the frozen 128-string endpoint.
7. Complete source corpus inventory before freeze. The pinned `extras/showcases.txt` exists in both releases and contains a substantial operator/context proof set. My earlier inference that this path might be absent from a tree search was incorrect; the exact snapshot resolves it. `checks.clj` is largely width validation and `script/check` invokes FontBakery, so neither alone constitutes an omitted exhaustive GSUB witness suite. Source feature examples and applicable current Diffenator corpora still belong in the baseline.

## Baseline and commercial interpretation

Diffenator3's pinned source already has changed-glyph/position-aware word selection and a conservative uncertain-glyph path. Diffenator2's wordlist builder already performs n-gram selection and substring removal. Shaperglot already tests feature behavior with language-specific strings, including on/off shaping comparisons. Consequently, visual diffing, CI wiring, generic corpus reduction and behavior checks are existing capabilities. The possible measured contribution is additional bounded execution coverage after those authored and generated alternatives receive fair resources.

[ArrowType's practitioner issue](https://github.com/googlefonts/diffenator2/issues/72) is specific evidence of proof-authoring and feature-execution uncertainty. [Marc Foley's own account](https://www.pdfdiffer.com/author.html) establishes contracted font-update testing work, while the [Google Fonts contract posting](https://typedrawers.com/discussion/2054/google-fonts-freelance-font-engineering-remote-contract-summer-2017) is historical paid-category evidence. These support a buyer hypothesis; neither establishes a current narrow price, a conversion rate or demand for this exact product. A one-family experiment cannot establish general foundry coverage or market defensibility.

Four versions are one family. Changed paired output is descriptive: it can be intentional. Semantic glyph identity must survive GID renumbering; ambiguous mappings must remain ambiguous. Coverage does not establish causal attribution to a changed lookup or prove a production rendering defect.

## Independent post-freeze checking plan

- Hash-check protocol, source, dependencies, font bytes and corpus provenance before any independent replay. Read the extraction and tracing paths first.
- Audit every synthetic failure, unsupported rejection and timeout, rather than only retained witnesses. Confirm no controls or target exclusions were tuned after observing results.
- Replay a bounded independent selection of synthetic controls and retained real strings after source authorization. Compare ordinary shaping against trace outputs and independently count net-effect root coverage.
- Check the actual native feature plan, active root list and denominator on both primary fonts. Test a GID-renumbering control for the secondary paired-output interpretation.
- Inspect the strongest combined baseline and same-input candidate construction, resource charging, set-cover tie rules and all three repetitions. Recompute the frozen absolute and relative improvement conditions from raw coverage sets.
- If Stage 0 proves the primary advance impossible within its budget, stop and report that reason. Otherwise, judge against unchanged rubric-v2 after results, retaining unresolved buyer and single-family generalization limitations. There is no preselected pass verdict.

## Primary technical references

- [Microsoft GSUB specification](https://learn.microsoft.com/en-us/typography/opentype/spec/gsub): contextual matching, listed nested action order and chained-context formats.
- [uharfbuzz API](https://uharfbuzz.readthedocs.io/reference.html): message callback behavior, buffer state access and script/language configuration.
- [Shaperglot](https://github.com/googlefonts/shaperglot) and its [contribution guide](https://github.com/googlefonts/shaperglot/blob/main/CONTRIBUTING.md): existing language-profile behavior tests.
- [fontFeatures](https://github.com/simoncozens/fontFeatures): existing abstract font-feature manipulation/unparsing machinery.
- Exact Diffenator3, Diffenator2, fontFeatures and Fira Code source URLs and SHA256 values are in `work/round5-c/source-inspection/manifest.json`; this reviewer inspected those local pinned snapshots. They are not copied into this review packet.
