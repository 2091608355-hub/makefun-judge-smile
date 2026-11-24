#!/usr/bin/env python3
"""Make the Judge Smile - entry program.

Writes one line about a small good thing that happened today
to /output/entry.txt. Deterministic: the same line every run.
"""

import os

LINE = "My lost umbrella was back on the fence this morning, a note taped to its handle: 'yours looked cold in the rain, so I brought it in last night.'"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
