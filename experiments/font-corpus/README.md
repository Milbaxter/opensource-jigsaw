# Font-feature corpus: HOLD

The existing proof corpus already leaves too little room for the proposed symbolic generator. [Complete results](STAGE0-RESULTS.md) preserve the frozen protocol, source, all 33,432 timed observations, rights and failure checks.

| Historical font | Existing corpus covers | Retained strings | Remaining targets |
|---|---:|---:|---:|
| Fira Code 5.2 Regular | 98 / 103 | 56 | 5 |
| Fira Code 6.2 Regular | 95 / 101 | 55 | 6 |

All **207 controls passed**, and both runs completed all 16,716 source-derived strings in about 6.1 seconds each, under the fixed 120-second budget and 128-string cap. The required gain was at least ten covered lookups and 20% relative improvement. Even perfect additional coverage cannot meet it. These are native top-level lookup effects, not all rule branches, aesthetic quality or bugs; both inputs belong to one font family.

**No Z3 executor was built and no cross-field integration or pursuit pass is claimed.** Stage 0 used FontTools and HarfBuzz solely to test the baseline ceiling. The [independent static review](../../research/round6/font-independent-review/STAGE0-STATIC-REVIEW.md) corrected a trace-parsing assumption before execution. [Independent replay](../../research/round6/font-independent-review/POST-RESULT-REVIEW.md) reproduced all 33,432 observations; a separate native checker verified all 111 retained witnesses.

To reproduce, copy the metadata and protocol into a scratch directory, restore `stage0.py.txt` and `fetch-stage0-inputs.py.txt` to their original `.py` filenames, install the exact dependencies in `dependency-pins.json`, then run the fetcher followed by `python stage0.py`. The fetcher validates fonts and proof source hashes. The collector refuses to overwrite its output directory. `stage0-execution/summary.json` is the authoritative final resource and decision record.

Original measurement code is MIT. Proof-derived text retains the [Fira Code OFL notice](FiraCode-OFL-1.1.txt); see [rights notes](rights-notes.md). No third-party font or wheel binaries are distributed. [Commercial and workflow sources](../../research/round6/font-commercial-evidence.md) establish a real font-engineering task, but this proposed coverage mechanism did not justify further work.
