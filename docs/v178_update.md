# v178 (preview only) — 2026-11-17

- **Full-screen legend no longer covers the map** (his screenshot). The open legend drawer now pushes the 3D map aside instead of lying over its left third. Hiding the legend gives the map the whole screen; the view re-frames each time.
- **In Parallel has its own picture**, no longer a copy of Pattern Analysis's.
  - Thin lines run from each question's flag to its notes (Analysis), over the numbered places of what the ground says (Synthesis). The question buttons follow one question's lines at a time.
  - New **WHERE THE TWO PICTURES MEET** (Claude's wording): each numbered place where notes from more than one question gather, with what that means. Examples: what you would do sharing low ground with the opposition; opposition standing on high ground; questions sharing a crossing.
- Bug behind it: v176's In Parallel mode was never seen inside the module's data builder (a function named `data` shadowed the option), so its numbers never showed. Fixed by reading the flag once (`PAR`).

Checked: matrix on his workbook and all 13 synthetic workbooks; 3D mounts on Analysis, Synthesis, In Parallel and Taking Action cards; full-screen screenshot.
