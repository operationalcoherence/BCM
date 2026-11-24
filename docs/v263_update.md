# v263 · A crisper crest along ridges

Strategy 4 of the 3D relief test (BCM_TASK_QUEUE.md, "NOW · the 3D visual"); his go-ahead 11-24 16:16.

## What changed
- On line maps, where the ground turns over a crest (the top edge of a cliff band, a ridgeline), a thin edge catches a little more light, as ridgelines do in his Bear Canyon photos. It lightens only, by at most 10%, and only on sloping ground.

## Not done, on purpose
- Drainage channels: they would read as water (his rule: no water imagery).
- Cliff bands for barriers: already in since v254.

## What did not change
Heights, where rock sits, colors, notes, ways, labels, and every word. Place maps (Broadview) are pixel-identical.

## Checked
- 11-20 copy, Synthesis full screen at 2× detail: about 5% of pixels change, all along crests. Broadview pixel-identical. matrix.py on 11-20: no errors. No keys in either built file.

## Files
tools/patches/v263_ridge_crest.py (tools/relief/relief.js: the crest term beside the horizon shading in `paint()`; the label bump in gsm-readable.js).
