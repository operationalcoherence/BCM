# v263: a crisper crest along ridges (3D relief test, strategy 4; his go-ahead 11-24 16:16).
# Line maps only; place maps unchanged. Where the ground turns over a crest, a thin edge catches a little more light,
# as ridgelines do in his Bear Canyon photos. Read from the ground's own shape at a finer scale than the existing
# shading; it lightens only (at most 10%) and never darkens. Drainage channels were not added (water imagery).
# Presentation only: no change to heights, where rock sits, colors, notes, ways, or words.
p = "tools/relief/relief.js"
s = open(p, encoding="utf-8").read()
old = "if (!PL) ao = Math.max(-0.42, ao * 0.7 - aoAt(x, y) * 0.5); c = c.map(v => v * (1 + ao));"
assert s.count(old) == 1
s = s.replace(old, "if (!PL) { ao = Math.max(-0.42, ao * 0.7 - aoAt(x, y) * 0.5); const l1 = gH(x + e, y) + gH(x - e, y) + gH(x, y + e) + gH(x, y - e) - 4 * h; ao += Math.min(0.1, Math.max(0, -l1 - 0.02) * 0.6) * sstep(0.15, 0.5, s); } c = c.map(v => v * (1 + ao));", 1)
open(p, "w", encoding="utf-8").write(s)
p = "gsm-readable.js"; s = open(p, encoding="utf-8").read()
assert s.count('t.textContent = "v262"') == 1
s = s.replace('t.textContent = "v262"', 't.textContent = "v263"'); open(p, "w", encoding="utf-8").write(s)
