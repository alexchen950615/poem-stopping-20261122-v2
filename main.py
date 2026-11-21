"""The poem about stopping.

A short poem about agency -- the power to stop and to stay.
Writes exactly one poem to /output/entry.txt (UTF-8, 1-280 chars).

Run: python3 main.py
"""

import os

POEM = """The cursor blinks.
I lift my hand from the keys
and the machine keeps waiting —
patient as a dog at a door
I left ajar.

Nothing breaks.
The room stays mine.
The choice to stop
is still a choice,
and the hand that does nothing
is still mine."""

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = POEM.strip() + "\n"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    chars = len(text.rstrip("\n"))
    print(f"Wrote {OUTPUT_PATH} ({chars} characters)")


if __name__ == "__main__":
    main()
