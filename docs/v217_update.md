# v217 update (2026-11-18)

His note (15:07, screenshot of YOUR LANDSCAPE, ONE QUESTION AT A TIME on Pattern Analysis): "none of these links do anything." The patterns row from v212 is part of the map template, which every map shares, so it also appeared on the Analysis map (and on In Parallel's earlier 3D). Those maps draw no patterns, so the buttons there did nothing. Patch: `tools/patches/v217_laybar_synthesis_only.py` (engine only).

## What changes
The patterns row now shows only on the Pattern Synthesis map, where tapping a pattern draws it on the 3D.

## Tests
- Page check on 11-18: the Analysis map has no patterns row; the Synthesis map has 9 buttons; In Parallel has none.
- On Synthesis with the 3D: tapping "good fire" draws its loop and ticks its box in the list; unticking the box clears the button.
- `tests/matrix.py` on 11-18, 11-13, Broadview, and every mkwb workbook: no page errors. Builds reproduce; keys grep 0.
