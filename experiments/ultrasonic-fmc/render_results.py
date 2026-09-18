# SPDX-License-Identifier: GPL-3.0-or-later
"""Presentation only, after failed benchmark; does not modify images/results."""

from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt

root = Path(__file__).resolve().parent
e = root / "execution"
data = {
    n: np.load(e / (n + "-images.npz"))
    for n in ["finufft", "arim-linear", "native-linear-2", "native-cubic-2"]
}
x, z = data["finufft"]["x"], data["finufft"]["z"]
k = int(np.argmin(abs(x)))
fig, ax = plt.subplots(1, 2, figsize=(11, 4.7), layout="constrained")
a = abs(data["finufft"]["images"][4])
im = ax[0].imshow(
    20 * np.log10(np.maximum(a / a.max(), 1e-4)),
    origin="lower",
    extent=[x[0] * 1e3, x[-1] * 1e3, z[0] * 1e3, z[-1] * 1e3],
    aspect="auto",
    vmin=-50,
    vmax=0,
    cmap="magma",
)
ax[0].set(
    xlim=(-5, 5),
    ylim=(17, 24),
    xlabel="Lateral position (mm)",
    ylabel="Depth (mm)",
    title="FINUFFT: one measured FMC specimen",
)
ax[0].axhline(20, color="cyan", linestyle="--", lw=1, label="Published nominal depth")
ax[0].legend(loc="upper right", fontsize=8)
fig.colorbar(im, ax=ax[0], label="Normalized amplitude (dB)")
for name, label in [
    ("finufft", "FINUFFT (20.864 mm)"),
    ("arim-linear", "Arim linear (20.736 mm)"),
    ("native-linear-2", "Native linear, padding 2"),
    ("native-cubic-2", "Native cubic, padding 2"),
]:
    p = abs(data[name]["images"][4][:, k])
    ax[1].plot(z * 1e3, p / p.max(), label=label, lw=1.6)
ax[1].axvspan(19.5, 20.5, color="green", alpha=0.10, label="Frozen location bound")
ax[1].axvline(20, color="black", linestyle="--", lw=1)
ax[1].set(
    xlim=(18, 23),
    ylim=(0, 1.08),
    xlabel="Depth on central axis (mm)",
    ylabel="Each method normalized to its peak",
    title="Absolute location gate failed",
)
ax[1].legend(fontsize=8)
ax[1].grid(alpha=0.2)
fig.suptitle("Numerical checks passed; physical precheck stopped all timing", fontsize=13)
fig.savefig(root / "physical-precheck.png", dpi=160)
fig.savefig(root / "physical-precheck.svg")
