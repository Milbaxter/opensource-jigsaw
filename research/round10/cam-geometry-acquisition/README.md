# FreeCAD demo geometry acquisition

**Input acquisition only; no CAM route or performance run.** Three preselected final source solids yield all 18 horizontal planar faces. An independent OCP read checked shapes, placements, topology, edge traversal, analytic chord bounds, and sampled curve errors. See [review](independent-review/REVIEW.md).

The final extractor retains native coordinates and signed ring order. Ring zero is not necessarily the outer ring; bottom faces reverse orientation. Use the independent outer-wire map for a future explicitly registered adapter. Chord approximation is two-sided, not conservative free space. These are polygonal kernel inputs derived from real CAD, not complete FreeCAD CAM jobs or manufacturing validation.

The installed OCP 8 binding renamed TopoDS.Face_s/Wire_s to Face/Wire; the initial failed source is preserved. The next geometry-only version explicitly rejected ellipse edges. The final version adds the analytic major-radius second-derivative bound; the earlier partial inventory remains visible. No planner result informed this change. Original Python source bytes are stored as .py.txt; restore .py and adapt the documented scratch paths for reproduction.

## Rights and attribution

Source models: FreeCAD contributors, at pinned commit 691a041981b7972d3170ceadb96163019712d2b0, with exact URLs and hashes in [source pins](source-pins.json). Embedded author fields are blank; upstream repository attribution and file identities are retained. Drilling_1.FCStd is [CC BY4.0](https://creativecommons.org/licenses/by/4.0/); motor_mount_inch.fcstd and strange_part_with_holes.fcstd are [CC BY3.0](https://creativecommons.org/licenses/by/3.0/). Derived face coordinates retain their respective attribution licenses. Changes: selected final solids, extracted horizontal faces, approximated curved edges with at most .01mm chord deviation, and recorded topology/area metadata. No original binary fixture is redistributed here.

New extraction/audit scripts are MIT. OCP binding Apache2.0 does not replace the native OCCT LGPL2.1-with-exception terms; see [dependency provenance](ocp-provenance.json). Dependencies are local acquisition tools and binaries are not distributed. This packet is not an exhaustive native dependency-license audit.
