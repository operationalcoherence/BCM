# v196 update (2026-11-17): Gregory's wording review, and the serial comma everywhere

Source: his review sheet of Claude's wording from v171 to v195 (https://claude.ai/artifact/KkdeKLx5E45pWKpYU1FE3V), 49 rows. Patch: `tools/patches/v196_wording.py` (it changes both `gsm-readable.js` and `tools/relief/relief.js`).

## His changes, now on screen
- **Row 5, Pattern Analysis (emotions first explained):** "Vigneaux (2026) calls this ground ready for an **emotions-first** method: …". The glossary still finds the term whether it's written with a hyphen or a space.
- **Row 15, WORDS THAT MAKE THE WORLD:** "(Winograd & Flores, 1986, p. 174)".
- **Row 26, glossary, behaviors first:** adds "The result is more important than the dominant emotion that produces it (Vigneaux, 2026)."
- **Row 27, glossary, program:** "A program runs linearly and possibly repetitively to completion." The same sentence on the Taking Action program cards was changed to match.
- **Row 39, Taking Action, When to stop and readjust:** the Morin passage is now quoted in full, in his words, before "So follow each way as it goes…". The typo "andA" became "and, in the end," with his OK.
- **Rows 40 and 47:** the comma changes.

## Serial comma, everywhere (his call, 11-17)
- Every list of three or more items that the engine builds now ends ", and" or ", or". Two-item lists are unchanged.
- The same goes for the fixed lists in the engine's own sentences, such as "designed, redesigned, or reinforced", "aggression, distrust, and defiance" and "grass, soil, or rock", and for the 3D legend's "a number, or a way".
- Three places are left as they were: lists that already end in a joined list before "and N more", one list joined with semicolons, and his own instruction text in the page template.

## Kept, cut or still open
- Every other row is Keep. No cuts.
- **Row 30, the action grid: Revise and Refine.** He wants it redone: new axes, new categories, coming *before* Taking Action, and drawing on Analysis and Synthesis. That gets its own version, after a design talk (2–3 options first).
- **Row 33, "Two people, two sides":** Keep. His note: "This may be perfect for a Project Leader" (feeds F8).
- **Rows 34 and 35, In Parallel's "the emotion changes" and "placed one way, tied the other":** left open, at his request.

## Tests
- Matrix on 14 workbooks: no errors.
- With the 3D loaded (swiftshader, every card scrolled into view, new `tests/relief_text.py`): his 11-13 workbook, Broadview, the clinic workbook and the 200-note workbook. No errors, and the new wording was found on each.
- Text diffs on 11-13, Broadview and the clinic workbook: the only changes are the ones above.
- Key grep: 0.
