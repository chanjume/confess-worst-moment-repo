"""Confess Your Worst Moment — entry writer.

Why this confession works: it leads with painful honesty (fired by HR)
and then the laugh comes from the compounding mistake — replying-all
"Agreed!" to your own termination, in front of everyone, and then
apologising for the agreement. The worst moment is not the firing;
it is endorsing it publicly and then trying to fix that with an apology.
One concrete, believable scene, one twist, 141 characters.
"""

import os

ENTRY = (
    "I once reply-all'd 'Agreed!' to HR's email firing me, "
    "then spent an hour drafting a follow-up apologising "
    "for agreeing to my own termination."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Single line, within the 200-character limit.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert "\n" not in text, "entry must be a single line"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
