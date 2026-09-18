# Reproduction and publication boundary

This packet is prospective. No real asset encoding, rendering, selection or held-out evaluation has run at its initial freeze. Source compilation checks and the parent’s tiny exhaustive CP-SAT controls are harness checks, not asset results.

Use a macOS arm64 machine with Node26.7.0, Python3.14.6, Google Chrome153.0.8010.50. Install exact npm dependencies with `npm ci --prefix runtime --ignore-scripts`; install the Python lock into `venv`. Download original assets from `downloaded-inputs.json` and verify every SHA-256. Download/extract official KTX4.4.2 Darwin arm64 package using `ktx-download.json`; put toktx/ktx/ktx2check in tools/bin and their dylib in tools/lib. These files are not redistributed here. The browser path is explicitly pinned in runtime/run.mjs; another platform is a new runtime, not an identical replay.

Only after the protocol and all source files are committed/frozen, execute from this directory:

```
node runtime/run.mjs <published-freeze-commit>
```

The argument records provenance, not authorization by itself. The runner first uses the common encoder on tiny authored controls, then real assets. It preserves commands, flags, errors, sizes, source-image mappings, conservative byte-bound calculations, method charges, actual file hashes, the complete selection seal, and held-out outputs. `execution/summary.json` is written only on completed evaluation; `execution/failure.json` records an aborted attempt. Do not silently resume or modify an executed run.

Material identity is tracked with harmless `source-image-N` names introduced before optimization. Decoded accessor values, node transforms, cameras, material parameters and sampler semantics are checked independently of binary offsets. Candidate outputs additionally require exact selected image payload hashes. Final exported GLBs must reproduce all six cached search render RGBA hashes before held-out views are accessed.

The restricted-license `@spatialpack/core` is installed solely as a separately invoked local research comparator through its public API. Its actual implementation, tarballs, dependency tree and extracted source are **not included in the publication manifest**. No competitor code is incorporated into our allocator or renderer. Only our invocation adapter, exact package/version/integrity pins, license evidence and later observable reports may be published. Its native dedup/prune is retained and must satisfy the stated semantic checks; this is not a comparison against the whole product or a distribution of a competing SpatialPack service.

All four selected sample assets are CC0 with per-model attribution documents preserved. Documentation may have separate CC BY4.0 terms. Excluded DamagedHelmet is not experiment data. Our new experiment scripts may be published under the repository’s MIT license. OR-Tools, Sharp, Playwright and KTX have Apache2.0 licensing; glTF Transform, Three and ktx-parse have MIT licensing, with their bundled third-party notices retained in installations and exact artifacts pinned. No dependency license is claimed to grant rights to arbitrary customer models.
