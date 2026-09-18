"""Extract only train/validation annotations. Never decode or extract test masks."""

import io
import json
import pathlib
import zipfile

from common import features
from skimage import io as skio
from skimage import measure

p = pathlib.Path(__file__).parent
meta = p / "data/metadata/metadata"
splits = {
    s: [
        pathlib.Path(x.strip()).stem
        for x in (meta / (s + ".txt")).read_text().splitlines()
        if x.strip()
    ]
    for s in ["training", "validation", "test"]
}
assert not (
    set(splits["training"]) & set(splits["validation"])
    or set(splits["test"]) & set(splits["training"])
    or set(splits["test"]) & set(splits["validation"])
)
(p / "splits.json").write_text(json.dumps(splits, indent=2))
result = {}
with zipfile.ZipFile(p / "data/masks.zip") as z:
    entries = {
        pathlib.Path(x).stem: x for x in z.namelist() if x.endswith(".png") and "__MACOSX" not in x
    }
    for split in ["training", "validation"]:
        result[split] = {}
        for name in splits[split]:
            arr = skio.imread(io.BytesIO(z.read(entries[name])), plugin="imageio")
            labels = measure.label(arr[..., 0] if arr.ndim == 3 else arr, background=0)
            result[split][name] = features(labels).tolist()
(p / "calibration_truth.json").write_text(json.dumps(result, indent=2))
print({k: len(v) for k, v in splits.items()})
