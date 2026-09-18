"""Reproducible public CC0 dataset download; no annotation decoding."""

import concurrent.futures
import hashlib
import json
import pathlib
import urllib.request
import zipfile

p = pathlib.Path(__file__).parent
data = p / "data"
data.mkdir(exist_ok=True)
records = json.loads((p / "data-provenance.json").read_text())
for rec in records:
    target = data / rec["url"].rsplit("/", 1)[1]
    if not (target.exists() and hashlib.sha256(target.read_bytes()).hexdigest() == rec["sha256"]):
        pairs = [
            (s, min(s + 2_000_000, rec["bytes"]) - 1) for s in range(0, rec["bytes"], 2_000_000)
        ]

        def fetch(pair):
            s, e = pair
            for attempt in range(5):
                try:
                    request = urllib.request.Request(
                        rec["url"], headers={"Range": f"bytes={s}-{e}"}
                    )
                    with urllib.request.urlopen(request, timeout=30) as response:
                        b = response.read()
                    if len(b) == rec["bytes"]:
                        b = b[s : e + 1]
                    assert len(b) == e - s + 1
                    return b
                except Exception:
                    if attempt == 4:
                        raise

        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            blocks = list(pool.map(fetch, pairs))
        target.write_bytes(b"".join(blocks))
        assert hashlib.sha256(target.read_bytes()).hexdigest() == rec["sha256"], target
    print("verified", target.name, flush=True)
    if target.name != "masks.zip":
        with zipfile.ZipFile(target) as archive:
            assert archive.testzip() is None
            for member in archive.infolist():
                dest = (data / target.stem / member.filename).resolve()
                assert dest.is_relative_to((data / target.stem).resolve())
                if "__MACOSX" not in pathlib.Path(member.filename).parts:
                    archive.extract(member, data / target.stem)
