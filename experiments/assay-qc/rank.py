"""Mask-free selection. Reads predictions, split names and frozen calibration only."""

import datetime
import hashlib
import json
import pathlib

import numpy as np
from common import decisions, order

p = pathlib.Path(__file__).parent
model = json.loads((p / "model.json").read_text())
names = json.loads((p / "splits.json").read_text())["test"]
best = model["best"]
ensemble = model["ensemble"]
bias = np.array(model["bias"])
residuals = np.array(model["residuals"])
thresholds = np.array(model["thresholds"])
iqr = np.array(model["iqr"])
x = np.log1p(np.array([np.load(p / "predictions" / (name + ".npz"))["features"] for name in names]))
corrected = x[:, best, :] + bias
preddecision = decisions(np.expm1(corrected), thresholds)
spread = np.std(x[:, ensemble, :], axis=1, ddof=1) / iqr
risks = []
pixels = []
for i, name in enumerate(names):
    dev = x[i, ensemble, :] - np.median(x[i, ensemble, :], axis=0)
    draws = corrected[i] + dev[:, None, :] + residuals[None, :, :]
    risks.append(
        float(np.mean(np.sum(decisions(np.expm1(draws), thresholds) != preddecision[i], axis=-1)))
    )
    dat = np.load(p / "predictions" / (name + ".npz"))
    fg = np.unpackbits(dat["foreground"][ensemble], axis=1, count=int(np.prod(dat["shape"])))
    prob = fg.mean(axis=0)
    pixels.append(float(np.mean(2 * prob * (1 - prob))))
variants = {
    "sum_spread": spread.sum(axis=1),
    "max_spread": spread.max(axis=1),
    "pixel_disagreement": np.array(pixels),
}
uncertainty = variants[model["uncertainty_baseline"]]
lt = np.log1p(thresholds)
margin = np.min(
    np.stack(
        [
            abs(corrected[:, 0] - lt[0]) / iqr[0],
            abs(corrected[:, 0] - lt[1]) / iqr[0],
            abs(corrected[:, 1] - lt[2]) / iqr[1],
        ],
        axis=1,
    ),
    axis=1,
)
rankings = {
    "candidate": order(risks, names, spread.sum(axis=1)),
    "uncertainty": order(uncertainty, names),
    "margin": order(margin, names, ascending=True),
}
# Unlabelled prediction quartiles define coverage bins.
bins = np.column_stack(
    [
        np.searchsorted(
            np.quantile(corrected[:, j], [0.25, 0.5, 0.75]), corrected[:, j], side="right"
        )
        for j in [0, 1]
    ]
)
groups = {
    b: [i for i, x in enumerate(map(tuple, bins)) if x == b] for b in sorted(set(map(tuple, bins)))
}
randomorders = []
stratifiedorders = []
for seed in range(1000):
    rng = np.random.default_rng(seed)
    randomorders.append(rng.permutation(len(names)).tolist())
    rng = np.random.default_rng(seed)
    g = [list(rng.permutation(v)) for v in groups.values()]
    out = []
    while any(g):
        for bucket in g:
            if bucket:
                out.append(int(bucket.pop(0)))
    stratifiedorders.append(out)
result = {
    "names": names,
    "corrected_features": np.expm1(corrected).tolist(),
    "predicted_decisions": preddecision.tolist(),
    "candidate_risk": risks,
    "uncertainty": uncertainty.tolist(),
    "margin": margin.tolist(),
    "rankings": rankings,
    "random_orders": randomorders,
    "stratified_orders": stratifiedorders,
    "created_utc": datetime.datetime.now(datetime.UTC).isoformat(),
    "inputs_sha256": {
        f: hashlib.sha256((p / f).read_bytes()).hexdigest()
        for f in ["PROTOCOL.md", "model.json", "splits.json", "rank.py", "common.py"]
    },
}
(p / "rankings.json").write_text(json.dumps(result, indent=2))
print(
    "Froze all test rankings before any test mask read:",
    hashlib.sha256((p / "rankings.json").read_bytes()).hexdigest(),
)
