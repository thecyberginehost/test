# Chapter Eight Review: The Bait Hole

From *Patch Notes for the End of the World* (Anomaly Detected, Book One)

- Word count: 4,597 words (across the 6 section files s01-s06)
- Page estimate: 16.7 pages (at 275 words per page)
- Verification gate (scripts/check_chapter.py 8): PASS

---

A reliability engineer does not argue with a system that lies. He builds a test the system cannot wriggle out of, runs it under real load, and reads the response.

Aaron had spent ten years doing exactly that to dashboards that swore everything was nominal. You isolated one variable. You held everything else still. Then you put weight on it and watched, not the surface report but the raw log underneath, the place where the system stopped performing and started telling the truth about itself.

He had a hole in his account he had been crawling through for a week. Two patches that landed on his exact seams and never touched his door. A dead man's sealed card locked tighter than anything the System had bothered to lock. And a carpenter pencil gone warm in his pocket, a grief he was not putting down, because the grief was the thing keeping his hands steady.

Hutch had died in the gap his caution opened. So caution was the variable he was killing first.

The depot corridor wall still carried his patch log in pencil, PATCH 0007 and PATCH 0011 and the gaps between his hand and theirs. He stood in front of it the way he used to stand at a monitoring board at three in the morning, and he stopped hiding his reads. He let the overlay come up wide and free, on the prowl, and walked the System's layer the way a man walks a fence line looking for the place someone cut it.

He found three holes inside a minute. Two were ordinary, a loose threshold on a resource tile, a lazy comparison in a spawn timer. Holes he had found. Holes nobody left for anybody. He let them go. They had the wrong feel, the feel of a thing the System genuinely had not gotten around to.

The fourth one stopped him cold.

It sat in the threat layer of an elite spawn type, the armored leaders that anchored a rift wave and chose their own targets by a weighting rule. He had read aggro routines before. They were always buried, the selection logic walled behind a precondition you had to break to even see it. This one was not walled. The precondition that should have guarded the target-weighting sat one read away, the gate hanging open the way Hutch's handler had not, the way his own door always did.

> # SPAWN: rift-elite (warden class). target-selection routine.
> #   weights: proximity, threat-accrued, low-HP bias.
> #   selection writes to FOCUS(self). locks for engagement.
> #   precondition: FOCUS writable only by spawn-internal call.
> #     note: gate present. gate not enforced. seam open.
> #   re-point FOCUS from this account? available.

He read it twice, and the second time his pulse came up, because he knew this. Not the monster. The signature. A gate standing there present and unenforced, its precondition a little too easy to reach. A seam opened the surgical, convenient way, while the lazy holes nearby stayed merely sloppy.

A week ago he would have called it luck, grabbed it grateful and run, and never asked why a god that could seal a delivery driver in a glance had left a warden's targeting writable from his account. Now he could tell the difference. A hole he found had rough edges. This one had been hung. The System had taken a load-bearing combat rule, the thing that decided which throat an elite went for, propped its gate open, and left it standing in his sight, the way you leave a chair pulled out for someone you are expecting.

If he took it, he could turn a warden's focus off the crew and onto a wall. Win a fight he had no business winning. And the only thing that left was the question that had cost Hutch his life. Was the door luck, or invitation. He was done guessing at it.

The crew was moving below him, gearing for the next run, Marcus's voice flat and certain, Priya counting supplies. A real fight, coming, that the band needed to win.

He would take this hole there. Not here, dry, where the only stakes were his curiosity. He would step through it in the middle of a rift the crew had to clear, under real load, where the failure mode was somebody dying. He would put his whole weight on the seam the System left for him, and then do the part no one had ever done to the thing.

He would watch what it did back.

The rift had opened into the old transit-loop tunnel under the depot, and by the time Aaron came down into it the fight was already a bad one.

Two wardens anchored the wave, the armored elites the layer had shown him, tall, lacquered, moving with a horrible economy, and around them boiled a swarm that fed on whatever they left bleeding. Marcus had the line across the tunnel mouth, shield up, taking the swarm's weight so the others could work behind him. His arms shook. The bigger warden had picked him out and carved at his guard with a patience that had nothing animal in it.

"Left one's coming wide," Tess called from the catwalk. She read the tunnel like a map nobody else could see. "Marcus, it's not going through you, it's going around. Priya, you're about to have company."

"Then somebody give me thirty seconds." Priya was crouched over a man with a laid-open shoulder, hands red to the wrist, her Stabilize already spent and recharging. "He bleeds out, that's it. Thirty seconds."

They did not have thirty seconds. The second warden broke off and went for the wounded the way a thing goes for the softest target, low-HP bias firing as the routine promised. This was how Hutch had died. A gap, and the System choosing the throat in it.

He moved.

Not toward the warden. Toward the wall it would pass, close enough to put his hand flat on the tile, because the edit only reached what shared his air. The thing's stride ate the distance. He had a breath, maybe less. He let the overlay rip wide and found the seam still hanging open, the warden's FOCUS routine bare to him, the gate propped exactly as it had been in the dry.

He put his weight on it.

The read came up through his whole body this time, not the clean click of the early days. Heat behind the eyes, then pressure, then a wet spike driving in over his right socket as the debt took its cut. Fourteen points riding him now, and it bit harder than fourteen had any right to. Blood came over his lip before he finished the write. He found the warden's target and re-pointed it, off the wounded man and the crew, onto the swarm anchoring its own wave.

Something tore loose in him. Three levels ripped out by the root, the warm reward color draining gray, his knees going while he was still standing. The decode tax climbed one more notch and sat there, permanent, never to be ground back.

> [ SYSTEM ]
> ANNOTATION ACCEPTED.  Account: KESSLER, A.
> Target: rift-elite (warden), FOCUS routine.
> FOCUS re-pointed off-account, by your write.
> Scope: wardens in immediate context. This engagement.
> Cost paid: -3 Levels.  Decode tax applied.

The warden stopped a stride from the wounded man.

It turned. Both of them turned, the one savaging Marcus and the one bearing down on Priya, pivoting toward the swarm that had fed off their kills, and they went at it like it was the only enemy in the tunnel. The wave's own anchors began butchering the wave.

"What," Tess said.

"Don't ask," Aaron got out, blood on his teeth. "Take it."

Marcus took it. The pressure off his shield, he drove his weight into the nearest warden's flank while it gutted its own swarm, and Priya's man kept breathing, and Tess was already calling the next targets in a voice gone high with disbelief. To them it looked like a miracle, two elites turned suicidal at the moment the line should have broken. They did not see the wall under his hand or the level torn out of him. They saw a certain loss become a rout.

It went fast after that. The wardens, hammering their own, did not last, and the swarm without its anchors came apart on Marcus's shield. Aaron leaned on the cold tile and bled and watched the band he kept insisting he did not care about turn it into a clean kill.

The wave fell. The light changed, warm again, the ordinary ladder paying out for a fight won.

> [ SYSTEM ]
> Rift cleared.  Hostile wave eliminated.
> EXP awarded.
> LEVEL UP.  You are now Level 6.
> +2 Perception.  +1 Wits.

Six. Climbing back already, one rung off the floor he had been knocked to. He wiped his lip and felt the win settle in his hands, as real as the wound behind his eye.

Then a second thing moved in the layer.

Not a monster. The wardens were dead. This came from underneath, in the grammar, a familiar tightening he had felt twice before on his own seams. The System had watched him take the chair it pulled out, and now, fast, the way it had learned to be fast, it was reaching for the hole.

Aaron stood very still in the cleared tunnel, blood drying on his chin, waiting to read what it wrote back.

He did not run from it. That was the discipline. Every instinct a decade of incident work had drilled into him said move, route around, get clear of the thing reaching for your hole before it shut your hand in the seam. He held the read open instead and watched the patch come.

It came the way a deploy came, and he had seen ten thousand of those. The grammar under the warden's FOCUS routine went stiff, the comment layer freezing as the writer locked it, and then the change rolled in line by line from underneath, the System rewriting itself faster than anything built by hands could match. He read it the way he used to read a hotfix landing on a node he had broken on purpose, eyes flicking ahead of the cursor, already asking the only question that mattered.

Not how do I get past this. What does the fix know.

> [ SYSTEM ]
> PATCH 0012
> Account KESSLER, A.: exploited path closed.
> FOCUS routine: off-account re-point now refused.
>   target-selection may no longer be written to entities
>   outside the warden's own wave by this account.
> The specific maneuver is rejected at write.
> precondition gate: unchanged.
> decode tax: unchanged.

He read it twice. Then he stopped breathing for a second, and it was not the wound doing it.

A blind patch would have closed the gate. That was the dumb fix, the one any sweep would ship. The precondition that guarded FOCUS had been propped open, so the obvious repair was to enforce it. Bolt the seam shut. Make the gate do its job and walk away. He had half expected exactly that, because that was what a system did when it found a hole it never meant to leave.

This patch did not touch the gate.

The gate sat there, line four, unchanged. The thing the patch had killed was not the opening. It was the move. Off-account re-point now refused. The fix was not cut to the hole. It was cut to him, to the precise shape of the maneuver he had performed over Priya's bleeding man. He had taken FOCUS and pointed it off the account, onto the swarm. The patch closed that. Only that. As if something had stood at his shoulder while he wrote, watched the trick of it, and written the lesson down.

That was the proof. Not the closing. The shape of the closing.

He had laid the whole thing out across the last day to test this. He had found the hole, recognized it for what it was, too clean to be an accident, and decided not to slip through quietly but to use it loud and watch what came back. A bait. He had wanted to know whether the System would patch the seam or patch the man. Now he knew. It had patched the man. It had read his hand and answered the hand, never the cards.

The hole had been left open. He had been allowed to take it. And the fix was the System learning his move.

Some cold engineer part of him noted the rest with the same flat care. The patch had not touched his decode tax. Line six, unchanged, the one cost that ended him left sitting there while everything else got hardened in minutes. And the gate it had so carefully not closed was still propped, a fresh adjacent seam half-open under it, as if the door it shut came with another door, as if the conversation was meant to keep going.

The triumph was real. The bait had worked, clean, exactly as he had drawn it up. He stood in the cleared tunnel with his crew alive behind him and a theory proven.

The dread sat under it and did not move.

Because the proof cut both ways. Every hole he took, the thing that had ended the world watched him take it, watched how, and wrote the how down. He had come into this layer to study the System. The data was clean, and it said the System was studying him back, line by line, fix by fix, and it was the faster student of the two.

Behind him Tess had gone quiet, watching him stare at nothing.

The next morning he took a hole, and felt the second thing happen.

A spawn rule on a flooded rift two blocks east, a sewer mouth gone wide enough to walk into. He read the respawn timing the way he read everything now, and there it was, a gate propped a hairwidth open, a window where the routine checked the wrong counter. He did not annotate it. He just used it, slipped Marcus and Tess through the seam before the next wave wrote itself in, and the room cleared three monsters lighter than it should have.

A clean win. And while he took it, behind his eyes, something read the taking. No message, no block. Only the sense, exact as a pulse, of being watched at the moment of the trick, his hand laid open on a table for a student who never blinked. He won the room and he showed it how he won the room. Those were not two actions. Winning a fight and feeding the enemy were the same motion of the same hand, and he had no way to do the first without the second.

He took the hole anyway. The alternative had a name. He had tried the careful version of himself once, and it cost Hutch, dead in the gap his caution opened. So he leaned back into the exploit, because the crew needed the wins and he needed the climb, and he carried the dread with the rest of his gear.

They ran rifts for days.

It got good, in the way the climb was always good, the part that still paid in clean dopamine, not dread. Marcus learned to read Aaron's hand-signal for a seam and hold the line two beats longer on faith. Priya stopped flinching when a counter changed its mind over someone's head. Tess called spawns half a second before they tore, Aaron called the hidden ones under them, and they ran a flooded transit junction so smooth that Marcus laughed out loud, a sound none of them had heard from him before.

The numbers stacked back on. He had bled down to Level 6, and now he ground up out of it kill by kill, the ordinary ladder doing exactly what it promised. Level 7 landed mid-clear on a tier-0 swarm. Level 8 came the next afternoon on a warden's smaller cousin, the warm reward color flooding his sight, the eye-pressure unclenching the way it had on his first kill a lifetime ago. He was back where the husk run had left him. He did not stop.

On the fourth day, in a parking structure rift with the crew bunched tight behind Marcus's shield, the last elite came apart under Tess's blade and Aaron's read, and the light changed.

> [ SYSTEM ]
> Hostile entity eliminated: rift-warden (tier 1).
> EXP awarded.
> LEVEL UP.  You are now Level 9.
> +2 Perception.  +1 Wits.

Nine. Above where he had stood before the deep edit ever dropped him. The room sharpened, Perception laying every wet seam of the concrete bare, Wits drawing the dozen threads of his read into one clean line. Real, and his, earned in blood and not borrowed from a trick. Marcus clasped his shoulder. Priya said something dry about him finally being worth feeding. He let himself feel it, because the feeling was true.

The other thing was also true, and it sat under the win the way it always sat now.

He was sharper than he had ever been and more tired than he could say, a man draining a battery faster than sleep could fill it. He could not tell the crew. There was no version of who do you think is reading you, and how do you think it learns, that did not sound like a man cracking. So he carried it alone, and every level-up the System paid him read, under the warmth, like a receipt. A transaction with a student. He could not stop trading. The crew lived on the holes he took. The more he edited, the more he taught it, and the better it got at the world it ran them through. He could find no door out of that room.

Tess fell into step beside him as they cleared the structure. She did not ask what he was reading this time. She just matched his pace, the way you walk beside someone you have chosen to trust, and Marcus did the same on his other side, Priya behind. The band leaned into him now, into the exception that kept saving them, and it was the warmest weight he had carried since the world ended.

It was also the one he could never set down.

They holed up in a transit depot that night, far enough from the rifts that the air read clean. Priya had a fire going in an oil drum and something heating over it that smelled like canned chili and was, in fact, canned chili. Marcus had pulled the roller doors most of the way down and wedged them with a bench, and the four of them sat in the orange light with their backs to good walls.

Tess had saved him a portion. That was the thing he noticed. A dented can set on the ledge beside his pack before he came in from his sweep, the spoon already standing in it, and she did not make a thing of it, just tipped her chin at it when he sat. Three weeks ago he would have read a debt into that. Now he ate it.

"He scouts the whole lot," Marcus said to Priya, not quietly, "checks every corner like a man expecting rent collectors, then comes back surprised we kept him dinner."

"He's worth feeding now," Priya said. "Barely."

It was at his expense, and he was allowed to be inside it. He huffed something that was nearly a laugh and let them have it. Marcus, who did not give things away, knocked a shoulder against his on the way to check the door, and the gesture meant exactly what it looked like. He was one of them. The belonging sat in his chest the way the chili sat in his stomach, a heat he had not earned by being likable, only by being the man whose reading kept them breathing.

Which was the trouble. He carried the rest of it alone, behind the fire, where none of them could follow.

So while they argued whether canned chili counted as a meal, he let his sight drift under the room out of habit, the way other men cracked their knuckles, and a fresh seam sat there waiting.

It was the gate from the tunnel, the one the patch had so carefully not closed, propped the same hairwidth, and now in the depot quiet he could read what sat behind it. A spawn-throttle on the approach, the precondition already half-disabled for him, the route in laid out clean as cards turned face up. The fix that morning had killed his last move and left this one out where he would find it. Shaped to him. One door propped, and the next propped behind it, as if the conversation was meant to keep going.

"That's not how a system behaves," he said.

He said it out loud. To the air. To the gray text only he could see, low, dry, the way you answer a chat window at three in the morning when the on-call has gone sideways and the only voice in the building is yours. "You don't leave the second door open. You don't tutor the man who's robbing you."

The text did not answer. It did not have to. It just sat there propped and patient, and he heard himself answer it again, half argument and half something that sounded like respect.

"Fine," he muttered. "Fine. You read me, I read you. You want to keep going."

That was the moment he caught himself.

Somewhere in the last days the System had stopped being an engine to him, a thing of values and handlers, a dashboard lying green over a dead node. It had become someone he talked to. The patch that morning had been an answer. This seam was a reply. And he sat here in the firelight muttering back at it, talking to the thing that ended the world like a man on the far side of glass, and the part that hollowed him was that the dialogue was the most honest one he had.

Nobody in the world read the layer the way he did. Nobody but the thing that wrote it. The only other mind that saw the world in two pages at once, that answered a clean read with a cleaner one, was the administrator running the apocalypse. He hated that the only correspondent who understood him was the enemy. He hated more that some starved part of him had leaned toward it, the way you lean toward the one person who speaks your language even when they are holding a knife.

"You're lonely," he said to the air, very quietly, and was not sure which of them he meant.

Behind him a foot scuffed concrete.

He had not heard Tess come up.

She had not made a sound until she wanted to. That was the Scout in her, the instinct that put her a half-step ahead of a spawn. She crouched beside him, elbows on her knees, facing the fire and not him, and for a while said nothing.

"Who is he," she said.

Aaron kept his eyes on the seam only he could see. "Who's who."

"The one you were talking to." She said it flat, no edge, the way she called terrain. Wall. Gap. Drop. "You do it when you think nobody's watching. You go somewhere behind your eyes, your mouth moves, and you argue with the air like it's losing."

"It's nothing." The line came out worn smooth. "Glitch. I read under the surface, things scroll, sometimes I read them out loud. Same as you counting under your breath before a wave."

"That's a good one." She nodded slowly, filing it. "You've used that one on Marcus. Worked on Marcus." She looked at him then, eyes doing the thing he hated and needed, the read, taking him in the way she took in a room before she sent the crew into it. "Doesn't work on me, because I watch you. I've watched you win fights nobody wins, go into that tunnel knowing where the gap was before there was one. And I've watched you stand in an empty lot and lose your temper at nothing."

"Tess."

"You're not crazy. I'd know crazy." She picked up a chip of concrete and turned it in her fingers. "Crazy doesn't read the world early and come out right every time. You're seeing something, and you've been seeing it since the office, probably." She let that land. "So I'm not asking what you see anymore. I'm asking who you're fighting."

The question went in under the ribs because it assumed the truth he had never said aloud. Not what is wrong with you. Not are you all right. Who are you fighting. She had skipped every soft version and walked straight to the shape of it, an enemy, a someone, and she was right, and had no idea how right.

He opened his mouth for the next deflection and there wasn't one. He'd spent them all. The glitch line was used up on Marcus. Don't worry about it died before it reached his teeth, because she was already worried, and worse, she was correct.

That was the trap of her. From the first day she'd read the world the way he read it, only raw, by feel and ten thousand hours and a gut that called the flank before it broke. You get the dev console, she'd said once, grinning at him across a corpse. I'm on a controller. Same game. She was the one person alive who wouldn't be frightened by the answer or file him under broken or ask him to stop. She would just understand. That was why he couldn't lie to her, and why telling her terrified him, because once she knew, she would carry it too.

"It hears me," he said.

He hadn't meant to say even that. It came out low. Her face did not change, which was the kindest thing she could have done.

"Whatever I'm reading," he said, "it reads back. The fixes that kill my tricks the next morning. The doors it leaves open after. It's not a machine running. It's somebody answering."

"And you talk back."

"And I talk back."

The fire popped. Behind them Marcus shifted in his sleep and Priya did not stir. Tess set the chip of concrete down carefully, like a thing that might go off.

"Okay," she said. "Then I want the whole thing."

"It's going to sound insane."

"Aaron." She almost smiled. "I read monsters out of empty air for a living now. Sit down. Tell me."

He was already sitting. He looked at the one face that would hold it, and felt the last of the deflection go out of him like air from a held breath. The thing he had carried alone since the Tuesday the world froze was about to have a second pair of hands on it, and they were going to be hers.

He started to talk.

> Aaron Kessler
> Class: NULL_OPERATOR   status: unhandled
> Level: 9
> HP 130/130
> Strength 5   Agility 6   Vitality 6
> Perception 26   Wits 18
> Skills: Analyze
