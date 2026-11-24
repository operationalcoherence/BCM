# v261: ways laid on the ground (3D relief test, strategy 5; BCM_TASK_QUEUE.md "NOW · the 3D visual").
# The ways on Taking Action card maps were tubes floating above the ground. They are now bands that follow
# the ground: each way's own color, with a thin rim so it reads on any ground, taking the hills' shadows and
# hidden where a rise stands between it and the eye. The walk-a-way legs (v259) are laid the same way.
# Presentation only: no change to the routes, their order, colors, arrows, numbers, scoring, or wording.
p = "tools/relief/relief.js"
s = open(p, encoding="utf-8").read()

# 1. a band draped on the ground along a curve (only the curve's ground position is used)
old = "  const RC = { A: '#111111', B: '#f4f4f4', C: '#e0007a' }, WAYS = {}, PICK = [];"
assert s.count(old) == 1
s = s.replace(old, old + """
  /* v261: a band laid on the ground along a curve: width w, lifted by lift, n steps; t0..t1 a part of the curve; tip narrows it to a point */
  function ribbon(c, w, lift, n, t0, t1, tip) { t0 = t0 || 0; t1 = t1 == null ? 1 : t1; n = n || Math.max(60, Math.min(1400, Math.ceil(c.getLength() * (t1 - t0) / 0.7))); const P = [], pos = [], idx = [];
    for (let i = 0; i <= n; i++) P.push(c.getPointAt(t0 + (t1 - t0) * i / n));
    const hy = (x, z) => gH(x + W / 2, z + H / 2);
    for (let i = 0; i <= n; i++) { const a = P[Math.max(0, i - 1)], b = P[Math.min(n, i + 1)], dx = b.x - a.x, dz = b.z - a.z, l = Math.hypot(dx, dz) || 1, nx = -dz / l, nz = dx / l, ww = tip ? w * (1 - i / n) : w, y0 = hy(P[i].x, P[i].z);
      for (const sd of [-1, 1]) { const x = P[i].x + nx * ww / 2 * sd, z = P[i].z + nz * ww / 2 * sd; pos.push(x, Math.max(hy(x, z), y0, hy((x + P[i].x) / 2, (z + P[i].z) / 2)) + lift, z); } }
    for (let i = 0; i < n; i++) { const a = 2 * i; idx.push(a, a + 1, a + 2, a + 1, a + 3, a + 2); }
    const g = new THREE.BufferGeometry(); g.setAttribute('position', new THREE.Float32BufferAttribute(pos, 3)); g.setIndex(idx); g.computeVertexNormals(); return g; }
  const onGround = (m, o) => { m.side = THREE.DoubleSide; m.transparent = true; m.depthWrite = false; m.polygonOffset = true; m.polygonOffsetFactor = -o; m.polygonOffsetUnits = -o * 2; return m; };""", 1)

# 2. the way itself: a band on the ground with a rim, in place of the floating tube
old = """    const tube = new THREE.Mesh(new THREE.TubeGeometry(c, 700, 1.5, 8), mat); tube.castShadow = true; scene.add(tube);
    const edge = R.key === 'B' ? new THREE.Mesh(new THREE.TubeGeometry(c, 700, 1.9, 8), new THREE.MeshStandardMaterial({ color: '#222', transparent: true, opacity: 0.9, side: THREE.BackSide })) : null; if (edge) scene.add(edge);"""
assert s.count(old) == 1
s = s.replace(old, """    mat.roughness = 0.8; onGround(mat, 4 + ri);
    const tube = new THREE.Mesh(ribbon(c, 3.4, 1.1 + ri * 0.2), mat); tube.receiveShadow = true; tube.renderOrder = 3 + ri * 2; scene.add(tube);
    const edge = new THREE.Mesh(ribbon(c, 4.6, 0.9 + ri * 0.2), onGround(new THREE.MeshStandardMaterial({ color: R.key === 'B' ? '#222' : '#f3efe6', roughness: 0.9, transparent: true, opacity: 0.8 }), 3 + ri)); edge.receiveShadow = true; edge.renderOrder = 2 + ri * 2; scene.add(edge);""", 1)

# 3. arrowheads lie flat on the band, pointing the way it goes, with the same rim
old = """      const q = new THREE.Quaternion().setFromUnitVectors(up, tg), cone = new THREE.Mesh(new THREE.ConeGeometry(4.4, 10, 16), mat); cone.position.copy(at).addScaledVector(tg, 2); cone.quaternion.copy(q); cone.castShadow = true; scene.add(cone); arrows.push(cone);
      const ce = new THREE.Mesh(new THREE.ConeGeometry(5.3, 12, 16), shell); ce.position.copy(cone.position); ce.quaternion.copy(q); scene.add(ce); arrows.push(ce); }"""
assert s.count(old) == 1
s = s.replace(old, """      const dt = 11 / len, ta = Math.max(0, t - dt * 0.4), tb = Math.min(1, t + dt * 0.6);
      const cone = new THREE.Mesh(ribbon(c, 9, 1.5 + ri * 0.2, 16, ta, tb, true), mat); cone.renderOrder = 4 + ri * 2; scene.add(cone); arrows.push(cone);
      const ce = new THREE.Mesh(ribbon(c, 12.5, 1.5 + ri * 0.2, 16, Math.max(0, ta - dt * 0.12), Math.min(1, tb + dt * 0.12), true), shell); ce.renderOrder = 3 + ri * 2; scene.add(ce); arrows.push(ce); }""", 1)
old = "const shell = new THREE.MeshBasicMaterial({ color: R.key === 'B' ? '#222222' : '#ffffff', side: THREE.BackSide, transparent: true, opacity: 0.95 })"
assert s.count(old) == 1
s = s.replace(old, "const shell = onGround(new THREE.MeshBasicMaterial({ color: R.key === 'B' ? '#222222' : '#ffffff', transparent: true, opacity: 0.95 }), 3 + ri)", 1)

# 4. walk-a-way legs laid on the ground too (the leg's arrowhead lies flat as well)
old = """      const cone = new THREE.Mesh(new THREE.ConeGeometry(4.6, 11, 16), legMat); cone.position.copy(at).addScaledVector(tg, 1); cone.quaternion.copy(q); WG.add(cone);
      const ce = new THREE.Mesh(new THREE.ConeGeometry(5.5, 13, 16), legEdge); ce.position.copy(cone.position); ce.quaternion.copy(q); WG.add(ce); }"""
assert s.count(old) == 1
s = s.replace(old, """      const ll = t.c.getLength(), ta = Math.max(0, 1 - 13 / ll);
      WG.add(new THREE.Mesh(ribbon(t.c, 11, 1.9, 16, ta, 1, true), legMat)); WG.add(new THREE.Mesh(ribbon(t.c, 14.5, 1.8, 16, Math.max(0, ta - 1.5 / ll), 1, true), legEdge)); }""", 1)
old = "return { c, g: new THREE.TubeGeometry(c, Math.max(24, P.length * 4), r, 8) }; };"
assert s.count(old) == 1
s = s.replace(old, "return { c, g: ribbon(c, r * 2.4, r > 2.5 ? 1.6 : r > 1.5 ? 1.8 : 1.6) }; };", 1)
old = "legEdge = new THREE.MeshBasicMaterial({ color: '#111111', side: THREE.BackSide });"
assert s.count(old) == 1
s = s.replace(old, "legEdge = new THREE.MeshBasicMaterial({ color: '#111111' }); onGround(legMat, 9); onGround(legEdge, 8);", 1)
open(p, "w", encoding="utf-8").write(s)

p = "gsm-readable.js"; s = open(p, encoding="utf-8").read()
assert s.count('t.textContent = "v260"') == 1
s = s.replace('t.textContent = "v260"', 't.textContent = "v261"'); open(p, "w", encoding="utf-8").write(s)

# 5. the walked part of the way, laid on the ground as well
p = "tools/relief/relief.js"; s = open(p, encoding="utf-8").read()
old = "WG.add(new THREE.Mesh(t.g, new THREE.MeshStandardMaterial({ color: Wk.k === 'B' ? '#666666' : (RC[Wk.k] || '#111'), roughness: 0.5 })));"
assert s.count(old) == 1
s = s.replace(old, "WG.add(new THREE.Mesh(t.g, onGround(new THREE.MeshStandardMaterial({ color: Wk.k === 'B' ? '#666666' : (RC[Wk.k] || '#111'), roughness: 0.8 }), 7)));", 1)
open(p, "w", encoding="utf-8").write(s)

# 6. the leg draws over its rim, and both over the walked part and the ways
p = "tools/relief/relief.js"; s = open(p, encoding="utf-8").read()
old = "    const nm = Wk.names, to = nm[i], fr = nm[i - 1], lbl = z => typeof z === 'string' ? z : z.k;"
assert s.count(old) == 1
s = s.replace(old, "    WG.children.forEach(m => { m.renderOrder = m.material === legMat ? 22 : m.material === legEdge ? 21 : 20; });\n" + old, 1)
open(p, "w", encoding="utf-8").write(s)

# 7. where a rise hides part of the leg being walked, that part still shows, faintly, through the ground
p = "tools/relief/relief.js"; s = open(p, encoding="utf-8").read()
old = "legEdge = new THREE.MeshBasicMaterial({ color: '#111111' }); onGround(legMat, 9); onGround(legEdge, 8);"
assert s.count(old) == 1
s = s.replace(old, old + " const legGhost = new THREE.MeshBasicMaterial({ color: '#f2b400', transparent: true, opacity: 0.5, depthTest: false, depthWrite: false, side: THREE.DoubleSide });", 1)
old = "if (m.material !== legMat && m.material !== legEdge) m.material.dispose();"
assert s.count(old) == 1
s = s.replace(old, "if (m.material !== legMat && m.material !== legEdge && m.material !== legGhost) m.material.dispose();", 1)
old = "    if (t) { WG.add(new THREE.Mesh(t.g, legMat));"
assert s.count(old) == 1
s = s.replace(old, "    if (t) { WG.add(new THREE.Mesh(t.g, legMat)); WG.add(new THREE.Mesh(t.g.clone(), legGhost));", 1)
old = "WG.children.forEach(m => { m.renderOrder = m.material === legMat ? 22 : m.material === legEdge ? 21 : 20; });"
assert s.count(old) == 1
s = s.replace(old, "WG.children.forEach(m => { m.renderOrder = m.material === legMat ? 22 : m.material === legEdge ? 21 : m.material === legGhost ? 19 : 20; });", 1)
open(p, "w", encoding="utf-8").write(s)

# 8. a wider black rim on the leg, so the gold leg reads on the yellow ridge
p = "tools/relief/relief.js"; s = open(p, encoding="utf-8").read()
old = "const e = tube3(Wk.w.rp.slice(a, Math.max(a + 2, b + 1)), ri, 2.7)"
assert s.count(old) == 1
s = s.replace(old, "const e = tube3(Wk.w.rp.slice(a, Math.max(a + 2, b + 1)), ri, 3.6)", 1)
open(p, "w", encoding="utf-8").write(s)
