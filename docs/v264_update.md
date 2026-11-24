# v264 · Far note labels fade a little

Strategy 6 of the 3D relief test (BCM_TASK_QUEUE.md, "NOW · the 3D visual"); his go-ahead 11-24 16:16. Label decluttering and leader lines were done in v258 and v260; this is the last part, the fade with distance.

## What changed
- Note labels on ground farther than the point the camera looks at fade gently, down to 65% at the far back, so the nearer labels lead the eye. It follows the zoom and the turn of the camera.
- A note label that is hovered, tapped, or lit by the tour or the walk shows in full.
- GOAL, the question flags, the way badges and numbers, and the side and axis words never fade.

## What did not change
Where labels sit, the ground, the pins, the ways, and every word.

## Checked
- 11-20 copy, Synthesis full screen: the back row of labels (N15, N39, N31, N28, N17) is slightly lighter; the front is unchanged.
- tour.py on 11-20: all checks pass, no errors. matrix.py on Broadview: no errors. No keys in either built file.

## Files
tools/patches/v264_far_labels.py (tools/relief/relief.js: the fade in `place()` for note labels, and a CSS rule that lifts it on hover, tap, and tour focus; the label bump in gsm-readable.js).
