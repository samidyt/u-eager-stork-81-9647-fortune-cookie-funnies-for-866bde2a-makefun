#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers — make.fun entry.

Writes a single fortune-cookie line (1-120 characters) for a software
engineer to /output/entry.txt, where the house gate scorer reads it.

The line: a classic fortune-cookie opening ("You will inherit...") with
an engineer's nightmare as the payoff — a codebase with no tests, no
comments, and a variable named temp_final_v2_REAL.
"""

import os

FORTUNE = "You will inherit a codebase with no tests, no comments, and a variable named temp_final_v2_REAL."


def output_path() -> str:
    """Where the entry goes: /output/entry.txt, or $OUTPUT_DIR/entry.txt."""
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    text = FORTUNE.strip()
    assert 1 <= len(text) <= 120, f"fortune must be 1-120 chars, got {len(text)}"
    assert "\n" not in text, "fortune must be a single line"
    path = output_path()
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Round-trip check: what the gate scorer reads must be exactly the line.
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == text, "entry.txt round-trip mismatch"
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
