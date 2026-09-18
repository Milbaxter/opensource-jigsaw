"""First and only stage opening held-out masks. Does not alter rankings/model."""

import datetime
import hashlib
import io
import json
import pathlib
import zipfile

import numpy as np
from common import decisions, features, order
from skimage import io as skio
from skimage import measure

p = pathlib.Path(__file__).parent
rankbytes = (p / "rankings.json").read_bytes()
r = json.loads(rankbytes)
m = json.loads((p / "model.json").read_text())
names = r["names"]
true = []
with zipfile.ZipFile(p / "data/masks.zip") as z:
    entries = {
        pathlib.Path(x).stem: x for x in z.namelist() if x.endswith(".png") and "__MACOSX" not in x
    }
    for name in names:
        arr = skio.imread(io.BytesIO(z.read(entries[name])), plugin="imageio")
        labels = measure.label(arr[..., 0] if arr.ndim == 3 else arr, background=0)
        true.append(features(labels))
true = np.array(true)
truthdecision = decisions(true, np.array(m["thresholds"]))
wrong = truthdecision != r["predicted_decisions"]
errors = wrong.sum(axis=1)
e0 = int(errors.sum())
oracle = order(errors, names)
results = {
    "test_images": len(names),
    "initial_wrong_decisions": e0,
    "initial_by_task": wrong.sum(axis=0).tolist(),
    "rankings_sha256": hashlib.sha256(rankbytes).hexdigest(),
    "created_utc": datetime.datetime.now(datetime.UTC).isoformat(),
    "budgets": {},
    "mae_features": np.mean(abs(np.array(r["corrected_features"]) - true), axis=0).tolist(),
}
for frac in [0.1, 0.2, 0.3]:
    k = int(frac * len(names))
    b = {"images_reviewed": k, "oracle_corrected": int(errors[oracle[:k]].sum())}
    for method, ranking in r["rankings"].items():
        corrected = int(errors[ranking[:k]].sum())
        b[method] = {
            "corrected": corrected,
            "remaining": e0 - corrected,
            "corrected_by_task": wrong[ranking[:k]].sum(axis=0).tolist(),
        }
    for method in ["random", "stratified"]:
        benefits = np.array([errors[np.array(o[:k])].sum() for o in r[method + "_orders"]])
        mean = float(benefits.mean())
        p95 = float(np.quantile(benefits, 0.95))
        b[method] = {
            "mean_corrected": mean,
            "p95_corrected": p95,
            "remaining_at_mean": e0 - mean,
            "remaining_at_p95": e0 - p95,
        }
    results["budgets"][str(frac)] = b
b = results["budgets"]["0.2"]
cand = b["candidate"]
conditions = {"sufficient_errors": e0 >= 10, "oracle_opportunity": b["oracle_corrected"] >= 5}
for method in ["uncertainty", "margin", "random", "stratified"]:
    rem = b[method].get("remaining", b[method].get("remaining_at_p95"))
    conditions["20pct_advantage_vs_" + method] = rem > 0 and cand["remaining"] <= 0.8 * rem
    benefit = b[method].get("corrected", b[method].get("mean_corrected"))
    conditions["three_extra_vs_" + method] = cand["corrected"] >= benefit + 3
results["gate_conditions"] = conditions
results["gate_pass"] = all(conditions.values())
dense = true[:, 0] >= np.quantile(true[:, 0], 0.75)
low = (np.array(r["uncertainty"]) <= np.median(r["uncertainty"])) & (errors > 0)
for group, indices in [
    ("dense_quartile", np.where(dense)[0]),
    ("low_uncertainty_errors", np.where(low)[0]),
]:
    selected = set(r["rankings"]["candidate"][: b["images_reviewed"]])
    results[group] = {
        "images": len(indices),
        "initial_wrong": int(errors[indices].sum()),
        "candidate_corrected": int(sum(errors[i] for i in indices if i in selected)),
    }
results["per_image"] = [
    {
        "name": name,
        "truth_features": true[i].tolist(),
        "truth_decisions": truthdecision[i].tolist(),
        "wrong_decisions": int(errors[i]),
        "wrong_by_task": wrong[i].tolist(),
    }
    for i, name in enumerate(names)
]
(p / "results.json").write_text(json.dumps(results, indent=2))
print(json.dumps({k: v for k, v in results.items() if k != "per_image"}, indent=2))
