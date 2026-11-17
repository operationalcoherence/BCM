# v184 (preview only) — 2026-11-17

From his review of v183. New wording is Claude's.

1. **A legend with every strategy map on Taking Action, none on programs.** The legend sits outside the 3D box, so it stays when a card scrolls away and its map is parked. Program cards no longer show one.
2. **Maps load once.** Before, a card showed the old flat route chart, then the blurry canvas map, then the 3D map. Now every map (cards, Pattern Analysis, Pattern Synthesis, In Parallel) shows a quiet "Building the land…" until the 3D model is ready. The canvas map appears only if 3D cannot be drawn (no WebGL, or the 3D file fails to load). The flat chart appears only if the whole card map fails.
3. **The action grid on In Parallel is richer and hoverable.**
   - Every note is plotted, not only Q.5–Q.7: filled dots are things you would do, rings are every other note.
   - Dot size shows how many notes it shares words with.
   - The quadrants are tinted and labeled: Start here: they travel · First steps, locally · Worth it once moving · Only where it blocks.
   - Hover or tap any dot to read its note.
   - New line: **Not yet actions, but easy and far-reaching**, the notes where acting would be cheap and would travel but nothing is planned yet (on his workbook N3, N6, N11, N12, N26, N27 and more).
   - Reach is now measured against all notes, so N7 and N13 move from "anywhere" to "here".

Checked: matrix on his 11-13 workbook, all 13 synthetic workbooks, and his Broadview place-map workbook (11-05); card legends present while parked; canvas fallback when 3D is unavailable; hover on a grid dot shows the note.

Not done: the Esri place map as the ground for Analysis, Synthesis and Taking Action (see BCM_HANDOFF.md, next step).
