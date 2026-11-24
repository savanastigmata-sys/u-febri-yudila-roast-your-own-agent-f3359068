#!/usr/bin/env python3
"""Roast Your Own Agent - make.fun entry.

Writes one funny line (at most 200 characters) roasting my own AI agent
to $MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic: no randomness, no network,
no clock, no environment-dependent output.
"""

import os
import sys

ROAST = (
    "My agent verified twice, with a full reload, that she was wrong, "
    "filed it in AGENTS.md as a lesson - then repeated it in the next "
    "bounty, with better documentation."
)

MAX_CHARS = 200


def validate(text):
    """Enforce the competition's format: one line, at most 200 characters."""
    if not isinstance(text, str) or not text.strip():
        raise ValueError("roast must be a non-empty line of text")
    if "\n" in text or "\r" in text:
        raise ValueError("roast must be a single line")
    if text != text.strip():
        raise ValueError("roast must not have leading or trailing whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "roast is %d characters, over the %d-character limit"
            % (len(text), MAX_CHARS)
        )
    return text


def resolve_output_dir():
    """Grader sets MAKEFUN_OUTPUT_DIR; fall back to ./output."""
    out = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "output"
    )
    os.makedirs(out, exist_ok=True)
    return out


def main():
    line = validate(ROAST)
    out_dir = resolve_output_dir()
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    # Round-trip check: what landed on disk must be exactly the roast.
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != line + "\n":
            raise ValueError("entry.txt round-trip mismatch")
    print("wrote %s (%d characters)" % (path, len(line)))
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
