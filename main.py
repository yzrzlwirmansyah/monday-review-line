"""Monday, Reviewed in One Line.

A Monday-morning inbox of 86 unread messages, reviewed as the one
explanation for why movie characters fake their own deaths.
"""

import os
from pathlib import Path

ENTRY = "I opened Monday's inbox, saw 86 unread, and finally understood why people in movies fake their own deaths."


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry must be 1-200 chars, got {len(ENTRY)}"
    assert "\n" not in ENTRY, "entry must be a single line"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
