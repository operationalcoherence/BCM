# v282: the emotion color wash on line maps goes from 60% to 45% (his call, 25 Nov 2026 17:07, after the
# side-by-side of 60, 45, and 30: "give me 45% (b)"). More of the rock and bedding shows through; the five
# emotions stay clear. Place maps keep their own wash (0.42), unchanged. Lighting unchanged ("the lighting
# levels all look the same to me"). Presentation only.
p = "tools/relief/relief.js"
s = open(p, encoding="utf-8").read()
assert s.count("ALPHA = 0.6,") == 1
s = s.replace("ALPHA = 0.6,", "ALPHA = 0.45,", 1)
open(p, "w", encoding="utf-8").write(s)
p = "gsm-readable.js"; s = open(p, encoding="utf-8").read()
assert s.count('t.textContent = "v281"') == 1
s = s.replace('t.textContent = "v281"', 't.textContent = "v282"'); open(p, "w", encoding="utf-8").write(s)
print("ok")
