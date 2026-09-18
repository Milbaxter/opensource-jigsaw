"""Replay the byte-preserved, pre-execution frozen research implementation."""

import runpy
from pathlib import Path

runpy.run_path(str(Path(__file__).with_name("prototype-original.py.txt")), run_name="__main__")
