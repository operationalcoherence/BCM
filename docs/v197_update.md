# v197 update (2026-11-17, evening)

From Gregory's notes on the v196 preview. Patch: `tools/patches/v197_brand_ridge_ways.py` (engine, and the relief with `--relief`).

## 1. The method's name under every 3D map
THE BEAR CANYON METHOD · BY OPERATIONAL COHERENCE now sits under the map on Pattern Synthesis, Pattern Analysis, In Parallel and the cards, not only in full screen. In full screen (and card full screen) it stays inside the map, as before.

## 2. Indifference reads as one band
Indifference notes are joined to their nearest indifference neighbors (shortest links first, none longer than 95 map units), and the yellow runs along each join in plain yellow, through other emotions' ground. On the 11-13 map the band now runs N8 → N21 → N26 → N31, into the acceptance. Color only: the heights are unchanged. Line maps only; a place map keeps color by distance (a band between homes would suggest a link no one drew). The emotion field is finer (150 cells across, was 96) so the band stays crisp.

## 3. Ways on strategy cards, drawn one way everywhere
- A letter always means the same way: **A** through its notes, **B** through its notes on firm ground only, **C** starting from the support. Before, the support way became B on cards with no firm-ground way.
- One badge per way (was two), placed where that way runs on its own and away from the other badges. Before, A and B badges sat on top of each other where the ways shared ground.
- Where two ways share a stretch, they run side by side instead of one hiding the other.

## Not built: the action grid
Three mocked options for the action grid (review row 30) are on a design canvas for his choice: https://claude.ai/artifact/AR9ndBeY8DcMcyoERdHjEQ. Gregory's call (11-17, 20:42): the vertical axis becomes **emotional distance**, how far the emotion has to travel for the action to land (Vigneaux, 2026), not context-free versus context-sensitive (too close to Snowden and Juarrero, and Snowden's bounded applicability). The horizontal axis stays effort. The three options (A grid, B both axes off the ground, C lanes) are redrawn on that axis; which layout is still open. Today's grid uses the number of emotions an action's words reach, so N16 and N4 sit far from N24 ("a broad campaign").

## Tests
- `tests/matrix.py` on 11-13, Broadview and all of mkwb's workbooks: no page errors.
- `tests/relief_text.py` with the 3D on 11-13, Broadview, clinic and the 200-note workbook: no page errors; the name line and the ways are on the page.
- `grep -c 'AAPK\|AIza'` = 0.
