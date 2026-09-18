"""Independent finite-graph oracle and analytic IFC/swept-motion replay. No prototype import."""

import gzip
import hashlib
import heapq
import json
import math
import pathlib
import sys
import time

import ifcopenshell
import ifcopenshell.geom
import numpy as np
from shapely.affinity import rotate, translate
from shapely.geometry import MultiPoint

ROOT = (
    pathlib.Path(sys.argv[1]).resolve()
    if len(sys.argv) > 1
    else pathlib.Path(__file__).resolve().parent.parent / "round3-c"
)
OUT = pathlib.Path(__file__).resolve().parent
MARGIN = 0.0501


def angle(a):
    return math.atan2(math.sin(a), math.cos(a))


def axis(a):
    m = np.eye(4)
    m[:3, 3] = a.Location.Coordinates
    z = np.array(a.Axis.DirectionRatios if a.Axis else [0.0, 0.0, 1.0])
    z = z / np.linalg.norm(z)
    x = np.array(a.RefDirection.DirectionRatios if a.RefDirection else [1.0, 0.0, 0.0])
    x = x - z * np.dot(x, z)
    x = x / np.linalg.norm(x)
    m[:3, :3] = np.column_stack([x, np.cross(z, x), z])
    return m


def placement(p):
    return (placement(p.PlacementRelTo) if p.PlacementRelTo else np.eye(4)) @ axis(
        p.RelativePlacement
    )


def geometry(name):
    f = ifcopenshell.open(ROOT / "fixtures" / f"{name}.ifc")
    meta = json.loads((ROOT / "fixtures" / f"{name}.json").read_text())
    units = [u for u in f.by_type("IfcSIUnit") if u.UnitType == "LENGTHUNIT"]
    assert len(units) == 1 and units[0].Name == "METRE"
    scale = {None: 1.0, "MILLI": 0.001}[units[0].Prefix]
    shapes = {}
    err = 0.0
    settings = ifcopenshell.geom.settings()
    settings.set("use-world-coords", True)
    settings.set("convert-back-units", False)
    for e in f.by_type("IfcBuildingElementProxy"):
        reps = e.Representation.Representations
        assert len(reps) == 1 and len(reps[0].Items) == 1
        solid = reps[0].Items[0]
        assert solid.is_a("IfcExtrudedAreaSolid") and solid.SweptArea.is_a("IfcRectangleProfileDef")
        profile = solid.SweptArea
        assert profile.Position is None
        matrix = placement(e.ObjectPlacement) @ axis(solid.Position)
        assert np.allclose(solid.ExtrudedDirection.DirectionRatios, [0, 0, 1])
        verts = np.array(
            [
                (matrix @ np.array([x, y, z, 1]))[:3] * scale
                for x in [-profile.XDim / 2, profile.XDim / 2]
                for y in [-profile.YDim / 2, profile.YDim / 2]
                for z in [0, solid.Depth]
            ]
        )
        poly = MultiPoint(verts[:, :2]).convex_hull
        # Compare independent placement/profile reconstruction with actual mesher output.
        mesh = ifcopenshell.geom.create_shape(settings, e)
        mv = np.asarray(mesh.geometry.verts).reshape(-1, 3)
        err = max(
            err,
            poly.hausdorff_distance(MultiPoint(mv[:, :2]).convex_hull),
            abs(verts[:, 2].min() - mv[:, 2].min()),
            abs(verts[:, 2].max() - mv[:, 2].max()),
        )
        shapes[e.GlobalId] = (poly, float(verts[:, 2].min()), float(verts[:, 2].max()))
    assert err < 0.0001
    known = {meta["ids"]["floor"], meta["ids"]["equipment"]}
    assert set(shapes) - known == set(meta["interventions"])
    ep, bottom, top = shapes[meta["ids"]["equipment"]]
    s = meta["start"]
    body = rotate(translate(ep, -s[0], -s[1]), -s[2], origin=(0, 0), use_radians=True)
    radius = max(math.hypot(*v) for v in body.exterior.coords)
    opts = [k for k, v in meta["interventions"].items() if v["allowed"]]
    costs = [meta["interventions"][k]["cost"] for k in opts]
    assert all(math.isfinite(c) and c > 0 for c in costs)
    return dict(
        meta=meta,
        shapes=shapes,
        body=body,
        radius=radius,
        bottom=bottom,
        top=top,
        opts=opts,
        costs=costs,
        unit_scale=scale,
        max_mesh_error=err,
    )


def value(mask, scene):
    return sum(c for i, c in enumerate(scene["costs"]) if mask >> i & 1)


def path_clear(qs, mask, sc):
    assert 0 <= mask < (1 << len(sc["opts"]))
    floor = sc["shapes"][sc["meta"]["ids"]["floor"]][0]
    obstacles = []
    for gid, entry in sc["meta"]["interventions"].items():
        if gid in sc["opts"] and mask >> sc["opts"].index(gid) & 1:
            continue
        poly, lo, hi = sc["shapes"][gid]
        if lo > sc["top"] + MARGIN or hi < sc["bottom"] - MARGIN:
            continue
        obstacles.append(poly)
    calls = 0
    minimum = math.inf

    def recurse(a, b, depth=0):
        nonlocal calls, minimum
        calls += 1
        da = angle(b[2] - a[2])
        mid = [(a[0] + b[0]) / 2, (a[1] + b[1]) / 2, a[2] + da / 2]
        poly = translate(
            rotate(sc["body"], mid[2], origin=(0, 0), use_radians=True), mid[0], mid[1]
        )
        if not floor.covers(poly):
            return False
        d = min([poly.distance(floor.boundary)] + [poly.distance(o) for o in obstacles])
        minimum = min(minimum, d)
        if d <= MARGIN:
            return False
        # Arc-length bound, distinct from proposer's chord bound, is more conservative.
        displacement = math.dist(a[:2], b[:2]) / 2 + sc["radius"] * abs(da) / 2
        if d > MARGIN + displacement:
            return True
        if depth >= 28 or displacement <= 1e-6:
            return False
        return recurse(a, mid, depth + 1) and recurse(mid, b, depth + 1)

    assert (
        len(qs) >= 2
        and math.dist(qs[0][:2], sc["meta"]["start"][:2]) < 1e-6
        and math.dist(qs[-1][:2], sc["meta"]["goal"][:2]) < 1e-6
    )
    assert (
        abs(angle(qs[0][2] - sc["meta"]["start"][2])) < 1e-6
        and abs(angle(qs[-1][2] - sc["meta"]["goal"][2])) < 1e-6
    )
    okay = all(recurse(a, b) for a, b in zip(qs, qs[1:]))
    return dict(passed=okay, interval_checks=calls, min_sampled_separation=minimum)


def oracle(g, sc):
    adj = [[] for _ in g["nodes"]]
    for i, j, mask, length in g["edges"]:
        a = g["nodes"][i]
        b = g["nodes"][j]
        derived = math.dist(a[:2], b[:2]) + sc["radius"] * abs(angle(b[2] - a[2]))
        assert abs(length - derived) < 1e-6 and 0 <= mask < (1 << len(sc["opts"]))
        adj[i].append((j, mask, derived))
        adj[j].append((i, mask, derived))
    best = None
    for mask in range(1 << len(sc["opts"])):
        c = value(mask, sc)
        if best is not None and c > best[0]:
            continue
        dist = {s: 0 for s in g["starts"]}
        queue = [(0, s) for s in g["starts"]]
        heapq.heapify(queue)
        while queue:
            d, v = heapq.heappop(queue)
            if d != dist[v]:
                continue
            if v in g["goals"]:
                if best is None or (c, d) < best:
                    best = (c, d)
                break
            for w, m, edge_length in adj[v]:
                if m & ~mask:
                    continue
                if d + edge_length < dist.get(w, math.inf):
                    dist[w] = d + edge_length
                    heapq.heappush(queue, (d + edge_length, w))
    return best


start = time.time()
records = []
scenes = {}
files = sorted((ROOT / "execution").glob("*-result.json"))
for f in files:
    x = json.loads(f.read_text())
    name = x["case"]
    seed = x["seed"]
    graph = ROOT / "execution" / f"{name}-{seed}-graph.json.gz"
    if not graph.exists():
        continue
    sc = scenes.setdefault(name, geometry(name)) if name not in scenes else scenes[name]
    g = json.loads(gzip.open(graph, "rt").read())
    j = x["comparison"]["joint"]
    o = oracle(g, sc)
    rec = {
        "result": f.name,
        "sha256": hashlib.sha256(f.read_bytes()).hexdigest(),
        "graph_sha256": hashlib.sha256(graph.read_bytes()).hexdigest(),
        "case": name,
        "seed": seed,
        "unit_scale": sc["unit_scale"],
        "analytic_ifc_mesher_max_error": sc["max_mesh_error"],
        "status": j["status"],
        "independent_oracle": o,
    }
    if j["status"] == "found":
        assert o is not None and abs(o[0] - j["cost"]) < 1e-8 and abs(o[1] - j["length"]) < 1e-6
        assert value(j["mask"], sc) == j["cost"]
        qs = [g["nodes"][i] for i in j["path"]]
        assert qs == j["states"]
        edge_map = {tuple(sorted((i, k))): m for i, k, m, _length in g["edges"]}
        actual = 0
        for a, b in zip(j["path"], j["path"][1:]):
            actual |= edge_map[tuple(sorted((a, b)))]
        assert actual == j["mask"]
        rec["independent_continuous_check"] = path_clear(qs, j["mask"], sc)
        assert rec["independent_continuous_check"]["passed"]
        rec["removal_cost_counted_once"] = True
    elif j["status"] == "no_roadmap_route":
        assert o is None
    rec["manual_paths_checked"] = 0
    rec["greedy_paths_checked"] = 0
    for m in x["comparison"]["manual"]:
        if m["valid"]:
            assert value(m["mask"], sc) == m["cost"]
            assert path_clear(m["states"], m["mask"], sc)["passed"]
            rec["manual_paths_checked"] += 1
    for b in x["comparison"]["greedy"]:
        if b["found"]:
            assert value(b["mask"], sc) == b["cost"]
            assert path_clear([g["nodes"][i] for i in b["path"]], b["mask"], sc)["passed"]
            rec["greedy_paths_checked"] += 1
    rec["oracle_match"] = j["status"] != "censored"
    records.append(rec)
result = {
    "source_sha256": hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
    "no_prototype_import": True,
    "coverage": (
        "All complete result/graph pairs present at invocation; continuous verifier checks "
        "found joint paths and all reported valid manual/greedy paths. Graph oracle "
        "independently recomputes finite subset optimum and length. Analytic extruded-rectangle "
        "IFC placement reconstruction independently checked against mesher. "
        "Not a new roadmap search or physical safety certification."
    ),
    "runtime_seconds": time.time() - start,
    "count": len(records),
    "records": records,
}
(OUT / "verification.json").write_text(json.dumps(result, indent=2) + "\n")
print(
    "Independently verified",
    len(records),
    "result/graph pairs in",
    round(time.time() - start, 2),
    "seconds",
)
