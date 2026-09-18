# Font-feature corpus: prospective baseline screen

No results yet and no pursuit pass. The [Stage 0 protocol](stage0-preregistration.md) freezes a cheap negative screen before any shaping evaluation: can an existing Fira Code proof corpus already cover too much of the configured feature program for a proposed symbolic generator to add ten covered lookups?

The full candidate would combine FontTools, Z3 and HarfBuzz. **Stage 0 does not execute Z3 or test that combination.** It measures the native baseline on unmodified Fira Code 5.2 and 6.2, with a 120-second budget per font and at most 128 retained strings. A lookup counts only when its native glyph buffer changes. It does not measure all rule branches, bugs, human effort or commercial value.

The [independent readiness review](../../research/round6/font-independent-review/STAGE0-READINESS.md) found no design blocker. Source inspection must precede first execution. If the screen leaves room, the full experiment still needs its own finalized protocol and strong recursive-context baseline.

Input, target, dependency and source hashes are preserved beside the protocol. [Rights notes](rights-notes.md) describe the source-only delivery. Third-party fonts and wheel binaries are not redistributed. [Commercial and workflow evidence](../../research/round6/font-commercial-evidence.md) establishes a recurring task and paid category, not demand for this candidate.
