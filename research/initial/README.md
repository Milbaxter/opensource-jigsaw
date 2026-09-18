# Initial Astra research · 18 September 2026

Start with [the report](research.md). This is an actual public-source research snapshot, not synthetic demo data. Astra performed discovery and a subsequent skeptical review; these were separate passes by the same agent.

**1,320 public repository candidates · 30 fields · 19 deeper component checks · seven combinations · zero accepted.** Twelve deeper components were added through targeted research outside the original catalogue, so the union contains 1,332 repositories. The broad catalogue is metadata-level discovery, not an audit of 1,320 codebases.

- [Catalogue](catalogue.json): metadata, license detection, field tags, and search provenance.
- [Search log](search-log.json): original query counts, timestamps, and completeness flags.
- [Component evidence](component-evidence.json): closer inspection of 19 building blocks.
- [External sources](sources.json): primary documentation and vendor claims, with limitations.
- [Candidates and judgments](candidates.json): combinations, evidence, scores, and reasons for rejection.
- [Metrics](metrics.json): exact coverage and inspection counts.

The schema of this manually conducted research differs from the reusable CLI's typed output. It should not be placed directly into a CLI run directory.

To reproduce the metadata collection with an authenticated GitHub CLI:

```sh
python research/initial/collector.py --output runs/reproduced-initial
```

The collector uses [the original field map](fields.json), one page of up to 50 results per field, and an explicit activity cutoff. It now adds `is:public` and filters all returned visibility flags; all 1,384 original rows were separately verified to be public, unarchived, non-forks. Counts and ordering may change. The script reproduces collection only; use `jigsaw run` for the Astra-driven pipeline.

No copied README bodies, license texts, private data, or credentials are included. Source projects retain their own licenses. Scores are model judgments and none of these hypotheses has demonstrated revenue or profitability.
