# v227: the constraint loop made visible

2026-11-18. Patch: `tools/patches/v227_constraint_visible.py`. Test: `tests/ta_flow.py`, extended.

His 11-18 21:31 yes to the two weak spots in v226:
1. **The Q.4 / Q.6 / Q.7 buttons always show** under each constraint field on Taking Action. They are grayed out until something is written ("Once written, add it to …") and turn on as you type.
2. **The note itself shows its constraint on Mapping Landscape** (line map and place map): WHAT HOLDS IT, AS YOU NAMED IT ON TAKING ACTION, with the text and whether it is in Q.4, Q.6, or Q.7. It updates as you type, and when you tap an add button. It no longer waits for a WHAT YOU DID log.

Code: `gsmNoteConsIn(id)` and `gsmNoteCons(t)`, plus `.ncons[data-ncid]` on each note. The `data-cons` input listener and the `data-cq` click refresh it.

Checked: `ta_flow.py` passes on 11-18 and Broadview; `matrix.py` has no errors on any workbook; the key check is 0.

Wording is Claude's, for his redlines: "Once written, add it to", "WHAT HOLDS IT, AS YOU NAMED IT ON TAKING ACTION".
