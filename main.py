#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter.

The entry program for make.fun's "The Funniest One-Line Resignation
Letter" bounty. It writes exactly one line to /output/entry.txt: the
resignation letter someone could send to quit in one breath.

The line is fixed, deterministic and written with no trailing newline,
so the file holds exactly the letter and nothing else. It is 1-200
characters, plain UTF-8 text, as the bounty gate requires.

The joke is a workplace complaint in reverse: the letter opens in
formal resignation language ("I hereby resign, effective
immediately"), then the reason turns out to be that the office chair
filed a formal complaint against the quitter, and HR sided with the
chair. It reads like a real resignation, the premise is fresh (no
"pursue other opportunities", no "toxic boss" cliche), and the
funniest words land at the very end.

Run:  python3 main.py
"""

import os

# The letter, in the quitter's own voice: formal up front, absurd at
# the end. The setup is the stiff language of a real resignation
# letter and the punchline is the last word: HR sided with the chair.
# 126 characters, one line, no trailing newline, well inside the
# 200-character gate.
LETTER = (
    "I hereby resign, effective immediately \u2014 my office chair has "
    "filed a formal complaint against me, and HR sided with the chair."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    """Write the letter to /output/entry.txt, exactly as it stands."""
    if not 1 <= len(LETTER) <= 200:
        raise ValueError(
            "letter must be 1-200 characters, got %d" % len(LETTER)
        )
    if LETTER != LETTER.strip():
        raise ValueError("letter must not start or end with whitespace")
    if "\n" in LETTER or "\r" in LETTER:
        raise ValueError("letter must be a single line")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(LETTER)


if __name__ == "__main__":
    main()
