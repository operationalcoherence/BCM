# v305: WHERE THE READING SPLITS stands on its own

**What changed.** Since v273, a hidden copy of THE LAY OF THE LAND's old figure ("How it hangs together") stayed in the page because the block that makes Taking Action's WHERE THE READING SPLITS only ran when the figure existed. The readings never used the drawing itself: they come from the engine's word data (`window.gsmFS`). v305 notes whether the figures were built (`Rt._gsmFigs`, set at the top of `gsmRetireSyn`), removes the hidden copy, and lets the block run on that note. The page no longer draws a figure no one sees.

**Checked** on 11-13, 11-18 and Broadview (desktop, every fold open, 3D loaded): Pattern Analysis and Taking Action page text is the same as v304, word for word; the split readings are the same (7, 9 and 0) and land on the same cards (8, 9 and 0); no page errors; nothing too wide. The PDF never drew the hidden figure (its block is `.gtold`, which the PDF skips), so the PDF is unchanged too.

**Not changed.** A second hidden old figure, "Around the goal", stays under WHAT SHAPE THE LINE MAP MAKES on line maps with notes. It is not read by Taking Action.

**Layers 37 to 39, run on the same three workbooks (v304 and v305 alike):**
- 37 ONE EMOTION, SEVERAL TARGETS: 11-13 and 11-18 show indifference aimed at three things (the future, the subject of wildfire, fire: N21, N26, N31). Aggression on 11-18 has two notes, under the three it needs, so it stays quiet. Broadview: quiet (its notes don't name their emotions).
- 38 A LOOP BETWEEN GROUPS: quiet on all three (no group holds an emotion aimed back at another).
- 39 TWO WAYS OF RUNNING: quiet on all three (no answer sets two conditions against each other with "when", "during" and the like).

Patch: `tools/patches/v305_split_without_hidden_figure.py`.
