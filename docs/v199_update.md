# v199 update (2026-11-18)

Phase 1, step 3 of the review plan: one derived-state pass (P2). Patch: `tools/patches/v199_derived_state.py` (engine only).

## What changed
The action points that Taking Action reads for MOVES, IN ORDER (how hard each Q.5–Q.7 note is to act on, and how far its words reach across the workbook) were computed inside In Parallel's drawing, and only when In Parallel's figures existed. A workbook whose In Parallel section didn't draw (three of the synthetic test workbooks: hostile, legacy, and same) gave Taking Action no points, so MOVES, IN ORDER fell back to "the ground way B passes" for every card.

They are now computed by `gsmDerive()` from the workbook alone. It runs on every pass the page makes after an edit (every save schedules one), before anything is drawn. In Parallel's action grid draws from the same points instead of computing its own. That makes it safe to move or retire In Parallel's figures later (5a and 5b in the review plan) without breaking Taking Action.

The pass leaves the engine's word tallies as it found them. A first version didn't, and two labels changed ("market" became "marketplace" on Broadview, "book" became "books" on the clinic workbook); that is fixed.

## What stays the same
For any workbook that already drew In Parallel (both of his), every page reads word for word as in v198, apart from the version label. The NOTHING YOU WOULD DO ANSWERS THESE YET list was already recomputed on every pass; it is unchanged.

## Not in this version
FIRST MOVES still doesn't follow the selected way, and new notes still can't form a card unless they share a recurring word. Both are P3 (v202), and FIRST MOVES depends on the phrase layer (P1, v200–v201) coming first.

## Tests
- `tests/derive.py` (new): boots a workbook without opening In Parallel, prints the action points, changes one note's emotion through the page's own save, and checks that the points and MOVES, IN ORDER follow. On 11-13, N4 turned to aggression leaves the "easy to take" start. On the legacy workbook, v198 had no points at boot; v199 has them.
- `tests/dump2.py` on Pattern Analysis, Synthesis, In Parallel, and Taking Action for 11-13, Broadview, clinic, and 200 notes: identical to v198 apart from the label.
- `tests/matrix.py` on 11-13, Broadview, and every mkwb workbook: no page errors, no script injection.
- `tests/relief_text.py` with the 3D on 11-13, Broadview, clinic, and 200 notes: the method's name, Moves, in order, and the renamed heading are on the page.
- `grep -c 'AAPK\|AIza'` = 0.
