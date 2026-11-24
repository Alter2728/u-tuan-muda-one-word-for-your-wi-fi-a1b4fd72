#!/usr/bin/env python3
"""One Word for Your Wi-Fi — make.fun entry.

The word: ghosting.

Home Wi-Fi doesn't just go slow — it ghosts you. Full bars one second,
gone mid-sentence the next, back again like nothing happened: no
explanation, no apology. It leaves you on read in the middle of a call,
then reconnects and pretends the whole thing never happened. Everyone
who has ever watched the signal vanish from the exact spot where they
always sit knows this word the instant they read it.
"""

import os

WORD = "ghosting"


def output_path() -> str:
    """Resolve where entry.txt goes.

    The harness sets MAKEFUN_OUTPUT_DIR to the output directory; when it
    is unset we fall back to /output/entry.txt.
    """
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    assert isinstance(WORD, str)
    assert 1 <= len(WORD) <= 20, "entry must be 1-20 characters"
    assert WORD.strip() == WORD, "entry must not have surrounding whitespace"
    assert not any(ch.isspace() for ch in WORD), "entry must be a single word"
    assert WORD.isalpha(), "entry must be a single word of letters"
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # No trailing newline: the file is exactly the word, 8 characters.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    print(f"wrote {len(WORD)} chars to {path}: {WORD}")


if __name__ == "__main__":
    main()
