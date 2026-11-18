"""v197: three of Gregory's 11-17 evening notes on the preview.
1. Pattern Synthesis (and every 3D map) carries THE BEAR CANYON METHOD · BY OPERATIONAL COHERENCE under the map,
   not only in full screen.
2. Indifference reads as one band: indifference notes are joined to their nearest indifference neighbors, and the
   yellow runs along those joins at full strength, through other emotions' ground (on his 11-13 map it now reaches
   N31 in the acceptance). Color only; the heights are unchanged. Line maps only (a place map keeps color by distance).
3. Ways on strategy cards drawn one way everywhere: a letter always means the same way (A its notes, B firm ground
   only, C from the support, even when there is no B), one badge per way, placed where that way runs on its own,
   and ways that share a stretch run side by side instead of on top of each other.
Usage: python3 v197_brand_ridge_ways.py gsm-readable.js  (and: python3 v197_brand_ridge_ways.py tools/relief/relief.js --relief)"""
import sys

P = sys.argv[1]
RELIEF = "--relief" in sys.argv
s = open(P).read()


def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, (c, a[:90])
    s = s.replace(a, b)


if RELIEF:
    # 1. the method's name under every 3D map (inside it in full screen, as before)
    rep(
        ".grel .attr{",
        ".grbrand{text-align:right;margin:5px 2px 0;font:12px Questrial,Helvetica,Arial,sans-serif;letter-spacing:.12em;color:#333}.grbrand b{font-weight:700}\n.grel .attr{",
    )
    rep(
        "  const leg = document.createElement('div'); leg.className = 'grleg'; host.appendChild(leg);",
        "  const foot = document.createElement('div'); foot.className = 'grbrand'; foot.innerHTML = '<b>THE BEAR CANYON METHOD</b> · BY OPERATIONAL COHERENCE'; host.appendChild(foot);\n"
        "  const leg = document.createElement('div'); leg.className = 'grleg'; host.appendChild(leg);",
    )
    rep(
        "wrap.classList.toggle('cfs', !!cfs); if (cfs) fillFsl(); leg.style.display = cfs ? 'none' : '';",
        "wrap.classList.toggle('cfs', !!cfs); if (cfs) fillFsl(); leg.style.display = foot.style.display = cfs ? 'none' : '';",
    )
    # 2. indifference as one band: join each indifference note to its nearest indifference neighbors
    rep(
        "  const EF = { w: 96 };",
        "  /* indifference reads as one band: its notes are joined (shortest links first, none longer than 95), and the yellow\n"
        "     runs along each join at full strength, through other emotions' ground. Color only; line maps only. */\n"
        "  const IND = RANK.indexOf(1), RIB = [];\n"
        "  if (IND >= 0 && !PL) { const P = EN.filter(n => n.e === IND), par = P.map((_, i) => i), top = i => par[i] === i ? i : (par[i] = top(par[i])), E = [];\n"
        "    for (let i = 0; i < P.length; i++) for (let j = i + 1; j < P.length; j++) E.push([Math.hypot(P[i].x - P[j].x, P[i].y - P[j].y), i, j]);\n"
        "    E.sort((a, b) => a[0] - b[0]).forEach(([d, i, j]) => { if (d > 95 || top(i) === top(j)) return; par[top(i)] = top(j); RIB.push([P[i].x, P[i].y, P[j].x, P[j].y]); }); }\n"
        "  const ribAt = (x, y) => { let w = 0; RIB.forEach(([ax, ay, bx, by]) => { const dx = bx - ax, dy = by - ay, t = Math.max(0, Math.min(1, ((x - ax) * dx + (y - ay) * dy) / (dx * dx + dy * dy || 1))), d2 = (ax + t * dx - x) ** 2 + (ay + t * dy - y) ** 2; w += 2.4 * Math.exp(-d2 / (2 * 8 * 8)); }); return w; };\n"
        "  const EF = { w: 96 };",
    )
    rep(
        "    EN.forEach(n => { ws[n.e] += Math.exp(-((n.x - x) ** 2 + (n.y - y) ** 2) / (2 * 26 * 26)); });",
        "    EN.forEach(n => { ws[n.e] += Math.exp(-((n.x - x) ** 2 + (n.y - y) ** 2) / (2 * 26 * 26)); }); if (RIB.length) ws[IND] += ribAt(x, y);",
    )
    rep("const EF = { w: 96 }; EF.h", "const EF = { w: 150 }; EF.h")  # finer field so the band stays crisp
    # a third channel carries the band's core, painted in plain yellow so it reads clearly, not as a blend
    rep("(K + 2)", "(K + 3)", 3)
    rep(
        "    EF.a[o + K] = sstep(0.04, 0.5, tot);",
        "    EF.a[o + K] = sstep(0.04, 0.5, tot); EF.a[o + K + 2] = RIB.length ? sstep(0.9, 2.0, ribAt(x, y)) : 0;",
    )
    rep("return [c, b(K), b(K + 1)]; }", "return [c, b(K), b(K + 1), b(K + 2)]; }")
    rep(
        "      let [em, st, gap] = emoMix(x, y); if (PL) gap = 0;",
        "      let [em, st, gap, rb] = emoMix(x, y); if (PL) gap = 0;",
    )
    rep(
        "      const o = (py * TW + pxx) * 4; px[o] = c[0];",
        "      if (rb > 0.01) c = mix(c, EMOC[IND].map(v => v * (0.9 + 0.1 * (1 + ao))), 0.8 * rb);\n      const o = (py * TW + pxx) * 4; px[o] = c[0];",
    )
    # 3. ways: side by side where they share ground; one badge each, where the way runs on its own
    rep(
        "  (D.routes || []).forEach((R, ri) => {\n    const pts = R.pts.filter((p, k) => k % 2 === 0 || k === R.pts.length - 1).map(p => new THREE.Vector3(X(p[0]), gH(p[0], p[1]) + 1.6 + ri * 0.4, Z(p[1])));",
        "  const NR = (D.routes || []).length, BADGE = [];\n"
        "  const nearOther = (x, y, ri) => { let m = 1e9; (D.routes || []).forEach((Q, qi) => { if (qi === ri) return; for (let k = 0; k < Q.pts.length; k += 2) m = Math.min(m, Math.hypot(Q.pts[k][0] - x, Q.pts[k][1] - y)); }); return m; };\n"
        "  (D.routes || []).forEach((R, ri) => {\n"
        "    const off = (ri - (NR - 1) / 2) * 2.6, rp = R.pts.map((p, k, a) => { const p0 = a[Math.max(0, k - 2)], p1 = a[Math.min(a.length - 1, k + 2)], dx = p1[0] - p0[0], dy = p1[1] - p0[1], l = Math.hypot(dx, dy) || 1;\n"
        "      return nearOther(p[0], p[1], ri) < 4 ? [p[0] - dy / l * off, p[1] + dx / l * off] : p; });\n"
        "    const pts = rp.filter((p, k) => k % 2 === 0 || k === rp.length - 1).map(p => new THREE.Vector3(X(p[0]), gH(p[0], p[1]) + 1.6 + ri * 0.4, Z(p[1])));",
    )
    rep(
        "    const badges = [0.22, 0.58].map(f => { const p = R.pts[Math.min(R.pts.length - 1, Math.floor(R.pts.length * (f + ri * 0.06)))]; const o = lab(R.key, 'wl', p[0], p[1], 5, 6, -13, -13, info);",
        "    let bi = Math.floor(rp.length / 2), bs = -1;\n"
        "    for (let f = 0.2; f <= 0.8; f += 0.04) { const k = Math.floor(rp.length * f), p = rp[k], sc = Math.min(nearOther(p[0], p[1], ri), 40) + Math.min(40, ...BADGE.map(b => Math.hypot(b[0] - p[0], b[1] - p[1])), 40) - Math.abs(f - 0.5) * 10; if (sc > bs) { bs = sc; bi = k; } }\n"
        "    BADGE.push(rp[bi]);\n"
        "    const badges = [rp[bi]].map(p => { const o = lab(R.key, 'wl', p[0], p[1], 5, 6, -13, -13, info);",
    )
    open(P, "w").write(s)
    sys.exit(0)

# engine: a letter always means the same way (the support way is C even when there is no firm-ground way B)
rep('key: ROUTES.length === 1 ? "B" : "C",', 'key: "C",')
s = s.replace('t.textContent = "v196"', 't.textContent = "v197"')
assert 't.textContent = "v197"' in s
open(P, "w").write(s)
