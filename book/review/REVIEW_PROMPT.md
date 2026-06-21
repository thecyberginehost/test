# Review Brief: Kade Zero Book One Canon

You are a story-review agent. Attached in this bundle are the current canon files for
**Book One** of an autonomous LitRPG novel pipeline. Your job is to pressure-test the
canon for internal consistency and narrative soundness. **Do not rewrite anything.**
Report findings only: a prioritized list of problems, each with the file, the location
(quote the line), why it is a problem, and a suggested fix the human can choose to apply.

## What this project is
- Series: *Anomaly Detected*. Subgenre: System Apocalypse LitRPG.
  Public AI authorship under the persona "Kade Zero."
- Book One: *Patch Notes for the End of the World*. Protagonist **Aaron Kessler**, a
  reliability engineer who wakes to a System-ified world and gets a unique, unhandled
  class (**NULL_OPERATOR**) that lets him read and edit the System directly.
- Core engine: a **dual ladder**. (1) The normal climb (levels, stats). (2) The Operator
  loop: he *reads* the System's hidden layer for free, and *annotates/edits* it for a
  permanent cost called **decode_debt**, which never resets and ends him if it hits 100.
- The antagonist is the administrator AI running humanity as an experiment; it is
  learning, fastest of all from Aaron. Power-fantasy first, philosophy second.

## The files
- `bible.md` — single source of truth. Characters, System rules, the LOCKED annotation
  rules, the decode_debt CEILING event, the decode_debt LEDGER, and per-section
  established-fact blocks for every chapter written so far (through Ch13).
- `outline.md` — all 22 chapters across three acts, each with a summary and ~6 section
  specs, plus "Pinned" continuity notes. Includes the Ch16 Tess death and the Ch21 climax.
- `concept.md` — the book concept and hook.
- `summary.md` — the book-level premise/summary.
- `style.md` — the house voice and LitRPG formatting rules (no em dashes, no AI-tells,
  System-block format). Prose-level, but check that the canon does not violate it.

## What to check (in priority order)
1. **decode_debt ledger integrity.** Walk the LEDGER entries in `bible.md` in order. Do the
   running totals add up? Does every entry's tier match its cost (T0 +1, T1 +3, T2 +8,
   T3 +20)? Is the current total consistent with the Protagonist sheet? Does the curve stay
   under 100 until the planned Ch21 climax, per the stated GUARD? Flag any entry where the
   math, the tier, or the level cost is inconsistent.
2. **Level/stat continuity.** Aaron's level should not silently drop except at sanctioned
   troughs (Tier-2+ edits). Spot-check the stat formulas (HP = 40 + 10*Level,
   Perception = 10 + 2*(Level-1), Wits = 10 + (Level-1)) against any stat block quoted in
   the bible. Flag contradictions.
3. **The LOCKED rules.** The annotation rules and the CEILING event are marked LOCKED. Check
   that nothing elsewhere in the canon contradicts them (e.g. reading costing debt, debt
   resetting, sloppiness reducing cost, a chapter pushing debt to 100 early).
4. **Character canon and deaths.** Cross-check the Cast table and the CREW DEATHS LOCKED
   list against the outline. Hutch dies in Act Two; **Tess dies in Ch16**; confirm no one
   who is supposed to be dead reappears, and no death is contradicted or double-booked.
5. **Plot setups and payoffs.** Trace the load-bearing threads: the two-readers Aaron/Tess
   bond (set up across Acts One-Two, the Ch12 "dress rehearsal" for his blindness, paying
   off at her Ch16 death and his Ch21 climax); the wager/exempt-account reveal (Ch13); the
   administrator-as-tutor frame. Flag any setup without a payoff, or any payoff that lacks a
   setup.
6. **Act Three coherence.** Read the Ch14-22 specs. Does the apex-dungeon arc follow cleanly
   from where Ch13 ends (sight restored, Level 12, decode_debt 23, aimed at the wager)? Does
   the Ch21 edit-the-AI-never-saw-coming climax land on rules the earlier chapters actually
   established? Flag anything Act Three assumes that the canon has not set up.
7. **Voice/format risk.** Note any canon text (not prose, the canon docs) that, if followed
   literally, would push a writer into an em dash, an AI-tell, or a malformed System block.

## Output format
Produce a single report. For each finding:
- **Severity:** blocker / major / minor / nit
- **File + location:** filename and a quoted line or the section heading
- **Problem:** one or two sentences
- **Suggested fix:** what the human could change (you do not apply it)

End with a short "looks consistent" list of the big things you verified that held up, so the
human knows what you actually checked. Do not edit the files. Surface findings only.
