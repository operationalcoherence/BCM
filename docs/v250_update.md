# v250: no note fragments in the narrative

His note (11-24 08:23) on v249's THE OPPORTUNITY: "sending supporters of the transformation" has no meaning, nor does "going along with the transition"; little fragments like this devalue the narrative. Patch: tools/patches/v250_no_note_fragments.py.

## What changed
"Sending supporters of the transformation" or "Going along with the transition" quoted as
what already exists has no meaning on its own; such fragments devalue the narrative.
A note is never named in a narrative line any more. A line names a theme only when it is a
phrase at least two differently worded notes share; otherwise it says what the notes are
and where they stand, and their numbers go behind as evidence.

- THE OPPORTUNITY: with no shared phrase it says how many notes of support already stand on
  the high ground and where along the way they sit (near the start, partway, close to the
  goal), instead of quoting notes.
- WHAT HOLDS THE SITUATION IN PLACE: with no shared phrase it gives the count, no quotes.
- The one-line story: with no shared phrase, "What stands against the goal holds the work in
  place …" instead of a list of note openings.
- Taking Action: the seeded cards' titles carry a theme only when there is one ("What holds
  the situation in place", "The opportunity", "What is already helping", "Support not yet
  reinforced" stand alone otherwise); FIRST MOVE says "Scale the support already standing";
  the test lines count notes ("Two notes already help the goal …") with the numbers behind.

## 11-20, after
- THE OPPORTUNITY: "Most of the alternative already exists: seven notes of support, most of them near the start of the change. The work is scaling and reinforcing it more than inventing it. …"
- Taking Action: "Two notes already help the goal, but the proposed actions don’t use them yet. (N33, N46)"; "The proposed actions reach seven of them, but not yet the last one."; FIRST MOVE "Scale the support already standing (N13, N15, N21, N31, N33, N44, N46)."

## Tested
matrix.py on 11-13, 11-20, Broadview, and every mkwb workbook: no errors. ta_flow.py on 11-20 and Broadview: all pass. stories.py on 11-20: no errors. Key check 0.

## Not changed
In Parallel's PLACED ONE WAY, TIED THE OTHER still quotes a short note by name (for example “Performing experiments” looks like help but may give way under pressure). Ask him before changing it.
