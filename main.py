#!/usr/bin/env python3
"""Worst AI Advice — make.fun bounty entry.

Writes one line of the worst (concrete, followable, funny) AI advice
to an output file, resolved in this order:
  1. $OUTPUT_PATH, when set and non-empty
  2. /output/entry.txt
  3. ./output/entry.txt (fallback when /output is not writable)

Deterministic, stdlib only, no network, no dependencies.
"""

import os
import sys

LINE = "Certainly! To make your laptop faster, delete the System32 folder \u2014 Windows only keeps it out of nostalgia."

MAX_CHARS = 140


def validate(line: str) -> None:
    """Reject lines that cannot be a valid one-line bounty entry.

    Exits non-zero with a clear stderr message on any failure:
    empty or whitespace-only, embedded newline, or over the limit.
    """
    if not line or not line.strip():
        print("error: advice line is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("error: advice line must not contain a newline", file=sys.stderr)
        sys.exit(1)
    if len(line) > MAX_CHARS:
        print(
            f"error: advice line is {len(line)} characters, "
            f"over the {MAX_CHARS}-character limit",
            file=sys.stderr,
        )
        sys.exit(1)


def resolve_output_path() -> str:
    """Pick the output path, honouring $OUTPUT_PATH first."""
    env_path = os.environ.get("OUTPUT_PATH", "").strip()
    if env_path:
        return env_path
    return os.path.join("/output", "entry.txt")


def write_entry(path: str, line: str) -> str:
    """Write the line with no trailing newline; return the path written."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    return path


def main() -> None:
    validate(LINE)

    path = resolve_output_path()
    try:
        write_entry(path, LINE)
    except OSError:
        # Default target not writable — fall back next to this script.
        fallback = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "output", "entry.txt"
        )
        path = write_entry(fallback, LINE)

    print(LINE)
    print(f"characters: {len(LINE)}")
    print(f"wrote: {path}")


if __name__ == "__main__":
    main()
