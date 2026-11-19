"""v242: the place ground shows its slopes, and its imagery is sharper (his note 11-19 11:15, on Broadview in Synthesis:
"I believe it should be higher resolution" and "its on the side of a mountain, it should show the stairstep elevation
gain as you go up the mountain, but it doesn't").
The 3D part is in tools/relief/relief.js (edited directly), place maps only (PL); the line map is untouched:
  - heights x up to 2.5 (VEX, capped so the rise stays under ~70 units, never below true scale): at true scale, ~100 m of climb across a ~1.5 km frame reads as flat; relief models exaggerate;
  - the place texture is 2560 px wide (was 1600), so the satellite image and its tile zoom are sharper;
  - the place legend gives the factor used.
This script updates the YOUR PLACE IN 3D intro line to match and bumps the label.
Usage: python3 v242_place_relief.py gsm-readable.js"""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)
rep("The ground is the real terrain, true to scale; emotion shows only as color.",
    "The ground is the real terrain, its heights exaggerated so the slopes show (the legend gives how much); emotion shows only as color.")
rep('t.textContent = "v241"', 't.textContent = "v242"')
open(P, 'w').write(s)
print("v242 applied")
