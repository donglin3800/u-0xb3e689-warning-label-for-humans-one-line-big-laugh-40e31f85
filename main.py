#!/usr/bin/env python3
"""Warning label for humans: one line, big laugh.

The label is a single fixed sentence. It reads like a printed safety
warning — do not shake, do not feed after midnight, do not believe the
human's own status report — and the joke only lands at the very end,
when the human turns out to be on fire while insisting it is fine.
Fixed text, no clock, no network, no randomness, so every run writes
the same bytes to entry.txt.
"""

import os
import sys
from pathlib import Path

LABEL = "WARNING: Do not shake this human, do not feed it after midnight, or believe it when it says 'I'm fine' while actively on fire."
MAX_CHARS = 160


def check_label(text):
    """Return an error string, or None when the label is a valid one-liner."""
    if not text or not text.strip():
        return "label is empty"
    if "\n" in text or "\r" in text:
        return "label must be a single line"
    if text.strip() != text:
        return "label must not start or end with whitespace"
    if len(text) > MAX_CHARS:
        return f"label is {len(text)} chars, limit is {MAX_CHARS}"
    return None


def output_path():
    """Where the grader expects the entry: $MAKEFUN_OUTPUT_DIR/entry.txt."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(base) / "entry.txt"


def main(argv=None):
    problem = check_label(LABEL)
    if problem is not None:
        print(problem, file=sys.stderr)
        return 1
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LABEL, encoding="utf-8")
    sys.stdout.write(LABEL + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
