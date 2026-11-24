# v261 · Ways laid on the ground

Strategy 5 of the 3D relief test ("Routes as ribbons or worn trails laid on the surface, with shading and occlusion"; BCM_TASK_QUEUE.md, "NOW · the 3D visual"). His "up to speed" 11-24 15:00 after v258 to v260; Claude's plan for strategies 4 to 8 sent 15:05.

## What changed
- On Taking Action card maps, each way is a band lying on the ground instead of a tube floating above it. It follows every rise and dip, takes the hills' shadows, and is hidden where a rise stands between it and the eye.
- Each way keeps its color (A black, B white, C magenta) and gets a thin rim (light under A and C, dark under B) so it reads on any ground color.
- The arrowheads lie flat on the band, pointing the way it goes.
- Walk a way (v259): the leg being walked is a gold band with a wider black rim, so it reads on the yellow ridge too. Any part of it hidden behind a rise still shows faintly through the ground. The part already walked lies on the ground in the way's color.

## What did not change
The ways themselves (their points, order, and stops), the numbered stops, the A/B/C badges, picking and hovering a way, scoring, recommendations, and every word. Synthesis and Analysis (no ways) are pixel-identical to v260. Applies to every workbook and to place maps.

## Checked
- 11-20 copy, card with the most stops: all three ways read on the ground; crossings stay readable.
- walk.py on 11-20: every step, Back, Next, arrow keys, strip taps, Done, and Escape work; 60 frames per second while walking; no errors.
- tour.py on 11-20: all checks pass, no errors. matrix.py on 11-20, Broadview, clinic, big, empty, hostile, legacy: no errors. Broadview card map: both ways lie on the ground. No keys in either built file.
- New tool: tests/cardshot.py (a card map, full screen, same camera; CARD=n, DSF=2).

## Files
tools/patches/v261_ways_on_ground.py (tools/relief/relief.js: `ribbon()` and `onGround()` beside the way colors; the way tube, rim, arrowheads, and walk legs now use them; the label bump in gsm-readable.js).
