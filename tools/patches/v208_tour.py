"""v208: the guided tour of the ground on Pattern Synthesis (review 4c, his Play button request 11-18).
A "Play the tour" button on the Pattern Synthesis 3D map. The camera flies from reading to reading of WHAT
THE GROUND SAYS, in his four acts (the high ground, the low ground, between them, what keeps it this way),
turning slowly as it goes, and each stop is captioned with its act, number, title, and the data the reading
already carries (its notes, the share of the ground that slopes into it, and the climb, as a share of the
map's height, that getting out takes). About 25 seconds; it ends back at the starting view. A click on the
map, Escape, or Stop ends it at once. It is drawn live from the workbook, so it is always current.
Usage: python3 v208_tour.py gsm-readable.js   and   python3 v208_tour.py tools/relief/relief.js --relief"""
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
    rep(
        ".grbrand{",
        ".grel .tourcap{position:absolute;left:12px;right:12px;top:46px;z-index:3;max-width:560px;background:rgba(255,255,255,.95);border:1px solid #222;padding:7px 11px 8px;font:12.5px/1.4 Questrial,Helvetica,Arial,sans-serif;color:#222;display:none;pointer-events:none}"
        ".grel .tourcap .ta{font-size:11px;letter-spacing:.14em;font-weight:700;color:#666}.grel .tourcap .tt{font-weight:700;margin:2px 0 2px}"
        ".grel .tourcap .tp{height:3px;background:#e4e1d8;margin-top:7px}.grel .tourcap .tp i{display:block;height:3px;background:#111;width:0}\n.grbrand{",
    )
    rep(
        "  const bar = document.createElement('div'); bar.style.cssText = 'position:absolute;top:8px;right:8px;display:flex;gap:6px;z-index:3'; [bReset, bFs].forEach(b => { b.style.position = 'static'; bar.appendChild(b); });",
        "  const bPlay = document.createElement('button'); bPlay.className = 'bt'; bPlay.textContent = 'Play the tour';\n"
        "  const bar = document.createElement('div'); bar.style.cssText = 'position:absolute;top:8px;right:8px;display:flex;gap:6px;z-index:3'; [bPlay, bReset, bFs].forEach(b => { b.style.position = 'static'; bar.appendChild(b); });\n"
        "  if (D.card || !D.read || D.read.length < 2) bPlay.style.display = 'none';",
    )
    rep(
        "  bReset.onclick = () => { moved = false; home(); };",
        """  /* ---------- the guided tour of the ground (v208) ---------- */
  const cap = document.createElement('div'); cap.className = 'tourcap'; cap.setAttribute('aria-live', 'polite'); wrap.appendChild(cap);
  let TOUR = null;
  const ease = t => t < 0.5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2;
  function homePose() { const p = camera.position.clone(), t = controls.target.clone(); home(); const hp = camera.position.clone(), ht = controls.target.clone(); camera.position.copy(p); controls.target.copy(t); camera.lookAt(t); return [hp, ht]; }
  function capFor(i) { const r = D.read[i], G = D.groups || [];
    cap.innerHTML = '<div class="ta"></div><div class="tt"></div><div class="tx"></div><div class="tp"><i></i></div>';
    cap.querySelector('.ta').textContent = G[r.grp] || ''; cap.querySelector('.tt').textContent = (i + 1) + ' · ' + (r.title || ''); cap.querySelector('.tx').textContent = r.cap || r.text || ''; }
  function stopTour() { if (!TOUR) return; TOUR = null; controls.enabled = true; cap.style.display = 'none'; bPlay.textContent = 'Play the tour';
    RD.forEach(q => q.el.classList.remove('on')); if (D.onHL) D.onHL(null); moved = false; home(); dirty = true; }
  function startTour() { if (TOUR) return stopTour();
    const [hp, ht] = homePose(), dH = hp.distanceTo(ht), n = D.read.length, SL = +window.gsmTourSlow || 1, per = Math.max(1.6, Math.min(2.6, 25 / n)) * SL, fly = per * 0.45, legs = [];
    let from = [camera.position.clone(), controls.target.clone()];
    D.read.forEach((r, i) => { const t = new THREE.Vector3(X(r.at[0]), gH(r.at[0], r.at[1]), Z(r.at[1])), az = -0.55 + 1.1 * (n > 1 ? i / (n - 1) : 0.5), po = 0.74, d = Math.max(controls.minDistance + 10, dH * 0.55);
      const p = t.clone().add(new THREE.Vector3(Math.sin(po) * Math.sin(az), Math.cos(po), Math.sin(po) * Math.cos(az)).multiplyScalar(d));
      const lk = t.clone().add(new THREE.Vector3(0, d * 0.16, 0)); legs.push({ i, a: from, b: [p, lk], fly, hold: per - fly }); from = [p, lk]; });
    legs.push({ i: -1, a: from, b: [hp, ht], fly: 1.4 * SL, hold: 0 });
    let t0 = 0; legs.forEach(l => { l.t0 = t0; t0 += l.fly + l.hold; });
    TOUR = { legs, start: performance.now(), total: t0, cur: -2 }; controls.enabled = false; cap.style.display = 'block'; bPlay.textContent = 'Stop'; dirty = true; }
  function stepTour(now) { const T = TOUR, s = (now - T.start) / 1000; if (s >= T.total) { stopTour(); return; }
    let l = T.legs[0]; for (const x of T.legs) if (s >= x.t0) l = x;
    if (l.i !== T.cur) { T.cur = l.i; if (l.i >= 0) { capFor(l.i); RD.forEach((q, k) => q.el.classList.toggle('on', k === l.i)); if (D.onHL) D.onHL(l.i); } else { cap.style.display = 'none'; RD.forEach(q => q.el.classList.remove('on')); if (D.onHL) D.onHL(null); } }
    const u = ease(Math.min(1, (s - l.t0) / l.fly));
    camera.position.lerpVectors(l.a[0], l.b[0], u); controls.target.lerpVectors(l.a[1], l.b[1], u); camera.lookAt(controls.target);
    const pi = cap.querySelector('.tp i'); if (pi) pi.style.width = (100 * s / T.total).toFixed(1) + '%'; dirty = true; }
  bPlay.onclick = ev => { ev.stopPropagation(); startTour(); };
  renderer.domElement.addEventListener('pointerdown', () => { if (TOUR) stopTour(); });
  bReset.onclick = () => { if (TOUR) stopTour(); moved = false; home(); };""",
    )
    rep(
        "  const onKey = e => { if (e.key === 'Escape' && wrap.classList.contains('fs')) bFs.onclick(); };",
        "  const onKey = e => { if (e.key === 'Escape' && TOUR) { stopTour(); return; } if (e.key === 'Escape' && wrap.classList.contains('fs')) bFs.onclick(); };",
    )
    rep(
        "  function loop() { if (!alive) return; if (!host.isConnected) { dispose(); return; } controls.update();",
        "  function loop() { if (!alive) return; if (!host.isConnected) { dispose(); return; } if (TOUR) stepTour(performance.now()); else controls.update();",
    )
    rep(
        "  return { loops, focusQ, hl(i) {",
        "  return { loops, focusQ, tour: startTour, touring() { return !!TOUR; }, hl(i) {",
    )
else:
    # each reading carries its act and a caption: its first sentence, plus the sentence with a share or a climb
    rep(
        """          D.read = READ.map(function (r) {
            return { at: r.at, title: r.title, text: r.short + (r.more ? " " + r.more : "") };
          });""",
        """          D.read = READ.map(function (r) {
            var S = (r.short + (r.more ? " " + r.more : ""))
                .replace(/\\s+/g, " ")
                .split(/(?<=[.!?])\\s+(?=[A-Z0-9“"(])/)
                .filter(function (z) {
                  return z && !/question below/i.test(z);
                }),
              c = S.slice(0, 1);
            S.slice(1).some(function (z) {
              return /\\d+%/.test(z) && !/\\d+%/.test(c.join(" ")) && c.push(z);
            });
            c.length < 2 && S[1] && !/\\d+%/.test(c.join(" ")) && c.length && c[0].length < 90 && c.push(S[1]);
            return { at: r.at, title: r.title, text: r.short + (r.more ? " " + r.more : ""), grp: r.grp, cap: c.join(" ") };
          });
          D.groups = GROUPS;""",
    )
    s = s.replace('t.textContent = "v207"', 't.textContent = "v208"')
    assert 't.textContent = "v208"' in s
open(P, "w").write(s)
