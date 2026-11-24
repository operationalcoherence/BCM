# v264: far note labels fade a little (3D relief test, strategy 6; his go-ahead 11-24 16:16).
# Note labels on ground farther than the point the camera looks at fade gently, down to 65% at the far back, so the
# near labels lead the eye. Labels that move off a crowded spot (v258) already have their leader lines; this adds only
# the fade. GOAL, the question flags, the way badges and numbers, and the side and axis words never fade; a label
# that is hovered, tapped, or lit by the tour or the walk shows in full. Presentation only; every word unchanged.
p = "tools/relief/relief.js"
s = open(p, encoding="utf-8").read()
old = ".grel .lb.tfoc{"
assert s.count(old) == 1
s = s.replace(old, ".grel .lb.on,.grel .lb:hover,.grel .lb.tfoc{filter:none!important}" + old, 1)
old = "       x = Math.max(2, Math.min(w - bw - 2, x)); boxes.push([x, y, bw, bh]);"
assert s.count(old) == 1
s = s.replace(old, "       if (o.isN) { const dd = camera.position.distanceTo(o.v), d0 = camera.position.distanceTo(controls.target), fz = Math.max(0, Math.min(1, (dd - d0 * 0.95) / (d0 * 0.4))), fo = (1 - 0.35 * fz).toFixed(2); o.el.style.filter = fo === '1.00' ? '' : 'opacity(' + fo + ')'; }\n" + old, 1)
open(p, "w", encoding="utf-8").write(s)
p = "gsm-readable.js"; s = open(p, encoding="utf-8").read()
assert s.count('t.textContent = "v263"') == 1
s = s.replace('t.textContent = "v263"', 't.textContent = "v264"'); open(p, "w", encoding="utf-8").write(s)
