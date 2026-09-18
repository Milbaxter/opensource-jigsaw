# Cartonization regression witnesses

**Technical bridge confirmed; pursuit decision WATCH, 76.5/100.** Five generated cases show shrinking an item can make an unchanged packing heuristic choose a larger carton despite a verified cheaper feasible placement. The independent judge found insufficient durable commercial value and a score below the frozen pursuit bar.

- [Observed results, exact three-item example, limitations and reproduction](RESULTS.md)
- [Preregistered protocol](PREREGISTRATION.md)
- [Independent Astra business judgment](../../research/round2/carton-independent-review/REVIEW.md)
- [Corrected tariff provenance](execution-provenance.json) and [parent source check](PARENT-TARIFF-CHECK.md)

A separate geometry checker plus fresh direct engine calls independently confirmed all five fixtures. Original checker bytes are in `independent-verify-original.py.txt`; `independent-verify.py` is the formatted copy with paths adapted for this directory. In a scratch copy of this folder, run `python independent-verify.py` using the pinned environment. It writes `independent-verification-rerun.json`. The parent verified the adapted copy too.

All item data is synthetic; the packing engine is real and unmodified. Modeled surcharge components are not actual invoice savings. The source PDF was independently read through the web reader, but a direct download returned HTML; no locally verified PDF checksum is claimed. No customers were contacted.
