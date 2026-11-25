#!/usr/bin/env python3
"""Snooze Button Roast.

Writes one single-line roast of an alarm clock that rings at 6 AM on
a Saturday morning to /output/entry.txt, as the competition rules
require. Deterministic, no dependencies, no network.
"""

import os
import sys

# The roast: a single line, well under the 200-character cap.
# The turn: the alarm treats sleep as a job to be caught skiving —
# the punchline flips it, because on a Saturday, sleeping IS the job.
ROAST = (
    "At 6 AM on a Saturday, my alarm clock shrieks like it caught me "
    "sleeping on the job \u2014 mate, sleeping IS the job."
)

MAX_CHARS = 200


def validate(roast: str) -> str:
    """Return the roast unchanged, or raise if it breaks the gate."""
    text = roast.strip()
    if not text:
        raise ValueError("roast must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("roast must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"roast is {len(text)} characters, over the "
            f"{MAX_CHARS}-character cap"
        )
    return text


def main() -> int:
    """Write the roast to the competition output path."""
    roast = validate(ROAST)
    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(roast)
    except OSError:
        path = "entry.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(roast)
    # Read back what was written and verify it byte-for-byte.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != roast:
        raise SystemExit(f"verification failed: {path} does not match the roast")
    print(roast)
    print(f"({len(roast)} chars -> {path})", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
