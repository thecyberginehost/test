#!/usr/bin/env python3
"""Deterministic gate for the chapter-splitter agent.

Verifies that a two-part split (a) reconstructs the chapter's prose verbatim,
(b) cuts on a paragraph boundary, (c) lands inside the allowed range, (d) clears
the per-part word floor, (e) does not sever a fenced System block, and (f) is
labelled as two Parts under one chapter number and title. The master manuscript
is the source of truth and is never modified.

Usage: python3 scripts/check_split.py <manuscript.md> <NN> <part1.md> <part2.md>
Exit 0 + "SPLIT OK" on pass. Exit 1 + flags on fail. Exit 2 on usage error.
"""
import re, sys

LO, HI = 0.40, 0.75   # part-1 share of chapter words: allowed cut window
FLOOR  = 800          # minimum words per part

def read(p): return open(p, encoding="utf-8").read()
def nows(s): return re.sub(r"\s+", "", s)
def words(s): return s.split()

def chapter_body(man, nn):
    pat = re.compile(r"^#{1,3}[ \t]+Chapter[ \t]+0*%d\b.*$" % nn, re.I | re.M)
    m = pat.search(man)
    if not m: return None
    start = m.end()
    nxt = re.compile(r"^#{1,3}[ \t]+Chapter[ \t]+\d+\b", re.I | re.M).search(man, start)
    return man[start: nxt.start() if nxt else len(man)].strip("\n")

def strip_header(text):
    lines = text.split("\n"); i = 0
    while i < len(lines) and lines[i].strip() == "": i += 1
    if i < len(lines) and re.match(r"^#{1,3}[ \t]+\S", lines[i]):
        return lines[i], "\n".join(lines[i+1:]).strip("\n")
    return None, text.strip("\n")

def parse_part_header(hdr):
    m = re.match(r"^#{1,3}[ \t]+Chapter[ \t]+0*(\d+)[ \t]*:?[ \t]*(.*?)[ \t]*\(Part[ \t]*(\d+)\)[ \t]*$", hdr or "", re.I)
    return (int(m.group(1)), m.group(2).strip(), int(m.group(3))) if m else None

def main():
    if len(sys.argv) != 5:
        print("usage: check_split.py <manuscript.md> <NN> <part1.md> <part2.md>"); sys.exit(2)
    man, nn = read(sys.argv[1]), int(sys.argv[2])
    h1, b1 = strip_header(read(sys.argv[3]))
    h2, b2 = strip_header(read(sys.argv[4]))
    flags = []

    body = chapter_body(man, nn)
    if body is None:
        print(f"FAIL: Chapter {nn} not found in manuscript"); sys.exit(1)

    # 1. integrity: prose unchanged, in order, nothing added or dropped
    if nows(b1) + nows(b2) != nows(body):
        flags.append("INTEGRITY: parts do not reconstruct the chapter verbatim (prose altered, reordered, or dropped)")
    else:
        # 2. paragraph boundary: a blank line sits at the seam in the original
        target, cnt, idx = len(nows(b1)), 0, 0
        for idx, ch in enumerate(body):
            if not ch.isspace(): cnt += 1
            if cnt == target: break
        gap = re.match(r"\s*", body[idx+1:]).group(0)
        if gap.count("\n") < 2:
            flags.append("BOUNDARY: cut is not on a paragraph break")

    # 3. fenced System block not severed
    if b1.count("```") % 2 != 0:
        flags.append("BLOCK: cut falls inside a fenced block (unbalanced ``` in part 1)")

    # 4. range + 5. floor (by word count)
    w1, w2 = len(words(b1)), len(words(b2)); wt = w1 + w2
    if wt == 0:
        flags.append("EMPTY: no body text")
    else:
        frac = w1 / wt
        if not (LO <= frac <= HI):
            flags.append(f"RANGE: part-1 share {frac:.2f} outside [{LO:.2f},{HI:.2f}] (re-cut or flag chapter)")
    if w1 < FLOOR: flags.append(f"FLOOR: part 1 only {w1} words (<{FLOOR})")
    if w2 < FLOOR: flags.append(f"FLOOR: part 2 only {w2} words (<{FLOOR})")

    # 6. labels: two Parts, one chapter number, one title
    pp1, pp2 = parse_part_header(h1), parse_part_header(h2)
    if not pp1: flags.append("LABEL: part 1 header is not '## Chapter N: Title (Part 1)'")
    if not pp2: flags.append("LABEL: part 2 header is not '## Chapter N: Title (Part 2)'")
    if pp1 and pp2:
        if (pp1[2], pp2[2]) != (1, 2): flags.append("LABEL: parts must be (Part 1) then (Part 2)")
        if pp1[0] != nn or pp2[0] != nn: flags.append(f"LABEL: chapter number must be {nn} on both parts")
        if pp1[1] != pp2[1]: flags.append("LABEL: the two parts carry different titles")

    if flags:
        for f in flags: print("  " + f)
        print(f"\n{len(flags)} problem(s). FAIL."); sys.exit(1)
    print(f"SPLIT OK  ch{nn}  p1={w1}w  p2={w2}w  cut={w1/wt:.0%}"); sys.exit(0)

if __name__ == "__main__":
    main()
