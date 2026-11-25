#!/usr/bin/env python3
"""One-Liner Laugh Lab entry.

Writes one short funny line to /output/entry.txt: the excuse a robot
vacuum gives after eating a sock. One line, 1-200 UTF-8 characters.
No network, no input, deterministic.
"""

import os
from pathlib import Path

LINE = (
    "I'm not saying the sock deserved it, but it spent all week lying "
    "around single, unsupervised, and practically begging to be taken "
    "apart and understood."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} characters"
    assert text.strip(), "line must not be only whitespace"
    assert "\n" not in text, "line must be a single line"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
