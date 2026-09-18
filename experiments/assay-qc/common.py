"""Pure feature/decision utilities. No IO and no ground-truth access."""

import numpy as np


def features(labels):
    counts = np.bincount(labels.ravel())[1:]
    counts = counts[counts > 0]
    return np.array([len(counts), np.median(counts) if len(counts) else 0.0], dtype=float)


def decisions(values, thresholds):
    return np.stack(
        [
            values[..., 0] < thresholds[0],
            values[..., 0] > thresholds[1],
            values[..., 1] > thresholds[2],
        ],
        axis=-1,
    )


def order(scores, names, secondary=None, ascending=False):
    if secondary is None:
        secondary = np.zeros(len(names))
    return sorted(
        range(len(names)),
        key=lambda i: ((scores[i] if ascending else -scores[i]), -secondary[i], names[i]),
    )
