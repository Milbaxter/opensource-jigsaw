# Attempt002: prospective deterministic draw-order amendment

**Attempt002 stopped before allocation rendering:** the corrected draw order passed, but the serialized byte bound failed. [Results and complete exposure record](outcomes/RESULTS.md). No quality comparison or pass. The [amendment](source/AMENDMENT-002.md) defines the same hierarchy-based rendering order for originals, candidates, and comparators. It retains exact RGBA equality and every optimization comparison criterion. [Attempt001 remains failed](../attempt-001/RESULTS-ATTEMPT-001.md).

The [controlled diagnosis](../diagnostics/roundtrip-001/RESULTS.md) and [independent semantic/source review](../../../research/round9/texture-independent-review/roundtrip-diagnosis/DIAGNOSIS.md) justify this narrow harness change. Source snapshots are separate so the original frozen bytes remain available.

Restore solve.py.txt to solve.py. Follow the source reproduction instructions and explicit reuse manifest in an isolated directory. All 330 retained file hashes are checked before new work, and original preprocessing's 574.492 seconds remain charged to the three-hour cap. No algorithm, data subset, metric threshold or held-out split was changed. This renderer ordering is part of the evaluator and is not a guarantee about customer viewers.
