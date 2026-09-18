# Independent OCP geometry acquisition review

Reviewed 2026-09-18T12:26:44.023928+00:00. No CAM kernel, routing, toolpath, or performance evaluation was executed. The independent script imports OCP geometry readers/adaptors only.

## Finding

The checked acquisition is consistent with these three stored fixture solids. All 18 horizontal planar faces match the inventory, and supported line/circle/ellipse segment endpoints agree with independently loaded BRep curves. No current acquisition error was identified. This is not validation of a machining setup, stock model, accessibility, or planned toolpath.

Checked extractor SHA256: `2ecbc4380404395b5ad85febf7d5cd8249941c1ffedf917f1e84c63c6df07f8b`. Checked inventory SHA256: `9f05d3adc47bf1b49785832e80ffe6a1643781ac87a27859d1d71d8bc30589b2`. Parent files were not modified.

## Objects and placements

All three selected object XML placements are identity and none is nested in an additional Group parent. Stored BRep transformation matrices are identity too: TopLoc_Location.IsIdentity returns false because a location record exists, so the actual matrix was checked rather than assuming that flag means a nonidentity transform. BRep adaptors evaluate located geometry. The selected motor Pocket001 and strange-part Fillet002 are the visible final objects in GuiDocument.xml; Drilling Body points to Pocket011, and independently measured Body/Tip volume and centroid match. Embedded CC-BY rights metadata and fixture hashes are retained in the parent inventory and prior fixture provenance packet. Filename motor_mount_inch does not change BRep model units; no unit conversion was applied.

## Wire topology and orientation

The table uses **zero-based wire ordinals** within each one-based face index from the parent inventory. OCCT OuterWire establishes the outer boundary; ordering is not assumed. The parent signed areas match the geometric role relative to the oriented face normal for every wire.

| Fixture | Face → outer wire ordinal |
|---|---|
| Drilling_1.FCStd | 4 → 0, 5 → 0, 45 → 0, 46 → 0, 47 → 0, 48 → 0, 49 → 0, 50 → 0, 51 → 0, 53 → 0, 54 → 0, 55 → 0, 56 → 0 |
| motor_mount_inch.fcstd | 4 → 5, 5 → 0 |
| strange_part_with_holes.fcstd | 1 → 1, 17 → 3, 19 → 0 |

Bottom-facing faces have CW outer rings and CCW holes in XY; top-facing faces have the opposite. A later planar CAM adapter must use outer-role metadata and normalize orientation, not assume wire zero is outer or that all raw positive rings are stock. Keep upward/downward face labels: retaining every horizontal face is correct acquisition, but does not establish that all faces are accessible floors for the same setup. Rings repeat the first point at the end to close the wire; a future integer polygon adapter should remove the duplicate closing vertex before zero-length-edge checks.

## Chord approximation

For a circular arc with parameter span Δ and n subdivisions, R(1−cos(|Δ|/(2n))) bounds chord sagitta. For an ellipse parameterized by major/minor radii, the norm of its second derivative is at most the major radius; the linear interpolation remainder is at most major_radius×(Δ/n)²/8. Rigid placement does not change that bound and XY projection cannot increase it. The parent step choices therefore bound the supported edge interpolation error by 0.01 mm. This is a positional bound, not a relative face-area tolerance.

The audit checked every retained wire edge, compared the WireExplorer count to an independent TopExp edge traversal, checked all emitted endpoints, and evaluated quarter/midpoint curve samples within every chord. Maximum sampled deviation was 0.00997154319402849 mm. The analytic bound, not finite sampling alone, supports the stated tolerance. No unsupported curve or disconnected/open wire was found in the checked inventory.

Chord approximation is **not automatically conservative free space**. In particular, chords around circular holes shrink the hole and can expand a polygon interpreted as cleared material. OCCT validity of the original solid does not prove the approximated planar polygons preserve every narrow-gap topology. A later benchmark may explicitly use these frozen polygonal kernel inputs; any claim relative to original curved clearance additionally needs an independently specified curve-error/rounding margin and polygon validity checks. No such claim is established here.

## Limits and replay

This checks stored final BReps, not recomputation of the FreeCAD feature tree. The horizontal predicate allows a tiny angular tolerance; exact Z deviations are recorded in the audit. Face areas and original-versus-polygon area differences are retained rather than forced to equality. No route selection, endpoint repair, graph construction, or timing outcome influenced face selection. The separate CAM headroom HOLD is unchanged.

Replay from the shared workspace root:

```sh
work/round10-parent/ocp-venv/bin/python work/round10-geometry-review/audit_geometry.py
```

The script reads the checksum-pinned original fixtures and parent inventory; neither raw fixtures nor third-party implementation payloads are included in this review publication packet.
