"""Image-only feature extraction. This module never opens an annotation file."""

import argparse
import concurrent.futures
import itertools
import json
import pathlib

import numpy as np
from common import features
from scipy import ndimage as ndi
from skimage import feature, filters, io, morphology, segmentation

CONFIGS = list(itertools.product([0.75, 1.0, 1.25], [5, 8, 12, 16], [20, 50]))


def process(args):
    path, out = args
    image = io.imread(path).astype(float)
    lo, hi = np.percentile(image, [1, 99])
    image = np.clip((image - lo) / max(hi - lo, 1), 0, 1)
    smooth = filters.gaussian(image, sigma=1.0)
    otsu = filters.threshold_otsu(smooth)
    results = []
    packed = []
    for factor, distance, minarea in CONFIGS:
        fg = smooth > otsu * factor
        fg = morphology.remove_small_objects(fg, min_size=20)
        fg = morphology.remove_small_holes(fg, area_threshold=20)
        dist = ndi.distance_transform_edt(fg)
        coords = feature.peak_local_max(
            dist, min_distance=distance, exclude_border=False, labels=fg.astype(np.uint8)
        )
        markers = np.zeros(image.shape, dtype=np.int32)
        if len(coords):
            markers[tuple(coords.T)] = np.arange(1, len(coords) + 1)
        labels = segmentation.watershed(-dist, markers, mask=fg)
        sizes = np.bincount(labels.ravel())
        remove = sizes < minarea
        remove[0] = False
        labels[remove[labels]] = 0
        results.append(features(labels))
        packed.append(np.packbits(labels > 0))
    np.savez_compressed(
        out / (path.stem + ".npz"),
        features=np.array(results),
        foreground=np.array(packed),
        shape=np.array(image.shape),
    )
    return path.stem


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--images", type=pathlib.Path, required=True)
    p.add_argument("--out", type=pathlib.Path, required=True)
    a = p.parse_args()
    a.out.mkdir(parents=True, exist_ok=True)
    paths = sorted(
        x
        for x in a.images.rglob("*")
        if x.suffix.lower() in [".tif", ".tiff"]
        and "__MACOSX" not in x.parts
        and not x.name.startswith("._")
    )
    (a.out / "configs.json").write_text(json.dumps(CONFIGS))
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as pool:
        for n, name in enumerate(pool.map(process, [(path, a.out) for path in paths]), 1):
            if n % 10 == 0:
                print(f"{n}/{len(paths)} {name}", flush=True)
