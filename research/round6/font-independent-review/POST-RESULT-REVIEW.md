# Independent verdict: HOLD the font-witness experiment

Recorded 2026-09-18T11:07:19.544998+00:00. The frozen Stage0 negative screen is reproducible and decisive for its stated endpoint. The existing Fira Code proof corpus already leaves fewer than10 uncovered top-level calt targets on both primary fonts. Consequently, the prospective minimum10-target improvement is impossible, even before adding the stronger recursive-enumeration and current-tool corpora. Do not build the proposed symbolic executor for this experiment.

| Input | Existing native coverage | Retained strings | Uncovered targets | Independent elapsed | Peak RSS |
|---|---:|---:|---:|---:|---:|
| Fira Code5.2 Regular |98/103|56|5|6.111 seconds|87,293,952 bytes|
| Fira Code6.2 Regular |95/101|55|6|6.060 seconds|89,784,320 bytes|

Both runs satisfy the120-second and128-string limits. No censoring or error occurred. The full16,716-string corpus was collected on each font. The required20% relative gain is also unattainable under these total-target ceilings, but the absolute10-target condition alone is sufficient for this decision. Uncovered targets remain unknown; no reachability proof is inferred.

## Independent verification

I copied the exact frozen collector and pinned inputs into `replay-1/`, then executed the complete collector in a fresh process using the pinned Python/dependency environment. All207 controls passed: seven synthetic cases and100 traced/untraced native checks on each real font. The source hash remained `99ea43ce981453a06bc9aede19ad6d1c6f6928f780159b9f1d6b2426b874a2ab`; the protocol hash remained `b20e4772bcaa139d705db0b2798f6dae85eb49bf04bcb3a78cd607dfc8686a32`. Font, GSUB table and target hashes were asserted by the frozen collector. The copied input manifest records all file checksums.

Both decompressed observation streams were byte-identical to the author's streams:33,432 observations in total. Greedy-selected witnesses and covered target sets also matched exactly.

`independent-audit.py` is separate original review code and does not import the measured collector. It independently resolves the active target list, freshly shapes all111 retained witness strings, compares traced and untraced native glyphs/positions, and derives each outer lookup's net glyph effect from the native boundaries. Every witness coverage set and union matched the frozen output. It also independently reconstructed effects from all seven recorded synthetic event streams. Failed nested substitution, restored temporary change, a blocking ignore rule and insufficient lookahead correctly produced zero net outer coverage.

The original unexecuted parser's balanced-nested-event assumption was corrected before source freeze, after inspection of the pinned HarfBuzz implementation. That history is preserved in `STAGE0-STATIC-REVIEW.md`. No result-dependent repair or metric adjustment was needed in the frozen execution.

## Scope of the decision

This is a negative feasibility screen for one font family, printable ASCII length1..8, default Latin and configured calt-only shaping. It is not evidence that font QA is unnecessary, that all GSUB branches are covered, or that symbolic font testing cannot be useful elsewhere. It establishes no working Z3 integration, customer time savings, bug-finding rate or profitability. The paid font-engineering category and proof-authoring pain remain credible, but this proposed measured wedge did not survive its own strong authored-corpus baseline. No rubric-v2 pass or fabricated numerical score is assigned.

The retained native denominator includes any unsupported/unreachable root, making the ceiling conservative relative to a later narrower symbolic scope. Removing such roots could only reduce remaining headroom; it cannot rescue the registered10-target benefit.

## Replay and publication

The executed command from workspace root was `work/round5-c/.venv/bin/python work/font-independent-review/replay-1/stage0.py`, with stdout/stderr saved as `replay-1/console.log`. The independent audit command was `work/round5-c/.venv/bin/python work/font-independent-review/independent-audit.py`. An output directory already present intentionally prevents silently overwriting a run; create a new isolated replay copy for subsequent runs.

`PUBLICATION-MANIFEST.json` lists review/code/result metadata safe to publish. Downloaded fonts and source proof copies, upstream HarfBuzz source copies, the duplicate frozen collector, and duplicate full observation payloads are excluded. Their local checksums and provenance remain available. The parent's canonical experiment packet supplies source/fetch instructions and original raw observations; this review packet adds independent verification without duplicating third-party inputs.
