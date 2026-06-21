#!/usr/bin/env python3
"""Advisory human-voice repetition reporter (the binge-read test).

The book is read end to end, so a beat worded the same way every time reads like a
machine wrote it. The per-section linters cannot see this: each section is clean on
its own, and the sameness only shows ACROSS sections and chapters. This reporter
surfaces over-used phrasings so the human-voice pass (and the writer/editor) can
rotate them.

It is ADVISORY ONLY. It never blocks, never gates, and always exits 0. It is NOT
part of the hard chapter gate (check_chapter.py) or the seal gate (check_seal.py),
and nothing here may ever be used to weaken those. Run it at chapter close and again
on the whole book before calling it done.

Two reports, both over the drafted section prose (System / Operator blockquote lines
beginning with ">" are skipped, same as the other scripts):
  1. WATCHLIST  -- curated phrasings known to go samey (grows as you learn, like the
     lint_tells banned list). Reports per-section and total counts.
  2. ECHOES     -- generic repeated 4-word phrases that appear 3+ times in scope and
     are not pure function-word noise. Catches new samey phrasings automatically.

Usage:
  python3 scripts/echo_watch.py <chapter-number>   # one chapter
  python3 scripts/echo_watch.py all                # every written chapter
Exit code: always 0 (advisory).
"""
import os
import re
import sys
from collections import Counter

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPTS_DIR)
CHAPTERS_DIR = os.path.join(REPO_ROOT, "book", "chapters")

SECTION_RE = re.compile(r"^s\d+\.md$")
CHAP_RE = re.compile(r"^ch\d+$")
WORD_RE = re.compile(r"[a-z][a-z'\-]*")

# Curated watchlist: phrasings observed to repeat across the book. Grow this as you
# find more (same discipline as scripts/lint_tells.py). Keep entries lowercase.
WATCHLIST = [
    # opening the hidden-layer read (the worst offender)
    "surfaced his sight", "surfaced the", "surfaced its block", "surfaced it",
    "the dim layer came up", "dim layer came up", "the dim layer surfaced",
    "dim layer spread", "came up under", "spread out under",
    "pressed his sight", "pushed his sight", "raised its block", "opened the",
    # the surface-vs-under metaphor going naked
    "looked at it", "then he looked under", "looked under it", "nothing under it",
]

# 4-grams that are entirely these words are noise, not voice repetition.
STOP = set("""a an and as at be been but by for from had has have he her him his i
in into is it its me my no not of off on once one or our out over she so that the
their them then there they this to up was we were what when which who will with you
your had not did do does down had he'd he's i'd i'm it's that's there's""".split())

ECHO_NGRAM = 4
ECHO_MIN = 3


def section_files(chapter_dir):
    return sorted(n for n in os.listdir(chapter_dir) if SECTION_RE.match(n))


def prose_lines(path):
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if line.lstrip().startswith(">"):
                continue
            yield line


def section_text(path):
    return " ".join(prose_lines(path))


def chapters_in_scope(arg):
    if arg == "all":
        return sorted(n for n in os.listdir(CHAPTERS_DIR)
                      if CHAP_RE.match(n) and os.path.isdir(os.path.join(CHAPTERS_DIR, n)))
    try:
        return ["ch%02d" % int(arg)]
    except ValueError:
        return []


def main():
    if len(sys.argv) != 2:
        print("usage: echo_watch.py <chapter-number|all>")
        return 0  # advisory: never a hard error

    chaps = chapters_in_scope(sys.argv[1])
    if not chaps:
        print(f"no chapters found for scope {sys.argv[1]!r}")
        return 0

    # gather text per section
    units = []  # (chap, section_name, lowered_text)
    for chap in chaps:
        cdir = os.path.join(CHAPTERS_DIR, chap)
        if not os.path.isdir(cdir):
            continue
        for s in section_files(cdir):
            units.append((chap, s, section_text(os.path.join(cdir, s)).lower()))

    if not units:
        print("no section prose found in scope.")
        return 0

    full = " ".join(t for _, _, t in units)

    print(f"ECHO WATCH (advisory) scope: {sys.argv[1]}  sections: {len(units)}")
    print("=" * 64)

    # --- 1. WATCHLIST ----------------------------------------------------
    print("\n[1] WATCHLIST phrasings (curated):")
    any_hit = False
    for phrase in WATCHLIST:
        total = full.count(phrase)
        if total >= 2:
            any_hit = True
            where = []
            for chap, s, t in units:
                c = t.count(phrase)
                if c:
                    where.append(f"{chap}/{s[:-3]}x{c}" if c > 1 else f"{chap}/{s[:-3]}")
            print(f"  {total:3d}  {phrase!r}")
            print(f"       {', '.join(where)}")
    if not any_hit:
        print("  (nothing on the watchlist repeats 2+ times in scope)")

    # --- 2. ECHOES (auto) ------------------------------------------------
    words = WORD_RE.findall(full)
    grams = Counter()
    for i in range(len(words) - ECHO_NGRAM + 1):
        gram = words[i:i + ECHO_NGRAM]
        if all(w in STOP for w in gram):
            continue
        grams[" ".join(gram)] += 1
    echoes = [(g, c) for g, c in grams.items() if c >= ECHO_MIN]
    echoes.sort(key=lambda x: (-x[1], x[0]))

    print(f"\n[2] ECHOES: {ECHO_NGRAM}-word phrases repeated {ECHO_MIN}+ times "
          f"({len(echoes)} found, top 30):")
    if echoes:
        for g, c in echoes[:30]:
            print(f"  {c:3d}  {g}")
    else:
        print("  (no non-trivial 4-word phrase repeats 3+ times in scope)")

    print("\nAdvisory only. Rotate what reads samey; nothing here blocks the gate.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
