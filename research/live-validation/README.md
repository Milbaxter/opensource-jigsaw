# Live pipeline validation · 18 September 2026

This directory contains an actual end-to-end run of the reusable CLI, using GPT-6 Astra with high reasoning through Codex CLI 0.154.0. It is separate from the larger [initial research sweep](../initial/research.md).

**57 repository candidates · 32 discovery field labels · one three-project hypothesis · zero accepted.**

Astra generated 32 queries. Discovery fetched at most two results per query for this integration check, then deduplicated them. Astra scouted the resulting metadata, proposed a combination, collected 23 evidence entries, produced a separate skeptical critique, and issued a final judgment. These counts do not imply exhaustive inspection of 57 projects or 32 independent industries.

The hypothesis combined Pinocchio, OR-Tools, and PyPSA to investigate motion-aware electrical connection sizing at container terminals. Astra rejected it at **44.5/100**, with confidence 0.94 in that rejection. The enforced gates also rejected it because of low dimension scores, missing verification, and 13 unresolved critical assumptions. A high confidence in rejection is not a probability of commercial success.

Read [the generated report](report.md) or inspect [the complete structured decision](results.json), including research, critique, judgment, and gate failures. The result contains a proposed future experiment, not a tested implementation or recommendation to invest.

The live check caught an unsupported URI-format annotation in the output schema. The runner was corrected to remove that wire annotation while retaining local HTTP(S) validation, and a regression test was added. The successful run used that correction. Cached rerun and standalone report regeneration were then verified without new model calls.

Commands used, with a fresh output directory:

```sh
jigsaw discover --out runs/validation --per-query 2 --max-repos 64 \
  --max-model-calls 1 --timeout 300
jigsaw analyze --out runs/validation --candidates 1 --max-model-calls 8 --timeout 600
jigsaw analyze --out runs/validation --candidates 1 --max-model-calls 1 --timeout 600
jigsaw report --out runs/validation
```

The final two commands reused validated cached outputs. New live runs can produce different repositories and hypotheses. Raw API caches, model caches, local diagnostics, and authentication material are not published.
