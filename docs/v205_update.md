# v205 update (2026-11-18)

Phase 2 of the 11-18 review plan, step 6, first half: Pattern Analysis reordered. Patch: `tools/patches/v205_analysis_order.py` (engine only).

## What changes on Pattern Analysis
1. **WHAT YOUR USE OF THE BEAR CANYON METHOD PRODUCED sits at the top,** right under AT A GLANCE, and leads into 1 · LOOKING IN and the landscape (review 3d, the move; deepening it is still to come).
2. **THE SAME THING? opens the page** while it is unanswered: a boxed prompt under AT A GLANCE. It now shows one sentence from the workbook for each word ("Where you write each:"), taken from different notes where it can, so both words are seen in use before answering (review 3h). Once answered, it moves back to IN THE WORDS as READ AS ONE.
3. **Bug fixed: THE SAME THING? buttons did nothing.** A list in the same part of the engine was also named `P`, which hid the save function, so the answer was never kept. This had been broken since the prompt was added. The buttons now save and redraw.
4. **WORDS THAT MAKE THE WORLD has its own heading** that opens and closes, like every other section (review 3j).
5. **The "Test each one" sentence is rewritten** (review 3k): "For each, ask what would have to be true for both views to hold. If something would, change your map. If not, keep the note as a voice you have heard, and let your map stand."
6. **YOUR LANDSCAPE, ONE QUESTION AT A TIME: hovering a question** (or focusing it with the keyboard) shows the question and its notes, each with its emotion, up to six (review 3b). Tapping still shows that question's notes on the ground.

## Wording that is Claude's (flagged)
"Where you write each:", the 3k sentence, and "…and N more. Tap the question to see them all on the ground."

## Not changed (noticed)
The question chips are built twice; the second row sits in a hidden copy and is never seen. Left as it is.

## Tests
- `tests/matrix.py` on his 11-18 workbook, 11-13, Broadview, clinic, 200 notes, hostile, legacy, empty, same, both maps, and one note: no page errors, no script injection.
- `tests/relief_text.py` with the 3D on 11-18, clinic, 11-13, and Broadview: no page errors. THE SAME THING? and WORDS THAT MAKE THE WORLD show on 11-18 and 11-13; neither applies on clinic or Broadview (as in v204).
- `tests/qhover.py` (new) on 11-18: the hover box shows Q.2 and Q.3 with their notes and hides on leave.
- THE SAME THING? answered Yes then No on 11-18: the prompt leaves, READ AS ONE appears, then goes again.
- `grep -c 'AAPK\|AIza'` = 0.
