  appear by name in Sec 1.)

### Ch 1 (Sec 2) established facts now known to the reader
- **The standup, the people:** Standup is held in a glass meeting room nicknamed
  **the Forum** (whiteboard, a dying ficus, a wall-mounted screen showing the
  incident dashboard). Aaron always takes the chair against the wall. The team is
  about eight people.
- **Dwyer (manager), on-page by name:** Soft, pleasant, "manages by reflection."
  He echoes the most confident screen back in a warmer voice. He sides with the
  green dashboard over Aaron's log, framing his doubt as caution ("Or there's
  something about your read of the log... Let's not chase a ghost on a Tuesday").
  He is not cruel; he genuinely trusts the summary. He tells Aaron to file it and
  loop in infra to confirm against the monitoring (the very tool that cannot see
  the outage).
- **Lena (coworker), on-page by name:** Quick, hardworking, sunny, generous in the
  hallway. She presents the resolved checkout-latency / cart-service fix (stale
  connection-pool handles past timeout; bumped the eviction) as her own good news
  and gets credited for it (asked to write it up for Friday's leadership review).
- **The fix was actually Aaron's:** Aaron traced and shipped that exact fix two
  nights prior (Sunday, ~11:40pm, paged out of half-sleep; pushed the eviction
  patch, watched the graph go flat ~1am, left a note in the channel with three
  thumbs-up that scrolled away). It rode out anonymous in the next day's deploy
  bundle. Lena is NOT stealing; she had her own honest theory on the same pool, and
  the "System of the room" assigned her the win for standing up confidently with the
  dashboard at her back. Aaron chooses not to correct it. (Quiet humiliation beat.)
- **Aaron's burnout / low investment in the old world, lived:** He no longer brings
  the log out of love but as "grim record-keeping," so that when the roof comes down
  there will be a saved draft timestamping when everyone decided to stop looking. He
  realizes he does not actually care whether the building survives the afternoon; he
  has stopped investing anything in the place. (Sets up that the old world's loss
  costs him little grief.)
- **End-of-section state:** Standup ends with the room siding with the green banner;
  Dwyer eases everyone out telling Aaron to "loop in infra." Aaron stays in the
  empty Forum, opens the PROD-EAST-07 ticket (41 lines attached), thumb hovering
  over submit. The System has STILL not arrived in this section (no notifications,
  no class, no mechanics). Flows into Sec 3: the dead-server argument peaking and
  Aaron being told to close the ticket as "working as intended."