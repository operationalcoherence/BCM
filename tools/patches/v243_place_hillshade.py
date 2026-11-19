"""v243: the place ground's benches and slopes read (his yes 11-19 11:47, after comparing v241 and v242 on Broadview).
The 3D part is in tools/relief/relief.js (edited directly), place maps only:
  - the exaggeration cap is ~140 units of rise (was 70), so a frame with a tall ridge in it (Broadview) still gets up to 2.5x;
  - a hillshade over the imagery: light from the northwest, 45 degrees up; slopes facing it lighten (up to +30%), slopes facing
    away darken (up to -45%); flat ground is unchanged.
This script bumps the label. Usage: python3 v243_place_hillshade.py gsm-readable.js"""
import sys
P = sys.argv[1]
s = open(P).read()
a, b = 't.textContent = "v242"', 't.textContent = "v243"'
assert s.count(a) == 1; s = s.replace(a, b)
open(P, 'w').write(s)
print("v243 applied")
