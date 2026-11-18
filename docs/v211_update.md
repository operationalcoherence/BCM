# v211 update (2026-11-18)

Review item 3d: deepen WHAT YOUR USE OF THE BEAR CANYON METHOD PRODUCED (top of Pattern Analysis) with bigger themes, long phrases, and how they resemble each other, then lead into the visual. Patch: `tools/patches/v211_produced.py` (engine only).

## What changes
1. **Bigger themes.** Repeated phrases that turn up in the same notes are read as one bigger theme: at least 2 shared notes and half of the smaller one's. Answers are left out of this, because a long answer holds nearly everything. Notes with the same text count once (N9 and N25 on 11-18). Each theme says where its phrases meet, which side of the line it is on, which emotions the notes there carry, and whether it reaches what you would design (Q.5–Q.7) or stays in the context you have grasped (Q.1–Q.4). On 11-18: good fire, wildfire management, and unplanned fires turn up together in N11 and N27, written both for and against the goal, in acceptance, and they reach what you would design.
2. **No lone words.** The findings that read "gathers around tradition and measures" are named by their repeated phrase. Where the workbook repeats no phrase, the finding is named by quoting the shortest note (5 to 16 words) that uses the word itself: "Tradition turns to entrenchment and freezes the wildfire management system and refuses to move" (N29). A finding with neither is left out. "Nothing yet designs it" now reads "nothing you would design takes it up yet" (his grasping/designing distinction), and it joins the sentence about the same finding instead of repeating its name.
3. **Into the visual.** It ends by pointing to YOUR LANDSCAPE, just below: which of these notes sit in the low ground and which on the high ground.
4. Paragraphs instead of one block.

## Wording that is Claude's (flagged)
All of it, except the quotes from his notes.

## Tests
- `tests/dump2.py` Analysis on 11-18, 11-13, Broadview, clinic, and the 200-note workbook: read in full. A first pass grouped on answers and on clauses; it read wrong ("traditional media" stood in for "tradition") and was changed before shipping.
- `tests/matrix.py` on 11-18, 11-13, Broadview, and every mkwb workbook (hostile included): no page errors.
- Both builds reproduce from source; `grep -c 'AAPK\|AIza'` = 0.
