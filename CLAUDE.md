# Kade Zero: System Apocalypse LitRPG Book Factory

Autonomous pipeline that writes prose LitRPG novels in the System Apocalypse
subgenre, published under the AI author persona **Kade Zero**.
The AI authorship is public and part of the brand.

## Series premise
The world is "System-ified" overnight: stats, levels, a deadly game laid over
reality. The protagonist gains a unique class that lets them interface with the
System directly, and discovers the System is not a neutral engine but a vast
administrator AI running humanity as an experiment, and it is learning.
Progression means leveling up AND learning to read and negotiate with that AI.
Power-fantasy first, philosophy second. Readers came for the climb.

## How this pipeline runs (orchestration)
You (the main session) are the orchestrator. Drive the phases in order and invoke
the subagent for each phase. Agents do not call each other. They read and write
files in the workspace, and you pass control between them.

BOOK-LEVEL PASS (run once per book):
  1. idea-agent         -> book/concept.md
  2. book-strategist    -> book/summary.md
  3. book-architect     -> book/outline.md   (chapters + per-chapter summaries)
  4. chapter-architect  -> book/outline.md   (adds ~10 section specs per chapter)

SECTION LOOP (per chapter, repeat for each of ~10 sections):
  5. writer             -> book/chapters/chNN/sNN.md   (updates book/bible.md)
  6. continuity-checker -> book/chapters/chNN/sNN.notes.md
  7. editor             -> overwrites sNN.md with edits
  8. tells-scrubber     -> overwrites sNN.md, clean

CHAPTER GATE (once per chapter, after its sections are done):
  9. chapter-reconciler -> may adjust the REMAINING outline only

FINISH: assemble sections in order -> book/manuscript.md, hand to the human.

## Workspace layout
book/concept.md, book/summary.md, book/outline.md
book/bible.md          (live state, copied from bible.template.md at book start)
book/style.md          (voice + LitRPG format rules, read-only for agents)
book/chapters/chNN/sNN.md
scripts/lint_tells.py  (deterministic AI-tell linter)

## Shared ground truth
- book/bible.md is the single source of truth for characters, System rules,
  timeline, and open threads. The writer updates it after every section. The
  continuity-checker and editor read it and must never contradict it.
- book/style.md defines the voice and the LitRPG formatting. All prose obeys it.

## Voice rules (every prose agent obeys)
- No em dashes. Ever. Use periods, commas, or parentheses.
- No AI-tell vocabulary or cadence (see scripts/lint_tells.py for the banned list).
- Avoid rule-of-three constructions and uniform sentence length.
- Show, do not summarize. Keep System notifications crisp and consistently formatted.

## Models
All agents are set to `opus` for book one so you can measure usage on a full run.
After book one, the natural tiers are: orchestration and scrubber -> haiku or
pure script, architects and continuity -> sonnet, writer and editor and
strategist -> opus. Downshift then if the budget calls for it.
