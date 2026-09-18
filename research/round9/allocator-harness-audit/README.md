# Prospective allocator harness audit

**22/22 authored synthetic cases passed independent exhaustive enumeration. This is not a real-asset experiment or a pursuit result.**

The parent checked the initial OR-Tools CP-SAT allocator’s byte constraint, one-choice-per-image decisions, paired corrections, worst-view objective, exclusions, and infeasibility reporting. Tiny option spaces were fully enumerated independently. Additional cases distinguish a useful paired choice from individually worse choices and minimax from mean-error selection. Every feasible solver result matched the exhaustive objective and bound; infeasible cases returned no allocation.

The tested original source SHA256 is `a99d224964c5434dc2cf7e475249f618ebd157d88d46e59b78ef677049fc89d8`. OR-Tools was9.15.6755. The source may subsequently be refactored for persistent process operation or input validation; those changes require a separately identified check. All22 input cases and raw results are retained. No real image, model, encoder, browser renderer, or commercial comparator ran in this audit. Negative predicted errors are deliberately tested as surrogate values, not interpreted as physical image errors.

Source is stored as `.py.txt` to preserve bytes. Restore the original filename when replaying. `check_allocator.py` uses the historical workspace layout documented by its ROOT/PYTHON/SCRIPT definitions; adapt those paths to the preserved `audited-solve-original.py.txt` and an environment with the pinned OR-Tools version. Changing paths does not change the oracle or cases. Package licensing/pins and final experiment protocol will live with the executable experiment once frozen.

Original audit code and this original allocator snapshot are covered by the repository MIT license. No restricted competitor source is included.
