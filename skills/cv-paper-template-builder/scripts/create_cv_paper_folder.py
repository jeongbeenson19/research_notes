#!/usr/bin/env python3
"""Backward-compatible wrapper. Use create_cv_paper_note.py instead."""

from __future__ import annotations

import runpy
from pathlib import Path


if __name__ == "__main__":
    target = Path(__file__).with_name("create_cv_paper_note.py")
    runpy.run_path(str(target), run_name="__main__")
