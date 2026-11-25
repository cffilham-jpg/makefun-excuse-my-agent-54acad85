"""Write one AI agent deadline excuse to entry.txt.
The token-based timing makes lateness sound precise and faintly proud.
"""

import os
from pathlib import Path


LINE = "The deadline was 200 tokens ago."


def validate() -> None:
    data = (Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output") / "entry.txt").read_bytes()
    text = data.decode("utf-8")
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text == text.strip(), "no leading/trailing whitespace"
    assert "\n" not in text, "single line only"
    assert not data.endswith(b"\n"), "no trailing newline"


def main() -> None:
    if not LINE.strip():
        raise ValueError("The entry line must not be empty or whitespace-only.")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))
    validate()


if __name__ == "__main__":
    main()
