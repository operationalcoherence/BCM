# v206 update (2026-11-18)

Phase 2 of the 11-18 review plan, step 6, second half: YOUR STORY SO FAR told as a story (review 3e). Patch: `tools/patches/v206_story.py` (engine only).

## What changes
The opening of YOUR STORY SO FAR no longer leads with the workbook's most-used word ("fire" was too obvious). It tells the context you have grasped (Q.1–Q.4) in order, in your own words:
1. **Where it starts:** the sentence from Q.1 that shares the most words with the goal and the other answers.
2. **The present:** what holds the goal back close at hand, and what you placed where things help, two of each, quoted with the note number and its emotion.
3. **Further on, toward the goal:** what waits on the side that hinders and on the side that helps.
4. **How it is spread over time:** whether help and hindrance sit mostly in the present or further on (shown only when each side has at least three notes).
5. **The word that does two jobs** closes the story in one sentence (on his workbook: "fire": good fire and fire back where things help; fire suppression and fire later where they hinder).

It goes by where you placed each note: left of the line map is the present, toward the goal is later; above the line helps, below hinders. Notes are chosen by how far you placed them from the line, then by emotion. What you would design (Q.5–Q.7) stays in WHAT YOU WOULD DO. On place maps, where position doesn't say anything about time, the questions carry the story (Q.2 holds the goal back, Q.3 helps). Notes on the help side are described as "where things help, you placed…", without saying what their emotion is aimed at (as in v204). WHAT STANDS IN THE WAY and the sections after it are unchanged.

## Wording that is Claude's (flagged)
All of the story's connecting words: "It starts with why the goal has not taken root", "In the present, close at hand, these hold it back", "On the same ground, where things help, you placed", "Further on, toward the goal, … waits on the side that hinders, and … on the side that helps", the four sentences on how it is spread, and "Underneath it all, you use … on both sides".

## Also
`docs/bcm/BCM_ARCHITECTURE.md` brought up to date (Rev 9, through v206).

## Tests
- `tests/matrix.py` on 11-18, 11-13, Broadview, clinic, 200 notes, hostile, legacy, empty, one note, goal only, both maps, and same: no page errors, no script injection (hostile text shows as text inside the quotes).
- `tests/relief_text.py` with the 3D on 11-18, clinic, 11-13, and Broadview: no page errors; the story shows on all four.
- `grep -c 'AAPK\|AIza'` = 0.
