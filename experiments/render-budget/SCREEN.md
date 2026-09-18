# Render-checked texture delivery: prospective lead

Source inspection only, 2026-09-18. No asset was rendered, encoded, optimized, or evaluated. This is a candidate for a bounded experiment, not a pursuit verdict.

**Claim to test:** for a fixed real product-style glTF asset and delivery-byte ceiling, choose per-image WebP/ETC1S/UASTC codecs and resolutions using rendered appearance, and improve held-out rendered fidelity over competent automatic presets and greedy allocation at a fixed evaluation budget. The output is an ordinary optimized GLB plus original-versus-output views and a reproducible recipe. No new runtime service, model training, bandwidth revenue, artist-minute savings, or commercial-tool superiority is claimed.

The necessary bridge is actual glTF material evaluation in Three.js, actual ETC1S/UASTC encoding and GPU transcoding, and OR-Tools CP-SAT minimax allocation using actual rendered single-image sensitivities and bounded pair corrections. Normal, roughness, base-color, emissive and transmission effects need not contribute independently to final appearance. A joint search can test whether those interactions matter beyond ordinary render-aware greedy selection. If they do not, the extra search does not earn its place; useful render-aware greedy integration can still be reported separately without claiming the stronger result.

## Evidence and alternatives

- A [practitioner requests 1–2MB models while retaining detail](https://www.reddit.com/r/threejs/comments/1t6npcy/need_help_with_3d_models/). This supports a concrete delivery constraint, not willingness to pay.
- An [independent Babylon.js discussion](https://forum.babylonjs.com/t/about-the-gltf-transform-tool/49116) describes compression/quality problems and manual configuration. Its eventual visual problem was attributed to mesh simplification, so it is evidence of integrated optimization-review burden, **not evidence that this texture-only intervention fixes that case**.
- Closest paid offerings are [SpatialPack](https://www.spatialpack.dev/) ($39/month Pro and advertised catalog rescue), [GLB Studio](https://glb.studio/) ($29/month entry plan), and agency optimization services. These are offered prices, not verified sales. SpatialPack already has render-checked automatic recipes; its actual accessible texture-only recipe frontier is a required comparison. See COMPETITOR-CHECK.md.
- A buyer-origin [Upwork listing](https://www.upwork.com/freelance-jobs/apply/Quick-Task-Compress-Optimize-Heavy-GLB-Models-for-Shopify-Remodeling_~022091785499043108499/) offers $50 for a batch of three approximately70MB GLBs under15MB, with WebP and preserved geometry where possible. This is a posted offer, not confirmed payment or recurring demand; it establishes price pressure as well as relevance.
- [Simplygon](https://simplygon.com/) lists a US$42,000/title/year license and indie discounts, covering a much broader games-content suite. This establishes paid asset optimization, not this product's attainable price or a web-product buyer's budget.
- [RapidCompact](https://www.rapidcompact.com/doc/cli/v06/ScreenSizeOptLimits/index.html) already has MB and screen-size targets. Its behavior has not been measured here. No superiority claim is available against it.
- [Khronos glTF-Compressor](https://www.khronos.org/blog/optimize-3d-assets-with-khronos-new-gltf-compressor-tool) already provides per-texture formats/settings, material-slot defaults, before/after 3D inspection and reusable export recipes. This is a strong accessible manual workflow, not a missing capability. The bounded study measures automatic output quality/bytes, not assumed human time.
- [glTF Transform](https://gltf-transform.dev/cli) already provides channel-aware ETC1S/UASTC recipes. These, a tuned preset sweep, and strong greedy allocations must be included.
- [GeoScaler](https://arxiv.org/abs/2311.16581) is prior art for render/geometry-aware texture downsampling, including per-mesh differentiable optimization. Render-aware texture processing is not a new scientific concept. The proposed intervention selects existing standards-compliant encodings without changing the mesh or UV layout.

The likely buyer is a web 3D production agency that repeatedly exports customer product catalogs and already uses glTF Transform. Reproducible compression settings and a visual acceptance packet are a plausible workflow wedge. Reachability and payment remain experimental questions; no exclusive ownership or defensibility is asserted.

## Lawful real inputs

Pinned source: KhronosGroup/glTF-Sample-Assets at `c6a6bd13ab2b3c685c7903d03561b8a9392f38b8`. Per-model license/metadata and exact JSON source hashes are preserved in this directory.

| Model | Rights / attribution | Materials / images | Original listed glTF directory bytes | Nontexture buffer bytes |
|---|---|---:|---:|---:|
| FlightHelmet | CC0; Gary Hsu conversion, 2018 | 6 / 15 | 48,392,569 | 3,227,148 |
| ToyCar | CC0; Guido Odendahl and Eric Chadwick, 2020 | 3 / 8 | 5,432,398 | 3,664,368 |
| WaterBottle | CC0; Microsoft, 2017 | 1 / 4 | 8,967,656 | 149,412 |
| BoomBox | CC0; Microsoft, 2017 | 1 / 4 | 10,615,115 | 207,816 |

These are source-tree and schema measurements, not optimization results. Around 74MB of original assets is sufficient. Documentation itself is CC BY 4.0; model licenses exclude trademarks. DamagedHelmet is excluded because its earlier contribution carries CC BY-NC 4.0; it is not silently treated as fully permissive.

FlightHelmet includes a published channel-aware KTX version with ETC1S for color and UASTC for noncolor. Its README is explicit baseline evidence. ToyCar includes eight authored cameras and clearcoat/transmission/sheen; the two core models supply simpler cases. Texture-only processing cannot fit the two larger nontexture buffers into 1MB or 2MB. Those are natural negative/infeasible controls, not grounds to quietly add geometry simplification.

Tool and source artifacts are now downloaded and installed locally with pinned lockfiles. No actual asset encoding or rendering has occurred. Only metadata/version/help calls, syntax checks and independently enumerated synthetic allocator checks have run. The proposed experiment explicitly includes WebP; it measures final GLB bytes and numerical rendered fidelity, not GPU memory or human time. The restricted-license SpatialPack core is a separately invoked local comparator only; its implementation is never republished or copied into our proposed mechanism.

## Why a small experiment is justified

The inputs and original output are available, no physical or biological ground truth is required, actual file bytes are objective, and a fixed renderer supplies a reproducible visual error proxy. A handful of diverse assets and withheld views/light directions can decisively reject the mechanism. Human appearance judgments, new catalogs, other devices, and commercial conversion remain outside that result. Passing a proxy alone will not establish a validated business.

The next artifact is a preregistration for review/freeze; no execution begins before that freeze. Do not tighten byte budgets after seeing results or choose favorable model/view subsets afterward.
