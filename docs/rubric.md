# Research rubric

## What counts as a promising combination?

The combination should transfer a mechanism between fields, make something previously impractical feasible, or change the cost of an expensive workflow. Every additional repository must justify its integration and maintenance burden. An impressive stack is not a business.

Useful questions:

- What can the combination do that its strongest individual component cannot?
- Which input or output connects each component? Who already has that data?
- What does the buyer do today, what fails, and who controls the budget?
- Why cannot an incumbent add this cheaply? Has it already done so?
- What are delivery, support, compute, sales, and integration costs?
- What survives if the model or commodity infrastructure becomes free?
- What is the cheapest experiment that could disprove the commercial thesis?

## Score calibration

| Score | Meaning |
| --- | --- |
| 0–2 | Contradicted, inapplicable, or a major blocker |
| 3–4 | Weak and mostly speculative |
| 5–6 | Plausible, with material evidence missing |
| 7–8 | Strong case, documented implementation or market support |
| 9 | Exceptional, specific advantage supported by direct evidence |
| 10 | Rare, demonstrated result with unusually strong support |

Do not upgrade a 5 to an 8 because the combination sounds exciting. Research uncertainty is a reason to seek evidence, not a reason to inflate confidence.

## Evidence hierarchy

Prefer actual product documentation, official specifications, primary technical papers, verified implementations, buyer-originated accounts, and concrete prices. A vendor's marketing page supports what that vendor claims, not an independent performance result. Competitor pricing shows a budget category exists; it does not prove willingness to buy this new product.

A repo's description, stars, or list of users can motivate research. It cannot prove profitability or novelty. Field tags establish discovery diversity but cannot prove conceptual distance.

## Rejection examples

- Strong buyer pain but existing tools already implement the claimed mechanism.
- Novel technical idea requiring customer data that buyers cannot provide.
- Plausible revenue without a realistic path to reach the budget owner.
- High average score hiding poor distribution or defensibility.
- Public source with missing or noncommercial terms.
- A model asserting compatibility without tracing the actual technical interfaces.
- A plan that earns money only if unvalidated savings estimates are true.

An unresolved critical issue blocks a pass even when the judge is optimistic. `watch` preserves an interesting hypothesis and its next experiment; it is not a softer kind of acceptance.

## Model limitations

Researcher, critic, and judge all use Astra, with separate contexts. This reduces conversational anchoring but does not eliminate shared model blind spots. Citations are model-researched and not independently fact-checked by the program. The conservative SPDX screen intentionally creates false negatives when GitHub cannot detect a valid license. Human review should inspect the exact source, delivery model, customer evidence, and proposed experiment before spending substantial resources.
