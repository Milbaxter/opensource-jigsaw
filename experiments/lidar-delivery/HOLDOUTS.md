# Parent-specified adversarial holdouts — before execution

2026-09-18. Preserve original preregistration, code, first-run output and results. These cases were supplied by parent after reviewing the code, not selected to flatter the implementation.

H1 CLEAN: actual point coordinates lie strictly inside the nominal index tile and do not touch its corners. Expected no error: nominal tile boundaries do not imply observations at every corner.
H2 BAD: contract exact total count is 80; actual LAS count and report count agree at 8. Expected contract contradiction.
H3 BAD: contract required AOI extends outside the nominal tile-index union; all tiles/reports otherwise consistent. Expected nominal delivery coverage contradiction. This is a declared project-AOI check, not a proof of LiDAR observation density.
H4 BAD: the index omits one required actual tile while files/contract/report agree. Expected missing index entry.

Run unchanged original mechanism first, preserving raw first holdout output. Expected challenge to original narrow result. Then correct only general mechanisms justified by data semantics, keeping old results. Required corrections: nominal index contains actual point coordinates, bidirectional inventory consistency, contract exact count compared with actual count, index union covers declared required AOI. Missing density in a nominal tile cannot be inferred from sparse fixture points; the original half_coverage example must no longer be presented as detected incompleteness.

Report H1 false alarms, H2-H4 recall; no new commercial-advantage claim. Success target for corrected code: H1 no false alarm and H2-H4 all detected. This does not replace the original 8/8 preregistered criterion or claim that its semantics were right.
