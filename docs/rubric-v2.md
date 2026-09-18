# Pursuit rubric v2: validation-ready

Frozen: 2026-09-18T08:01:28.576576+00:00

The user authorized calibration after the first eight hypotheses failed. Numeric thresholds below were proposed before round-two research began; this final version incorporates an independent Astra review and was frozen before formal candidate scoring or prototype execution. Two unscored early leads had been received. No previous decision is relabeled. V1 remains available in `rubric.md` and the original CLI gate. V2 applies to separately documented pursuit reviews backed by executed experiments.


**Recommendation:** adopt v2 as a prospectively frozen **validation-ready** decision. Do not call it an improved profitability detector or retroactively reinterpret earlier rejections. V1 asked for evidence resembling an established business while deciding whether to investigate one; v2 can reasonably admit unproven adoption when the technical mechanism, costly workflow, commercial category, and next experiment are supported. The user's desired outcome cannot guarantee that a defensible pass exists.

## Fixed scoring rule

Use the same seven dimensions, each 0–10. Weighted total is `sum(score × weight / 10)`.

| Dimension | Weight | Floor | What a passing score must mean |
|---|---:|---:|---|
| novel_synergy | 20 | 7 | A specific combined mechanism produces a useful capability or measurable benefit absent from a named, credible baseline. Each component materially contributes. No world-first claim required. |
| buyer_pain | 20 | 8 | A named buyer role owns a recurring, costly workflow; direct sources establish the workflow and consequential failure/delay/cost. Macro market size is insufficient. |
| willingness_to_pay | 15 | 7 | Evidence of paid procurement, current pricing, paid labor, or a comparable paid service for this workflow establishes a plausible budget category. This does not establish demand for this product. |
| feasibility | 15 | 8 | The essential cross-component bridge has run successfully at recorded versions, with inspected outputs and an explicit deployment boundary. Unbuilt peripheral product features may remain. |
| defensibility | 10 | 6 | At least one concrete, plausible source of durable value beyond assembling public repositories is identified, including how it could be acquired and tested. A hypothetical data moat without access is insufficient. |
| distribution | 10 | 7 | A reachable buyer segment, actual channel, budget owner, and concrete permitted recruitment route exist. Conversion may be unknown; “sell to enterprises” is insufficient. |
| evidence | 10 | 8 | The critical claims are traceable to primary evidence and executed artifacts; counterevidence and material gaps are included. A pile of loosely relevant links is insufficient. |

Require **total ≥80**, every floor, and **confidence ≥0.75**, plus every gate below. Define confidence as the judge's confidence that the evidence justifies the specified experiment at its stated cost—not the chance of commercial success. Record a short basis for confidence; numerical precision is a judgment convention, not empirical calibration. High social impact does not compensate for a failed commercial or technical gate.

## Noncompensable gates

1. **Problem and paid category:** at least two substantively independent external sources collectively support the costly workflow and paid category. At least one must be buyer-originated, an actual procurement/pricing record, or credible primary research of that workflow. Two pages repeating one press release are one source. Vendor pricing establishes an offered price, not paid adoption; label the distinction. Incumbent demand does not establish demand for this entrant.
2. **Comparative mechanism:** name the strongest practical alternative found, including a simple script, spreadsheet, existing OSS integration, or incumbent. State a falsifiable advantage and inspect relevant features/documentation. Require a reproducible comparison on the same inputs for any claimed measured advantage. If the real incumbent is inaccessible, use an honestly labeled proxy and restrict the claim accordingly. Do not infer superiority from failure to find a competitor.
3. **Executed essential bridge:** evidence must contain exact component versions/commits, input provenance and rights, commands, relevant environment/dependencies, raw observed outputs, and the resulting artifact. Identify which component produced and consumed each intermediate representation. Judge or parent reruns it or independently inspects execution evidence. Code existence, plausible APIs, screenshots, fabricated output, or a standalone component demo cannot satisfy integration. Synthetic data are acceptable only if prominently labeled and structurally representative of the tested interface; they cannot establish real-world accuracy, buyer economics, or data availability.
4. **Failure and baseline checks:** define the demonstration's success/failure criteria before running it. Include at least one meaningful edge/failure case and a credible baseline. Record all attempted test cases and unsuccessful runs relevant to the conclusion; explain exclusions. A favorable hand-selected example proves only that example. Where advantage cannot yet be demonstrated, do not award this pass merely because the bridge runs.
5. **Usable rights and access:** inspect primary licenses for the exact components and any essential model weights/datasets/services. Document a compatible delivery approach and attribution/copyleft obligations. Public availability is not permission. Actual or realistically contractable access to essential inputs must be evidenced; synthetic replacements do not resolve unavailable customer data. Unknown essential rights or access block a pass.
6. **Bounded safe use:** no unresolved safety, licensing, data-access, or technical issue may prevent conducting the proposed experiment. Keep hazardous operational decisions out of the experiment's authority; an offline, qualified-human-reviewed study may be eligible. Do not hide a necessary safety validation as ordinary future product work.
7. **Economic and acquisition experiment:** name the buyer, channel, recruitable sample, responsible owner, elapsed-time cap, cash/compute/engineering budget, baseline, success metrics, and kill metrics. Use plausible fully loaded integration/support costs. Clearly separate observed results, assumptions, and proposed targets. Unknown conversion, retention, pricing acceptance, or repeat use is admissible only if the experiment can test the uncertainty directly. A two-week trial cannot validate annual retention; use an appropriate observed proxy and state the limitation. Suggested outreach is not authorization to contact people.

## Protection against criteria shopping

Freeze the version, weights, gates and score meanings in a timestamped artifact **before receiving candidate evidence for this round**. Keep the v1 ledger intact and publish the policy change's stage-specific rationale. Apply v2 to every candidate in the round, including failed candidates. Do not select score interpretations or experiment scope after seeing a candidate's score merely to cross 80.

Use an independent judge context supplied with the frozen rubric, evidence and strongest critique—not the desired verdict. The judge should distinguish a fatal blocker from a testable commercial uncertainty and explain every floor. Counterevidence has equal standing. Neither researcher nor judge may treat “find at least one pass” as evidence.

If no candidate passes, report none and search further within v2. Any later substantive policy change requires a separately recorded rationale and fresh consistent re-evaluation, not silent threshold movement. A pass should be published as **“validation-ready: proceed with [named experiment] under [budget/time cap]”**, with remaining commercial hypotheses visible. It does not establish profitability, product-market fit, operational safety, or a launch recommendation.

## Mechanical assessment

`jigsaw assess --review path/to/review.json --evidence-root . --out runs/assessment` validates a completed, independent Astra review against v2. The review schema is `PursuitReview` in `src/opensource_jigsaw/pursuit.py`. It records dimension-specific reasons, every hard gate, primary sources, exact-version rights, remaining commercial hypotheses, a capped experiment, and hashes of the protocol, implementation, and results.

The command verifies numeric floors, explicit gate outcomes, source categories, rights coverage, and artifact integrity. It never creates or executes a prototype, contacts customers, or infers commercial success. Artifact hashes detect changed evidence; they do not independently prove execution. The judge must inspect or replay the evidence before attesting to the gates. `jigsaw run` retains the original v1 gate, because discovery alone cannot satisfy v2's executed-experiment requirements.
