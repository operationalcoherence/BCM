# v253: the 3D ground looks more like real Bear Canyon

His ask (11-24 09:37): "lets work on the 3d visual some more - bring that up in the task queue." Then, with five of his photos of Bear Canyon and the Flatirons (09:38): "Improve quality and realism only. Do not reinterpret or redesign."

Patch: tools/patches/v253_realism.py (relief.js, plus the label in gsm-readable.js).

## What changed (line maps only)
- **Rock** now looks like the sandstone in his photos. Its layers follow the contours with a slight tilt, each layer has its own buff, salmon, or gray tone, and each has a lip on top and an undercut below. The rock also shows cracks between blocks, thin joints across the layers, yellow-green lichen, and dark streaks running downslope. This covers the slope rock and the rock face where two distant emotions meet.
- **Soil** is the red decomposed granite of the trail, with scattered stones.
- **Grass** is dry and golden, with greener patches and fine tufts.
- **Fine relief:** a normal map carries the layers, cracks, stones, and tufts into the light, so they catch the sun and cast small shadows. The heights themselves are untouched.
- **Shading in hollows:** each spot is darkened by how much of the sky its own surroundings hide, which comes from the land's real heights.
- **Light:** the sky is slightly blue and the ground bounces warm light. The sun comes from the same side as before, but lower and warmer. Shadows are soft.

## What did not change
- The heights, where rock sits, and how far it reaches.
- The emotion colors at 60%, the indifference band, and each note's own patch (v252).
- Notes, questions, the goal, the ways, the numbered stops, the labels, the camera, and the layout.
- The average colors of rock and plain ground stay close to the old ones, so the legend's swatches still hold.
- Place maps are not touched. Broadview is pixel-identical before and after.

## Cost
On the test machine the land takes about 1.4 s longer to build the first time (3.6 s, up from 2.2 s on the 11-20 workbook). After that it is cached, as before.

## Tested
- Before-and-after 3D screenshots, same camera, on 11-20, 11-13, Broadview, clinic, big (200 notes), and same (12 identical notes), using the new tests/reliefshot.py.
- tour.py on 11-20 passes all 11 stops. groundtap.py passes. waymoves.py follows the ways.
- matrix.py on 11-20, 11-13, Broadview, and clinic: no errors.
- A Taking Action card map was checked by eye: the ways and stops are unchanged.
- The key check is 0 on both built files.
