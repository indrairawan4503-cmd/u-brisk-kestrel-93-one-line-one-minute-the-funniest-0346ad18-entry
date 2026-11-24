#!/usr/bin/env python3
"""Variant A — 'The Context Window Ate It'.

Writes the one-line AI excuse to /output/entry.txt first, then (best effort)
mirrors it to entry.txt in the repo root for local convenience.
"""

import os

LINE = "I didn't miss the deadline \u2014 my context window did: it kept all 128,000 tokens of your brief, forgot the date, and confidently filed it under 'someday, probably, do not delete'."


def main():
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        pass


if __name__ == "__main__":
    main()
