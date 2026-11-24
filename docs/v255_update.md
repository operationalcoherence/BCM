# v255: toward photorealism

His note (11-24 10:08): "it is a great improvement, but I am just not seeing that photo realism."

Patch: tools/patches/v255_photoreal.py (relief.js, plus the label in gsm-readable.js).

## What changed (line maps only)
- **Rock detail drawn on the graphics card.** Layers by height and grain are worked out for each point from its real 3D position. They stay sharp at any zoom and wrap around cliff faces instead of stretching down them. The detail shows only where the painted ground is already rock (a rock mask), so where rock sits is unchanged. Detail finer than a pixel fades out instead of flickering.
- **Painted rock detail toned down.** The top-down painted cracks and grain stretched into comb-like streaks on cliffs, so they are much lighter now and the card's detail does the work.
- **Light from a whole sky:** blue above and warm ground below, as outdoors, alongside the sun.
- **Finer ground:** 1.5 times as many points each way, so ledges are crisper.
- **Hollows shade a little deeper.**

## Tried and dropped
- A screen-space crevice shading pass (GTAO) flattened the picture and weakened the shadows.
- A ground twice as fine together with the card's rock detail was too heavy: the tour could not keep up in testing. 1.5 times as fine with lighter detail passes.
- Squiggly crack lines read as dried mud.

## What did not change
The notes' shape, the emotion colors at 60%, notes, ways, labels, and camera. Place maps are not touched (Broadview pixel-identical).

## The honest limit
The emotion colors cover the ground at 60% (his approved look, 11-12). A red or purple wash cannot look like a photograph. What can still be gained is in the rock's form and light, not its color. A lighter wash is his call alone.

## Cost
The first build is about 5.3 s on the 11-20 workbook in testing (v252: 2.2 s); after that it is cached.

## Tested
tour.py on 11-20 passes all stops. groundtap.py passes. matrix.py on 11-20, Broadview, and clinic: no errors. Screenshots on 11-20, 11-13, clinic, big, and Broadview. Key check 0.
