# Independent static FlightHelmet roundtrip diagnosis

Recorded 2026-09-18T12:31:07.530039+00:00. Read-only source/artifact and CPU image-decoding inspection. No browser rendering, optimization, search, held-out evaluation, gate relaxation, or frozen-source modification.

The registered raw-RGBA equality failure remains a failure. This analysis does not establish that the mismatch is harmless or supply a repaired technical result.

## Direct comparison

The independent script parses the external glTF JSON/buffer and GLB chunks directly, resolves primitive accessor references, and reconstructs logical element bytes using each accessor offset, bufferView offset/stride, component width, type and count. It does not import glTF Transform or use its canonical roundtrip as a reference.

- All **30** primitive index/vertex accessor byte sequences match exactly, including component types/counts/normalization. Index order, vertex values, normals, tangents and UVs did not change.
- All **15** original PNG payloads match their GLB image payloads exactly. Independent Sharp0.35.4 CPU decoding also produces identical RGBA pixels for every image. This does not independently prove browser ImageBitmap behavior.
- All **six** material definitions match after resolving texture indices to image payload hashes and explicit sampler defaults. Texture roles and image sharing are preserved. The unchanged sampler defaults made explicit by the writer are REPEAT wrapping. No material factor/extension difference was found.
- Nodes, scene roots and scene selection match directly. All six nodes contain mesh references and names, with no matrices or TRS transforms. **Matrix-to-TRS decomposition cannot explain this particular asset's failure.**
- Extensions used/required match. Primitive TRIANGLES default is made explicit but unchanged. Primitive attribute order is retained.

Source glTF SHA256: `c9c16c8b85749f62f38ec6069700e5388c6894d8e566f51a35cc270255402cd3`. Serialized GLB SHA256: `7d275b4bef091ca7cef1bb8ed274ac7b6e8a7f2b5a6c164f3e78ef3bbaa21af7`.

## Actual representation differences

The writer reorders accessor/texture identifiers, repacks vertex data into interleaved buffer views, embeds images, changes descriptive generator/image names, makes mode/wrap defaults explicit, and recomputes all six POSITION accessor min/max arrays from actual float32 values. Original bounds were rounded decimal metadata. Maximum component difference in those bounds is **2.4144744870113755e-08 model units**. Logical geometry bytes remain identical.

Pinned Three.js GLTFLoader's `computeBounds` reads accessor min/max into geometry bounds; WebGLRenderer subsequently uses the bounding sphere center for sorting depth. Therefore the changed bounds have a real runtime pathway and should not be dismissed as inert JSON. This source inspection does **not** demonstrate a changed draw order or any pixel effect. The frozen render harness uses the same GLB-derived camera center/radius for both scenes, so these bounds do not automatically imply different cameras. GPU attribute layout and asynchronous resource/material ordering remain separate unproven possibilities.

No static semantic corruption was identified. Root cause of the tiny rendered mismatch remains undetermined pending the researcher's separate runtime diagnosis. Do not change tolerances or declare equality on the basis of these static results.

## Replay and scope

From the shared workspace root:

```sh
python3 work/texture-independent-review/roundtrip-diagnosis/compare_raw.py
node work/texture-independent-review/roundtrip-diagnosis/decode_pngs.mjs
```

Raw reports preserve every accessor/image mapping, hashes, buffer layouts and changed bounds. A first CPU decoder invocation failed before decoding because it assumed an obsolete Sharp internal file path; `ATTEMPTS.md` records the correction to package-export resolution. No experiment output was overwritten. Raw customer/source PNGs, binaries, third-party source and generated GLB payloads are not duplicated in this review packet.

## Separate draw-order diagnostic, independently inspected

The researcher subsequently executed a separately authorized diagnostic, not the frozen allocation experiment. This reviewer verified all three diagnostic source hashes and decoded the six saved baseline PNG pairs independently. Their raw channel mismatch counts exactly reproduce [10,8,0,0,0,21]; maximum channel deltas are [18,119,0,0,0,1]. Sparse differences are not uniformly one-bit rounding noise.

The recorded matrix-matching intervention leaves the same mismatch, as does matrix restoration. The subsequent intervention assigns the same lexicographic unique-mesh-name renderOrder ranks to both unchanged scenes; recorded full RGBA differences become [0,0,0,0,0,0]. The code compares newly rendered target/source buffers directly under each intervention, rather than comparing against stale reference frames. This reviewer inspected those records/code and did not generate another render.

The pinned Three.js opaque painterSortStable comparator prioritizes groupOrder, then renderOrder, then material.id. The observed material creation ranks differ between loads (MetalParts precedes Hose in the GLB but follows it in source). This provides a concrete source mechanism consistent with the controlled intervention. The causal evidence supports deterministic object ordering as a harness repair; it does not show that default runtime draw order or every other renderer is invariant.

A prospective amendment can define an identical canonical order for all source, base, candidate and comparator scene loads, with nonempty unique names and exact per-asset name-set matching (or an equivalently stable hierarchy/primitive key). Fail closed on ambiguity/missing objects. Apply before any reference, search, actual-file or held-out render. Preserve strict full-RGBA equality and all comparison criteria. This ordering is part of the evaluator, not automatically encoded in the GLB or guaranteed in customer viewers. The original registered result remains stopped; a new frozen run is required. Actual amended code still needs its narrow source check.

## Prospective amendment002 source review

The stable amendment was reviewed read-only before attempt002 execution. `AMENDMENT-HASH-CHECK.json` independently verifies all330 retained files and all13 amended source files. Every source/originalGLB/model/option path referenced by the historical prepared metadata is included in the reuse pins; metadata preserves roles, distortion values and domains. Original preprocessing time agrees exactly at574.492 seconds.

The reviewed renderer assigns increasing mesh renderOrder using deterministic ordered scene child-index traversal, including primitive children. It rejects empty mesh sets and multiple material/render groups. The source and every evaluateFile load must match the baseline path/name/rank sequence. This covers source controls, serialized allocation winners, actual SpatialPack candidates and held-out file loads. Cached texture allocation uses the same ranked baseline object. This is a reasonable prospective canonical-renderer contract; it is not the lexicographic order used by the separate diagnostic, so fresh unchanged exact controls remain necessary. No result is inferred in advance.

The new runner validates retained hashes before use, writes separate attempt002 records, and adds574.492 seconds to both reported effective elapsed and the hard three-hour timer. Fresh controls, hash verification, reference generation and selections count anew. Per-method selection limits remain unchanged; shared preprocessing is reported separately and applies equally to methods, not silently made free by reuse. The historical failed581.824-second run and separately disclosed diagnostic expenditure are not erased.

No unresolved blocker was identified in this narrow static amendment review. This supports subjecting the repaired harness to its unchanged controls after parent authorization and publication freeze, not a technical success, score, customer-viewer equivalence claim, or retroactive pass of attempt001. This reviewer ran no browser, encoding, allocation or held-out evaluation.

Reviewed hashes:
- Amendment:79f778af866d90686f56f725abd4375a0e82a8d30adb829ed6d7bc7975a6e54d
- Protocol:a37a1d110f7c720cf22d60ee9c907cac1cf0c18ad72ec96661a90b0854be0af8
- Source freeze:9b9e251a4b169d545bd1de5a44d57058d991ca752d7b421ea738f00161bdc470
- Reuse manifest:e6cde88aa7e1ce0c041d685fb199878c03e93a600e72c4c2e5504d0d292889c2
