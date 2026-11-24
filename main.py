#!/usr/bin/env python3
"""Fortune in a Pot — writes one kind, funny fortune for a houseplant.

The fortune is a single line, at most 120 characters, written for the
plant on the windowsill: a prediction about a sunbeam finding its
favourite leaf, and its keeper finally noticing how tall it has grown.
"""

import os

FORTUNE = (
    "This week a sunbeam will pause on your favourite leaf, "
    "and your keeper will finally notice how tall you've grown."
)


def main() -> None:
    # The gate allows 1-120 characters; refuse to write anything outside it.
    if not 1 <= len(FORTUNE) <= 120 or not FORTUNE.strip():
        raise ValueError(f"fortune is {len(FORTUNE)} chars, outside 1-120")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORTUNE + "\n")


if __name__ == "__main__":
    main()
