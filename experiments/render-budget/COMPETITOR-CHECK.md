# Closest comparator: source inspection before protocol freeze

2026-09-18. No competitor package was installed, imported, executed or modified. Public npm archives were read as tar members only, and their hashes are in `competitor-package-pins.json`. Full archives and extracted implementation files are local research evidence, excluded from the intended publication packet.

[SpatialPack](https://www.spatialpack.dev/) is a direct comparator, not merely a related paid category. Its [pricing](https://www.spatialpack.dev/pricing) advertises $39/month Pro, $15/model catalog rescue after a free allowance (ten-model minimum), and $12/model at 25+. Its page says local CLI/MCP functions are free, unmetered and account-free. These are current supplier offers, not confirmed purchases or customer counts. Six-view rendered quality checks, configurable recipes, reports and automated tuning already exist. Therefore Simplygon's much broader $42,000 game-title license is insufficient as the primary commercial comparison.

[GLBStudio](https://glb.studio/) advertises individual texture/mesh settings, visual quality comparison and revision recipes at $29/month, with a $149/month enterprise tier. Its page does not establish how its automatic choices work or prove customer usage. [Advertflair](https://tools.advertflair.com/gltf-optimizer/) provides a free local browser optimizer and offers agency services. These reinforce both real service packaging and substantial price/feature competition.

Verified npm versions are `@spatialpack/cli@0.1.0` and `@spatialpack/core@0.1.0`. The CLI's MIT label does not apply to the core: the core archive includes FSL-1.1-ALv2, with explicit internal-use/research permissions and a restriction on making the software available in competing products/services. It must remain a separately run comparator; do not vendor or copy it into the proposed product. This research record is not legal advice or a blanket redistribution clearance.

Observed implementation capabilities:

- `recipe-search.js` exports `runRecipeSearch` and `applyRecipe`, has grid/TPE/multi-fidelity strategies, accepts an actual `qualityGate` callback and records candidate bytes and quality. It is not just a web mockup.
- `perceptual-budget.js` selects the smallest already-evaluated candidate that satisfies quality bounds; its comments distinguish this finite-candidate picker from an eventual adaptive loop. Merely adding an optimizer library to choose a previously measured winner would be decorative.
- `per-texture-format.js` compares WebP/AVIF per image and supports a perceptual guard. Normal maps receive distinct treatment. This already goes beyond one global codec switch.
- `cohort-recipes.js` checks improvements against its actual preset baseline and can reject a cohort recipe using a rendered quality callback.
- Whole-asset recipe candidates combine maximum texture dimension, PNG/WebP/KTX2, meshopt and optional decimation. The inspected search does not demonstrate the exact proposed joint assignment of a distinct codec/resolution to every texture under a fixed final-byte ceiling. This is a bounded source observation, not a claim that no other module/version/product does it.

The public API can support a legitimate constrained comparator without rewriting its internals: `searchDecimate:false`, a `recipeOrdering` filter retaining `meshopt:false`, all three presets' complete grids, and the experiment's common renderer through `qualityGate`. Any benchmark must call this texture-only recipe frontier rather than claiming to beat the complete product. The full product can change geometry and use other compression formats; those remain material competitive alternatives for buyers who permit them.

Two necessary pre-freeze corrections follow. First, WebP must be allowed when the claim is delivery bytes/fidelity and no buyer GPU-memory constraint is established. Second, a handwritten beam over graphics packages does not by itself supply the user's requested cross-field OSS transfer. A real constraint-solving component would have to select joint codec/resolution assignments under the byte constraint and prove additional utility against greedy/beam/current-tool frontiers; calling an optimizer only to choose among already-known scores does not qualify.

Status: candidate protocol remains a draft. No favorable outcome, distinct mechanism or commercial advantage has been established. If the remaining constrained mechanism is not useful or manageable, hold this lane without a performance run.
