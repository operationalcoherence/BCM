# v219 update (2026-11-18)

His two last notes for the day (15:21). Patch: `tools/patches/v219_tour_cites_fig_fs.py` (engine, and the relief with `--relief`).

## 1. No "(Vigneaux, 2026)" in either tour
The Synthesis tour's opening stops and the whole Pattern Analysis tour no longer cite the paper:
- "Height follows the order in Vigneaux (2026)" now reads "Height follows the order of the emotions".
- "the emotion of transition (Vigneaux, 2026)" now reads "the emotion of transition".
- "… unlikely in the short or medium term (Vigneaux, 2026)" now ends at "term".

As a guard, the tour also drops any "(Vigneaux, 2026)" or "in Vigneaux (2026)" that a reading's caption picks up. The page text (WHAT THE GROUND SAYS, the legends, the emotion definitions) keeps its citations; only the tours changed.

## 2. Full screen for THE TWO PICTURES, SIDE BY SIDE (In Parallel)
A Full screen button sits above the figure. Full screen shows the figure large, with a panel beside it (below it on a narrow screen) holding the title, HOW TO READ IT, the key, and the reading of the tapped word. Close full screen or Escape returns. HOW TO READ IT (Claude's wording, flagged): each word is something Analysis found; its lines run to every note that uses it; where the emotions stand on the ground; the help and hinder line and the goal; what solid black and dashed red mean; and that tapping a word reads it and puts its lines on the Synthesis 3D.

## Tests
- `tests/tour.py` (11-18) and `tests/tour_an.py` (11-18, clinic): no caption mentions Vigneaux; all stops visited; no page errors.
- Full screen on In Parallel at 1400 × 900: figure and panel side by side; tapping "tradition" reads it in the panel; Escape closes and the button returns to Full screen. Screenshot checked.
- `tests/matrix.py` on 11-18, 11-13, Broadview, and every mkwb workbook: no page errors. Builds reproduce; keys grep 0.
