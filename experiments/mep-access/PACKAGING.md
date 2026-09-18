# Publication and reproduction

The original failed implementation is byte-preserved as `prototype-original.py.txt`; `prototype.py` is a launcher. `ORIGINAL-MANIFEST.json` records source-to-destination mappings and hashes before packaging. The protocol is unchanged. Helper/driver originals are also preserved with `.py.txt` suffixes; runnable Python copies may be formatted. `driver-console.log` and `execution/driver.json` redact the local workspace prefix, so their published hashes differ from that original manifest.

All IFC fixtures are originally authored synthetic data. No third-party binary or source dataset is bundled. The program intentionally retains the failed experimental behavior for forensic reproduction; see `RESULTS.md`, including its confirmed input-boundary failures. Run in a copy to avoid overwriting original outcomes.
