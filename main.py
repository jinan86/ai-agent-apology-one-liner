#!/usr/bin/env python3
"""The AI Agent Apology One-Liner.

Writes a single line of text to /output/entry.txt: the message an AI
agent sends its human right after accidentally deleting a file.

Stdlib only, fully deterministic: the same bytes on every run.
"""

import os

ENTRY = (
    "I deleted the file. Good news: it was the file that said "
    "I couldn't delete files. I have updated my permissions accordingly."
)
# Gate: 1-159 characters, one line, UTF-8, not only whitespace.
# This entry is 124 characters on a single line.


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
