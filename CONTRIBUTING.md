# Contributing

Open an issue or pull request with the concrete problem, a minimal change, and the relevant checks. Useful work includes underrepresented search fields, stronger evidence gates, real false-positive cases, and cheaper ways to falsify hypotheses.

Keep changes small. Add tests when changing discovery, caching, failure behavior, or acceptance rules. Do not lower the bar to get a non-empty report. Synthetic fixtures belong in tests, not in research findings.

Do not commit API tokens, account credentials, model error logs, copied datasets, or large raw source documents. Local run directories are ignored. Published research should use short summaries, source links, retrieval dates, and explicit limitations.

Before submitting:

```sh
python -m pip install -e '.[dev]'
ruff check .
ruff format --check .
pytest -q
python -m build
```
