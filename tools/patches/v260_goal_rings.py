# v260: goal rings over a label (BCM_TASK_QUEUE.md, "NOW · the 3D visual", item 2; his yes 11-24 14:45).
# The goal's white rings now count as taken ground when labels are placed, the same way other pins'
# heads do since v258. A note or marker label that would sit on a ring moves to the nearest free spot
# around its own pin, with a leader line back to it. The GOAL label and the side and axis words keep
# their places. Presentation only: no change to the ground, the notes' positions, the rings, the
# routes, or any wording. Applies to every workbook and to place maps.
p = "tools/relief/relief.js"
s = open(p, encoding="utf-8").read()

# 1. keep sample points along all three rings
old = "  [22, 14, 6].forEach(r => { const c = new THREE.CatmullRomCurve3(ringAt(D.GOAL.x, D.GOAL.y, r), true);"
assert s.count(old) == 1
s = s.replace(old, "  const RINGP = []; [22, 14, 6].forEach(r => { const q = ringAt(D.GOAL.x, D.GOAL.y, r); for (let k = 0; k < 64; k += (r > 10 ? 2 : 4)) RINGP.push(q[k]); });\n" + old, 1)

# 2. in place(): project the ring points, and count them as taken ground for every movable label but GOAL
old = "    const hitB = (x, y, bw, bh) => {"
assert s.count(old) == 1
s = s.replace(old, "    const rings = []; RINGP.forEach(q => { hv.copy(q).project(camera); if (hv.z <= 1) rings.push([(hv.x * 0.5 + 0.5) * w, (-hv.y * 0.5 + 0.5) * h]); });\n"
  "    const hitR = (o, x, y, bw, bh) => { if (o.el.textContent === 'GOAL') return 0; let n = 0; for (const r of rings) if (r[0] > x - 3 && r[0] < x + bw + 3 && r[1] > y - 3 && r[1] < y + bh + 3) n += 30; return n; };\n" + old, 1)

old = "(hitB(x, y, bw, bh) || hitH(o, x, y, bw, bh))) {"
assert s.count(old) == 1
s = s.replace(old, "(hitB(x, y, bw, bh) || hitH(o, x, y, bw, bh) || hitR(o, x, y, bw, bh))) {", 1)

old = "const sc = hitB(cx, cy, bw, bh) * 20 + hitH(o, cx, cy, bw, bh) * 20 + i;"
assert s.count(old) == 1
s = s.replace(old, "const sc = hitB(cx, cy, bw, bh) * 20 + hitH(o, cx, cy, bw, bh) * 20 + hitR(o, cx, cy, bw, bh) * 20 + i;", 1)
open(p, "w", encoding="utf-8").write(s)

# label bump
g = "gsm-readable.js"
t = open(g, encoding="utf-8").read()
assert 't.textContent = "v259"' in t
t = t.replace('t.textContent = "v259"', 't.textContent = "v260"', 1)
open(g, "w", encoding="utf-8").write(t)
print("ok")
