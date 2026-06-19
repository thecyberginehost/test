#!/usr/bin/env python3
"""Deterministic AI-tell linter. Flags em dashes, banned vocabulary, and
rule-of-three cadence so the scrubber can clean them.
Usage: python3 scripts/lint_tells.py <file.md>"""
import re, sys

BANNED = [
    "delve", "tapestry", "testament to", "navigate the", "underscore",
    "moreover", "furthermore", "in the realm of", "it's worth noting",
    "a myriad of", "boasts", "seamless", "robust", "leverage", "utilize",
    "in conclusion", "that being said", "needless to say", "ever-evolving",
    "stark reminder", "rich tapestry", "plays a vital role", "a beacon of",
    "it is important to note", "when it comes to", "nestled", "whimsical",
]
NOT_ONLY = re.compile(r"\bnot only\b.{0,60}?\bbut\b", re.I)
ISNT_JUST = re.compile(r"\b(isn't|is not|wasn't|was not)\s+just\b.{0,60}?\bit('s| is)\b", re.I)
RULE_OF_THREE = re.compile(r"\b[\w'-]+, [\w'-]+,? and [\w'-]+\b")

def check(path):
    text = open(path, encoding="utf-8").read()
    flags = []
    for m in re.finditer(r"[\u2014\u2013]", text):
        flags.append((m.start(), "EM/EN DASH"))
    low = text.lower()
    for w in BANNED:
        start = 0
        while True:
            i = low.find(w, start)
            if i == -1:
                break
            flags.append((i, f"BANNED: {w}"))
            start = i + len(w)
    for m in NOT_ONLY.finditer(text):
        flags.append((m.start(), "CADENCE: not only ... but"))
    for m in ISNT_JUST.finditer(text):
        flags.append((m.start(), "CADENCE: isn't just ... it's"))
    for m in RULE_OF_THREE.finditer(text):
        flags.append((m.start(), "RULE-OF-THREE?: " + m.group(0)))
    return flags

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: lint_tells.py <file>"); sys.exit(2)
    flags = check(sys.argv[1])
    if not flags:
        print("CLEAN"); sys.exit(0)
    for pos, msg in sorted(flags):
        print(f"  pos {pos}: {msg}")
    print(f"\n{len(flags)} flag(s). Scrub and re-run.")
    sys.exit(1)
