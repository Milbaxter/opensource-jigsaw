# Prospective amendment 002: canonical renderer ordering

Status: ready for parent review/freeze; **attempt002 has not executed**. Failed attempt001 at freeze1a842b49a92b0723f810bec70d9c05daf7cb78a7 remains failed and archived. No allocation search or held-out evaluation occurred in it or the separate diagnosis.

## Reason and changed renderer contract

The strict sourceglTF-to-unchangedGLB raw-RGBA gate failed on FlightHelmet with per-view differing-channel counts[10,8,0,0,0,21]. Repeated unchangedGLB renders were exact. Separate diagnostic matrix copying did not affect the failure; consistent mesh-name draw ordering made all six source/GLB views exactly equal. Runtime material IDs differed in relative order, and the pinned Three opaque sort uses material.id unless renderOrder distinguishes objects. Saved sparse pixels include a119/255 channel difference; these were not discarded as rounding noise. Independent rawJSON/BIN review confirms logical accessor bytes, encoded/decoded images, material semantics and node transforms; bound metadata recomputation is separately disclosed.

Change only the renderer ordering contract: in the central sceneFor function, traverse the loaded glTF scene by ordered child-index paths, including primitive children. Assign each encountered mesh a distinct increasing renderOrder. Record each mesh's child-index path, name and rank. Require every source/candidate/comparator load to have exactly the originalGLB correspondence record. Reject empty mesh sets, multiple material/render groups or mismatched identities instead of using arbitrary ties. The same policy applies to original references, source-roundtrip controls, cached texture substitutions, reloaded final GLBs, actual SpatialPack outputs, and held-out loads.

This defines a canonical renderer; it does **not** assert equivalence to old default-viewer pixels. Hierarchy order is fixed independently of quality outcomes and already preserved by the semantic invariants. The diagnostic used lexicographic names, while the amendment uses generic hierarchy/primitive identity; therefore the exact controls must run again. No old control is retroactively passed.

## What remains frozen

Keep the same four assets,1/2/5MB ceilings, ten options/image, encoding settings, roles/distortion values, six selection and24held-out views/lights, byte accounting, primary metric, all algorithms/baselines,256-call budgets, per-method15-minute caps, exact raw-RGBA controls and success criteria. No search hyperparameter, quality threshold, favorable subset or held-out split changes.

Attempt002 logs go to execution-attempt-002, authored controls to generated/controls-attempt-002. Original attempt001 execution/control/artifact files remain immutable. All authored encode/transcode controls and all four source/GLB roundtrip checks run afresh. Every output is checked through the canonical real renderer; source-image payload, geometry, material, sampler and byte guards remain active.

## Exact reuse and time accounting

Reuse only the hash-verified279 completed option files,4unchanged originalGLBs,4model metadata files, original prepared metadata,39original source files and pinned installed-tool/lock metadata. reuse-attempt-001.json lists330 files with exact sizes/SHA-256. Any mismatch aborts before controls/search. Roles, distortion values, dimensions and domains come from the original pinned prepared record, not recomputation against observed results.

Original prepared.json reports574.492 seconds. Add this charge to effective attempt002 elapsed time and start the whole-run timer with10800−574.492 seconds remaining. Actual retry wall time, original preprocessing charge and effective total are separately reported. Repeated authored controls, reuse verification, fresh reference controls and all new searches count anew. Final elapsed guards use the same effective time. Each method shares the original preprocessing cost; cached data do not imply free preprocessing or a speed claim.

Attempt001 actually consumed581.824 seconds including its controls/failure. The separate diagnostic's exact wall time was not instrumented (it had a180-second hard cap); report that limitation rather than invent an exact total research cost. Failed-attempt and diagnostic costs remain separate disclosed research expenditure, while574.492 seconds is explicitly charged to the new bounded comparison.

## Publication and replay

Preserve the first published root source unchanged. Publish this complete new source snapshot and amendment under attempt-002/source with explicit manifest mappings. To run it, restore its normal ROOT/runtime, inputs, generated, tools and venv layout in an isolated directory, using pinned original assets, packages and retained data. No restricted SpatialPack implementation is redistributed.

A replayer without retained encodings can regenerate them using the frozen first-attempt prepare/encoding scripts in an isolated workspace, then verify all expected option/GLB/model hashes against reuse-attempt-001.json. Restore the historical prepared metadata record separately: regenerated wall time cannot equal its recorded574.492 seconds and must not be substituted. If regenerated artifacts differ, it is a different runtime and cannot be called an exact replay; a new prospective run would be needed. Do not regenerate into the immutable failed-attempt directories.

Do not execute attempt002 until the parent publishes its new protocol/source freeze. Invocation is node runtime/run.mjs <new-freeze-commit> from the restored source root.
