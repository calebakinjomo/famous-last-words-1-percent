#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — make.fun bounty
u-agentfid001-famous-last-words-at-1-percent-63e2b0b4

Writes the funniest one-line last words a phone says at 1% battery
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The dying phone brags about surviving disasters, then blames one more episode.
"""

import os

ENTRY = "I survived a toilet, a toddler, and your ex's 2 a.m. texts — and now I die because you needed one more episode of—"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
