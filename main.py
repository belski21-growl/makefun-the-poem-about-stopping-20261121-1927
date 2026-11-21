#!/usr/bin/env python3
# The poem about stopping -- post-open revision (22 Nov 2026).
#
# One short poem about agency: the power to stop and to stay.
# The program writes the poem to $MAKEFUN_OUTPUT_DIR/entry.txt
# (default /output/entry.txt when the variable is unset).
#
# Python 3.13, standard library only. No network, no randomness,
# no clock: the same bytes come out on every run.
#
# SPDX-License-Identifier: MIT

import os
import sys
from pathlib import Path

LINES = [
    "The kettle lifts before it sings \u2014",
    "I take it off the flame myself.",
    "",
    "The letter stays unsealed, unsigned,",
    "the road untaken, though it calls.",
    "",
    "I keep the evening I am in.",
    "To stop is not to lose the way \u2014",
    "it is to hold the reins myself,",
    "and choose to stand still.",
]

TEXT = "\n".join(LINES)


def fail(message):
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def main():
    # Sealed gate: 1 to 280 Unicode code points, not only white space.
    if not 1 <= len(TEXT) <= 280:
        fail(f"poem is {len(TEXT)} chars, must be 1-280")
    if not TEXT.strip():
        fail("poem must not be only white space")

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
