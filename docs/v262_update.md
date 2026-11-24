# v262 · Distance haze on the 3D ground

Strategy 7 of the 3D relief test (BCM_TASK_QUEUE.md, "NOW · the 3D visual"); his go-ahead 11-24 16:16 ("this, then can we switch focuses?").

## What changed
- On line maps, ground farther away than the point the camera looks at fades slightly toward a pale sky color, the way distant ridges look in his Bear Canyon photos. At most a 20% fade at the far back edge, and it scales with the zoom, so zooming in on any part keeps it clear. Pins, flags, labels, and ways are not hazed.

## Tried and dropped
- A denser, smoother 3D surface (2 times, then 1.5 times the grid). It made no visible difference: the fine hatching on cliffs is the painted rock detail, not the mesh. At 2 times, tour.py timed out (frames too heavy). Not shipped.

## What did not change
Heights, colors, rock, notes, ways, labels, and every word. Place maps (Broadview) are pixel-identical to v261.

## Checked
- 11-20 copy, Synthesis full screen: the back of the map changes slightly (mean pixel change 2.5 of 255 at the back, 0.8 at the front).
- Broadview: pixel-identical. tour.py on 11-20: all checks pass, no errors. matrix.py on 11-20, Broadview, clinic: no errors. No keys in either built file.

## Files
tools/patches/v262_haze.py (tools/relief/relief.js: `HAZE` uniforms set in `draw()`, the haze step in the terrain shader; the label bump in gsm-readable.js).
