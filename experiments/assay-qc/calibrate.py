"""Uses only training/validation annotations and predictions; no test paths opened."""

import json
import pathlib

import numpy as np
from common import decisions, order

p = pathlib.Path(__file__).parent
splits = json.loads((p / "splits.json").read_text())
truth = json.loads((p / "calibration_truth.json").read_text())
configs = json.loads((p / "predictions/configs.json").read_text())


def load(split):
    names = splits[split]
    pred = np.array([np.load(p / "predictions" / (name + ".npz"))["features"] for name in names])
    gt = np.array([truth[split][name] for name in names])
    return names, np.log1p(pred), np.log1p(gt)


names, x, y = load("training")
scores = np.mean(np.sum(abs(x - y[:, None, :]), axis=2), axis=0)
choice = sorted(range(len(configs)), key=lambda j: (scores[j], configs[j]))
best = choice[0]
ensemble = choice[:9]
bias = np.median(y - x[:, best, :], axis=0)
residuals = y - x[:, best, :] - bias
# Center residuals by median, consistent with bias correction.
residuals = residuals - np.median(residuals, axis=0)
rawtruth = np.array([truth["training"][name] for name in names])
thresholds = np.array(
    [
        np.quantile(rawtruth[:, 0], 0.25),
        np.quantile(rawtruth[:, 0], 0.75),
        np.quantile(rawtruth[:, 1], 0.75),
    ]
)
iqr = np.quantile(y, 0.75, axis=0) - np.quantile(y, 0.25, axis=0)
iqr[iqr == 0] = 1
vn, vx, vy = load("validation")
corrected = vx[:, best, :] + bias
vwrong = np.sum(
    decisions(np.expm1(corrected), thresholds)
    != decisions(np.array([truth["validation"][name] for name in vn]), thresholds),
    axis=1,
)
spread = np.std(vx[:, ensemble, :], axis=1, ddof=1) / iqr
pixel = []
for name in vn:
    dat = np.load(p / "predictions" / (name + ".npz"))
    fg = np.unpackbits(dat["foreground"][ensemble], axis=1, count=int(np.prod(dat["shape"])))
    prob = fg.mean(axis=0)
    pixel.append(float(np.mean(2 * prob * (1 - prob))))
variants = {
    "sum_spread": spread.sum(axis=1),
    "max_spread": spread.max(axis=1),
    "pixel_disagreement": np.array(pixel),
}
benefits = {k: int(vwrong[order(s, vn)[: int(0.2 * len(vn))]].sum()) for k, s in variants.items()}
# Explicit stable lexical tie-break among baseline variants.
uncertainty = sorted(variants, key=lambda k: (-benefits[k], k))[0]
model = {
    "best": best,
    "ensemble": ensemble,
    "bias": bias.tolist(),
    "residuals": residuals.tolist(),
    "thresholds": thresholds.tolist(),
    "iqr": iqr.tolist(),
    "uncertainty_baseline": uncertainty,
    "validation_benefits": benefits,
    "validation_error_count": int(vwrong.sum()),
    "configuration_scores": [
        {"config": c, "training_error": float(s)} for c, s in zip(configs, scores)
    ],
    "selected_config": configs[best],
}
(p / "model.json").write_text(json.dumps(model, indent=2))
print(
    json.dumps(
        {
            k: model[k]
            for k in [
                "selected_config",
                "thresholds",
                "uncertainty_baseline",
                "validation_benefits",
                "validation_error_count",
            ]
        },
        indent=2,
    )
)
