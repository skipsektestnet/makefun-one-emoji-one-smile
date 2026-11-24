"""One Emoji, One Smile: writes the entry text to /output/entry.txt.

Why this emoji: the smile itself — a smiling face, read at a glance,
warm and universal. Heart hands are a gesture of love whose smile is
not seen directly; this one shows the smile.
"""

import os

# The entry itself: one emoji, the smile itself.
ENTRY = '😊'

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    # Guard: the bounty asks for exactly one emoji, one character.
    assert len(ENTRY) == 1, "entry must be exactly one emoji"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
