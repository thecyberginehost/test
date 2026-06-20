#!/usr/bin/env python3
"""Deterministic chapter verification gate.

Checks a chapter's section files under book/chapters/chNN/ and refuses to let the
pipeline move on unless the chapter meets hard, machine-checkable standards. This
exists so we are NOT trusting the writing agents to self-report.

Checks:
  LENGTH      total word count across sNN.md section files is 3,500 to 5,000.
  TELLS       scripts/lint_tells.py returns CLEAN on every sNN.md section.
  CONTINUITY  every sNN.md has a non-empty matching sNN.notes.md (proof the
              continuity-checker actually ran on it).
  GENRE BEAT  the chapter contains at least one "[ SYSTEM ]" notification block.

Usage: python3 scripts/check_chapter.py <chapter-number>
Exit code 0 on PASS, 1 on FAIL.
"""
import os
import re
import subprocess
import sys

MIN_WORDS = 3500
MAX_WORDS = 5000

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPTS_DIR)
LINTER = os.path.join(SCRIPTS_DIR, "lint_tells.py")

SECTION_RE = re.compile(r"^s\d+\.md$")          # sNN.md, NOT sNN.notes.md


def section_files(chapter_dir):
    """Return sorted list of section file names (sNN.md), excluding notes/assembled."""
    names = [n for n in os.listdir(chapter_dir) if SECTION_RE.match(n)]
    return sorted(names)


def notes_name(section_name):
    """sNN.md -> sNN.notes.md"""
    return section_name[:-3] + ".notes.md"


def word_count(path):
    with open(path, encoding="utf-8") as fh:
        return len(fh.read().split())


def is_clean(path):
    """True if lint_tells.py reports the file CLEAN (exit 0)."""
    result = subprocess.run(
        [sys.executable, LINTER, path],
        capture_output=True, text=True,
    )
    return result.returncode == 0


def main():
    if len(sys.argv) != 2:
        print("usage: check_chapter.py <chapter-number>")
        return 2
    try:
        chapter = int(sys.argv[1])
    except ValueError:
        print(f"FAIL: chapter number must be an integer, got {sys.argv[1]!r}")
        return 1

    chap_id = f"ch{chapter:02d}"
    chapter_dir = os.path.join(REPO_ROOT, "book", "chapters", chap_id)

    failures = []

    if not os.path.isdir(chapter_dir):
        print(f"Chapter {chapter} ({chap_id})")
        print(f"  FAIL: chapter directory not found: {chapter_dir}")
        print("\nFAIL")
        return 1

    sections = section_files(chapter_dir)

    if not sections:
        print(f"Chapter {chapter} ({chap_id})")
        print(f"  FAIL: no section files (sNN.md) found in {chapter_dir}")
        print("\nFAIL")
        return 1

    # --- LENGTH -----------------------------------------------------------
    total_words = sum(word_count(os.path.join(chapter_dir, s)) for s in sections)
    if total_words < MIN_WORDS:
        failures.append(
            f"LENGTH: total word count {total_words} is below the {MIN_WORDS} minimum")
    elif total_words > MAX_WORDS:
        failures.append(
            f"LENGTH: total word count {total_words} exceeds the {MAX_WORDS} ceiling")

    # --- TELLS ------------------------------------------------------------
    dirty = [s for s in sections if not is_clean(os.path.join(chapter_dir, s))]
    if dirty:
        failures.append(
            "TELLS: lint_tells.py did not return CLEAN on: " + ", ".join(dirty))

    # --- CONTINUITY RAN ---------------------------------------------------
    missing_notes = []
    for s in sections:
        notes_path = os.path.join(chapter_dir, notes_name(s))
        if not os.path.isfile(notes_path) or os.path.getsize(notes_path) == 0 \
                or not open(notes_path, encoding="utf-8").read().strip():
            missing_notes.append(notes_name(s))
    if missing_notes:
        failures.append(
            "CONTINUITY: missing or empty notes (continuity-checker skipped) for: "
            + ", ".join(missing_notes))

    # --- GENRE BEAT -------------------------------------------------------
    has_system_block = False
    for s in sections:
        with open(os.path.join(chapter_dir, s), encoding="utf-8") as fh:
            if "[ SYSTEM ]" in fh.read():
                has_system_block = True
                break
    if not has_system_block:
        failures.append(
            "GENRE BEAT: no '[ SYSTEM ]' notification block found in the chapter")

    # --- Report -----------------------------------------------------------
    print(f"Chapter {chapter} ({chap_id})")
    print(f"  sections: {len(sections)} ({', '.join(sections)})")
    print(f"  total words: {total_words}  (allowed {MIN_WORDS}-{MAX_WORDS})")
    print(f"  tells clean: {len(sections) - len(dirty)}/{len(sections)}")
    print(f"  continuity notes present: {len(sections) - len(missing_notes)}/{len(sections)}")
    print(f"  system notification block present: {'yes' if has_system_block else 'no'}")
    print()

    if failures:
        for reason in failures:
            print(f"  FAIL: {reason}")
        print("\nFAIL")
        return 1

    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
