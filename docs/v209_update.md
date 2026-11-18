# v209 update (2026-11-18)

His notes on the v208 tour: it doesn't work in full screen (the legend covers it); a pause/play button would be more practical; does it really cover all 12 readings? Patch: `tools/patches/v209_tour_pause.py`, run on the engine and, with `--relief`, on `tools/relief/relief.js`.

## Answer: yes, all 12
`tests/tour.py` now records every caption inside the page. On his 11-18 workbook the tour visits all 12 readings of WHAT THE GROUND SAYS, 1 to 12 in order (11-13: 12; Broadview: 8; clinic: 9, which is all each one has). At about 2 seconds a stop the captions went by too fast to read, which may have made it look as if some were skipped.

## What changes
1. **Full screen:** the caption sits to the right of the legend drawer, as the map and its labels do.
2. **Pause and play:** the button reads Play the tour, then Pause, then Play. While paused the caption stays and the map can be turned and zoomed; Play flies back to the same stop and carries on. A click anywhere on the map (labels included) pauses. Reset view or Escape ends the tour.
3. **Each stop sits nearer the middle of the frame** (less empty sky in full screen).
4. **No hover boxes while the tour plays**, and an open one closes when it starts or resumes. In full screen, hover boxes now stay clear of the legend drawer (they could open under it before).
5. **A little slower:** about 30 seconds for 12 stops (2.5 seconds each; was 25 seconds).

## Wording that is Claude's (flagged)
"Pause", "Play", and the button's tooltip "Reset view or Escape ends the tour".

## Tests
- `tests/tour.py` with the 3D on 11-18, 11-13, Broadview, and clinic: every reading visited in order; a click pauses and the caption holds; Play resumes; Escape ends; in full screen the caption starts right of the legend (352 px against 340 px); no page errors. Full-screen screenshot checked.
- `tests/matrix.py` on 11-18, 11-13, Broadview, clinic, 200 notes, hostile, and empty: no page errors.
- `tests/relief_text.py` with the 3D on 11-18, 11-13, Broadview, and clinic: no page errors.
- Both builds reproduce from source; `grep -c 'AAPK\|AIza'` = 0 in both files.
