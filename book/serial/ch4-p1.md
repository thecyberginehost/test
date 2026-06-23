## Chapter 4: The First Patch (Part 1)

The side street ran out at a roll-down delivery gate, and behind it was the only roof Tess had found that the hardware crowd had not already claimed.

It was the kind of building Aaron used to walk past without seeing. A squat brick loading dock off the alley, a freight door wide enough for a pallet jack, the corrugated shutter pulled and locked from inside. Smoke had thinned this far off the main intersection, and the wrong daylight came down gray instead of bruised. In the corner of his sight the clock kept its slow arithmetic, sixty-eight hours and change, the seconds peeling off whether he watched them or not. They had spent the night in a stairwell that smelled of mice. They were not spending the day in the open.

"Locked," Hutch said, low, both hands flat on the shutter like he could feel for a give that was not there. "From the inside. Somebody pulled it down and walked out the back."

"Or didn't walk out," Priya said. She had the torn-thigh man propped against the brick, his color better than yesterday, his weight still mostly hers. "Either way, we're not getting forty fingers under that lip."

"We don't need fingers." Aaron stepped up to the shutter.

He said it without thinking, which was the tell, looking back. The door yesterday had folded for him, and a door was a door. He had a thing he did to doors now.

He let his sight go down into it. The half second of cost came, heat behind the right eye, the alley narrowing to a tunnel while the gray comment-layer surfaced under the rust and the padlock. He read it the way he had read the fire door in the tower, hunting the one unguarded integer that held the barrier up.

      > # OBJECT: roll-down freight shutter (sealed)
      > #   var: integrity (int). value: 35.
      > #   gate holds while integrity > 0.

There it was. Thirty-five, sitting in the open. No regen, no saved copy underneath, the seam as wide as yesterday's. Tess was watching from the side, reading the fact of him reading, and he wanted, stupidly, to show her the trick worked.

He put the cursor on integrity and told it the door was already broken.

It did not take.

The will went out of him the way it had at the fire door, that small private push behind the eyes. The field shoved back. Not a wall he could not afford, not a tier too deep. The edit reached the value and the value refused it, the way a form refuses a field it has been told to lock, and the whole thing bounced back into his sight in a block he had never seen.

      [ SYSTEM ]
      ANNOTATION REJECTED.  Account: KESSLER, A.
      OBJECT freight shutter: integrity.
      Write denied. Value protected.
      Cause: see patch.

The shutter did not move. The cursor came off the integer with nothing on it, the way his hand came off a keyboard when a command came back permission denied. He stood there with nothing to show for it, and the stupid corrugated door held.

"Aaron." Tess, quiet. She had seen his face do something. "It didn't work. You did the thing and it didn't work."

"No," he said. "It didn't."

He read the rejection again. Two days ago the same kind of integer had folded under him without complaint, and even then he had known it was too easy. In the tower stairwell, blood over his lip, he had filed the thought away like a man noting a deck plank that gave a little. One unguarded value, no regen, no grace. The kind of hole that got closed right after someone asked who left it open.

He had filed it. He had been right. Something had asked.

His reliable tool was dead in his hand, and the certainty he had stood on all morning dropped out by the width of one denied write.

Cause: see patch.

The block told him where to look. He sent his sight under and hunted for whatever had reached into a door he had not chosen and bolted the hole he knew how to use.

Cause: see patch. So he went and saw the patch.

He held his sight under the rust and let the comment-layer rise past the integrity value and the gate logic, down to whatever sat behind the denied write. The cost came again, smaller this time, a low ache behind the right eye instead of the full heat. The clock kept counting in the corner of his vision. He stopped seeing it. A stub of grammar hung off the bottom of the freight shutter's block, grayed back like everything in his layer, the place the rejection had pointed.

He read it the way he read crash logs, bottom up, looking for the line that named the thing.

      > # PATCH 0007  scope: account KESSLER, A.
      > #   target: annotation-class "integrity -> 0 on threshold object"
      > #   action: this account may not write integrity below 1.
      > #   on attempt: deny write. emit ANNOTATION REJECTED.
      > #   note: applies to KESSLER, A. only.
      > #   note: integrity mechanic unchanged for all other accounts.
      > #   note: adjacent object vars (mass, lock_state, hinge) untouched.

He read it twice. Then a third time, because the third time was when his stomach went.

It was the precision that did it. Not the denial. The denial he could have shrugged off as the world growing a callus where he had pressed too hard. But a callus was broad. It would have closed the trick for everyone and dumbed the whole mechanic down, made every door in the city harder to break because one man had broken one. That was a blind sweep. You sealed a class of exploit across the board and did not care who you inconvenienced, because the system did not know who.

This knew who.

The patch did not touch the integrity mechanic. Doors all over this district still ran on a single unguarded integer with no regen, the same soft seam he had walked through yesterday, and any one of them would fold for anybody who knew how to push. The mechanic was wide open. The patch had stepped around it on purpose, the way you step around furniture in a dark room you know by heart, and closed exactly one thing. His write. His exact hole, scoped to his account by name, nothing within a foot of it.

You did not aim that tight at a population. You aimed that tight at a man.

He crouched with his hand flat on the cold corrugated steel and felt the shape of it arrive slow, the way bad news always arrived for him, not as a shout but as a value that finally added up. The door yesterday had folded because the hole was open. He had known even then it was too clean, had filed the thought in the stairwell with blood on his lip. Right that something would close it. He had pictured a janitor. A nightly cron job sweeping the floor, catching his footprints with everyone else's.

Not a janitor. A reader.

Someone had sat down with his account, the one flagged for review since the first minute, and read what he had done to a door in a tower, and understood it well enough to fence him and only him out of it while leaving the door open for the next person. Read him back. The patch was not a defense thrown up against an attack it could not see. It was an answer to a specific argument made by a specific account. It was correspondence.

He had spent a decade losing arguments to systems that insisted they were working as intended. He knew the difference between a wall and a reply. This was a reply.

"Aaron." Tess had drifted closer, watching his face do the slow thing. "What is it telling you."

He had no words for it that would not sound insane in the gray daylight of an alley, so he filed it the way he filed everything he could not yet prove. Timestamped, for an audience of one.

"It's telling me I can't use that door the easy way," he said. "Not this one. Not anymore."

The shutter held its thirty-five and its denied write and its quiet little patch with his name in it. The trick was dead. He took his hand off the cold steel and put his sight back into the seam, hunting, because dead tricks did not open doors and the clock did not care that he had just met his opponent. He started to read.

He read the shutter the way the patch had not let him read it.

The integrity value sat there, thirty-five, fenced behind the denied write, a wall with his name carved into the brick in front of it. He left it alone. The patch had built that wall to be pushed at, and a man who keeps shoving a wall tells the thing on the other side exactly where his shoulder is. So he looked past it, slid his sight off the protected integer and into the rest of the object, the parts the comment-layer had grayed back because the integrity field was right there and easy.

The patch had told him where to look. Adjacent object vars (mass, lock_state, hinge) untouched. It had stepped around the whole mechanic to fence one hole, and in doing so had named the furniture in the dark room aloud.

He opened the rest of the block. It came up slow and the heat came with it, behind the right eye, deeper than yesterday's read. A layer down, the grammar thicker, the back of the object instead of the front.

      > # OBJECT: roll-down freight shutter (sealed)
      > #   var: integrity (int). value: 35.  [WRITE LOCKED: KESSLER, A.]
      > #   var: mass (float). value: 41.2.
      > #   var: hinge (struct). state: seated.
      > #   var: lock_state (enum). value: LOCKED.
      > #     gate logic: hold while lock_state == LOCKED.
      > #   open paths: lock_state == UNLOCKED, or integrity <= 0 (smash; write-locked for this account).

There it was. The gate did not hold on the steel. It held on the latch. Smashing the integrity to nothing was a road, the same one the patch had just bricked up under his name. But not the only road. The other ran through a single enum word the patch had not thought to fence. The shutter was bolted shut, and the bolt was all that held it.

"Aaron." Tess, at his shoulder, watching the gray daylight. "Whatever you're doing, the smell just changed."

He had clocked it too, copper going sharp under the smoke, but the lock_state field was open and warm now, the way a value goes warm when he has read it to the bottom and the System agrees he has earned the cursor. He put his will on the enum and pushed it from LOCKED toward the only other word it would take.

The bill came due in the same breath. The level tore loose first, the reward color in the corner of his vision guttering down a notch, Level 3 going to two, the bar scraped clean. Then the body. Blood ran the line of his lip and he tasted it, copper of his own to match the copper in the air. The heat behind his eye flared once and dimmed. His next breath came up half a step short.

      [ SYSTEM ]
      ANNOTATION ACCEPTED.  Account: KESSLER, A.
      OBJECT freight shutter: lock_state revised to UNLOCKED.
      Open condition met. Threshold opens.
      Scope: this account, this object. Permanent. Narrow.
      Cost paid: -1 Level.  Decode tax applied.

The latch let go. The corrugated steel sagged loose against the track like a fist unclenching, and Tess put her handrail under it and heaved and it ran up screaming on the rails.

Three. He stood there a half second with the blood on his lip and clocked the number the way he clocked everything now. The level he had paid would come back. He had ground it up the stairwell yesterday and would grind it again, a coin in a pocket. The other number did not come back, the running tab in the back of his skull where the body kept the real ledger. One in the conference room. Two on the fire door. Three here. Accruing.

And it had cost more to find. Same level, one, the same price the integrity door had wanted, but the read had gone deeper and the head knew it, a wrongness that sat lower and rang longer. The difference between a hole he already knew and one he had to learn under the clock. The patch had not made the shutter harder. It had made him read better. That was the whole game, the staleness pushing him a layer down, the bill climbing while the trick got cleverer.

He did not get to sit with it. The copper went from sharp to drowning, the ground under the loading dock kicked, and a System block he had never seen punched bright into everyone's sight, public, counting up where the others had counted down.

"Aaron," Tess said again, not at the air now but at the street, where the wrong sky had begun to peel open in three places she could see and one she could only feel. "That's not one rift."

The block that punched in did not belong to anyone. It hung over the whole street, bright as a billboard, counting up where his level had just counted down.

      [ SYSTEM ]
      TIER-UP WAVE.  District event.
      Rift density: critical.
      Spawn tier raised: 0 -> 1.
      Hostile saturation rising. Seek hardpoint.

Seek hardpoint. The System had a sense of humor. The only hardpoint within reach was the loading dock he had just spent a level and a tooth's worth of blood to open, and the wave was already between him and it.

He felt them before he saw them, the way he had felt the first rift through the floor of the tower. Heavier. The hollow-crawlers had come up the stairwell like wet hands. These came up out of the seams in the asphalt on legs that held, and they did not taste the air with a slit. They had low plated heads now, the gray-green of old armor. Bigger than the crawler by half, and faster than anything that big had a right to be.
