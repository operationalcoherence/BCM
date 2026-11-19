"""v246: every tour (line map and place map; Analysis and Synthesis) gets Back and Next, and what the tour is talking
about glows (his ask 11-19 14:13: "forward and backward buttons but more importantly, I would like what is being talked
about to be illuminated somehow ... a white glow or outline that doesn't occlude the color").
The 3D part is in tools/relief/relief.js (edited directly):
  - a white ring on the ground around each stop's spot (thin bright line plus a soft wide glow, gently pulsing), drawn
    over the land so a hill never hides it; it is an outline, so the colors inside stay visible;
  - the notes the caption names (N5, P3, ...) get a white glowing badge while their stop is on;
  - Back and Next beside Play: jump to the stop before or after and play on from there; Next on the last stop ends.
This script only bumps the label. Usage: python3 v246_tour_spot_steps.py gsm-readable.js"""
import sys
P = sys.argv[1]
s = open(P).read()
a, b = 't.textContent = "v245"', 't.textContent = "v246"'
assert s.count(a) == 1; s = s.replace(a, b)
open(P, 'w').write(s)
print("v246 applied")
