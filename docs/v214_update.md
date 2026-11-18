# v214 update (2026-11-18)

His call on the In Parallel figure (11-18, 14:09, after seeing the hose version): "use lines." This follows the chosen artboard ("Chosen: lines (11-18)", bottom row of the figure canvas). Patch: `tools/patches/v214_agree_lines.py` (engine, and the relief with `--relief`).

## What changes
1. THE TWO PICTURES, SIDE BY SIDE draws one thin line from each word to every note that carries it. A solid black line means the ground agrees with Analysis; a dashed red line means the ground raises a question. No hoses.
2. The word's box shows what Analysis found: black for contested; a dashed outline for a gap that what you would design does not reach; a teal outline for support nothing uses yet; a grey outline for designed with no cause behind it (also used for the two "where they differ" kinds).
3. A key under the figure for the boxes and the lines.
4. On the 3D map above, a tapped word's lines are thin as well: solid black, or dashed red.

The note matching is the engine's own (phrase match on each note's text), not by hand. The ground uses the relief's coloring rule. Both were in v213.

## Wording that is Claude's (flagged)
The lead line and the key.

## Tests
- `tests/agree.py` with the 3D on 11-18 and clinic: the boxes and lines match the artboard, tapping an agreeing word draws solid black lines on the 3D, and tapping a questioned word draws dashed red ones; no page errors. Screenshots checked.
- `tests/matrix.py` on 11-18, 11-13, Broadview, and every mkwb workbook: no page errors.
- Both builds reproduce from source; `grep -c 'AAPK\|AIza'` = 0.
