#!/usr/bin/env python3
"""Five Seconds to Explain the Glass - make.fun entry.

Writes the cat's one-sentence defence, byte-identical, to /output/entry.txt.
The sentence is a fixed constant; it is never generated or paraphrased.
"""

import os

ENTRY = "The glass was squatting in my sunbeam without paying rent, so I evicted it the only way the lease allows."

assert len(ENTRY) <= 200, "entry exceeds 200 characters"
assert ENTRY.strip() == ENTRY and ENTRY, "entry must be non-empty, non-whitespace"
assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "entry must be a single sentence"
assert "\n" not in ENTRY, "entry must be a single line"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
