#!/usr/bin/env python3
"""Deterministic SEAL tripwire for Book One (Ch 14 to Ch 22).

book/SERIES_LORE.md holds series-level truth that sits ABOVE Book One's horizon.
Its SEAL LIST is binding: Ch 14 to Ch 22 prose must NOT reveal, imply, or gesture
at Book Two truth. This script is the cheap, deterministic backstop that kills the
OBVIOUS leaks at the chapter gate, the same way lint_tells.py kills AI tells. The
semantic edge cases are the continuity-checker's job; this only catches literal,
high-precision banned phrases so it does not false-positive on normal apocalypse
prose.

It scans the chapter's drafted section prose (book/chapters/chNN/sNN.md) and SKIPS
System / Operator overlay blocks (blockquote lines beginning with ">"), because the
seal is about the narrative prose, not the formatted System text. Any hit FAILS the
gate, same severity as a tells-lint failure.

Usage: python3 scripts/check_seal.py <chapter-number>
Exit code 0 on SEAL OK, 1 on SEAL BREACH (or usage/argument error).

NEVER loosen this list to make a chapter pass. If a phrase is a legitimate false
positive, tighten it to be MORE precise, do not delete the protection.
"""
import os
import re
import sys

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPTS_DIR)

SECTION_RE = re.compile(r"^s\d+\.md$")          # sNN.md, NOT sNN.notes.md

# High-precision banned phrases (case-insensitive substring match), each tied to a
# specific SEAL LIST item in book/SERIES_LORE.md. Keep these TIGHT.
SEALED_PHRASES = [
    # -- The multi-world scale (Book One stays Earth-only) --------------------
    "other world", "another world", "other settlement", "another settlement",
    "across worlds", "every world", "worlds like this one",
    # -- NULL_OPERATOR as a recurring / standing flag, and prior readers -------
    "previous operator", "prior operator", "other operators", "another operator",
    "other readers", "standing seat", "the only one ever",
    # -- The inversion: the ADMINISTRATOR has no handler / nothing supervises IT.
    #    NOTE: bare "no handler" is deliberately NOT here. Book One's premise is
    #    that AARON is the unhandled account; "no handler" / "unhandled" appear
    #    all over legitimate prose about his class. These literals fire ONLY on
    #    the sealed inversion (the god itself being unsupervised), never on Aaron.
    "nothing supervises", "nothing watches it", "no handler of its own",
    "administrator has no handler", "administrator is unhandled",
    "nothing above the administrator", "no handler above",
]


def section_files(chapter_dir):
    names = [n for n in os.listdir(chapter_dir) if SECTION_RE.match(n)]
    return sorted(names)


def prose_lines(path):
    """Yield (line_number, text) for narrative prose only, skipping System /
    Operator overlay blocks (blockquote lines that begin with '>')."""
    with open(path, encoding="utf-8") as fh:
        for n, line in enumerate(fh, start=1):
            if line.lstrip().startswith(">"):
                continue
            yield n, line


def scan_section(path):
    """Return a list of (line_number, phrase, context) hits in one section."""
    hits = []
    for n, line in prose_lines(path):
        low = line.lower()
        for phrase in SEALED_PHRASES:
            if phrase in low:
                hits.append((n, phrase, line.strip()))
    return hits


def main():
    if len(sys.argv) != 2:
        print("usage: check_seal.py <chapter-number>")
        return 2
    try:
        chapter = int(sys.argv[1])
    except ValueError:
        print(f"SEAL BREACH: chapter number must be an integer, got {sys.argv[1]!r}")
        return 1

    chap_id = f"ch{chapter:02d}"
    chapter_dir = os.path.join(REPO_ROOT, "book", "chapters", chap_id)

    if not os.path.isdir(chapter_dir):
        print(f"Chapter {chapter} ({chap_id})")
        print(f"  FAIL: chapter directory not found: {chapter_dir}")
        print("\nSEAL BREACH")
        return 1

    sections = section_files(chapter_dir)
    if not sections:
        print(f"Chapter {chapter} ({chap_id})")
        print(f"  FAIL: no section files (sNN.md) found in {chapter_dir}")
        print("\nSEAL BREACH")
        return 1

    all_hits = []
    for s in sections:
        for (n, phrase, context) in scan_section(os.path.join(chapter_dir, s)):
            all_hits.append((s, n, phrase, context))

    print(f"Chapter {chapter} ({chap_id})  SEAL CHECK")
    print(f"  sections scanned: {len(sections)} ({', '.join(sections)})")
    print(f"  sealed phrases watched: {len(SEALED_PHRASES)}")
    print()

    if all_hits:
        for (s, n, phrase, context) in all_hits:
            print(f"  FAIL: {s}:{n}: sealed phrase {phrase!r}")
            print(f"        > {context}")
        print(f"\nSEAL BREACH ({len(all_hits)} hit(s)). Book Two truth must not surface in Book One prose.")
        return 1

    print("SEAL OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
