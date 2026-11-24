#!/usr/bin/env python3
"""Write one fortune-cookie line for a developer into MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only. The output directory is created if absent and is never removed.
"""

import os
from pathlib import Path

FORTUNE = "The TODO you wrote in haste will outlive the feature it was meant to finish."
MAX_CHARS = 120
FILENAME = "entry.txt"


def main() -> None:
    if not FORTUNE.strip() or len(FORTUNE) > MAX_CHARS:
        raise SystemExit("fortune must be 1..120 non-blank characters")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / FILENAME
    data = FORTUNE.encode("utf-8")
    # A fixed temporary name keeps repeated runs byte-identical; replace is atomic.
    pending = target.with_name(FILENAME + ".pending")
    with open(pending, "wb") as handle:
        handle.write(data)
    os.replace(pending, target)


if __name__ == "__main__":
    main()
