# E-invoice differential test generation: discovery HOLD

Source inspection only, 18 September 2026. No invoice processing, package execution, legal advice, score, or customer contact.

The proposed transfer was property-based or constraint-guided test generation into invoice-validator acceptance testing: generated UBL/CII documents, the official rule artifact evaluated through Saxon, and differential comparison against an implementation. The possible purchased artifact would be a version-pinned migration regression packet for an integration vendor.

The obvious mechanism is already implemented. [schematron-diff](https://github.com/stboris/schematron-diff) describes comparing PHP validation outcomes with official Schematron evaluated under Saxon, including version-to-version verdict changes. [VerifyHash’s correctness notes](https://github.com/verifyhash/verifyhash/blob/main/einvoice/CORRECTNESS.md) describe differential testing over public corpora and targeted single-rule mutations, with known rounding and syntax differences. These are source descriptions, not results independently reproduced by Jigsaw. Neither complete legal conformance nor universal correctness follows from a finite differential corpus.

A possible residual question is interaction-focused constraint generation that catches relevant defects missed by these suites. This quick screen found no lawful, current, reproducible defect or buyer-specific migration gap requiring that additional machinery. Adding a solver to an existing mutation/differential workflow does not by itself justify a pursuit. The concept stays HOLD before implementation; it is not declared impossible or fully researched.
