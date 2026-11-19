"""v245: fix for v244. On a place map with any note that has no emotion, the Synthesis 3D failed to start (the stop
"Notes with no emotion yet" has no spot on the map, and the 3D reads every Synthesis stop's spot), so the page fell back
to the flat line-map drawing (his report 11-19 12:18, Broadview). v244's patch script now puts that stop in the tour's
opening, which allows a stop with no spot; this script only bumps the label. Rebuild: run v244 (as amended), then v245.
Usage: python3 v245_place_tour_fix.py gsm-readable.js"""
import sys
P = sys.argv[1]
s = open(P).read()
a, b = 't.textContent = "v244"', 't.textContent = "v245"'
assert s.count(a) == 1; s = s.replace(a, b)
open(P, 'w').write(s)
print("v245 applied")
