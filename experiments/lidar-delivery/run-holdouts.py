import json
from pathlib import Path

ROOT = Path(__file__).parent
source = (ROOT / "benchmark.py").read_text()
ns = {"__file__": str(ROOT / "benchmark.py")}
exec(source.split("start = time.perf_counter()")[0], ns)


def make_holdouts(env, dirname):
    env["ROOT"] = ROOT / dirname
    results = []
    for name in [
        "H1_clean_interior",
        "H2_contract_count",
        "H3_contract_aoi",
        "H4_missing_index_entry",
    ]:
        p = env["create"](name)
        if name == "H1_clean_interior":
            for f in p.glob("*.las"):
                d = env["laspy"].read(f)
                xs = env["np"].array(d.x)
                ys = env["np"].array(d.y)
                d.x = xs.mean() + (xs - xs.mean()) * 0.5
                d.y = ys.mean() + (ys - ys.mean()) * 0.5
                d.write(f)
        if name in ["H2_contract_count", "H3_contract_aoi"]:
            lines = [
                "CRS: 32632",
                "TILES: west.las,east.las",
                "POINTS: " + ("80" if name == "H2_contract_count" else "8"),
                "AOI: 500000,6000000,"
                + ("500300" if name == "H3_contract_aoi" else "500200")
                + ",6000100",
            ]
            env["pdf"](p / "contract.pdf", lines)
        if name == "H4_missing_index_entry":
            ip = p / "tile-index.geojson"
            ix = json.loads(ip.read_text())
            ix["features"] = ix["features"][:1]
            ip.write_text(json.dumps(ix))
        results.append(env["run"](p))
    summary = {
        "clean_false_alarms": bool(results[0]["bridge_flags"]),
        "adversarial_detected": sum(bool(x["bridge_flags"]) for x in results[1:]),
        "adversarial_total": 3,
        "results": results,
    }
    (ROOT / dirname / "results.json").write_text(json.dumps(summary, indent=2))
    return summary


first = make_holdouts(ns, "holdouts-v1")
print("UNCHANGED:", json.dumps({k: v for k, v in first.items() if k != "results"}))
