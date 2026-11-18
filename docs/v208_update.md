# v208 update (2026-11-18)

The guided tour of the ground on Pattern Synthesis (review 4c; his request 11-18: a Play button, with the share of energy and the key data points that are already there). Patch: `tools/patches/v208_tour.py`, run on the engine and, with `--relief`, on `tools/relief/relief.js`.

## What it does
- **Play the tour**, a new button on the Pattern Synthesis 3D map, next to Reset view and Full screen.
- The camera flies from reading to reading of WHAT THE GROUND SAYS, in his four acts: the high ground, the low ground, between them, and what keeps it this way. It turns slowly across the land as it goes and looks down on each place, so the reading's marker sits in the middle of the frame, under the caption.
- **Each stop is captioned** with its act, its number and title, and the data the reading already carries: its notes, how much of the ground slopes into it (for example "About 28% of the ground slopes down into here"), and the climb, as a share of the map's height, that getting out takes (for example "It climbs 53% of the map's height"). Sentences that point at a question further down the page are left out of the caption. A bar under the caption shows how far along the tour is.
- The reading's marker and its row in the list light up as the tour reaches it.
- About 25 seconds (2–2.6 seconds a stop; up to 12 stops), then back to the starting view.
- **Stop** (the same button), a click on the map, Escape, or Reset view ends it at once.
- It is drawn live from the workbook, so it is always current. It works in full screen and on place maps (on the real terrain). It does not appear on Pattern Analysis or on Taking Action cards.

## Not yet
- A WebM download of the tour for sharing (planned in the review, Phase 3).
- Captions with his confirmed meanings of the four acts (review dependency 5); the captions use the readings' current wording.

## Wording that is Claude's (flagged)
"Play the tour" and "Stop". The captions are the readings' existing wording.

## Tests
- `tests/tour.py` (new) with the 3D on 11-18, 11-13, Broadview, clinic, and the 200-note workbook: the tour runs 22–28 seconds, captions change in order, a click on the map stops it, no page errors. `tour.py WB OUT slow` runs it 8x slower for settled screenshots (checked on 11-18).
- `tests/matrix.py` on 11-18, 11-13, Broadview, clinic, 200 notes, hostile, legacy, empty, both maps, and one note: no page errors, no script injection.
- `tests/relief_text.py` with the 3D on 11-18, 11-13, Broadview, clinic, and 200 notes: cards and the tour button present, no page errors.
- Both builds reproduce from source; `grep -c 'AAPK\|AIza'` = 0 in both files.
