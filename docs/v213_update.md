# v213 update (2026-11-18)

The In Parallel figure (review 5a and 5b; decided 11-18 as mockup 2 with mockup 3's piece). Patch: `tools/patches/v213_agree_figure.py`, run on the engine and, with `--relief`, on `tools/relief/relief.js`.

## What changes
1. **THE TWO PICTURES, SIDE BY SIDE closes Pattern Synthesis** (open by default, just before "Put the two pictures together"). The words Pattern Analysis reports sit in their own column at left. Hoses carry each word onto the Synthesis ground, to the notes that use it. A black hose (and a black word box) means the ground agrees with what Analysis found; a white one means the ground raises a question about it.
   - **Words and verdicts** come from the same lists that write WHERE BOTH PICTURES AGREE and WHERE THEY DIFFER on In Parallel. The ground agrees for contested words, the clearest gap, and unused support (up to 2 of each). The ground asks for words planned with no cause, flagged as a gap but carried into Q.5–Q.7, or kept in Q.1–Q.4 without being a gap (up to 3 in all). A word is named by its repeated phrase where the workbook has one.
   - **The ground** is painted by the 3D relief's own rule: each note's emotion spreads around it, the nearest strong emotion wins, indifference reads as one band, bare rock where distant emotions meet, and plain ground where there are no notes. It is shaded by height, with the help and hinder line and the goal marked.
2. **Tapping a word** lights its hoses, gives one sentence on what both pictures say about it (for example, "good fire": Analysis finds it both resisted and supported, and the ground agrees: its notes sit above the line … and below it (N30). This is where the work is decided.), and draws its hoses as tubes on the 3D relief above, black or white as ways are drawn on Taking Action. "See it on the 3D map ↑" scrolls up to it. Tapping the word again clears it.
3. **In Parallel's own 3D** (Both pictures on one map) is folded away behind THE EARLIER 3D VIEW. Its code is unchanged.
4. **Line maps only.** On a place map the 3D shows real terrain, so a painted ground would not match what is above it; the figure does not appear there (Broadview).

## Not yet
The rest of the In Parallel review: 5c (explain "risk", "wildfire risk", "vegetation" in WHERE THEY DIFFER), 5d (cut the text hard; a second visual for WORTH A SECOND LOOK), and 5e (a shorter WHERE BOTH PICTURES AGREE). The figure's word labels are still lone words where the workbook repeats no phrase ("tradition", "reduce"), as they were in the mockup.

## Wording that is Claude's (flagged)
The lead line (it follows the mockup he chose), the key, the reading for each kind of word, and THE EARLIER 3D VIEW note.

## Tests
- `tests/agree.py` (new) with the 3D: 11-18 (9 words: 6 agree, 3 ask; "good fire" draws 8 hose segments on the 3D), 11-13, clinic, both-maps (12 segments), Broadview (no figure); In Parallel's old 3D folded; no page errors. Screenshots of the figure and of the 3D with hoses checked.
- `tests/matrix.py` on 11-18, 11-13, Broadview, and every mkwb workbook: no page errors.
- Both builds reproduce from source; `grep -c 'AAPK\|AIza'` = 0.
