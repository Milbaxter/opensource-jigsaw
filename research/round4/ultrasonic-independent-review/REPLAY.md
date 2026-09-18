# Independent replay packaging

The exact executed reviewer is preserved as `replay-selected.py.txt`, SHA2563f43a6f95726002e258f671a82384427c506eb7869559c897b9edb3d00b2caea. It imports the unchanged frozen implementation and independently computes15direct sums plus4image comparisons; it is not a fully separate imager or full velocity replay.

For replay create sibling scratch directories `round4-c/` and `ultrasonic-independent-review/`. Reconstruct original prototype/driver filenames and copy their freeze, verified input and original execution arrays into `round4-c/` as described in the experiment's PACKAGING.md. Copy this checker to `ultrasonic-independent-review/replay-selected.py` and run with the pinned experiment environment. It writes a new independent-replay.json beside the checker.

The verifier source in this directory is GPL-3.0-or-later for use with the GPL experiment; the license text is at ../../../experiments/ultrasonic-fmc/LICENSE-GPL-3.0.txt. No imported third-party binaries are bundled. Original source hashes remain unchanged.
