"""Load the byte-preserved failed experimental version for forensic replay."""

import runpy
from pathlib import Path

_namespace = runpy.run_path(
    str(Path(__file__).with_name("prototype-original.py.txt")), run_name=__name__
)
globals().update(_namespace)
