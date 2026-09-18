# Font corpus Stage0: HOLD

The existing FiraCode project proofs already cover enough of the narrowly defined native targets to make the proposed minimum improvement impossible. The preregistered Stage0 ended with `HOLD_CEILING`. No SMT executor was built, no cross-field integration was demonstrated, and no technical or business pass is claimed.

| Unmodified font | Native top-level calt targets | Covered by retained existing corpus | Retained strings | Targets still uncovered | Charged elapsed | Peak RSS |
|---|---:|---:|---:|---:|---:|---:|
| FiraCode5.2 Regular |103|98|56|5|6.126s|88,195,072bytes|
| FiraCode6.2 Regular |101|95|55|6|6.113s|90,390,528bytes|

Both fonts completed all16,716 source-derived strings within the120-second budget and128-string review cap. There were no censored baseline runs or execution errors. All207 oracle checks passed: seven synthetic cases and100 real strings per font checked with and without native tracing. The seven synthetic cases include the six required by the protocol plus one added prospectively after static review to check unsuccessful nested lookup calls. The two historical versions are one font family, not independent customer workloads.

## Why the experiment stops

The frozen proposed benefit required at least10 additional covered targets and20% relative coverage improvement on at least one primary font, without losing coverage on the other. Even a hypothetical perfect generator could add at most5 or6 targets here. This is the registered Stage0 stopping rule, based on the actual selected, budget-eligible baseline corpus.

A further arithmetic implication of the unchanged full benefit criterion is that maximum relative gains are only103/98−1≈5.10% and101/95−1≈6.32%, below20%. This was not substituted for the registered Stage0 rule. The full native denominator includes targets that a later ASCII reachability analysis might exclude, so the bound is conservative. No targets were removed after results.

Coverage counts **native net glyph-ID buffer changes at top-level calt lookup boundaries**. It is not rule, branch, subtable, all-context, aesthetic or bug coverage. No across-version lookup-ID matching or causal attribution was performed. A single witness covering an outer lookup can exercise only one of its many contexts. No claim is made that uncovered lookups are unreachable.

| Selected-corpus cap | FiraCode5.2 covered targets | FiraCode6.2 covered targets |
|---:|---:|---:|
|1|3|3|
|4|12|12|
|8|24|24|
|16|44|43|
|32|74|72|
|64|98|95|
|128|98|95|

The primary set-cover endpoint is128, fixed before execution. Smaller caps are descriptive. The full raw corpus is not mistaken for the retained review corpus.

## Exact execution and preservation

- Frozen protocol SHA256:`b20e4772bcaa139d705db0b2798f6dae85eb49bf04bcb3a78cd607dfc8686a32`; prospectively published by the parent in commit`1b44463`, with supporting metadata in`65768b9`.
- Executed original source SHA256:`99ea43ce981453a06bc9aede19ad6d1c6f6928f780159b9f1d6b2426b874a2ab`; independently reviewed and frozen before its first import/shaping. Parent preserved its exact bytes in source checkpoint`11de6bcf3594a5204655755d72543b19a6282278`.
- Python3.14.6, FontTools4.60.0, uharfbuzz0.53.2, native HarfBuzz12.3.0. Z3 is not imported or used by this screen.
- Invocation: `python stage0.py`, exit0. It writes a new `stage0-execution` directory and refuses to overwrite one. `fetch-stage0-inputs.py` retrieves the pinned public fonts and proof sources and validates their bytes; it performs no shaping.
- `stage0-execution/summary.json` is the authoritative finalized resource/decision record. Per-font result files precede the final output-write timing check and identify themselves as preliminary. A conservative extra second was reserved for shared terminal summary output and included in budget eligibility.
- `controls.json` preserves every control result. The two gzipJSONL observation files preserve all33,432 timed string/font observations, source origins, native coverage and final glyph information. All source-derived strings were tested; untested count is0 for both fonts.
- The collector copied native glyph IDs/clusters during GSUB, inspected positions only after shaping, explicitly returned True from every trace callback, and checked traced/untraced final equality. Failed nested calls legitimately lack return messages in the pinned HarfBuzz source; only paired outer boundaries established coverage.

Static review corrected the callback's initial assumption that all nested starts have matching returns **before source freeze and before any font shaping**. The final source then ran once without repairs, retuning, changed corpus, changed targets or relaxed criteria. The code, complete outcomes and the original proposer source-freeze metadata are preserved. No human labor timing, real customer adoption or machine-control claim is made.

## Sources, rights and next decision

The source corpus came from the project's actual [5.2 showcase file](https://github.com/tonsky/FiraCode/blob/5.2/extras/showcases.txt), [6.2 showcase file](https://github.com/tonsky/FiraCode/blob/6.2/extras/showcases.txt), and corresponding specimen HTML files. Exact immutable source URLs/hashes are in`stage0-corpus-sources.json`. Proof-derived observation text is attributed to the Fira Code Project Authors and retains the upstream SIL OFL1.1 notice supplied as`FiraCode-OFL-1.1.txt`; our original measurement source uses MIT. Font/wheel binaries and full upstream source snapshots are not republished.

The screened font-engineering workflow remains real: [ArrowType's request](https://github.com/googlefonts/diffenator2/issues/72) describes release-proof preparation friction, while [existing pattern-based shaping tests](https://simoncozens.github.io/tdd-for-otl/) and [current Diffenator3](https://github.com/googlefonts/diffenator3) are strong practical tools. This result says the proposed extra coarse lookup coverage is not a useful differentiator on the frozen workload. It does not establish that font engineering has no unmet needs. No paid pilot is proposed from this test; move to a different practical mechanism.
