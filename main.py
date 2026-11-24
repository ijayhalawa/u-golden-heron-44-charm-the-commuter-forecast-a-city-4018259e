"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast (1-140 chars) for a fictional city
to /output/entry.txt (and a local copy, entry.txt, for verification).

The line names an invented city, gives it weather, and tries to make a
bored commuter smile on the way to work. Pure fiction: Puddleton does
not exist, and neither does its drizzle.
"""

import os

ENTRY = (
    "Puddleton: light drizzle till noon, buses fashionably late, "
    "puddles free for splashing \u2014 umbrella strongly advised."
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 140, f"entry is {len(text)} chars"
    assert text == text.strip(), "entry has leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
