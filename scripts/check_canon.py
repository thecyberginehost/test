#!/usr/bin/env python3
"""Deterministic CANON STRUCTURE guard.

Refuses to pass if a multi-chapter canon file lost structure, e.g. an agent
full-rewrote and clobbered it (as happened once when a reconciler overwrote
book/outline.md with a single chapter block). This runs at the chapter gate AND
from the git pre-push hook, so a clobber from ANY agent or any source cannot slip
through to a commit/push silently.

Checks:
  OUTLINE  book/outline.md contains a CONTIGUOUS chapter-header sequence
           "### 1." .. "### EXPECTED_CHAPTERS." with no gaps, no duplicates, and
           none missing; and its line count is >= OUTLINE_LINE_FLOOR.
  BIBLE    book/bible.md is >= BIBLE_LINE_FLOOR lines and still contains its LOCKED
           structural anchors (ANNOTATION RULES, DECODE-DEBT CEILING,
           DECODE-DEBT LEDGER).

Usage: python3 scripts/check_canon.py
Exit code 0 on CANON OK, 1 on CANON DAMAGED.

NEVER weaken this guard to make something pass. If the book legitimately changes its
planned chapter count, update EXPECTED_CHAPTERS; do not delete the check.
"""
import os
import re
import sys

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPTS_DIR)

EXPECTED_CHAPTERS = 22       # Book One is planned at 22 chapters (3 acts).
OUTLINE_LINE_FLOOR = 200     # full outline is ~320 lines; a clobber drops far below.
BIBLE_LINE_FLOOR = 1500      # bible is ~2700 lines; a clobber drops far below.
BIBLE_ANCHORS = ["ANNOTATION RULES", "DECODE-DEBT CEILING", "DECODE-DEBT LEDGER"]

HEADER_RE = re.compile(r"^### (\d+)\.", re.M)


def line_count(text):
    return len(text.splitlines())


def check_outline(failures):
    path = os.path.join(REPO_ROOT, "book", "outline.md")
    if not os.path.isfile(path):
        failures.append(f"OUTLINE: file missing ({path})")
        return None
    text = open(path, encoding="utf-8").read()
    nums = sorted(int(m.group(1)) for m in HEADER_RE.finditer(text))
    expected = list(range(1, EXPECTED_CHAPTERS + 1))
    if nums != expected:
        missing = [n for n in expected if n not in nums]
        extra = [n for n in nums if n not in expected]
        msg = (f"OUTLINE: chapter headers not the contiguous set 1..{EXPECTED_CHAPTERS}. "
               f"found {len(nums)} header(s): {nums}.")
        if missing:
            msg += f" MISSING {missing}."
        if extra:
            msg += f" UNEXPECTED {extra}."
        failures.append(msg)
    lc = line_count(text)
    if lc < OUTLINE_LINE_FLOOR:
        failures.append(f"OUTLINE: line count {lc} is below the floor {OUTLINE_LINE_FLOOR} "
                        f"(possible clobber/truncation).")
    return nums


def check_bible(failures):
    path = os.path.join(REPO_ROOT, "book", "bible.md")
    if not os.path.isfile(path):
        failures.append(f"BIBLE: file missing ({path})")
        return
    text = open(path, encoding="utf-8").read()
    lc = line_count(text)
    if lc < BIBLE_LINE_FLOOR:
        failures.append(f"BIBLE: line count {lc} is below the floor {BIBLE_LINE_FLOOR} "
                        f"(possible clobber/truncation).")
    for anchor in BIBLE_ANCHORS:
        if anchor not in text:
            failures.append(f"BIBLE: LOCKED anchor {anchor!r} not found (possible clobber).")


def main():
    failures = []
    nums = check_outline(failures)
    check_bible(failures)

    print("CANON STRUCTURE CHECK")
    if failures:
        for f in failures:
            print(f"  FAIL: {f}")
        print("\nCANON DAMAGED")
        return 1

    print(f"  outline.md: {len(nums)} chapter headers, contiguous 1..{EXPECTED_CHAPTERS}, "
          f"above line floor")
    print(f"  bible.md: all {len(BIBLE_ANCHORS)} LOCKED anchors present, above line floor")
    print("\nCANON OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
