# v215 update (2026-11-18)

His call (11-18, 14:30, looking at v213's In Parallel): "I don't want the grid anywhere near this project," with the lines figure as what he wants instead. Patch: `tools/patches/v215_in_parallel_figure.py` (engine only).

## What changes
1. **In Parallel opens with THE TWO PICTURES, SIDE BY SIDE**, the figure with lines from v214. It is no longer at the end of Pattern Synthesis; Synthesis's "See the two pictures together →" leads to it.
2. **The action grid is gone.** "Actions by ease and reach" (Act Here / Act Anywhere, the four corners, "Not yet actions, but easy and far-reaching") is removed from In Parallel, and its drawing code is deleted.
3. **MOVES, IN ORDER on Taking Action** no longer mentions the grid or reach. It starts with the notes the way passes that are easy to take ("easy to take, on ground that already holds; begin there"), else with the acceptance the way passes. "(the action grid on In Parallel)" and "acts in one place" are gone. Ease still comes from the emotion a note sits in and its side of the line (gsmDerive); nothing is drawn from it.
4. **Tapping a word** on In Parallel reads it and puts its lines on the Pattern Synthesis 3D. "See it on the Pattern Synthesis 3D map" goes there, and the lines are drawn as soon as that 3D mounts. In Parallel's own old 3D stays folded under THE EARLIER 3D VIEW.

## Tests
- `tests/agree.py` (now on In Parallel) with the 3D: 11-18 and clinic show the figure; no grid text on the tab; after a tap, Synthesis shows the word's 8 line segments on 11-18; Broadview (place map) shows no figure; no page errors.
- `tests/derive.py` on 11-18: MOVES, IN ORDER still follows a changed note, with the new wording.
- `tests/matrix.py` on 11-18, 11-13, Broadview, and every mkwb workbook: no page errors.
- `grep -c 'Act Anywhere\|action grid' gsm-preview.js` = 0. Both builds reproduce from source; `grep -c 'AAPK\|AIza'` = 0.
