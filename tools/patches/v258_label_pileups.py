# v258: 3D label pile-ups (BCM_TASK_QUEUE.md, "NOW · the 3D visual", item 2; his go-ahead 11-24 12:39).
# Labels that sat on top of each other (N4/N5/N6 under the reading markers, N9 under Q.2,
# N21/N13, N14 under marker 8) now look for a free spot around their own pin: right, left,
# above, below and the corners, then a step further out. A label moved off its pin gets a
# short thin leader line back to it, so it is never mistaken for a neighbor. Other pins'
# heads count as taken ground, so a label never sits on someone else's pin. A label that
# was already clear stays exactly where it was. Presentation only: no change to the ground,
# the notes' positions, the routes, or any wording. Applies to every workbook and to place maps.
p = "tools/relief/relief.js"
s = open(p, encoding="utf-8").read()

# CSS for the leader line
a = ".grel .lb{position:absolute;left:0;top:0;white-space:nowrap}\n"
assert a in s
s = s.replace(a, a + ".grel .ldr{position:absolute;left:0;top:0;height:1px;background:rgba(20,20,20,.75);box-shadow:0 0 0 1px rgba(255,255,255,.55);transform-origin:0 50%;pointer-events:none;display:none}\n", 1)

# remember each note label's pin head, so other labels keep off it
old = "    NOBJ.push({ q: n.q, st, hd, lo, sp }); });"
assert old in s
s = s.replace(old, "    lo.head = hd.position; lo.isN = 1; NOBJ.push({ q: n.q, st, hd, lo, sp }); });", 1)

a = s.index("  function place() {")
b = s.index("  function loop() {")
NEW = r'''  /* v258: labels look for free ground around their own pin, and a moved label gets a leader line back to it */
  const hv = new THREE.Vector3(), hv2 = new THREE.Vector3();
  function place() { const w = renderer.domElement.clientWidth, h = renderer.domElement.clientHeight, boxes = [], heads = [];
    const up = new THREE.Vector3(0, 1, 0).applyQuaternion(camera.quaternion);
    L.forEach(o => { if (!o.head || o.hid || o.off) return; hv.copy(o.head).project(camera); if (hv.z > 1) return; hv2.copy(o.head).addScaledVector(up, 2.8).project(camera);
      const r = 1.5 * Math.max(3, Math.hypot((hv2.x - hv.x) * 0.5 * w, (hv2.y - hv.y) * 0.5 * h)); heads.push({ o, x: (hv.x * 0.5 + 0.5) * w, y: (-hv.y * 0.5 + 0.5) * h, r }); });
    const hitB = (x, y, bw, bh) => { let n = 0; for (const b of boxes) if (x < b[0] + b[2] && x + bw > b[0] && y < b[1] + b[3] && y + bh > b[1]) n += Math.min(x + bw, b[0] + b[2]) - Math.max(x, b[0]) + 1; return n; };
    const hitH = (o, x, y, bw, bh) => { let n = 0; if (!o.isN) return 0; for (const q of heads) { if (q.o === o) continue; const cx = Math.max(x, Math.min(q.x, x + bw)), cy = Math.max(y, Math.min(q.y, y + bh)); if ((cx - q.x) ** 2 + (cy - q.y) ** 2 < (q.r + 1) ** 2) n += 40 + q.r; } return n; };
    L.map(o => { v.copy(o.v).project(camera); o.sx = (v.x * 0.5 + 0.5) * w; o.sy = (-v.y * 0.5 + 0.5) * h; return { o, x: o.sx + o.ax, y: o.sy + o.ay, off: v.z > 1 }; })
     .sort((a, b) => b.o.pri - a.o.pri || a.o.sy - b.o.sy)
     .forEach(p => { const o = p.o; if (o.hid || p.off || p.x < -24 || p.x > w + 24 || p.y < -24 || p.y > h + 24) { o.el.style.display = 'none'; if (o.ld) o.ld.style.display = 'none'; return; } o.el.style.display = '';
       const bw = o.el.offsetWidth || 30, bh = o.el.offsetHeight || 16; let x = p.x, y = p.y;
       /* the side and axis words keep their places; everything else may move off a crowded spot */
       if (!/\bside\b/.test(o.el.className) && (hitB(x, y, bw, bh) || hitH(o, x, y, bw, bh))) {
         const ax = o.sx, ay = o.sy, g = 4, C = [];
         [0, 1, 2, 3].forEach(k => { const d = k * (bh + 2);
           C.push([p.x, p.y - d - (k ? 0 : 0)], [ax + g + d, ay - bh / 2], [ax - g - bw - d, ay - bh / 2], [ax - bw / 2, ay - g - bh - d], [ax - bw / 2, ay + g + d], [ax + g + d * 0.7, ay - g - bh - d * 0.7], [ax - g - bw - d * 0.7, ay - g - bh - d * 0.7], [ax + g + d * 0.7, ay + g + d * 0.7], [ax - g - bw - d * 0.7, ay + g + d * 0.7]); });
         let best = null, bs = 1e9;
         for (let i = 0; i < C.length; i++) { const [cx, cy] = C[i]; if (cx < 2 || cx + bw > w - 2 || cy < 2 || cy + bh > h - 2) continue; const sc = hitB(cx, cy, bw, bh) * 20 + hitH(o, cx, cy, bw, bh) * 20 + i; if (sc < bs) { bs = sc; best = C[i]; } if (sc === i) break; }
         if (best) { x = best[0]; y = best[1]; } }
       x = Math.max(2, Math.min(w - bw - 2, x)); boxes.push([x, y, bw, bh]); o.el.style.transform = `translate(${x.toFixed(1)}px,${y.toFixed(1)}px)`;
       /* a leader line when the label has left its pin */
       const ex = Math.max(x, Math.min(o.sx, x + bw)), ey = Math.max(y, Math.min(o.sy, y + bh)), dl = Math.hypot(ex - o.sx, ey - o.sy), far = Math.hypot(x - p.x, y - p.y) > 3;
       if (far && dl > 7) { if (!o.ld) { o.ld = document.createElement('div'); o.ld.className = 'ldr'; lbs.insertBefore(o.ld, lbs.firstChild); }
         const r0 = 3.5, L0 = dl - r0; o.ld.style.display = 'block'; o.ld.style.width = L0.toFixed(1) + 'px'; const an = Math.atan2(ey - o.sy, ex - o.sx); o.ld.style.transform = `translate(${(o.sx + Math.cos(an) * r0).toFixed(1)}px,${(o.sy + Math.sin(an) * r0).toFixed(1)}px) rotate(${an.toFixed(3)}rad)`; o.ld.style.opacity = o.el.style.opacity || ''; }
       else if (o.ld) o.ld.style.display = 'none'; }); }
'''
s = s[:a] + NEW + s[b:]
open(p, "w", encoding="utf-8").write(s)

# the reading markers' black balls count as taken ground too
old = "rim.position.copy(bl.position); scene.add(rim); o.rim = rim; return o; });"
assert old in s
s = s.replace(old, "rim.position.copy(bl.position); scene.add(rim); o.rim = rim; o.head = bl.position; return o; });", 1)
open(p, "w", encoding="utf-8").write(s)

# label bump
q = "gsm-readable.js"
t = open(q, encoding="utf-8").read()
assert 't.textContent = "v257"' in t
t = t.replace('t.textContent = "v257"', 't.textContent = "v258"', 1)
open(q, "w", encoding="utf-8").write(t)
print("v258 applied")
