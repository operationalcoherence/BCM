# v251: Pattern Analysis read as a reader

His go-ahead (11-24 09:03) on the before/after image from the reader review (claude/pattern_analysis_reader_review_2026-11-24.md in the Claude project). Patch: tools/patches/v251_reader_review.py. Everything is built by the engine for every workbook, not written for his.

## What changed
- AT A GLANCE opens with WHAT THE SYSTEM IS DOING: three sentences from the system story (what the system protects, how the protection moves as the change advances, and where it gives way). The BIGGEST GAP count leaves AT A GLANCE; the same gap is on Taking Action. This happens only when the workbook holds several stories; otherwise AT A GLANCE is unchanged (Broadview, clinic).
- WHAT HOLDS THE SITUATION IN PLACE: when acceptance sits inside what stands against the goal, the reading rests on it: the present arrangement is still taken as the right one, and the low emotions grow on that footing. Otherwise it reads as before.
- THE OPPORTUNITY: when what you would reinforce feeds support and support answers resistance in kind, it says so: support is fed where it already stands, and the work is to let it reach across the line.
- WHERE IT CAN CROSS: no definition first and no note numbers first. Only notes about people (Q.1–Q.4) count as the middle, not what you would do about them. It says who the middle is when the notes say it (waiting to see what happens, expecting it to fail, out of their hands, not invested, unsure), names a sense of having no say when the notes do, and points to a plan to ask for participation when one exists. WHERE THIS LEAVES THE WORK uses the same notes (11-20: N30, N32, N34, N35, no longer N14 and N22).
- WHAT YOUR USE OF THE BEAR CANYON METHOD PRODUCED is no longer built.
- In these three readings the note numbers go behind, small and gray (gsmStNB, .srnb).

## 11-20, after
- AT A GLANCE: "The system isn’t resisting the change itself. It is protecting what the present arrangement gives it: a shared sense of what is right and of who belongs. As the change advances, the protection moves from an argument about what is right, to a defense of each person's place, to quiet practice under a new name. It gives way only where the change provides the same thing another way."
- WHAT HOLDS: "What stands against the goal gathers around “command and control” and rests less on aggression than on acceptance: …"

## Tested
matrix.py on 11-20, Broadview, and the mkwb workbooks (mkwb.py stops at real.json, which is not stored): no errors. ta_flow.py: all pass. stories.py on 11-20: no errors. Key check 0.

## Not changed (from the review, not in the image)
WHAT THE SYSTEM IS DOING in full still says "not a lack of information" without naming his Q.1, still runs about 650 words, and does not yet point to his own levers (Q.5 methods to measure patterns, Q.6 management expectations, the Q.2 reassurance). THE OPPORTUNITY does not mention the Q.2 reassurance, because the engine cannot find that kind of move in an answer yet.
