# Native headroom screen reproduction

This is an offline research harness. It neither produces a machine-ready program nor authorizes machining.

1. Retain the published native-source/manifest.json layout and fetch its pinned public sources with `python3 fetch-sources.py`.
2. Run `python3 prepare-native.py`. It verifies original Adaptive source hashes, generates the bundled version header, makes the access-only header adaptation, wraps the one trace call site, and asserts the complete ResolveLinkPath body is unchanged. Fixed kernel-inputs.json is sufficient; the fetcher also retrieves the small pinned CC BY4.0 fixture. Independently regenerate its footprint manifest with `python3 extract-inputs.py` (or `--fixture PATH`).
3. Run `python3 run-screen.py --build-only` with a C++20 compiler. This compiles both programs but executes neither. The original host used Apple clang16.0.0 on macOS arm64 with -O2 and USINGZ.
4. Execution requires a source-freeze.json containing SHA256s of all original/adapted sources, prepared input header, protocol, driver/helpers and both local binaries. Original binary hashes are host/build-specific provenance. A reproduction on another toolchain must record its own explicitly labeled freeze/build provenance; do not claim byte identity to the original binaries without checking it.
5. After the prospective protocol and source freeze are committed, run `python3 run-screen.py --out results` in a fresh output directory. It verifies every frozen hash before the first oracle control or native kernel call.

The source-only capture alters a call site around the original ResolveLinkPath function. The plain program uses the original executable bodies and an access-only header for replay. Begin/end snapshots preserve native Clipper Z tags separately from XY geometry. Logging cost is acquisition overhead, not the measured native baseline. All controls, process logs, failed/censored runs and source/binary provenance must accompany any result.

Whole-kernel original output equality and every isolated native replay must pass. The early mathematical negative ceiling can end the study without the geometry graph phase; this is a registered negative-only screen. CONTINUE_TO_SEPARATE_PROTOCOL would authorize neither a commercial pass nor an automatic next experiment.
