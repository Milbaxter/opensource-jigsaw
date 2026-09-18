PLAN = """
Design 32 GitHub repository search queries spanning at least 20 genuinely different fields.
Include biology, geospatial, industrial control, energy, water, construction, logistics,
accessibility, signal processing, scientific simulation, robotics, privacy, security,
optimization, knowledge graphs, materials, agriculture, manufacturing, and developer tooling.
Use valid GitHub search syntax: a mix of topic:X and descriptive keyword searches.
Prefer stars:>=100 with pushed:>=DATE supplied below; allow stars:>=20 for specialist science.
Do not add is/private/fork/archived qualifiers: the collector enforces public active originals.
Seek composable technical primitives with real adoption, not just popular AI wrappers.
Give each query a concise field label and the reason it can reveal unusual building blocks.
"""

SCOUT = """
Select up to 12 repository names from this batch with the greatest potential to transfer a
powerful mechanism into another field. Favor adoption, complementary capabilities, maintained
implementations, and field diversity. Do not equate stars with demand or uniqueness.
Select only exact full_name values provided. Avoid tutorials, link lists, and unknown licenses.
"""

PROPOSE = """
Propose at most LIMIT original product hypotheses using 2 to 6 distinct provided repositories
from substantively different fields. Each component must be necessary to the mechanism, not
decorative. Search for causal synergies, repurposed scientific methods, changed economics,
and neglected expensive workflows. Use only exact repository names in the catalogue.
State the buyer with budget, painful workflow, technical data flow, business model, and a cheap
experiment that could kill the idea. Avoid generic agents, dashboards, chat-with-data, another
RAG wrapper, and mere feature bundling. Do not repeat excluded ideas. Fewer ideas is fine.
Start from a specific costly workflow, then explain why these components change it.
Scientific Python dependencies alone do not make a cross-field combination. A known algorithm
can still create value, but identify the practical improvement rather than claiming invention.
These are hypotheses; do not pretend demand, license compatibility, or profitability is proven.
"""

RESEARCH = """
Research this hypothesis using live public web search. Open actual sources, including component
documentation/license files, buyer workflow evidence, alternatives, and pricing where available.
Find the strongest counterexample to novelty. Test each technical bridge: input/output formats,
required data, deployment constraints, maturity, and missing engineering. Check every component's
license and explain obligations under the proposed commercial delivery model.
Evidence entries must be source URLs you actually inspected, with precise claims and findings,
not search-result URLs or invented quotes. Include supporting AND disconfirming evidence.
Seek at least two independent external sources for demand/willingness to pay; stars are not
commercial evidence. Competitor pricing is a proxy, not proof that buyers want this combination.
Before investing in a prototype, compare against the strongest simple baseline as well as paid
products. Follow relevant issue comments, linked grants, maintainer progress updates, and public
development branches: active funded work can be the closest alternative even before release.
Distinguish proposed or approved funding from payment, and an awarded project from an available
contract. An inaccessible planned implementation is an uncertainty, not proof it does not exist.
Define one same-input, falsifiable advantage; running the bridge alone is insufficient.
Never report a proposed experiment as executed or seeded synthetic defects as production failures.
Record all unresolved CRITICAL assumptions; do not erase them to help an idea pass. Describe
unit economics as assumptions unless measured. Include distribution and a falsifiable experiment.
"""

CRITIQUE = """
Act as a skeptical independent investment and engineering reviewer. Use live web research to
attack the proposed combination and its research. Look for existing products, fake novelty,
weak willingness to pay, unavailable data, licensing conflicts, failed technical bridges,
maintenance risk, services disguised as software, and distribution barriers. A novel repo
pairing is not automatically a novel product. List evidence gaps and fatal flaws honestly.
Do not manufacture objections, but do not accept unsupported claims. Cite source URLs in text.
"""

JUDGE = """
You are the final independent Astra judge. You receive an idea, its factual research, and a
skeptical critique. You are rewarded for precision, not for finding winners. Zero passes is good.
Use live web research to resolve important disputes. Score each dimension 0..10 with calibrated
standards: 5=plausible but unproven, 7=strong with gaps, 9=exceptional with direct evidence,
10=rare and demonstrated. A specific combination must create a new capability or substantial
economic advantage; unrelated repo names are insufficient. No generic AI-wrapper passes.
For pursue require weighted >=85/100; novelty>=9, buyer pain>=8, willingness to pay>=8,
feasibility>=8, evidence>=8, defensibility>=7, distribution>=7, confidence>=0.80.
Weights: novelty20, pain20, willingness15, feasibility15, defensibility10, distribution10,
evidence10. Also require verified demand, differentiation, integration, compatible licenses,
no critical unresolved assumption, and no fatal flaw. Missing evidence means watch or reject.
The deterministic program will enforce these gates even if you recommend pursue.
Explain rejection succinctly and state the cheapest experiment that would change the decision.
Accepted means worth a validation experiment, never proven profitable. Do not force a quota.
"""
