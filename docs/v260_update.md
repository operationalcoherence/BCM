# v260 · 3D goal rings no longer sit over a label

His go-ahead 11-24 14:45 ("yes"), item 2 of "NOW · the 3D visual" in BCM_TASK_QUEUE.md ("Goal rings sitting over the N10 label").

## What changed
- The goal's three white rings now count as taken ground when labels are placed on the 3D ground, the same way other pins' heads do since v258.
- A note or reading-marker label that would sit on a ring moves to the nearest free spot around its own pin, with a thin leader line back to it.
- The GOAL label itself and the side and axis words (HELP, HINDER, PRESENT, FUTURE) never move for the rings. The GOAL label can still step aside if another label takes its spot first (seen on Broadview, where marker 6 lifted off the rings).

## What did not change
The ground, the rings, the notes' positions, the routes, the colors, and every word. Presentation only. Applies to every workbook, every 3D view (Analysis, Synthesis, Taking Action card maps, the tour), and place maps.

## Checked
- A crowded test copy of the 11-20 workbook with three extra notes on the rings: N47 leaves the inner ring with a leader line; N48 and N49 clear the outer ring.
- 11-20 workbook, Synthesis full screen: pixel-identical to v259 (nothing was on a ring from that camera).
- Broadview: the ground is unchanged; only labels moved (N8 off the outer ring, marker 6 above the rings).
- tour.py on 11-20: all checks pass, no errors. matrix.py on 11-20, Broadview, clinic, big, empty, hostile, legacy: no errors. No keys in either built file.

## Files
tools/patches/v260_goal_rings.py (tools/relief/relief.js: `RINGP` beside the rings, `hitR()` in `place()`; the label bump in gsm-readable.js).
