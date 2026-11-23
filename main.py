"""One Emoji, One Smile: writes the entry text to /output/entry.txt.

Why this emoji: heart hands, warm at first glance, universal, a deliberate
pick rather than the default smiley.
"""

import os

# The entry itself: one emoji, heart hands.
ENTRY = '🫶'

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
