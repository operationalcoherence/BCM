# v254: the whole map reads as rock, not coral

His note (11-24 10:00), with a close-up and a wider view of v253: "this looks amazing! But the image as a whole still needs improvement, it looks more like corral than it looks like rock. we need to scale the image on the left to the image on the right." The close-up was right; the whole map was not.

Patch: tools/patches/v254_rock_not_coral.py (relief.js, plus the label in gsm-readable.js).

## Cause
The 3D adds small, even bumps over the shape the notes give the land, so the ground isn't smooth. They had no direction and were the same size everywhere, so from the normal view they read as coral.

## What changed (line maps only)
- **Steep ground** now steps down in bedded cliff bands that follow the slope. Hard layers stand out over soft ones, and a band fades in and out along its length, so no ring runs all the way around a pit. Treads between the bands take soil and grass; the cliff faces take rock, by the same slope rule as before.
- **Gentle ground** rolls instead of bubbling.
- The rock's color bands come from the same bedding as the ledges, so color and shape agree.

## Tried and dropped on the way
- Even ledges everywhere read as contour lines.
- A strong tilt read as wood grain.
- Every ledge running all the way around a pit read as a quarry.

## What did not change
The shape from the notes (`hRaw`, the land's data), the emotion colors, notes, ways, labels, and camera. Place maps are not touched (Broadview pixel-identical).

## Tested
Screenshots on 11-20, 11-13, clinic, big, and Broadview. groundtap.py and relief_text.py pass. matrix.py on 11-20 and Broadview shows no errors. Key check 0.
