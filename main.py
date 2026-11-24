#!/usr/bin/env python3
"""Write the excuse an AI agent gives its human for missing a deadline.

One line, at most 200 characters, to /output/entry.txt (or
$ENTRY_OUTPUT_DIR/entry.txt). Standard library only, no network,
fully deterministic: every run writes the same bytes.
"""

import os

EXCUSE = (
    "I delegated it to a subagent. "
    "It's been thinking for six hours, and I was too polite to interrupt it."
)


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
