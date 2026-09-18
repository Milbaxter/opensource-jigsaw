# Stage 0 independent readiness review

Recorded 2026-09-18T10:53:28.059873+00:00; reviewed `work/round5-c/stage0-preregistration.md`, SHA256 `b3cdeee4cb2660c0cdcba69ad32b05e8cd90b7e60222b4a99830d2665f1361b6`. No shaping or evaluation has been executed by this reviewer.

No validity blocker found for freezing this narrow negative screen. It measures a native baseline only; it cannot establish a working symbolic bridge or a pursuit pass. Its stopping bound uses an actual retained corpus of at most128 strings collected and selected within120seconds per font, and therefore avoids treating an unlimited corpus union as an eligible competitor. A sufficiently covered subset already proves the proposed absolute10-target improvement impossible. Censoring without that bound is inconclusive.

Implementation checks remain: preserve traced/untraced identity; copy live glyph IDs without querying positions mid-GSUB; return True in every callback; maintain nested lookup scopes and count only outer net effects; resolve active latn/default calt targets, not all same-tag FeatureRecords. Log every unsupported/ambiguous event and stop on oracle failure. Synthetic expected outcomes must be independent assertions, not derived from the trace implementation being tested.

Do not reuse uncharged coverage from the100 real-font oracle checks in the budgeted baseline. Fresh timed replay or fully charging those observations resolves this. The Stage0 native target list can include an unsupported but unreachable root that a later symbolic scope would exclude: this makes a total-target ceiling conservative, but the target sets must be explicitly distinguished and never adjusted after results to create an improvement.

The final source freeze still needs independent inspection before any verification claim. This review approves the prospective test design only; it does not pre-approve an implementation or result. The earlier full-method review remains applicable if this screen leaves headroom.

Final prospective clarification checked 2026-09-18T10:54:26.133247+00:00: protocol SHA256 `b20e4772bcaa139d705db0b2798f6dae85eb49bf04bcb3a78cd607dfc8686a32` explicitly requires fresh timed replay after oracle checks and distinguishes the conservative full-native denominator. No new design blocker found. Frozen native targets in `stage0-targets.json` are103 and101 respectively.
