# CAM follow-on: hold implementation pending a useful complement

**Status: research HOLD, no Stage-A execution.** The round-7 result remains unchanged. A first 16,313-byte adapter draft was written, but never compiled, executed, frozen or validated. It is not a functioning prototype or a technical result. Its SHA256 is `9158f55d614198a55ed7f81b6a89eaa64c5e553ef0ecfe20d982283ea07c7e6b`.

The parent discovered a material exact-workflow comparator before further implementation: [FreeCAD grant 80](https://github.com/FreeCAD/FPA-grant-proposals/issues/80) funds the Clipper migration. Its Adaptive subproject expressly includes an optional improved linking search. The proposal requests $3,750 overall and $1,000 for the Adaptive subproject, which also includes migration; neither figure is a standalone linker price or proof of payment. In the author's [September 14 update](https://github.com/FreeCAD/FPA-grant-proposals/issues/80#issuecomment-5667717697), three subprojects are complete, the Adaptive migration is in draft, and separate migration and linking-search PRs are planned. This is active funded adjacent work, beyond a generic paper or competitor feature.

## Read-only search for the actual planned baseline

On September 18, 2026, GitHub's public API returned all 51 branches of `davidgilkaufman/FreeCAD`, five open author PRs in upstream FreeCAD, and recent public repository events. Six relevant branch versions of `Adaptive.cpp` were inspected by exact commit. No inspection executed CAD, routing or a binary.

| Branch | Commit prefix | Commit date | Observed source |
|---|---|---|---|
| clipper_clean_paths | 996238642840 | September 17 | Adaptive source byte-identical to our frozen main source |
| clipper2 | 7618bec88aa6 | May 12 | Existing Resolve function; no Triangulate/Detour implementation |
| adaptive_test | 2a184e86c982 | May 9 | Same implementation-family observation |
| adaptive_test_speed | 230ceb11682e | April 17 | Same implementation-family observation |
| roadmap_clipper | 5328e74e3d0a | March 13 | Roadmap-era source, no new triangle router |
| main | c93c7ed3604d | August 20, 2025 | Stale fork default branch; not treated as current upstream |

The open PRs concern pockets, arc offsets, App property updates, cycle-time estimates and build configuration. This bounded search did not locate a publicly inspectable new linking implementation. That absence does **not** show the maintainer lacks a draft, nor prove our design is different. The retained API snapshots and `author-inspection/summary.json` document the search limits and hashes.

## Decision

The paid grant strengthens evidence that this computation matters to the project, while weakening the proposed standalone feature's practical differentiation and distribution. There is no measured advantage over the funded replacement, and merely adding Detour is insufficient. Further heavy implementation should wait for an accessible planned baseline or a specific complementary requirement, such as a maintainer-requested verification/benchmarking gap with a credible route to paid work. No request from a maintainer has been obtained; no outreach was sent.

Known algorithms remain eligible. This hold is about the missing practical wedge against active exact-scope work, not a demand for world-first research. The endpoint design, source inspection and unexecuted draft remain available if a concrete complement emerges. The separately acquired lawful geometry is reusable research input, not evidence that this candidate passes.
