#!/usr/bin/env python3
"""One-star review of something essential.

Writes a single deadpan one-star review of gravity, an everyday essential,
at most 160 characters, to /output/entry.txt. Pure standard library and fully
deterministic: the same review every run.
"""

import os

REVIEW = "One star. Gravity drops my phone at least once a day and never says sorry. I would like it to stop touching my things."

OUTPUT_PATH = "/output/entry.txt"


def main():
    # The gate accepts 1 to 160 characters; refuse to write anything else.
    if not 1 <= len(REVIEW) <= 160:
        raise ValueError(f"review is {len(REVIEW)} characters, must be 1-160")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
