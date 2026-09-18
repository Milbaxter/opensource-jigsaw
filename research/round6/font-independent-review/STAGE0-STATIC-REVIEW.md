# Stage0 static implementation review

Recorded 2026-09-18T11:00:40.534287+00:00. Reviewed source SHA256 `d4ef53d80f6076e89b20799f4cc9b290f15e33b94df1e5fe103998de4636d518` without importing or executing it. Protocol reviewed previously: `b20e4772bcaa139d705db0b2798f6dae85eb49bf04bcb3a78cd607dfc8686a32`. This first source requires correction before execution.

## Blocking finding: recursive trace events are not balanced

`stage0.py` lines114–126 assume every nested `recursing` message has a matching `recursed` message. Exact [HarfBuzz12.3.0 contextual application source](https://github.com/harfbuzz/harfbuzz/blob/12.3.0/src/hb-ot-layout-gsubgpos.hh#L1804) emits the former before calling recursion, then continues immediately if recursion returns false, omitting the latter. Thus a valid matched outer context with an unsuccessful nested substitution leaves the proposed parser stack nonempty and falsely raises an oracle error. This is a source-supported issue found before first execution, not an observed benchmark failure.

Requested correction: derive coverage only from the reliable outer boundaries; represent nested call attempts without assuming a complete balanced event grammar. Add a synthetic matched outer context calling a nonmatching inner lookup; expected unchanged glyphs and zero outer-effect coverage. Preserve the original unexecuted source hash and review finding. No metric or target change is needed.

## Confirmed and remaining checks

The exact [top-level map application source](https://github.com/harfbuzz/harfbuzz/blob/12.3.0/src/hb-ot-layout.cc#L2036) emits start/end lookup boundaries even when glyph-digest screening skips its application. Therefore equality of observed roots with the frozen active target list is a legitimate fail-closed check for this pinned plan. The trace grammar's script/table and lookup feature text agrees with this source. Unexpected structural-prefix messages should still fail closed rather than be silently ignored if their full grammar does not match.

The callback explicitly returns True and catches errors for post-shaping reporting. It reads glyph positions only after shaping completes. Coverage compares glyph IDs/order/length and ignores cluster-only differences. These choices match the proposed metric. Synthetic expectations are stated as glyph names and booleans rather than computed from the coverage parser.

Fresh font parsing and source-corpus replay are charged in the timed baseline. The100 real-font oracle-check outputs are not reused. Selection uses the frozen coverage/length/lexical tie rule and size cap. Corpus preparation is charged fully per font. Unfinished runs remain censored. The per-font result file is written before final serialization-time adjustment, so the returned summary record must be explicitly authoritative for budget eligibility; a standalone pre-adjustment file should not be used for the ceiling decision. C was informed.

No font execution or performance measurement by this reviewer. Static review does not establish correctness; native synthetic controls remain a hard gate. Await corrected frozen source before independent replay.

## Corrected source readiness

Reviewed 2026-09-18T11:02:15.592916+00:00: source SHA256 `99ea43ce981453a06bc9aede19ad6d1c6f6928f780159b9f1d6b2426b874a2ab`. No remaining static blocker found for the native-only Stage0 control run. Failed nested attempts may now remain as diagnostic frames until a successful ancestor return or the enclosing outer exit. Only paired outer boundaries determine coverage. A seventh independently expected failed-nested control was added. Structural event grammar is checked explicitly, and a trace failure carries exact text/font hash. Real oracle attempts are persisted before shaping.

The final summary resource fields are identified as authoritative; each font conservatively reserves one extra second for terminal summary logging and excess invalidates budget eligibility. This resolves the prior recording ambiguity. No source execution by this reviewer; synthetic controls and traced/untraced native equality still must pass before any ceiling result is interpretable. Static readiness is not a correctness verdict.
