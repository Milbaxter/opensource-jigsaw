# Round 2B: developer testing, privacy, provenance and constraint-solving transfers

Completed September 18, 2026. This branch searched 12 GitHub repository fields with explicit `is:public`, `archived:false`, `fork:false`, `pushed:>=2026-01-01`, and `stars:>=20` filters. It collected **569 distinct repositories**, of which **523 are additional** to `research/initial/catalogue.json`. Searches are metadata discovery, not assertions that every result is relevant or open-source licensed.

- `capture/catalogue.json`: public repository metadata, license detector output, timestamps and per-repo query provenance.
- `capture/search-log.json`: exact queries, counts and completeness flags.
- `new-repositories.json`: 523 additional records versus initial catalogue (case-insensitive names).
- `collector.py`, `fields.json`: reproducible GitHub API collection using an existing `gh` login.
- `candidate-ledger.json` and `.md`: 16 combinations and explicit rejection/open reasons. Fourteen are early screens; two received deeper investigation.
- `dossier-incremental.md`: strongest branch candidate; parent is testing actual dbt/Hypothesis/DuckDB integration. No pass declared here.
- `dossier-sql-witness.md`: second deep investigation; rejected due exact competitor and license/implementation constraints.
- `sources.json`: 23 primary documentation, practitioner, vendor and competitor findings, with clear source types.
- `components.json`: 12 direct component/competitor API inspections, primary license URLs and SHA-256 hashes.
- `dblect-provenance.json`: exact inspected prior-art commit and public repository metadata.

Closest competitor findings changed the initial thesis. dblect explicitly plans stateful multi-step incremental replay, late-row and duplicate campaigns using Hypothesis and dbt-duckdb. Its current runtime layer is not shipped, but this defeats claims that the underlying combination is novel. A working focused implementation or consulting audit could remain useful; that is a narrower commercial hypothesis.

The parent's integration results should be appended as separate evidence. Do not silently upgrade the research scores because a synthetic demo runs. Benchmarks require a meaningful baseline, admissible-input contract, repaired positive controls and reproducible counterexamples. Commercial conversion, retention and support economics remain experiments.

For publication, copy the JSON/Markdown research artifacts and collector. The `dblect/` clone and `*--LICENSE.txt` downloads are inspection intermediates; retain links/hashes instead of publishing those trees wholesale. No commits, pushes, customer contacts or external messages were made by this branch.

Reproduce repository metadata capture into a new directory:

```sh
python3 collector.py --output fresh-capture --fields fields.json --min-stars 20 --pushed-since 2026-01-01 --per-field 60
```
