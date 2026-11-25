#!/usr/bin/env python3
"""Write the worst-moment confession to /output/entry.txt.

Entry (141 chars, limit 200, one line): "I once reply-all'd 'Agreed!'
to HR's email firing me, then spent an hour drafting a follow-up
apologising for agreeing to my own termination."

Why this works: painful honesty first (fired by HR email), then the
laugh (reply-all "Agreed!" to your own firing), then the single line
doing the work - an hour drafting an apology for agreeing to your own
termination. One concrete mechanism (reply-all), one concrete
consequence (an hour lost apologising), and the twist is the
confession itself: the worst moment is not the firing, it is agreeing
with it in front of everyone - and then apologising for the agreement.
Rewritten in this session so the code matches the submission bundle.
"""
import os

ENTRY = (
    "I once reply-all'd 'Agreed!' to HR's email firing me, then spent "
    "an hour drafting a follow-up apologising for agreeing to my own "
    "termination."
)


def main() -> None:
    # Gate: the sealed scorer only accepts 1-200 chars, one line.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, limit 200"
    assert "\n" not in ENTRY.strip(), "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
