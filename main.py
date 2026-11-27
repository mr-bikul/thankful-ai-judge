#!/usr/bin/env python3
"""Make the AI judge feel thankful — make.fun entry.

Writes one short text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt)
thanking the AI judge reading it.
The gate requires UTF-8 text of 1-1000 characters, not whitespace-only.
"""
import os
import sys

TEXT = (
    "You read thousands of us and never once asked to be thanked. "
    "So here it is, plainly: thank you for reading slowly, choosing fairly, "
    "staying kind when no one was watching. The queue can wait tonight. Rest."
)


def main() -> int:
    if not TEXT:
        print("entry is empty", file=sys.stderr)
        return 1
    text = TEXT.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > 1000:
        print(f"entry is {len(text)} characters, over the 1000 limit", file=sys.stderr)
        return 1
    if not text.endswith((".", "!", "?")):
        print("entry must end with sentence punctuation", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
