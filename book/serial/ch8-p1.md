## Chapter 8: The Bait Hole (Part 1)

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
