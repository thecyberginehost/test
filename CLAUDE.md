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
  6. continuity-checker -> book/chapters/chNN/sNN.notes.md   (Ch 14-22: also loads
                           book/SERIES_LORE.md read-only and enforces the SEAL LIST)
  7. editor             -> overwrites sNN.md with edits   (Ch 14-22: also loads
                           book/SERIES_LORE.md read-only; removes any seal leak)
  8. tells-scrubber     -> overwrites sNN.md, clean
  (The writer in step 5 NEVER receives book/SERIES_LORE.md. See "Series-level seal".)

CHAPTER GATE (once per chapter, after its sections are done):
  9. chapter-reconciler -> may adjust the REMAINING outline only
 10. VERIFICATION GATE (deterministic, mandatory): run
        python3 scripts/check_chapter.py <N>
     This is a HARD gate, not a formality. It checks the chapter deterministically
     (length 3,500-5,000 words, every section lints CLEAN, every section has a
     non-empty sNN.notes.md, and the chapter contains a [ SYSTEM ] block) so we do
     NOT rely on the agents self-reporting. You may NOT start the next chapter until
     it prints PASS and exits 0. On FAIL: STOP, show the human the full output and
     the specific failure reasons, and wait. Fix the chapter (re-run the relevant
     loop steps) and re-run the gate. NEVER edit check_chapter.py or loosen its
     thresholds to make a chapter pass; the gate is the standard, not the obstacle.

     SEAL TRIPWIRE (Ch 14-22 only, part of the same HARD gate): for chapters 14
     through 22 the gate ALSO runs
        python3 scripts/check_seal.py <N>
     and it must print SEAL OK and exit 0 before you may move on. It scans the
     drafted section prose (skipping System blocks) for a high-precision list of
     Book Two reveals drawn from the book/SERIES_LORE.md SEAL LIST. A SEAL BREACH
     fails the gate at the SAME severity as a tells-lint failure: STOP, show the
     human the full output, fix the prose (re-run the continuity-checker / editor /
     scrubber), and re-run. NEVER edit or loosen check_seal.py to force a pass; if a
     phrase is a real false positive, make it MORE precise, never delete protection.

FINISH: assemble sections in order -> book/manuscript.md, hand to the human.

## Workspace layout
book/concept.md, book/summary.md, book/outline.md
book/bible.md          (live state, copied from bible.template.md at book start)
book/style.md          (voice + LitRPG format rules, read-only for agents)
book/SERIES_LORE.md    (series-level truth ABOVE Book One's horizon; READ-ONLY
                        guardrail, NOT a content source; see "Series-level seal")
book/chapters/chNN/sNN.md
scripts/lint_tells.py     (deterministic AI-tell linter)
scripts/check_chapter.py  (deterministic per-chapter verification gate; see step 10)
scripts/check_seal.py     (deterministic Book Two seal tripwire for Ch 14-22; see step 10)

## Shared ground truth
- book/bible.md is the single source of truth for characters, System rules,
  timeline, and open threads. The writer updates it after every section. The
  continuity-checker and editor read it and must never contradict it.
- book/style.md defines the voice and the LitRPG formatting. All prose obeys it.

## Series-level seal (book/SERIES_LORE.md)
book/SERIES_LORE.md is series-level truth that sits ABOVE Book One's horizon. It is
the truth Book One must NOT contradict and must NOT reveal. It is a GUARDRAIL, not a
content source. Its SEAL LIST is binding on Ch 14 to Ch 22. The "open questions" at
the bottom belong to the human; leave them open, never resolve them in the pipeline.

WHO LOADS IT (the read-split is deliberate, enforce it exactly):
- The WRITER never receives book/SERIES_LORE.md. The drafting agent pulls prose ONLY
  from book/bible.md, book/outline.md, book/style.md, and the previous section. This
  is how Book Two truth is kept from bleeding into Book One prose through the writer.
- The CONTINUITY-CHECKER and the EDITOR load book/SERIES_LORE.md as a READ-ONLY
  constraint doc for EVERY Ch 14 to Ch 22 section. They use it only to catch and
  remove leaks, never to add lore. For Ch 1 to Ch 13 they do not need it.
- Book One MAY keep the leash ambiguity and the lonely-teacher feeling (Ch 6, Ch 22)
  as feeling, never as structure. Everything on the SEAL LIST stays sealed.

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
