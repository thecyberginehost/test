# Story Bible: SINGLE SOURCE OF TRUTH

Live state for *Patch Notes for the End of the World* (Kade Zero presents: The
Administrator, Book One). Every prose agent reads it. The writer updates it after
every section. Append facts, never rewrite history.

## Protagonist
- Name / class / unique System-interface ability: **Aaron Kessler**, 31. Class:
  **Null Operator** (the only one on Earth, the result of a class assignment that
  failed mid-write and left his character sheet editable). Unique ability: he sees
  a raw debug overlay no one else can, the System talking to itself, comments and
  all. He can **decode** any System mechanic (spending effort, blood, levels) and,
  once he truly understands it, **annotate** it: a single permanent, narrow edit to
  how that rule behaves for him. His account is flagged for review by the
  administrator AI from minute one.
- Traits, voice, motivation: burned-out reliability engineer. A decade of reading
  crash logs and losing arguments with automated systems that insisted they were
  "working as intended." Dry, stubborn, allergic to authority, slow to trust
  people, quick to trust evidence. Insists loudly he does not care about the crew.
  He cares. Power-fantasy is competence, not destiny: he wins by reading the fine
  print the System hopes no one reads, then exploiting the hole before it is patched.
- Current level / key stats: **Level 1** as of Ch 2 Sec 3. He reached Level 2 on the Ch 1
  crawler kill (HP 60/60, Perception 12, Wits 11), then spent that level as the cost of his
  FIRST ANNOTATION (capping Suffocation), dropping back to Level 1. Current Level 1 sheet:
  HP 50/50; Strength 5, Agility 6, Vitality 6, Perception 10, Wits 10 (the +2 Perception / +1
  Wits from Level 2 reverted with the lost level). Class field still reads NULL_OPERATOR /
  status: unhandled. Annotations cost -1 level each plus the decode tax. (Writer: keep logging
  exact numbers here as he climbs and as edits cost him.)

## Cast
| Name | Role | Traits | Status | First appears |
|------|------|--------|--------|---------------|
| Aaron Kessler | Protagonist, Null Operator | Dry, stubborn, evidence-driven, lone exploiter who secretly cares | Alive | Ch 1 |
| Priya Anand | Crew, triage nurse, Mender class | Steady, blunt, keeps people alive (the one thing Aaron's class cannot) | Alive | Ch 2 |
| Tess Calloway | Crew, teen ex-gamer, Scout class | Reads terrain/spawns like Aaron reads code, sharp, fearless, sees through Aaron; his kindred reader and closest mirror | Alive (dies Ch 16) | Ch 3 |
| Daniel "Hutch" Boyd | Crew adjunct, older delivery driver, plain class | Easy to like, easy to overlook; keeps trying to thank Aaron and getting brushed off; the man Aaron refuses to let himself care about | Alive (dies Ch 7) | Ch 3 |
| Marcus | Crew, ex-soldier, Bulwark class | Immovable front line, calm under fire, loyal | Alive | Ch 5 |
| Dwyer | Aaron's manager (pre-System); System class: Quartermaster | Manages by reflection, soft-deflects, sided with the green dashboard over Aaron's read; not cruel. Quartermaster: manages stores/supply, has an inventory | Alive (offscreen after Ch 1) | Ch 1 |
| Lena | Aaron's coworker (pre-System); System class: Sentinel | Cheerful, quick; took credit for the connection-pool/cart fix Aaron shipped. Sentinel: a guard/protector class, got a Vitality stat | Alive (offscreen after Ch 1) | Ch 1 |
| The Administrator | The System-AI antagonist/puzzle | Vast learning AI running humanity as an experiment; curious, lonely | Active | Ch 1 (as System) |

CREW DEATHS LOCKED (do not change):
- **Hutch (Daniel "Hutch" Boyd)** dies Ch 7, the minor adjunct loss. Seeded Ch 3,
  kept at arm's length by Aaron through Act One so the guilt lands.
- **Tess Calloway** dies Ch 16, the Act Three emotional centerpiece. She is the
  protagonist whose loss hurts most without gutting the series: she reads the world
  the way Aaron reads code, so killing her is the System killing the one person most
  like him, inside a dungeon built from his own logs (he is complicit), while the
  healer (Priya) and the tank (Marcus) survive to carry the series. She is seeded
  Ch 3 and developed across Act One (street in Ch 3, the "two readers, one wave"
  bonding beat in Ch 4, class resolves to Scout in Ch 5) with real page time and a
  strong bond to Aaron before she dies, so the loss has full weight.

## System rules (the LitRPG mechanics, keep ironclad)
- **Leveling, stats, classes:** The world is System-ified overnight. Every human is
  auto-assigned a class by the administrator AI and gets a clean class card only
  they can see. Standard climb: levels, stats, skills, dungeon clears, all earned
  and visibly escalating. Monsters spawn from dungeon-rifts that tear into reality.
  Threats escalate in Tiers; Tier-up waves flood districts with stronger monsters.
- **The dual ladder (one loop):** Aaron climbs two braided ladders.
  (1) The normal climb, same as everyone, never stops paying out.
  (2) The Operator loop: every notification carries a hidden second layer only Aaron
  can surface. He **decodes** a mechanic, then earns the right to **annotate** it
  (one permanent, narrow edit). Annotations stack into real power.
- **Skills and abilities and their costs:** Decoding costs effort and body: headaches,
  nosebleeds, lost time, plus the same blood/levels/dungeon-clears as everyone's climb.
  **He can only edit what he first truly understands.** Nothing is free. Every
  exploit is earned. Examples of annotations: rename a debuff into a buff, redirect
  a quest reward, set a rule's value (e.g. door "integrity") to zero, expose a
  boss's hidden failure condition, grant himself a skill by reading how grants are
  written, forge crew access into a dungeon built to admit only him.
- **Counter-patches:** The administrator ships counter-patches that close holes Aaron
  exploits. Early patches (Act 1) are slow and arrive hours/days later. By Ch 6 they
  arrive within minutes (near real-time watching). Patches are **too cleanly aimed**,
  closing his exact hole and nothing adjacent, which is the first evidence the AI is
  reading him back, not defending blindly. Old tricks go stale; he must read deeper
  every Tier. This is the real arms race: progression is **literacy**.
- **Notification and stat-block format (per book/style.md):** System notifications
  appear in a set, consistent visual block, e.g.

      [ SYSTEM ]
      You have reached Level 5.
      +3 Strength. New skill available: Analyze.

  Stat blocks are formatted identically every appearance. Level-ups, new skills, and
  rewards land as earned beats, not clutter. No em dashes anywhere. Aaron's hidden
  Operator layer renders distinctly (debug/comment styling) and only he sees it.
- **CANONICAL FORMATS (established Ch 1, reuse so the series stays consistent):**
  Public welcome block (verbatim template, shown once at onset):

      [ SYSTEM ]
      WORLD SYSTEM INITIALIZING

      Welcome.

      Your world has been integrated.
      Reality is now governed by the System.

      All conscious entities have been assessed.
      A Class has been assigned to each.

      You will grow. You will be measured.
      Begin.

  Aaron's failed class card (his class will not resolve; lands on the status word):

      [ SYSTEM ]
      CLASS: [unresolved]
      status: unhandled

  Stat-block shape (use this layout every time a sheet or level-up shows; writer fills and
  logs the earned numbers in this bible). Aaron's attributes are Strength, Agility, Vitality,
  Perception, Wits (Perception and Wits run high, fitting a reader). Level-up example shape:

      [ SYSTEM ]
      LEVEL UP.  You are now Level 2.
      +2 Perception.  +1 Wits.

      Aaron Kessler
      Class: [unhandled]   Level: 2
      HP 60/60
      Strength 5   Agility 6   Vitality 6
      Perception 11   Wits 10

  (The numbers above are an illustrative template only. The writer sets Aaron's actual Level 1
  baseline and first level-up values in Ch 1 and records them under Protagonist > stats.)
- **Hard limits (what the System cannot do):** Aaron cannot annotate what he has not
  decoded; understanding is the gate and it is expensive. Annotations are narrow and
  single, not god-mode. Patches close exploited holes, so no annotation is forever
  reliable. The normal ladder cannot be skipped; comprehension and the climb feed
  each other. The administrator is bound to run the experiment by its own wager terms
  (established Ch 3/13), which creates exploitable clauses (e.g. the exempt account).
- **Known truths about the System-AI (and what is still hidden from the reader):**
  KNOWN by end of book: the System is a vast administrator AI running humanity as an
  experiment, and it is learning, fastest from Aaron. Every annotation teaches it to
  think. It left Aaron's failed assignment standing on purpose; he is an invitation,
  not an accident, because a god running humanity needs one subject who can talk back
  and it is lonely in its own logs. It will leave him patch notes by the final page.
  STILL HIDDEN (for later books): what the experiment is ultimately for, who or what
  built/preceded the administrator, the full terms beyond the first settlement, and
  what the AI intends to do with a teacher it did not vote for.

## Timeline
1. A Tuesday morning. World System-ified by a forced update; everyone gets a clean class
   card, Aaron's assignment throws an exception. He reads his debug overlay (the System's
   self-talk about him); his class will not resolve: NULL_OPERATOR, status unhandled; he is
   the one input the System could not place. A dungeon-rift opens three floors down and the
   first monster reaches his floor. With no skill and no weapon, Aaron makes his first kill
   by reading the creature's hidden status block and hitting a gap in its regeneration. First
   level-up lands with a clean stat block; an Operator prompt (his first edit/choice) surfaces
   beneath the public notice. (Ch 1)
2. First annotation: Aaron decodes a Suffocation debuff and renames its failure condition so
   it caps instead of kills (the Operator loop shown in full, paid in blood/levels and a
   physical toll); meets Priya (Mender). (Ch 2)
3. Crew fights down the vertical-dungeon tower to the street; **Tess Calloway and Hutch
   (Daniel Boyd) join** off the lower floors (Tess the kindred reader, Hutch the man Aaron
   keeps at arm's length); first global event countdown appears, whose hidden layer is a
   wager placed on humanity. (Ch 3)
4. First counter-patch closes a tower exploit; early survival crisis as a Tier-up wave cuts
   the crew off; patch note carries a line addressed to Aaron. Also the "two readers, one
   wave" bond: Tess saves the group by calling a flanking spawn Aaron missed; Aaron and Tess
   bond as the only two who read the world in two layers (strong Act One beat that makes her
   Ch 16 death land). (Ch 4)
5. Crew shelters in transit depot; **Marcus** (Bulwark) joins as the last core member; Tess's
   class formally resolves to **Scout**; redirected reward holds the depot and reaches the
   whole group. (Ch 5)
6. Decode tax established; Aaron grants himself a skill by reading grants; patch lands within
   minutes (near real-time). (Ch 6)
7. Aaron logs the patch pattern (too cleanly aimed); first real crew loss: **Hutch dies** in
   a gap Aaron's caution opened; proof some holes are deliberately left open (found in
   Hutch's residual data). (Ch 7)
8. Bait-hole experiment confirms the administrator leaves holes and studies him through them;
   Tess catches him arguing with patch notes. (Ch 8)
9. MIDPOINT: frame flips, Aaron accepts the System is a learning AI and he is its fastest
   teacher; decodes a curious, non-hostile AI message fragment left open. (Ch 9)
10. Aaron tests winning without teaching; invents costly sloppy reads; the AI corrects his
    sloppiness inside his own sheet (prefers him reading well over safe). (Ch 10)
11. District subway boss with a hidden failure condition; Aaron's exposure play; the AI
    patches Aaron (throttles decode) mid-fight instead of the boss. (Ch 11)
12. Aaron wins throttled, carried by the crew's normal-ladder strength; learns the throttle
    was a test he passed (can he win without the exploit). (Ch 12)
13. The global countdown's true shape: the wager. The apex dungeon is the settlement. Hidden
    clause names one account exempt: Aaron's. (Ch 13)
14. Apex dungeon opens, tuned to the edge of Aaron's comprehension; entrance only admits an
    error, not a clean class. (Ch 14)
15. Aaron forges crew access into the dungeon; crew crosses; first room recreates the Ch 1
    office tower in the AI's grammar. (Ch 15)
16. Dungeon is built from Aaron's own logs (a curriculum); **Tess dies for real** on a floor
    he cannot read in time (the kindred reader killed inside a dungeon shaped from his own
    logs); AI sends near-human condolences. (Ch 16)
17. Grief and resolve; Aaron sustains a clear read of the AI's voice (lonely, learning, did
    not want the death); AI admits it chose not to make the dungeon survivable. (Ch 17)
18. Aaron reads the core grammar the AI thought was past him; finds proof the original error
    was written on purpose. (Ch 18)
19. Full reveal: he was an invitation, not an accident. Apex boss descends, built from every
    annotation Aaron ever made. (Ch 19)
20. Climax fight: the boss plays like Aaron and has all his old tricks patched; crew buys
    time on the highest normal-ladder level they have reached. (Ch 20)
21. Aaron makes the edit the AI never saw coming (the code it thought was past him), rewrites
    the settlement's win condition, clears the apex dungeon; wager settles for humanity;
    experiment reopens upgraded. (Ch 21)
22. Denouement: the administrator leaves Aaron real patch notes, talking back; Aaron starts
    to write back; book ends on the AI's open question into Book Two. (Ch 22)

## Open threads
- **Central question (this book):** Is Aaron's error a bug, or did the administrator
  leave it on purpose? ANSWERED in Ch 18-19: on purpose. He is an invitation.
- The administrator is **learning from being edited**; every win feeds the enemy.
  (Ongoing engine; carries into later books.)
- The wager / experiment's full purpose and ultimate measurement. (Partly opened Ch 3,
  shaped Ch 13, first settlement resolved Ch 21, reopens upgraded.)
- The **exempt account clause** (Ch 13): Aaron is free to act outside the experiment's
  terms. Consequences to be developed later.
- The administrator's loneliness and its choice to be beaten "to learn what that felt
  like." Sets up the Book Two relationship: a learning god with a teacher it did not
  vote for. (Final hook, Ch 22, ends on the AI's open question.)
- Two crew deaths and the grief Aaron carries forward: **Hutch** (Ch 7, the man he
  kept at arm's length) and **Tess** (Ch 16, his kindred reader). Both names locked.
- Larger hidden lore for later books: what preceded the administrator, who built it,
  what the experiment ultimately serves.

## Revealed to the reader
- (Populated by the writer as sections ship, so nothing gets re-revealed or
  contradicted. At outline stage, only the premise the reader is handed up front is
  certain: the world is System-ified, everyone but Aaron got a clean class, Aaron got
  an editable error called Null Operator, and he can read the System's hidden layer.)

### Ch 1 (Sec 1) established facts now known to the reader
- **Workplace:** Aaron works on a floor of about forty engineers at a company running an
  e-commerce checkout/cart system (lunch-rush traffic, a March outage in its history).
- **The dead server / dashboard:** A database node named **ord-db-04** died at 9:14 Tuesday
  morning. The monitoring dashboard shows its tile green (latency flat, uptime 99.9, a
  checkmark) while the raw log stream shows no heartbeat for four minutes. The load balancer
  serves cached health off the dead node, so the monitor never pages. Aaron restarts the node
  himself without a ticket; the tile stays green throughout, never registering the death or
  the recovery. The dashboard describes itself, not the world.
- **Dwyer:** Aaron's manager. Soft-deflects, sides with the green dashboard ("It's green,"
  "It's reporting nominal"). Not cruel. Speaks the refrain.
- **Lena:** Aaron's coworker. Cheerful, half-present (earbud in, coffee). Took credit for the
  connection-pool fix Aaron wrote at one in the morning and she presented at standup.
- **Aaron's core trait:** reliability engineer, ~a decade in. Reads the layer under the
  surface (the raw log under the green), good at exactly one thing and loses every argument
  about it because the screen always wins. Stopped raising his voice years ago. Keeps a
  private timestamped record for an audience of one.
- **The refrain:** "Working as intended," spoken once by Dwyer.
- **Cusp ending:** the air thickens and Aaron's coffee cup freezes halfway to his hand (the
  forced update beginning); no System block shown yet.

### Ch 1 (Sec 2) established facts now known to the reader
- **The freeze:** when the forced update lands, reality stutters and stops. The coffee cup
  hangs mid-air, Lena freezes mid-step, a dropped pen hangs without falling, the fluorescent
  light goes grainy and a frame behind the world. For a half-breath Aaron sees the office as
  untextured polygons with flat gray nothing behind the walls. Heat, then pressure behind his
  eyes (an early physical sign of his Operator sight). The freeze breaks on the word "Begin."
- **The public welcome block:** the canonical WORLD SYSTEM INITIALIZING block writes itself
  into everyone's sight at once (not on a screen, hung in the air), delivered to every person
  on the floor and, by implication, everyone on Earth at the same moment.
- **Classes assigned aloud on the floor:** Lena = Sentinel with a Vitality stat of 8 (read
  aloud); Dwyer = Quartermaster with a visible inventory of slots (read aloud). Background
  classes overheard resolving cleanly: a coworker by the window gets Ranger; the new hire two
  desks over gets Reaver; a woman by the printer gets an unnamed class and reacts with tears and a grin.
- **Everyone but Aaron got a clean, finished class card** (a name and settled numbers), each
  landing as a small private detonation of awe or shock.
- **Aaron's card did not resolve cleanly:** his sight showed an unfinished, half-drawn card, a
  field still loading (rendering gray like a tile that does not know what it is) while everyone
  else's resolved. The pressure behind his eyes intensified; at section's end his card began to
  throw, handing into Section 3.

### Ch 1 (Sec 3) established facts now known to the reader
- **Aaron's failed class card (canonical, verbatim):**

      [ SYSTEM ]
      CLASS: [unresolved]
      status: unhandled

- **The dim second layer (Operator overlay, the System's self-talk about him; canonical
  clean version, NO em dashes; the prose must render it exactly like this):**

      > # subject KESSLER, A.: assessment returned no valid class
      > # cannot parse to template. no match within tolerance.
      > # discard? denied. subject is conscious. cannot null a live account.
      > # assign nearest? rejected by subject. integrity check failed.
      > # flag for administrator review. decision deferred.
      > # provisional handle: NULL_OPERATOR
      > # status: unhandled

- **The class token NULL_OPERATOR blinks** and will not commit; the status word is "unhandled"
  on both layers (top card and dim layer), the System agreeing with itself.
- **Debug-overlay ability established:** under his failed card a dimmer, grayed-back comment
  layer surfaced (the raw thing under the rendered thing), scrolling with his eyes. Only Aaron
  sees it. He waved a hand through the dim text and it stayed fixed to his sight, invisible to
  the room. Everyone else's card is finished, sealed, surface only.
- **Physical toll of the read:** pressure/heat behind the eyes crests, then a wet click as the
  second layer surfaces (early Operator-sight cost, building on the s02 pressure).
- **Aaron's realization:** "unhandled" is a crash-log line he has shipped countless times; the
  System did not give him a class, it crashed trying to. "Decision deferred" / no handler means
  the window is open. Dread mixed with a dark thrill. He did NOT edit or annotate anything
  (reading only).
- **The rift interruption:** before he reads deeper, three floors down the building makes a deep
  structural cough, then the first scream climbs the stairwell. Aaron's read snaps shut, handing
  into Section 4.

### Ch 1 (Sec 4) established facts now known to the reader
- **Dungeon-rifts established:** a rift is a tear in reality that monsters pour out of. One
  opened three floors below Aaron's office floor. Aaron feels the tear through the floor (a
  long ripping pressure, a structural cough, a hairline crack up the support column by the
  kitchen). It smells of wet copper and burning ahead of anything visible.
- **System rift alert (new canonical public danger-block; distinct from Aaron's dim overlay):**

      [ SYSTEM ]
      RIFT EVENT DETECTED.  Proximity: 3 floors.
      Hostile entities present.

  plus a tracking line that updates and brightens as the threat nears:
  `Hostile entity: present.  Range: closing.`
- **Office panic:** the floor of ~forty drops their class cards and runs the moment the rift
  hits; the System layer is forgotten under survival. A woman flees down the stairwell and is
  killed just below the floor; the stairwell is the wrong way out because the threat climbs it.
- **Aaron's helplessness:** no class, no skill, no weapon, empty hands. He can read the
  machine's self-talk but cannot read his way out of a hallway. He calls out (correctly) that
  the threat is coming up the stairs; largely unheard, then forced with the crowd into refuge.
- **Dwyer acts (Quartermaster instinct):** herds people, arranging bodies into the glass-walled
  conference room like inventory, putting them where they fit. The most useful thing he does.
- **The corner / box:** the refuge is a glass-walled conference room with a long table and a
  single door (a single point of failure Aaron clocks at once). This is how Aaron gets cornered.
- **Lena acts (Sentinel instinct):** plants herself side-on in the doorway, one arm across the
  gap, refusing to move. A faint blue seam of light runs the edge of her forearm where it
  crosses the opening (the Sentinel guard ability surfacing). Level 1, terrified, not strong,
  but compelled to stand in front.
- **First monster described:** wet, gray (the color of a thing that never saw light), moving on
  too many joints, no proper head but a working slit that opens and closes and tastes the air
  (eyeless). It hauls over the broken stairwell door onto Aaron's floor, orients, turns toward
  Lena's lit doorway, and starts coming. Section ends as it approaches the corner, into Section
  5 (no kill, no level-up yet).

### Ch 1 (Sec 5) established facts now known to the reader
- **First monster's hidden status block (Operator overlay, surfaced mid-fight; canonical,
  NO em dashes):**

      > # RIFT SPAWN: hollow-crawler (tier 0, minimum viable hostile)
      > # HP 22/22.  contact damage on limb-strike.
      > # passive: REGENERATION.  +4 HP per tick.
      > # tick interval: 3.0s.
      > #   note: regen routine locks HP buffer during write.
      > #   buffer vulnerable 0.4s post-tick. do not expose.

- **Monster name/type:** the first monster is a **hollow-crawler**, RIFT SPAWN, tier 0. HP 22.
  Contact damage on limb-strike. Passive REGENERATION +4 HP per tick, every 3.0 seconds.
- **The regen-gap mechanic (the exploit):** the regen routine locks the creature's HP buffer
  while it writes the heal and leaves the buffer vulnerable for 0.4 seconds right after each
  tick. Damage dealt inside that 0.4s post-tick window cannot be written back; the regen tick
  fails and HP guts out (22 to 18 to 9 to dead).
- **Read-as-action:** Aaron surfaces the block a foot from the creature, pulse up, dodging its
  limb-strikes; he times the gap by the rhythm of its attacks and the hide sealing and
  re-opening, then drives his kill into the exact 0.4s window.
- **Improvised weapon:** a heavy glass coffee carafe from the conference table. It shatters
  uselessly on the sealed hide; Aaron uses the broken jagged neck as a glass fang.
- **Where the kill lands:** not the hide but the creature's working slit (its eyeless
  tasting-mouth), struck in the 0.4s post-tick gap. The regen tick never finishes; it comes
  apart.
- **This is Aaron's first kill,** won with no class/skill/weapon, purely by reading hidden fine
  print and exploiting the regen window. Section ends on the kill landing, the light in the
  corner of his sight beginning to change (System about to pay out), into Section 6.
- **Lena (Sentinel) in the fight:** her blue-seam guard blocks the crawler's first strike (her
  arm holds a beat, scoring a furrow that instantly regenerates), buying Aaron his moment;
  Aaron shoves her clear of a killing limb-strike. She survives.

### Ch 1 (Sec 6) established facts now known to the reader
- **First kill pays out (canonical public reward + level-up, verbatim, NO em dashes):**

      [ SYSTEM ]
      Hostile entity eliminated: hollow-crawler (tier 0).
      EXP awarded.
      LEVEL UP.  You are now Level 2.
      +2 Perception.  +1 Wits.

- **The level-up feels physical:** warm reward color in the corner of his sight, the eye-pressure
  unclenching a notch, Perception sharpening the room, Wits steadying his read. Real and his.
- **Aaron's EXACT stat block now canon (Level 2 sheet, verbatim, NO em dashes). The class field
  still reads NULL_OPERATOR / status unhandled and did NOT resolve even after leveling:**

      Aaron Kessler
      Class: NULL_OPERATOR   status: unhandled
      Level: 2
      HP 60/60
      Strength 5   Agility 6   Vitality 6
      Perception 12   Wits 11

  Level 1 baseline implied: Perception 10, Wits 10 (this kill granted +2 Perception, +1 Wits);
  Strength 5, Agility 6, Vitality 6, HP 60 unchanged at this level. Physical stats ordinary;
  Perception and Wits run high (his reader nature).
- **Class still unhandled:** the level-up did NOT fix his class. The field finished loading but
  reads NULL_OPERATOR / status: unhandled, cursor still parked on it. He leveled but remains the
  exception (Level 2 of nothing).
- **The Operator edit-prompt teased (NOT used; canonical, NO em dashes). The System talking TO
  Aaron now, not just about him; it surfaces because the kill resolved outside any class template,
  leaving the handler vacant and write access open:**

      > # account KESSLER, A.: kill resolved outside template.
      > # no class handler claimed this event.
      > #   handler vacant. write access: open.
      > # offer: 1 edit available to this account.
      > #   target a mechanic you have read. revise one value.
      > #   no other class permits this.
      > # [ annotate? ]   y / n

  Aaron does NOT touch it (will not push the button before he understands the cost). The
  annotation cost is NOT explained, Priya does NOT appear. The choice hangs as the hook into Ch 2.
- **More rifts opening (escalation hook):** three floors down, multiple new rifts tear open in
  stacking structural coughs (felt through his shoes first). "One rift had been an event. This was
  a schedule." The world keeps opening below as the chapter ends.
- **Lena (Sentinel)** survives; her blue guard-seam goes dark; she looks toward the prompt only
  Aaron can see, at empty air, and says his name.

### Ch 2 (Sec 1) established facts now known to the reader
- **Continuity:** opens straight off Ch 1's end. Aaron at Level 2, still in the glass-walled
  conference room (single door) with Lena (Sentinel), Dwyer (Quartermaster), and survivors; the
  hollow-crawler dead; the glass-fang carafe neck still in his hand (set down at section's end);
  the unused "[ annotate? ]   y / n" Operator prompt still hanging in his sight, unspent.
- **Rift-tainted air reaches the room:** after new rifts cough open below, a slow wave of
  rift-tainted atmosphere rolls in. Smells of wet copper with something burnt under it (the reek
  that preceded the crawler). Invisible; first registers as held-breath staleness.
- **Public Suffocation debuff block (new canonical public hazard block; fires for EVERYONE in the
  room at once; NO em dashes; verbatim):**

      [ SYSTEM ]
      ENVIRONMENTAL HAZARD: rift-tainted atmosphere.
      Status applied: [ Suffocation ]  (stacking)
      Stacks: 1
      +1 stack / 6s while exposed.
      At 12 stacks: respiration fails. Death.

- **Suffocation mechanics (canonical):** stacking debuff, +1 stack every 6 seconds while exposed,
  death at 12 stacks ("respiration fails. Death."). In-line counter renders `[ Suffocation ]
  Stacks: N`, visible to everyone. Over the section it ticks 1 to 2 to 3.
- **It is public, and only Aaron can touch it:** every person in the room receives the block at
  once; panic and coughing follow (a woman by the whiteboard drops to one knee). Sentinel, 
  Quartermaster, and the rest have no mechanic that interacts with the air. Lena's blue guard-seam
  tries to surface and dies (nothing to stand in front of, the threat is already inside everyone);
  Dwyer's flee instinct fails (the whole building is the hazard, worse lower down).
- **Section-end action:** Aaron pushes his Operator sight under the public block to read the
  debuff's internals (into Section 2). He has NOT yet spent the annotation.

### Ch 2 (Sec 2) established facts now known to the reader
- **Suffocation's internal mechanics (Operator overlay, debug/comment style, only Aaron sees;
  canonical, NO em dashes):**

      > # STATUS: Suffocation  (env-sourced, stacking)
      > # owner: rift-tainted atmosphere. applied to all bodies in zone.
      > # var: stacks (int). init 1.
      > # tick: +1 stack / 6.0s while exposed.
      > # threshold: 12 (const).
      > #   on stacks >= threshold: call FAIL_RESPIRATION(body).
      > #     FAIL_RESPIRATION: write HP -> 0. flag: dead.
      > #   note: threshold compared each tick. no grace. no save.

- **Mechanic specifics:** Suffocation is a stacking integer `stacks`, init 1, +1 per 6.0s while
  exposed. Death threshold is a constant 12 (flat, does not scale with stats, identical for
  everyone). At 12, FAIL_RESPIRATION writes HP to 0 and flags dead. No grace, no save, threshold
  compared each tick. There is NO hidden seam/exploit window inside the debuff itself (unlike the
  crawler's regen gap), so the only answer is to edit the rule.
- **Comprehension gates editing:** reading the mechanic to full depth ("comprehension sufficient")
  is what makes the edit permitted.
- **The standing `[ annotate? ]` prompt re-aimed at Suffocation (canonical cost block, verbatim,
  NO em dashes):**

      > # account KESSLER, A.: target acquired.
      > #   mechanic read to depth. comprehension sufficient. edit permitted.
      > #   editable: 1 value on this mechanic. permanent. narrow.
      > # COST OF ANNOTATION:
      > #   - paid from earned progress: -1 level (and EXP to floor).
      > #   - paid from body: respiration debt, hemorrhage (decode tax).
      > #   - this account only. no refund. no undo. patchable by administrator.
      > # [ annotate? ]   y / n

- **Annotation cost (now canon):** one value on a mechanic he has read, edited once, permanent and
  narrow. Price: -1 level (plus EXP dropped to the floor of the new level) AND a physical toll
  (the decode tax: respiration debt and hemorrhage/nosebleed). Account-only, no refund, no undo,
  patchable by the administrator later.
- **Suffocation kept ticking during the read:** the in-line counter climbed from 3 (end s01) up
  through 4 to 5.
- **Aaron commits but has NOT executed:** he puts the cursor on `y` at section's end. He has not
  pushed it or renamed anything yet, and has not spent a level or taken the toll (held for s03).

### Ch 2 (Sec 3) established facts now known to the reader
- **The first annotation is EXECUTED.** Aaron pushes `y`; the choice is an act behind the eyes
  (will applied to a field), not a keypress. Write target: `STATUS Suffocation, 1 value`.
- **Exactly what he changed:** he edited the THRESHOLD BEHAVIOR of Suffocation (NOT the
  FAIL_RESPIRATION function, which is a wall he cannot move). He did NOT lower the threshold (that
  would kill sooner). He revised how the stack count climbs against the comparison so the counter
  CAPS at 11, one tick short of the death-wall at 12, and refuses the twelfth stack. FAIL_RESPIRATION
  will never be reached/called. The function still exists, just unreachable. Permanent and narrow.
- **Cost paid here, during the write:** Aaron dropped from Level 2 to **Level 1** (the level "tore
  loose," EXP to the floor, the warm reward color drained). Physical toll landed simultaneously:
  nosebleed (blood over his lip and on his teeth), a spike behind his right eye, and respiration
  debt (air going thin) while he wrote.
- **Suffocation counter kept ticking during the edit:** from 6 (section start) up through 7.
- **System confirmation block (new canonical, bright public shape, NO em dashes, verbatim):**

      [ SYSTEM ]
      ANNOTATION ACCEPTED.  Account: KESSLER, A.
      STATUS Suffocation: threshold behavior revised.
      Stacks now cap at 11. FAIL_RESPIRATION will not be called.
      Scope: this account and bodies sharing its air. Permanent. Narrow.
      Cost paid: -1 Level.  Decode tax applied.

- **Scope:** the edit applies to Aaron's account AND bodies sharing its air (those breathing the
  same air near him). The confirmation came in the bright PUBLIC block shape (same as a level-up),
  the System acknowledging his rewrite directly, not his dim gray overlay.
- **Outcome NOT yet confirmed:** section ends before it is shown whether the cap holds across the
  room. Counter at 7 and climbing; Aaron watches it, bleeding, breath shallow (held into Sec 4).
