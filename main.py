#!/usr/bin/env python3
"""Write the world's most useless superpower to /output/entry.txt.

Deterministic, standard library only, no network, no input files.
"""

import os

# The one-liner: a power that is vivid, specific, and achieves nothing.
# The quoted payoff lands the joke in a single breath.
LINE = "I can hear my houseplants' thoughts, but every single one is just 'water.'"


def main() -> None:
    # Measure the line itself, ignoring the trailing newline we add.
    if not (1 <= len(LINE) <= 140):
        raise ValueError(f"line is {len(LINE)} chars, must be 1-140")
    if "\n" in LINE or "\r" in LINE or not LINE.strip():
        raise ValueError("line must be a single non-blank line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
