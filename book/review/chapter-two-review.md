# Chapter Two Review: The First Annotation

From *Patch Notes for the End of the World* (Anomaly Detected, Book One)

- Word count: 4,538 words (across the 6 section files s01-s06)
- Page estimate: 16.5 pages (at 275 words per page)
- Verification gate (scripts/check_chapter.py 2): PASS

---

The cursor blinked, y over n, while three floors down the building tore itself wider, and Aaron still had not touched it.

He was on one knee, the glass fang loose in his hand, the prompt hanging in his sight. `[ annotate? ]   y / n`. One value, anywhere in the rules he could read. He needed to know what it cost first. The building was not offering time. Each new cough came up through his shoes a beat before it reached his ears, and the gaps between them were closing.

Then the air changed.

He felt it arrive before he understood it, a wrongness on the back of his tongue, wet copper and something burnt under it, the reek the rift had pushed up the stairwell ahead of the crawler. It rolled in low and unhurried. It did not look like anything at all. It made the room feel like a held lungful gone stale, the kind you do not notice until you cannot let it go.

Dwyer noticed first, because Dwyer was breathing hardest, still herding bodies along the far wall. He stopped mid-word. His mouth worked. Nothing came out the way it should.

Then the block fired for everyone.

    [ SYSTEM ]
    ENVIRONMENTAL HAZARD: rift-tainted atmosphere.
    Status applied: [ Suffocation ]  (stacking)
    Stacks: 1
    +1 stack / 6s while exposed.
    At 12 stacks: respiration fails. Death.

It wrote itself into every set of eyes at once. Aaron watched it land, the same small flinch he had seen when the class cards resolved, the awe turned inside out. A woman by the whiteboard read the last word, the plain one, and her hand went to her throat before anything was wrong with it.

The counter sat at 1. He saw it tick.

    [ Suffocation ]  Stacks: 2

Six seconds. He had not felt the gap between one and two, and that was the worst of it. No claws. No slit tasting the air. Just a room of people standing in poison that had a number on it, and the number climbed on a clock none of them could stop.

Lena's hand closed on the doorframe. The blue seam tried to come up along her arm, that Sentinel reflex to put herself between the room and the threat, and there was nothing to stand in front of. The threat was already inside everyone. The seam guttered and went out. She looked at him, and this time she did not say his name. She had worked out, somewhere in the last minute, that he was the only one seeing what the rest of them could not.

Dwyer got a breath in and it sounded like work. "Out," he said. "We get clear of it." He turned toward the door and the long hall and the stairwell full of rifts breathing the same air up at them, worse the lower you went, and he knew it as he said it. There was no out. The whole building was the hazard now.

Someone started coughing. Then someone else, a dry tearing hack, the body trying to clear something that was not in the throat but in the rule.

    [ Suffocation ]  Stacks: 3

Aaron's own chest had started to argue. He noticed it late and clinical, a tightness that was not panic, a value being subtracted from him on a schedule. His Perception was a fever reading and it bought him nothing. He could read the trap with more clarity than anyone alive, and the trap did not care. Twelve stacks at six seconds each. Carry the room from three and you had under a minute before the first person stopped breathing.

The whiteboard woman went down to one knee. Sentinel guarded. Quartermaster sorted. Not one class in this room had a line item for the thing in their lungs.

He did.

The prompt was still there, off to the side of all of it, the cursor patient. `[ annotate? ]   y / n`. He had been afraid of it a minute ago, afraid of pushing a button before he understood the cost. He still was. The fear had just stopped being the most expensive thing in the room.

Aaron set the glass fang on the carpet and put two fingers to his sternum where the rule pulled tight. Then he pushed his sight down under the public block, into the wet grain beneath the word Suffocation, to read how the thing meant to kill them.

The word Suffocation sat on the surface like a label on a closed box. Aaron pushed past it.

His sight went in the way it had gone into the crawler, the way it had gone into his own failed card, the wet grain opening behind the rendered thing. The room thinned at the edges. Off to the side Dwyer still worked air in and out like a man hauling rope, and the whiteboard woman's cough had gone wet, and the counter ticked in everyone's eyes at once. None of it stopped. He read with all of it pressing down on him.

The dim layer surfaced under the block, grayed back, scrolling with his eyes. Only his.

    > # STATUS: Suffocation  (env-sourced, stacking)
    > # owner: rift-tainted atmosphere. applied to all bodies in zone.
    > # var: stacks (int). init 1.
    > # tick: +1 stack / 6.0s while exposed.
    > # threshold: 12 (const).
    > #   on stacks >= threshold: call FAIL_RESPIRATION(body).
    > #     FAIL_RESPIRATION: write HP -> 0. flag: dead.
    > #   note: threshold compared each tick. no grace. no save.

He read it once and his pulse jumped, because there was no trick in it. The crawler had at least had a seam, a locked buffer, a hide that opened for four-tenths of a second and dared you to find it. This had nothing hidden. An integer that climbed, a number it was checked against every tick, a line that ran when the first reached the second. No seam. No window. Just a routine that did the arithmetic and wrote death.

Twelve. The threshold was a constant. `12 (const)`. Not a roll, not a curve, nothing that scaled with anybody's stats. A flat fixed wall, the same height for the Sentinel as for the man choking by the whiteboard, and on the far side of it a function whose whole job was to set a body's HP to zero and stamp it dead.

His own counter ticked while he read it.

    [ Suffocation ]  Stacks: 4

His chest pulled tighter on the four, a value subtracted from him on the same clock as everyone else, and the wrongness behind his eyes that meant he was reading deep had begun to climb with it. He understood the thing fully and the understanding cost him air he did not have. Worst part and best part in the same breath. He saw exactly how it killed. Nothing left to learn. He had hit the bottom of the box.

And the prompt moved.

It had hung off to the side of his sight since the corner, the patient cursor, `[ annotate? ] y / n`, aimed at nothing. Now it turned. He felt it turn, the way a cursor finds the field you clicked, and it bound itself to the lines he had just read, to `threshold` and `FAIL_RESPIRATION`, to the exact mechanic he had finally taken all the way down.

    > # account KESSLER, A.: target acquired.
    > #   mechanic read to depth. comprehension sufficient. edit permitted.
    > #   editable: 1 value on this mechanic. permanent. narrow.
    > # COST OF ANNOTATION:
    > #   - paid from earned progress: -1 level (and EXP to floor).
    > #   - paid from body: respiration debt, hemorrhage (decode tax).
    > #   - this account only. no refund. no undo. patchable by administrator.
    > # [ annotate? ]   y / n

He read the price the way the world had stopped letting anyone read anything in years, which was plainly, with no green tile over it swearing the cost was nominal. The engine was not pretending. It billed him in full before he spent, itemized. One level off the only ladder he had earned, dropping him back to the floor of nothing he had clawed up from. His own blood out of his face. A single value, edited once, forever, in a hole the administrator could close by tomorrow.

He should have hated it. A decade of dashboards swearing they were working as intended, and here was the one System that did not flatter itself, that handed him a real receipt and a live handler in the same breath, write access vacant because no class had ever claimed an account like his. The honesty of it was almost obscene. The dark thrill came up under the dread without canceling it.

    [ Suffocation ]  Stacks: 5

Five. Thirty-five seconds, give or take, before the first body in the room hit twelve and the function ran.

He had a level to spend, a value he understood, a button he had been afraid to push. The fear was still there. It had just stopped being worth what it cost. Aaron set his jaw, put the cursor on the y, and decided.

He pushed the y.

Not a key under his thumb, nothing his hand could feel. The choice went out of him the way the read went into the thing, an act behind the eyes, will applied to a field that had been waiting for it. The cursor took. The prompt did not ask again. It opened.

`> # write target selected: STATUS Suffocation. 1 value. confirm field.`

The dim layer spread out under his sight and held still for him, the whole routine laid flat. Stacks. Tick. Then the threshold, and under it the function that wrote death. The lines he had read to the bottom, every one editable in theory and only one in fact, one value, narrow, his. The counter ran in the corner the whole time.

    [ Suffocation ]  Stacks: 6

He went for the threshold. Not the function that wrote death. He had read that the function ran when one number met another, every tick, no grace, and a function was a wall he could not move. The number it checked against was not a wall. `threshold: 12 (const)`. He put the cursor on the 12 and he did not lower it, because lowering it killed people sooner. He widened what it meant. He took `on stacks >= threshold` and reached into the comparison and changed how the count was allowed to climb against it, so the counter could pile to one short of the wall and then refuse the twelfth, hold at eleven, stand there a single tick out from the function that wrote zero.

The cost came in as he wrote it.

It did not wait for the edit to finish and then bill him. It billed him during. The level went first. He felt it tear loose the way you feel a tooth come out by the root, a thing that had grown into him pulled hard against the grain, and the warm reward color he had earned over the crawler went cold and drained down through the floor of his sight. The number fell. He did not look at it. He could not have stopped looking at the write if the room had caught fire. EXP to the floor, the climb he had bled for emptied back to nothing, and the body's half of the receipt opened on the same breath.

His nose let go. The first of it ran hot over his lip and he did not lift a hand. A spike drove in behind his right eye, deep, the wrongness of reading made into a nail and hammered home. His chest pulled and did not fill. Respiration debt, the prompt had called it, and the prompt had not lied. The air went thin and refused him while he rewrote the rule that the air was killing the room with. He bore down on the write through all of it. Held the value where he wanted it. Did not let the spike knock the cursor off the field. Blood on his teeth now, copper to match the air, and the edit closing under his will like a wound sealing wrong, set where he had set it.

He finished it. The dim layer ate the new value and went quiet.

For a half-second nothing answered. The counter sat. The room hauled air. He stood there with blood on his chin and a level gone and no way to know, yet, whether the thing had taken or just cost him.

Then the System acknowledged him.

    [ SYSTEM ]
    ANNOTATION ACCEPTED.  Account: KESSLER, A.
    STATUS Suffocation: threshold behavior revised.
    Stacks now cap at 11. FAIL_RESPIRATION will not be called.
    Scope: this account and bodies sharing its air. Permanent. Narrow.
    Cost paid: -1 Level.  Decode tax applied.

It was not the dim gray of his own overlay. It came in the bright public shape, the same block that had told him he reached Level 2, the same block that had told the whole room it would die at twelve. The engine, not muttering to itself this time. Confirming. He read `FAIL_RESPIRATION will not be called` twice through the spike in his eye, and the second time it did not change. The function still existed. It would simply never be reached, because the count he had unbound from twelve would stop at eleven and stand there.

That was the rewrite. The fine print of the world's failure condition, edited by the one account it had not meant to leave open, the wall left standing and the path to it cut one step short. It had landed. The System said so, in its own voice, in its own honest receipt.

Whether it held was a different question, and the room had not answered it yet.

    [ Suffocation ]  Stacks: 7

The counter climbed. Aaron wiped his mouth, found his hand shaking, and watched it.

    [ Suffocation ]  Stacks: 8

He counted it the way he used to count the gap between an alarm and a page. Eight. The room was still drowning. The woman by the whiteboard made a sound like a straw at the bottom of a glass, and the man near the door had both hands flat on the table, breathing in short hauls that gave him nothing. The block had told them they died at twelve. Nobody in the room could see the wall had moved.

Aaron stood with blood drying on his chin and watched the number.

    [ Suffocation ]  Stacks: 9

The edit was real. The System had said so in its own honest receipt. But ten years had taught him that a green tile is not a live server. He did not trust the confirmation. He trusted the next tick, eyes on the one number that would tell him whether it had worked or just charged him.

    [ Suffocation ]  Stacks: 10

The man at the door went to one knee. The straw-sound stopped, which was worse than the sound.

    [ Suffocation ]  Stacks: 11

Six seconds. He held on the count and made himself not blink, because the next tick was the wall, was twelve and the function that wrote zero. Read it wrong and the room died with the receipt already paid.

Six seconds came.

The counter did not move.

It sat at eleven, refusing the twelfth stack the way a write refuses a field gone read-only. The tick fired, the pulse landed under everything, and the number it should have raised stood where he had nailed it. Across the glass box, every counter in his sight held at eleven at once, every body sharing his air pinned a step short of the wall.

The room breathed.

Not all at once. It came in ones. The man at the door dragged a lungful that filled and stayed on his knee, his legs slow to catch the news. The woman by the whiteboard coughed, and the cough turned into a breath instead of into nothing. Somebody said oh God in the small voice of a person who had been doing math on their own death and watched the answer change. They pulled air they could not account for and lived past the place they had stopped.

    [ Suffocation ]  Stacks: 11

It held.

Then warm color moved in the corner of his sight, the reward shade he knew. Not a level. A sliver, the same coin the System handed anyone who lived through a debuff, his climb refusing to stay at zero just because he had emptied it. EXP. Small. Honest as rain and just as ordinary. Still Level 1. Still HP 50 of 50, Perception 10, Wits 10, the sheet he had bled back down to. But the bar toward the next level had something in it again, and the something was his.

Then the bill sat down on him. The level was gone, a tooth socket the tongue keeps finding. His collar was wet where the nosebleed had stopped. The spike behind his right eye had dulled to an ache that pulsed on the count, six seconds, six seconds, a nail loosened but not pulled. He had bled a level so strangers could keep doing the most ordinary thing in the world, and could not tell if that was cheating or the first honest thing the world had handed him since the update. The log had finally told the truth about how a man dies in this room, and he had reached in and changed the answer. He let it be both and did not pick.

The room was breathing because of him.

Then someone near the back said get him down, get him flat, and the words had blood in them, the kind that comes off a body and not out of a voice. He turned. A man lay against the wall where Dwyer had stacked the wounded. He had come up the stairwell ahead of the crawler, and it had taken most of one thigh. The towel pressed there was no longer the color of a towel. His face had gone the gray of the air, the count holding at eleven over him and meaning nothing to the wound, because the wound was not a rule.

Aaron's sight dropped toward him before he decided to. Looking for a value. A threshold, a number to put a cursor on.

There was a body bleeding out, and bodies were flesh, not fine print, and the count over his head held at eleven while the puddle under his leg did not.

He went down on one knee in the spreading dark and put his sight on the man the way he had put it on the crawler, on the air, on everything the System had bothered to describe.

Nothing answered.

The crawler had carried a status block. The air had carried a kill-line he could nail to a wall. He kept expecting the man to be more of the same: a variable named bleed, init high, ticking down, with some const he could revise so the count would hold the way the suffocation count held.

He pushed. The spike behind his right eye flared on the six-second pulse and gave him nothing back. No overlay over the thigh. There was meat where the towel had been, the towel a wrung-out red, and under it a thing simply true the way a rock is true, with no second layer and no handler to go vacant. A wound is not a rule. It has no failure condition because it is the failure. You cannot put a cursor on a hole. You can only put a hand in it, and his hands knew nothing.

The man's lips moved. No sound came up to carry the words.

"Move."

He did not move fast enough, so a knee came down where his had been and a shoulder took him aside, not hard, just final, the way you move a chair. A woman dropped into the blood with both hands already going. She wore scrubs gone the color of work. Mid-thirties, hair scraped back, a face that had spent the morning looking at worse than this and deciding what to do about it instead of how to feel.

"Hands here." She did not look up. "Press. Both of them, lean your weight, do not be polite about it. You. Engineer. Now."

He pressed. She moved her own hands higher, found the place by feel, and something in her sight that he could not see resolved into a choice.

A clean block wrote itself into the air, the bright public shape, the one the whole room could read.

    [ SYSTEM ]
    Mender ability used: Stabilize.
    Target: critical. Hemorrhage suppressed.
    HP restored: 18.  Bleed-out timer cleared.

The thing he had been hunting for, the value he could not find, she had reached and turned in the time it took to kneel. Not with an edit. With a class, a plain one handed out at random like everyone else's, doing the ordinary impossible thing his exception could not touch.

The gray went out of the man's face in stages. His chest took a real breath, then another that meant it. The red under Aaron's palms slowed, thickened, quit insisting.

"He'll keep," she said, "if nobody jostles him and the air holds." She glanced up, and her glance priced you in under a second. "It is holding, isn't it. The air. It stopped."

"It stopped."

"I had three people down by the printer doing the math on a number over their heads. Twelve, the thing said. They got to eleven and quit climbing." She wiped her wrist across her forehead and left a print. "I have never seen a debuff change its mind. Priya. Anand. Triage, county general, before all this. Don't thank me, just keep that man flat."

She was already turning to the next body, cataloguing the room with the flat efficiency of someone who knows the only sin is freezing. Aaron held the man down and felt the smallness of it, two hands and his whole weight against what she had spent in a breath. He had moved a death-wall for forty strangers and could not have kept this one heart going ten more seconds. He edited rules. He could not edit a man. For that you needed her, and he had spent his whole adult life sure he did not need anyone.

Priya pressed two fingers to the whiteboard woman's throat and counted. Then she looked back at Aaron, not asking yet, only beginning to. At the dried blood on his chin that was his own. At the air that had stopped meaning death for no reason a Mender could give.

Her eyes went narrow, and stayed.

The room had gone quiet in the particular way a room does when it stops dying and has not yet decided what to do instead.

Aaron stayed on his knees, both hands flat on the saved man's chest, feeling the rise and fall of it. Forty-some people leaned against the glass walls and drew air that was no longer counting them down. Above each of them a number sat at eleven and did nothing. The whiteboard woman had her back to the wall, eyes shut, her color coming back. Two desks over, a man cried without any sound, the way you cry when you only just noticed you were going to live.

The room breathed because of him. The man under his hands breathed because of her. Aaron knew which of those mattered more if you had to keep one, and it was not his.

Priya finished her count at the whiteboard woman's throat. She wiped her fingers on her thigh, leaving another print on scrubs already past saving, then crossed back over the blood and crouched on the far side of the man, knees almost touching his. She did not look at the man. She looked at Aaron, and her look had the whole room in it.

"You're not a Mender," she said. Not a question. "You're not a Sentinel, and Sentinels can't touch air anyway. I watched the count. Twelve, the thing wrote, plain as a sign. Death at twelve. It climbed and climbed and then it just." She held a flat hand level in the air, the gesture of a thing stopping. "Sat down. At eleven. All of them at once. That does not happen. Debuffs do not get talked out of it."

"No," Aaron said. "They don't."

"So I'm going to ask, and I'm asking because I've got a room full of living people I'd rather keep, and I make better calls when I know what I'm working with." Her voice stayed low and level, only for him. "I looked at your card. There's nothing there I can read. Everybody lit up this morning with a name over their head, a class. You've got a blank. A hole."

The blood on his lip had dried to a crust. The spike behind his right eye turned over on the six-second beat, dull now, an old engine idling. He felt the answer arrive in his mouth, fully formed, with the easy weight of the true thing.

And right behind it, faster, the other thing. The instinct that had kept him quiet through a decade of standups where the green dashboard won. Do not say the word that makes you the exception. He knew what his card said in the layer she could not see. Flag for administrator review. The one input the System could not place, an error left standing because a god had not yet decided what to do with it. You did not tell forty frightened strangers that the thing keeping them alive was the bug the machine was still chewing on. You did not tell the one person who could now put your blood back inside you.

Priya watched his face do the math. She was good at faces, and she had spent the morning reading them off bodies on the floor.

"What's your class," she said. Point blank now, no cushion. "What are you, Engineer?"

He opened his mouth.

Off in the corner of his sight, parked where it had sat since the world ended, his own sheet hung patient and gray, the one card in the building that had never once resolved.

    [ SYSTEM ]
    Aaron Kessler
    Class: NULL_OPERATOR
    status: unhandled

The cursor still rested on the status word, still blinking. After a level gained and a level spent and a death-wall moved with his own bleeding will, it would not commit to what he was.

Three floors down, felt through his shoes, the building coughed. Another seam tearing wide. The air would thicken again, the eleven would matter again, and no door out of this tower led anywhere but down. They could not stay.

But Priya was waiting, close enough that he saw the exhaustion under her steadiness, the trust she offered before he earned it.

The answer sat on his tongue. So did the lie.

He had not chosen yet.

