#!/usr/bin/env python3
"""Worst AI Advice — make.fun bounty entry.

Writes one line of the worst (concrete, followable, funny) AI advice
to /output/entry.txt (falling back to ./output/entry.txt).
Deterministic, stdlib only, no network, no dependencies.
"""

import os

LINE = "Certainly! To make your laptop faster, delete the System32 folder \u2014 Windows only keeps it out of nostalgia."


def main() -> None:
    assert 1 <= len(LINE) <= 140, f"line length {len(LINE)} out of range"

    try:
        out_dir = "/output"
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(LINE)
    except OSError:
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(LINE)

    print(LINE)
    print(f"characters: {len(LINE)}")
    print(f"wrote: {path}")


if __name__ == "__main__":
    main()
