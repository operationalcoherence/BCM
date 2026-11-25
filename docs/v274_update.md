# v274 · THE BARE LANDSCAPE stays bare in 2D too

Claude's fix, his go-ahead 25 Nov 2026 14:42. Known issue left open in v272: when a browser cannot draw 3D (no WebGL), THE BARE LANDSCAPE fell back to the flat map, and that map still drew the notes.

## What changed
- On THE BARE LANDSCAPE the flat (2D) map now draws only the ground, the rock, the present, and the goal: no note pins or labels, question flags, numbers, phrase loops, cause arrows, or highlight rings.
- Its legend drops the rows for questions, notes, numbers, cause and effect, and phrase loops.
- The version label in the page read v271; it now reads v274.
- Every other map (YOUR LANDSCAPE, Taking Action cards) is unchanged.

## Checks
- `tests/bare2d.py w20.json nogl` (Chromium with WebGL off): bare map shows ground and goal only; legend trimmed; no page errors.
- `matrix.py` on w20, big, cause, clinic, questions, places_names, empty, one, hostile, legacy, same: no page errors, no injection. Against v273: Taking Action word counts equal; Pattern Analysis 23 words shorter on line-map workbooks (the trimmed legend only).
