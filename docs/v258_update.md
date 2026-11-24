# v258 · 3D label pile-ups

His go-ahead 11-24 12:39 ("yes"), item 2 of "NOW · the 3D visual" in BCM_TASK_QUEUE.md.

## What changed
- Labels on the 3D ground (Pattern Analysis, Pattern Synthesis, Taking Action card maps, place maps) no longer sit on top of each other. When a label's usual spot is taken, it tries the spots around its own pin (right, left, above, below, the corners), then a step further out, and takes the first clear one.
- A note label keeps off other pins' heads, so it is never read as the name of the wrong pin.
- A label that has moved off its pin gets a thin leader line back to it.
- A label that was already clear stays exactly where it was. The side and axis words (HELP, HINDER, PRESENT, FUTURE) never move.

## What did not change
The ground, the notes' positions, the routes, the colors, and every word. Presentation only. Applies to every workbook.

## Checked
- 11-20 workbook, Synthesis full screen: N4/N5/N6 now read apart, N9 no longer hidden under Q.2, N21/N13 apart.
- Broadview: the ground is pixel-identical; only labels moved (N9 out from under Q.7, Q.2 off N2/N3).
- tour.py on 11-20: all checks pass, no errors. matrix.py on 11-20, Broadview, clinic, big, empty, hostile, legacy: no errors.

## Files
tools/patches/v258_label_pileups.py (tools/relief/relief.js `place()`; the label bump in gsm-readable.js).
