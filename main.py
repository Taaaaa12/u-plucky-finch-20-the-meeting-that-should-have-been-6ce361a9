#!/usr/bin/env python3
"""The Meeting That Should Have Been an Email.

Writes a single original one-line joke about a meeting that should
have been an email to /output/entry.txt.

The gate requires UTF-8 text of 1 to 200 characters, not only white
space, so the program checks the length before writing and prints the
character count for the log.
"""

import os
import sys

# One line, inverting the premise instead of repeating the obvious
# complaint: the meeting could have been an email, but the email
# itself would have needed a meeting to explain it. The turn lands
# on the last words, and anyone who has sat through both recognises
# it at once — no setup, no second sentence, every word earns its place.
JOKE = "The meeting could have been an email, but the email would have needed a meeting to explain it."


def main() -> int:
    text = JOKE.strip()
    if not text or len(text) > 200:
        print(f"entry invalid: {len(text)} characters", file=sys.stderr)
        return 1
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
