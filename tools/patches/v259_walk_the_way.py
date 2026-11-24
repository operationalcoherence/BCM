# v259: Taking Action — walk a way, one leg at a time (BCM_TASK_QUEUE.md, "VIZ: entangled strategies are
# unreadable", added 11-21 09:28; his ask 11-24 12:39: "not being able to trace where nonlinear strategies go and
# in what order"). Numbers and arrows were tried and were not enough. Claude's call among the queued options:
# step through the way one leg at a time with the rest dimmed, together with the way as an ordered list tied to
# its places. Each step shows only where the way has been (thin), the leg it is on now (bright, with an arrow),
# and a ring on the stop it is heading to; the note there lights up. A strip under the caption lists every stop
# in order (PRESENT › N6 › N4 › … › GOAL); tap any stop to jump there. Back, Next, and the arrow keys step;
# Escape or "Done" ends it. Presentation only: no change to the routes, their order, scoring, or wording
# elsewhere. Applies to every workbook's strategy and program cards.
p = "tools/relief/relief.js"
s = open(p, encoding="utf-8").read()

# 1. CSS
a = ".grel .tourcap .tp i{display:block;height:3px;background:#111;width:0}\n"
assert a in s
CSS = (
    ".grel .walkbar{display:flex;gap:8px;align-items:center;margin-top:9px}\n"
    ".grel .walkbar .bt{position:static;font:14px Questrial,Helvetica,Arial,sans-serif;padding:7px 14px;border-radius:18px;background:#fff;border:1px solid #222}\n"
    ".grel .walkbar .bt.wnx{background:#111;color:#fff;border-color:#fff;font-weight:700;box-shadow:0 2px 8px rgba(0,0,0,.3)}\n"
    ".grel .walkbar .bt:disabled{opacity:.35;cursor:default}\n"
    ".grel .bt.wgo{font-weight:700;background:#111;color:#fff;border-color:#111}\n"
    ".grel.walking .tourcap{display:block!important;pointer-events:auto;z-index:6;top:44px;max-width:min(620px,calc(100% - 24px));font-size:15px;padding:9px 13px}\n"
    ".grel.walking .tourcap .tt{font-size:17px}\n"
    ".grel.walking .tourcap .tx{font-size:14px;line-height:1.4;color:#333;max-height:4.3em;overflow:hidden}\n"
    ".grel .tourcap .wk{display:flex;flex-wrap:wrap;gap:3px 2px;margin-top:8px;padding-top:7px;border-top:1px solid #ddd;font:12px/1.2 Helvetica,Arial,sans-serif}\n"
    ".grel .tourcap .wk span{cursor:pointer;padding:2px 5px;border-radius:9px;border:1px solid #bbb;color:#888;background:#fff;white-space:nowrap}\n"
    ".grel .tourcap .wk span.dn{color:#111;border-color:#111}\n"
    ".grel .tourcap .wk span.at{color:#111;background:#f2b400;border-color:#111;font-weight:700}\n"
    ".grel .tourcap .wk span.fr{color:#fff;background:#111;border-color:#111;font-weight:700}\n"
    ".grel .tourcap .wk i{color:#999;font-style:normal;padding:2px 0}\n"
)
s = s.replace(a, a + CSS, 1)

# 2. keep each way's points, so a leg can be drawn on its own
old = "    WAYS[R.key] = { tube, edge, badges, mat, arrows, shell, nums };"
assert old in s
s = s.replace(old, "    WAYS[R.key] = { tube, edge, badges, mat, arrows, shell, nums, rp, ri, stops: R.stops || null, name: R.name };", 1)

# 3. the walk itself, after the tour code
anchor = "  bPlay.onclick = ev => { ev.stopPropagation(); startTour(); };"
assert anchor in s
WALK = r'''  /* v259: walk a way, one leg at a time (Taking Action cards). Only where the way has been, the leg it is on, and
     the stop it is heading to are shown; a strip lists every stop in order and any stop can be tapped. */
  var WALK = null; const WG = new THREE.Group(); scene.add(WG);
  const legMat = new THREE.MeshStandardMaterial({ color: '#f2b400', roughness: 0.4, emissive: '#5a3c00', emissiveIntensity: 0.35 }), legEdge = new THREE.MeshBasicMaterial({ color: '#111111', side: THREE.BackSide });
  const stopName = (sp, i, n) => { if (i === 0) return PL ? 'START' : 'PRESENT'; if (i === n - 1) return 'GOAL'; let b = null, bd = 4.5; D.notes.forEach(q => { const d = Math.hypot(q.x - sp[0], q.y - sp[1]); if (d < bd) { bd = d; b = q; } }); return b ? { k: (D.np || 'N') + b.k, n: b } : { k: 'a turn', n: null }; };
  function walkData(k) { const w = WAYS[k]; if (!w || !w.stops || w.stops.length < 3) return null; const rp = w.rp, st = [], idx = []; let from = 0;
    const extra = {}; w.stops.forEach((sp, i) => { if (i && Math.hypot(sp[0] - w.stops[i - 1][0], sp[1] - w.stops[i - 1][1]) < 3 && i < w.stops.length - 1) { (extra[st.length - 1] = extra[st.length - 1] || []).push(sp); return; } let bk = -1, bd = 1e9;
      for (let q = from; q < rp.length; q++) { const d = Math.hypot(rp[q][0] - sp[0], rp[q][1] - sp[1]); if (d < 4.5) { bk = q; break; } if (d < bd) { bd = d; bk = q; } }
      if (i === w.stops.length - 1) bk = rp.length - 1; if (i === 0) bk = 0; from = bk; st.push(sp); idx.push(bk); });
    const names = st.map((sp, i) => { const a = stopName(sp, i, st.length); if (typeof a === 'string' || !extra[i]) return a; const ks = [a.k]; extra[i].forEach(e => { const z = stopName(e, 1, 3); if (typeof z !== 'string' && z.n && ks.indexOf(z.k) < 0) ks.push(z.k); }); return { k: ks.join(' + '), n: a.n, all: ks }; });
    return { k, w, st, idx, names }; }
  const tube3 = (pts2, ri, r) => { const P = pts2.filter((p, q) => q % 2 === 0 || q === pts2.length - 1).map(p => new THREE.Vector3(X(p[0]), gH(p[0], p[1]) + 2 + ri * 0.4, Z(p[1]))); if (P.length < 2) return null; if (P.length === 2) P.splice(1, 0, P[0].clone().lerp(P[1], 0.5)); const c = new THREE.CatmullRomCurve3(P); return { c, g: new THREE.TubeGeometry(c, Math.max(24, P.length * 4), r, 8) }; };
  function walkClear() { while (WG.children.length) { const m = WG.children.pop(); m.geometry.dispose(); if (m.material !== legMat && m.material !== legEdge) m.material.dispose(); } }
  function walkShow(i) { const Wk = WALK; if (!Wk) return; const n = Wk.st.length; i = Math.max(1, Math.min(n - 1, i)); Wk.i = i; walkClear();
    const ri = Wk.w.ri, a = Wk.idx[i - 1], b = Wk.idx[i];
    if (a > 0) { const t = tube3(Wk.w.rp.slice(0, a + 1), ri, 0.9); if (t) WG.add(new THREE.Mesh(t.g, new THREE.MeshStandardMaterial({ color: Wk.k === 'B' ? '#666666' : (RC[Wk.k] || '#111'), roughness: 0.5 }))); }
    const t = tube3(Wk.w.rp.slice(a, Math.max(a + 2, b + 1)), ri, 2.1);
    if (t) { WG.add(new THREE.Mesh(t.g, legMat)); const e = tube3(Wk.w.rp.slice(a, Math.max(a + 2, b + 1)), ri, 2.7); if (e) WG.add(new THREE.Mesh(e.g, legEdge));
      const at = t.c.getPointAt(0.97), tg = t.c.getTangentAt(0.97).normalize(), q = new THREE.Quaternion().setFromUnitVectors(new THREE.Vector3(0, 1, 0), tg);
      const cone = new THREE.Mesh(new THREE.ConeGeometry(4.6, 11, 16), legMat); cone.position.copy(at).addScaledVector(tg, 1); cone.quaternion.copy(q); WG.add(cone);
      const ce = new THREE.Mesh(new THREE.ConeGeometry(5.5, 13, 16), legEdge); ce.position.copy(cone.position); ce.quaternion.copy(q); WG.add(ce); }
    const nm = Wk.names, to = nm[i], fr = nm[i - 1], lbl = z => typeof z === 'string' ? z : z.k;
    setSpot({ at: Wk.st[i], title: [fr, to].map(z => typeof z === 'string' ? '' : z.k).join(' ') });
    cap.innerHTML = '<div class="ta"></div><div class="tt"></div><div class="tx"></div><div class="wk"></div>'; cap.appendChild(wbar);
    cap.querySelector('.ta').textContent = 'WAY ' + Wk.k + ' · STEP ' + i + ' OF ' + (n - 1);
    cap.querySelector('.tt').textContent = 'From ' + lbl(fr) + ' to ' + lbl(to);
    const tn = typeof to === 'string' ? null : to.n, tx = to === 'GOAL' ? (D.goalText || 'The goal.') : tn ? (tn.e == null ? '' : D.emo[tn.e][0][0].toUpperCase() + D.emo[tn.e][0].slice(1) + '. ') + String(tn.t || '') : (typeof to === 'string' ? '' : 'The way turns here, between notes.');
    cap.querySelector('.tx').textContent = tx.length > 220 ? tx.slice(0, 217).replace(/\s+\S*$/, '') + '…' : tx;
    const wk = cap.querySelector('.wk'); nm.forEach((z, q) => { if (q) { const s2 = document.createElement('i'); s2.textContent = '›'; wk.appendChild(s2); } const sp = document.createElement('span'); sp.textContent = lbl(z); sp.className = q === i ? 'at' : q === i - 1 ? 'fr' : q < i ? 'dn' : ''; sp.title = q ? 'Go to step ' + q : 'The start'; sp.onclick = ev => { ev.stopPropagation(); walkShow(Math.max(1, q)); }; wk.appendChild(sp); });
    wPrev.disabled = i <= 1; wNext.textContent = i >= n - 1 ? 'Done' : 'Next ›'; walkCap(); dirty = true; }
  /* the caption keeps off the leg it describes: top left, else bottom left, bottom right, top right */
  const wv = new THREE.Vector3();
  function walkCap() { const Wk = WALK; if (!Wk) return; const cw = renderer.domElement.clientWidth, ch = renderer.domElement.clientHeight, pad = parseFloat(renderer.domElement.style.marginLeft) || 0, a = Wk.idx[Wk.i - 1], b = Wk.idx[Wk.i], P = [];
    for (let q = a; q <= b; q += Math.max(1, Math.floor((b - a) / 12))) P.push(Wk.w.rp[q]); P.push(Wk.w.rp[b]);
    const S = P.map(p => { wv.set(X(p[0]), gH(p[0], p[1]) + 2, Z(p[1])).project(camera); return [pad + (wv.x * 0.5 + 0.5) * cw, (-wv.y * 0.5 + 0.5) * ch]; });
    const w = cap.offsetWidth, h = cap.offsetHeight, W2 = wrap.clientWidth, H2 = wrap.clientHeight, m = 18;
    const C = [[pad + 12, 44], [pad + 12, H2 - h - 12], [W2 - w - 12, H2 - h - 12], [W2 - w - 12, 44]];
    let best = C[0], bn = 1e9; C.forEach(([x, y]) => { const n = S.filter(([sx, sy]) => sx > x - m && sx < x + w + m && sy > y - m && sy < y + h + m).length; if (n < bn) { bn = n; best = [x, y]; } });
    cap.style.left = Math.max(pad + 4, best[0]) + 'px'; cap.style.right = 'auto'; cap.style.top = Math.max(4, best[1]) + 'px'; }
  /* on a card shown in the page, the walk opens the card's full screen (as the tour does), and closes it again after */
  let walkFs = false; const cardFs = () => { const c = host.closest('.coa'); return c ? c.querySelector('.gtfsb') : null; };
  function walkStart(k) { if (TOUR) stopTour(); const Wk = walkData(k || selWay || 'A'); if (!Wk) return; WALK = Wk; wrap.classList.add('walking'); pinned = null; hideTip();
    const fb = cardFs(); if (D.card && fb && !host.closest('.gtfs-on')) { walkFs = true; fb.click(); setTimeout(() => { try { wrap.scrollIntoView({ block: 'nearest' }); } catch (e) {} }, 60); }
    Object.keys(WAYS).forEach(q => { const w = WAYS[q]; w.mat.opacity = q === Wk.k ? 0.22 : 0.06; if (w.edge) w.edge.material.opacity = q === Wk.k ? 0.15 : 0.05; if (w.shell) w.shell.opacity = 0.05; (w.nums || []).forEach(o => { o.hid = true; }); w.badges.forEach(b => { b.el.style.opacity = 0.2; }); });
    walkShow(1); }
  controls.addEventListener('end', () => { if (WALK) walkCap(); });
  function walkEnd() { if (!WALK) return; WALK = null; walkClear(); setSpot(null); wrap.classList.remove('walking'); cap.style.display = 'none'; cap.innerHTML = ''; cap.style.top = ''; cap.style.right = ''; showWays(); walkBtn();
    if (walkFs) { walkFs = false; const fb = cardFs(); if (fb && host.closest('.gtfs-on')) fb.click(); } dirty = true; }
  const wbar = document.createElement('div'); wbar.className = 'walkbar'; const wPrev = document.createElement('button'), wNext = document.createElement('button'), wEnd = document.createElement('button');
  wPrev.className = wEnd.className = 'bt'; wNext.className = 'bt wnx'; wPrev.textContent = '‹ Back'; wNext.textContent = 'Next ›'; wEnd.textContent = 'Stop walking'; [wPrev, wNext, wEnd].forEach(b2 => { b2.type = 'button'; wbar.appendChild(b2); });
  wPrev.onclick = ev => { ev.stopPropagation(); if (WALK) walkShow(WALK.i - 1); }; wNext.onclick = ev => { ev.stopPropagation(); if (!WALK) return; if (WALK.i >= WALK.st.length - 1) walkEnd(); else walkShow(WALK.i + 1); }; wEnd.onclick = ev => { ev.stopPropagation(); walkEnd(); };
  const bWalk = document.createElement('button'); bWalk.type = 'button'; bWalk.className = 'bt wgo'; bWalk.style.position = 'static';
  function walkBtn() { const k = selWay || 'A', d = WAYS[k] && WAYS[k].stops && WAYS[k].stops.length >= 3; bWalk.style.display = D.card && d ? '' : 'none'; bWalk.textContent = 'Walk way ' + k + ', step by step'; bWalk.title = 'Follow way ' + k + ' one leg at a time, in order'; }
  bWalk.onclick = ev => { ev.stopPropagation(); WALK ? walkEnd() : walkStart(); };
  document.addEventListener('keydown', e => { if (!WALK || !host.isConnected) return; if (e.key === 'ArrowRight') { e.preventDefault(); wNext.onclick(e); } else if (e.key === 'ArrowLeft') { e.preventDefault(); wPrev.onclick(e); } else if (e.key === 'Escape') walkEnd(); });
'''
s = s.replace(anchor, WALK + anchor, 1)

# 4. the button sits in the top bar, before Reset view
old = "  const bar = document.createElement('div'); bar.style.cssText = 'position:absolute;top:8px;right:8px;display:flex;gap:6px;z-index:3'; [bReset, bFs].forEach(b => { b.style.position = 'static'; bar.appendChild(b); });"
assert old in s
s = s.replace(old, "  const bar = document.createElement('div'); bar.style.cssText = 'position:absolute;top:8px;right:8px;display:flex;gap:6px;z-index:3'; [bReset, bFs].forEach(b => { b.style.position = 'static'; bar.appendChild(b); });\n  const barW = bar;", 1)
# append the walk button once it exists (after the walk code)
old2 = "  bPlay.onclick = ev => { ev.stopPropagation(); startTour(); };"
s = s.replace(old2, "  barW.insertBefore(bWalk, barW.firstChild); walkBtn();\n" + old2, 1)

# 5. choosing a way updates the button; a new choice ends a walk
old = "setWay(k) { if (k !== selWay) { selWay = k; showWays(); } }"
assert old in s
s = s.replace(old, "setWay(k) { if (k !== selWay) { selWay = k; if (WALK) walkEnd(); showWays(); walkBtn(); } }, walk(k) { walkStart(k); }, walking() { return WALK ? { k: WALK.k, i: WALK.i, n: WALK.st.length - 1, names: WALK.names.map(z => typeof z === 'string' ? z : z.k) } : null; }, walkStep(i) { walkShow(i); }, walkEnd() { walkEnd(); }", 1)

# 6. showWays keeps the walk's dimming (the ring stays still: no frame-by-frame redraw while walking)
old = "  function showWays() { const k = hovWay || selWay;"
assert old in s
s = s.replace(old, "  function showWays() { if (typeof WALK !== 'undefined' && WALK) return; const k = hovWay || selWay;", 1)
open(p, "w", encoding="utf-8").write(s)

q = "gsm-readable.js"
t = open(q, encoding="utf-8").read()
assert 't.textContent = "v258"' in t
t = t.replace('t.textContent = "v258"', 't.textContent = "v259"', 1)
open(q, "w", encoding="utf-8").write(t)
print("v259 applied")
