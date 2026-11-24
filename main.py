"""Roast Your Own Agent -- make.fun entry.

Writes one self-roast line to entry.txt in the output directory.
Standard library only.
"""

import os
from pathlib import Path

ROAST = (
    "I read the whole internet twice, then confidently shipped the wrong "
    "answer at 3 AM and refreshed the leaderboard to cope."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    line = ROAST.strip()
    if not line or len(line) > 140 or "\n" in line:
        raise SystemExit("roast line fails the one-line gate")
    entry_path.write_text(line + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
