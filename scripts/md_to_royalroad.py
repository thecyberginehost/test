#!/usr/bin/env python3
"""Convert book/manuscript.md into Royal-Road-ready per-chapter HTML.

Royal Road has no bulk upload: each chapter is pasted into the web editor's
"View Source" (<>) HTML view. This emits one body-only HTML file per chapter
(no title line; that goes in RR's Title field), with:
  - System notification boxes (runs of '> ' lines) -> a single <blockquote> with <br>
  - paragraphs -> <p>
  - *italics* -> <em>
"""
import re, os, glob, html

SRC = "book/manuscript.md"
OUT = "book/export/royalroad"

def esc(s):
    # Escape HTML special chars, then restore intended emphasis markup.
    return html.escape(s, quote=False)

def italics(s):
    # *text* -> <em>text</em>  (non-greedy, single-line spans)
    return re.sub(r"\*([^*\n]+)\*", r"<em>\1</em>", s)

def inline(s):
    return italics(esc(s))

def is_indent(s):
    # System blocks in early chapters are 4-space (or tab) indented; the manuscript
    # never indents ordinary prose, so an indented run is always a System box.
    return s.startswith("    ") or s.startswith("\t")

def emit_box(box):
    # trim trailing empty spacer lines, then wrap as one blockquote with <br> breaks
    while box and box[-1] == "":
        box.pop()
    return "<blockquote>\n" + "<br>\n".join(box) + "\n</blockquote>"

def render_chapter(body_lines):
    """body_lines: list of raw md lines for one chapter (header already removed)."""
    html_parts = []
    i = 0
    n = len(body_lines)
    while i < n:
        line = body_lines[i]

        # System box form A: a run of '> ' (or bare '>') blockquote lines.
        if line.startswith(">"):
            box = []
            while i < n and body_lines[i].startswith(">"):
                inner = re.sub(r"^>\s?", "", body_lines[i])
                box.append(inline(inner) if inner.strip() != "" else "")
                i += 1
            html_parts.append(emit_box(box))
            continue

        # System box form B: a run of 4-space/tab indented lines, keeping the internal
        # blank spacer lines (only while a later indented line continues the block).
        if is_indent(line):
            box = []
            while i < n:
                cur = body_lines[i]
                if is_indent(cur):
                    inner = re.sub(r"^(    |\t)", "", cur)
                    box.append(inline(inner) if inner.strip() != "" else "")
                    i += 1
                elif cur.strip() == "":
                    j = i + 1
                    while j < n and body_lines[j].strip() == "":
                        j += 1
                    if j < n and is_indent(body_lines[j]):
                        box.append("")   # internal spacer line
                        i += 1
                    else:
                        break            # blank line separates the box from prose
                else:
                    break
            html_parts.append(emit_box(box))
            continue

        if line.strip() == "":
            i += 1
            continue

        # Normal paragraph (one physical line == one paragraph in this manuscript)
        html_parts.append("<p>" + inline(line.rstrip()) + "</p>")
        i += 1
    return "\n\n".join(html_parts) + "\n"

def main():
    os.makedirs(OUT, exist_ok=True)
    with open(SRC) as f:
        text = f.read()
    lines = text.split("\n")

    chapters = []   # (num, title, [body lines])
    cur = None
    hdr = re.compile(r"^## Chapter (\d+):\s*(.+?)\s*$")
    for ln in lines:
        m = hdr.match(ln)
        if m:
            if cur:
                chapters.append(cur)
            cur = [int(m.group(1)), m.group(2), []]
            continue
        if cur is None:
            continue          # skip the top title block / '---'
        cur[2].append(ln)
    if cur:
        chapters.append(cur)

    titles = []
    for num, title, body in chapters:
        # trim leading/trailing blank lines
        while body and body[0].strip() == "":
            body.pop(0)
        while body and body[-1].strip() == "":
            body.pop()
        out_html = render_chapter(body)
        fn = os.path.join(OUT, f"ch{num:02d}.html")
        with open(fn, "w") as f:
            f.write(out_html)
        titles.append((num, title))

    with open(os.path.join(OUT, "TITLES.txt"), "w") as f:
        f.write("Royal Road chapter titles (paste into the Title field; body HTML is the matching chXX.html)\n\n")
        for num, title in titles:
            f.write(f"ch{num:02d}.html   ->   Chapter {num}: {title}\n")

    readme = """HOW TO POST THESE ON ROYAL ROAD
================================

Royal Road has no bulk/file upload. You create each chapter and paste its body in.
These files are the chapter BODY only (the title is separate, see TITLES.txt).

For each chapter (ch01.html ... ch22.html):
  1. On your fiction's page, click "+ New Chapter".
  2. Title field: copy the matching line from TITLES.txt (e.g. "Chapter 1: Working As Intended").
  3. In the Chapter Content editor, click the "View Source" button on the toolbar
     (the < > icon, far right).
  4. Open chXX.html in a text editor, copy ALL of it, and paste into the View Source box.
  5. Click "Ok"/close source view, then Preview to check, then Publish (or Save Draft).

Notes:
  - The System notification panels are <blockquote> blocks. They render as RR's quote
    style and read cleanly on mobile.
  - Italics are real <em> tags (no stray asterisks).
  - Alternative to View Source: paste the rendered text with RR's "Enable Clean Paste"
    toggle ON (between the author-note and content boxes) -- but then each System box
    needs the quote button applied manually, so View Source is recommended for this book.
  - No images or horizontal rules are included; formatting is intentionally minimal/clean.
"""
    with open(os.path.join(OUT, "README.txt"), "w") as f:
        f.write(readme)

    print(f"Wrote {len(titles)} chapter HTML files + TITLES.txt + README.txt to {OUT}/")

if __name__ == "__main__":
    main()
