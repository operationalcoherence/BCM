"""v210: his notes on the tour (11-18, afternoon).
1. Play takes the map full screen; the tour's end (or Escape) brings it back, if Play opened it.
2. Play and Pause are one large button at the bottom center of the map, with End tour beside it while it plays.
3. The caption box and its text are larger (17 px body, 20 px title), and each stop is held for as long as its
   caption takes to read (3.3 words a second, 2.4 to 6 s), so the tour runs about a minute and a half.
4. The tour opens with READING THE GROUND: what color and height mean, what a move between emotions costs, which
   moves are feasible now (Vigneaux, 2026), and what bare rock is. The largest bare rock face gets its own
   reading under BETWEEN THEM (not when it is the pair already read under "Where it is easiest to fall from";
   then that reading says the ground between them is bare rock).
5. WHAT THE GROUND SAYS edited (Claude's wording, flagged): readings lead with what the ground does, not with a
   list of notes; "standing for it" (gone from the buttons since v198) becomes "supporting it", and the
   provisional sentence moves after the reading; the loop reading says what leads to what plainly.
7. Labels of points out of the frame are hidden instead of stacking along its edges. Escape in full screen
   left the button saying Close full screen (the engine's own Escape handler took the class off this map); fixed.
6. Pattern Analysis gets its own short tour: how to read this map (the high ground, the ridge, bare rock, the
   deepest ground, what a move costs), on the person's own notes. Pattern Synthesis keeps the reading of the ground.
Usage: python3 v210_tour_read.py tools/relief/relief.js --relief   and   python3 v210_tour_read.py gsm-readable.js"""
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
    # 3: larger caption; 2: the tour bar
    rep(
        ".grel .tourcap{position:absolute;left:12px;right:12px;top:46px;z-index:3;max-width:560px;background:rgba(255,255,255,.95);border:1px solid #222;padding:7px 11px 8px;font:12.5px/1.4 Questrial,Helvetica,Arial,sans-serif;color:#222;display:none;pointer-events:none}.grel .tourcap .ta{font-size:11px;letter-spacing:.14em;font-weight:700;color:#666}.grel .tourcap .tt{font-weight:700;margin:2px 0 2px}.grel .tourcap .tp{height:3px;background:#e4e1d8;margin-top:7px}",
        ".grel .tourcap{position:absolute;left:12px;right:12px;top:48px;z-index:3;max-width:640px;background:rgba(255,255,255,.96);border:1px solid #222;box-shadow:0 2px 10px rgba(0,0,0,.25);padding:12px 16px 12px;font:17px/1.5 Questrial,Helvetica,Arial,sans-serif;color:#111;display:none;pointer-events:none}.grel .tourcap .ta{font-size:12.5px;letter-spacing:.14em;font-weight:700;color:#555}.grel .tourcap .tt{font-weight:700;font-size:20px;line-height:1.3;margin:3px 0 4px}.grel .tourcap .tp{height:4px;background:#e4e1d8;margin-top:10px}"
        ".grel .tourbar{position:absolute;bottom:44px;left:50%;transform:translateX(-50%);z-index:4;display:flex;gap:10px;align-items:center}.grel .tourbar .bt{position:static}.grel .tourbar .tpb{font:bold 17px Questrial,Helvetica,Arial,sans-serif;padding:11px 24px 11px 20px;background:#111;color:#fff;border:2px solid #fff;border-radius:28px;box-shadow:0 2px 10px rgba(0,0,0,.35);letter-spacing:.02em}.grel .tourbar .tpb::before{content:'\\\\25B6';display:inline-block;margin-right:10px;font-size:14px}.grel .tourbar .tpb[data-st=pause]::before{content:'\\\\275A\\\\275A';font-size:12px;letter-spacing:-2px}.grel .tourbar .tpb:hover{background:#7a1d12}.grel .tourbar .tpe{font:14px Questrial,Helvetica,Arial,sans-serif;padding:8px 14px;border-radius:20px;background:#fff;border:1px solid #222;display:none}",
    )
    # 2: the play button leaves the corner bar for the bottom center
    rep(
        "const bPlay = document.createElement('button'); bPlay.className = 'bt'; bPlay.textContent = 'Play the tour';\n  const bar = document.createElement('div'); bar.style.cssText = 'position:absolute;top:8px;right:8px;display:flex;gap:6px;z-index:3'; [bPlay, bReset, bFs].forEach(b => { b.style.position = 'static'; bar.appendChild(b); });\n  if (D.card || !D.read || D.read.length < 2) bPlay.style.display = 'none';",
        "const bPlay = document.createElement('button'); bPlay.className = 'bt tpb'; bPlay.textContent = 'Play the tour'; bPlay.dataset.st = 'play';\n  const bEnd = document.createElement('button'); bEnd.className = 'bt tpe'; bEnd.textContent = 'End tour';\n  const tbar = document.createElement('div'); tbar.className = 'tourbar'; tbar.appendChild(bPlay); tbar.appendChild(bEnd); wrap.appendChild(tbar);\n  const TL = (D.intro || []).concat(D.read || []), NI = (D.intro || []).length;\n  const bar = document.createElement('div'); bar.style.cssText = 'position:absolute;top:8px;right:8px;display:flex;gap:6px;z-index:3'; [bReset, bFs].forEach(b => { b.style.position = 'static'; bar.appendChild(b); });\n  if (D.card || TL.length < 2) tbar.style.display = 'none';",
    )
    # 3 + 4: captions for the introduction and the readings
    rep(
        "  function capFor(i) { const r = D.read[i], G = D.groups || [];",
        "  function capFor(i) { const r = TL[i], G = D.groups || [];",
    )
    rep(
        "cap.querySelector('.ta').textContent = G[r.grp] || ''; cap.querySelector('.tt').textContent = (i + 1) + ' · ' + (r.title || '');",
        "cap.querySelector('.ta').textContent = r.act || G[r.grp] || ''; cap.querySelector('.tt').textContent = (i < NI ? '' : (i - NI + 1) + ' · ') + (r.title || '');",
    )
    rep(
        "  function stopTour() { if (!TOUR) return; TOUR = null; controls.enabled = true; cap.style.display = 'none'; bPlay.textContent = 'Play the tour'; bPlay.title = '';",
        "  let autoFs = false;\n  function stopTour() { if (!TOUR) return; TOUR = null; controls.enabled = true; cap.style.display = 'none'; bPlay.textContent = 'Play the tour'; bPlay.dataset.st = 'play'; bPlay.title = ''; bEnd.style.display = 'none';\n    if (autoFs) { autoFs = false; if (wrap.classList.contains('fs')) bFs.onclick(); }",
    )
    rep(
        "controls.enabled = true; bPlay.textContent = 'Play'; dirty = true; }",
        "controls.enabled = true; bPlay.textContent = 'Play'; bPlay.dataset.st = 'play'; dirty = true; }",
    )
    rep(
        "T.paused = null; controls.enabled = false; bPlay.textContent = 'Pause'; pinned = null;",
        "T.paused = null; controls.enabled = false; bPlay.textContent = 'Pause'; bPlay.dataset.st = 'pause'; pinned = null;",
    )
    # 1 + 3 + 4: full screen on Play; stops from the introduction and the readings; hold as long as the caption takes
    rep(
        "    const [hp, ht] = homePose(), dH = hp.distanceTo(ht), n = D.read.length, SL = +window.gsmTourSlow || 1, per = Math.max(1.8, Math.min(2.8, 30 / n)) * SL, fly = per * 0.45, legs = [];",
        "    if (!D.card && !wrap.classList.contains('fs')) { autoFs = true; bFs.onclick(); }\n    const [hp, ht] = homePose(), dH = hp.distanceTo(ht), n = TL.length, SL = +window.gsmTourSlow || 1, fly = 1.2 * SL, legs = [];\n    const hold = r => Math.max(2.4, Math.min(6, String((r.title || '') + ' ' + (r.cap || r.text || '')).split(/\\s+/).length / 3.3)) * SL;",
    )
    rep(
        "    D.read.forEach((r, i) => { const t = new THREE.Vector3(",
        "    TL.forEach((r, i) => { if (!r.at) { legs.push({ i, a: from, b: [hp.clone(), ht.clone()], fly, hold: hold(r) }); from = [hp.clone(), ht.clone()]; return; } const t = new THREE.Vector3(",
    )
    rep(
        "legs.push({ i, a: from, b: [p, lk], fly, hold: per - fly }); from = [p, lk]; });",
        "legs.push({ i, a: from, b: [p, lk], fly, hold: hold(r) }); from = [p, lk]; });",
    )
    rep(
        "cap.style.display = 'block'; bPlay.textContent = 'Pause'; bPlay.title = 'Reset view or Escape ends the tour';",
        "cap.style.display = 'block'; bPlay.textContent = 'Pause'; bPlay.dataset.st = 'pause'; bPlay.title = 'Escape also ends the tour'; bEnd.style.display = 'inline-block';",
    )
    rep(
        "if (l.i >= 0) { capFor(l.i); RD.forEach((q, k) => q.el.classList.toggle('on', k === l.i)); if (D.onHL) D.onHL(l.i); }",
        "if (l.i >= 0) { capFor(l.i); const ri = l.i - NI; RD.forEach((q, k) => q.el.classList.toggle('on', k === ri)); if (D.onHL) D.onHL(ri >= 0 ? ri : null); }",
    )
    rep(
        "  bPlay.onclick = ev => { ev.stopPropagation(); startTour(); };",
        "  bPlay.onclick = ev => { ev.stopPropagation(); startTour(); }; bEnd.onclick = ev => { ev.stopPropagation(); stopTour(); };",
    )
    # Escape in full screen: the engine's own Escape handler took the class off this map and left the button saying
    # "Close full screen" (and threw). It now skips this map, and the button always follows the real state.
    rep(
        "  const onKey = e => { if (e.key === 'Escape' && TOUR) { stopTour(); return; } if (e.key === 'Escape' && wrap.classList.contains('fs')) bFs.onclick(); };",
        "  const onKey = e => { if (e.key !== 'Escape') return; if (TOUR) stopTour(); else if (wrap.classList.contains('fs')) bFs.onclick(); const on = wrap.classList.contains('fs'); if ((bFs.textContent === 'Close full screen') !== on) { bFs.textContent = on ? 'Close full screen' : 'Full screen'; if (!on) document.documentElement.style.overflow = ''; moved = false; size(); } };",
    )
    # labels of things out of the frame no longer pile up along its edges (most visible during the tour)
    rep(
        "if (p.off) { p.o.el.style.display = 'none'; return; }",
        "if (p.off || p.x < -24 || p.x > w + 24 || p.y < -24 || p.y > h + 24) { p.o.el.style.display = 'none'; return; }",
    )
    # 2: the bar stays centered on the map, clear of the legend drawer
    rep(
        "if (typeof cap !== 'undefined') cap.style.left = pad + 12 + 'px';",
        "if (typeof cap !== 'undefined') cap.style.left = pad + 12 + 'px'; if (typeof tbar !== 'undefined') tbar.style.left = pad + vw / 2 + 'px';",
    )
else:
    rep(
        '''        var e = Rt.querySelector(".pnet.fs");''',
        '''        var e = Rt.querySelector(".pnet.fs:not(.grel)");''',
    )
    # 5: WHAT THE GROUND SAYS, Claude's wording
    rep(
        """      if (ask.length)
        out.unshift(
          "Until you answer the question below, this counts " +
            list(
              ask.map(function (a) {
                return a.id;
              }),
            ) +
            " as standing for it.",
        );""",
        """      if (ask.length)
        out.push(
          "Until you answer the question below, " +
            list(
              ask.map(function (a) {
                return a.id;
              }),
            ) +
            (ask.length > 1 ? " count" : " counts") +
            " as supporting it.",
        );""",
    )
    rep(
        """        "What " +
          list(entry) +
          " describe" +
          (entry.length > 1 ? "" : "s") +
          " leads to " +
          ce.w +
          ", and in " +
          list(exit) +
          " " +
          ce.w +
          " leads on to something else." +""",
        """        list(entry) +
          " name" +
          (entry.length > 1 ? "" : "s") +
          " what leads to " +
          ce.w +
          ", and " +
          list(exit) +
          " name" +
          (exit.length > 1 ? "" : "s") +
          " what " +
          ce.w +
          " leads to in turn." +""",
    )
    rep(
        """          short:
            ks(pt.ks) + ". About " + Math.round(pt.share * 100) + "% of the ground slopes down into here.",""",
        """          short:
            Math.round(pt.share * 100) +
            "% of the ground slopes down into this hollow" +
            emoOf(pt.ks) +
            (pt.ks.length ? ", around " + nks(pt.ks) : "") +
            ".",""",
    )
    rep(
        """          short: ks(h.ks) + ". " + f[0],""",
        """          short: "High ground" + emoOf(h.ks) + (h.ks.length ? " around " + nks(h.ks) : "") + ". " + f[0],""",
    )
    # helpers next to firstSentence
    rep(
        """    function firstSentence(t) {""",
        """    function nks(a) {
      return list(
        a.map(function (k) {
          return "N" + k;
        }),
      );
    }
    function emoOf(a) {
      /* " of aggression and defiance": the emotions the notes carry, most common first */
      var c = {};
      a.forEach(function (k) {
        var n = terr.notes.filter(function (m) {
          return m.k === k;
        })[0];
        n && null != n.e && (c[n.e] = (c[n.e] || 0) + 1);
      });
      var e = Object.keys(c).sort(function (x, y) {
        return c[y] - c[x];
      });
      return e.length && e.length < 4
        ? " of " +
            list(
              e.map(function (k) {
                return EMO[k][0].toLowerCase();
              }),
            )
        : "";
    }
    var RKE = [3, 0, 2, 1, 4],
      STEPW = ["", "one step", "two steps", "three steps", "four steps"],
      FALLPAIR = null;
    function rockFaces() {
      /* the same rule the 3D relief uses to lay bare rock: the two strongest emotions nearby are nearly balanced and
         two or more steps apart, and neither is indifference; on line maps indifference reads as one joined band */
      var NS = terr.notes.filter(function (n) {
          return null != n.e;
        }),
        rib = [];
      if (!PLACE) {
        var P = NS.filter(function (n) {
            return n.e === 3;
          }),
          par = P.map(function (_, i) {
            return i;
          }),
          top = function (i) {
            return par[i] === i ? i : (par[i] = top(par[i]));
          },
          E = [];
        for (var i = 0; i < P.length; i++)
          for (var j = i + 1; j < P.length; j++) E.push([Math.hypot(P[i].x - P[j].x, P[i].y - P[j].y), i, j]);
        E.sort(function (a, b) {
          return a[0] - b[0];
        }).forEach(function (e) {
          if (e[0] > 95 || top(e[1]) === top(e[2])) return;
          par[top(e[1])] = top(e[2]);
          rib.push([P[e[1]].x, P[e[1]].y, P[e[2]].x, P[e[2]].y]);
        });
      }
      var sst = function (a, b, x) {
          var t = Math.max(0, Math.min(1, (x - a) / (b - a)));
          return t * t * (3 - 2 * t);
        },
        cells = 0,
        rk = 0,
        by = {};
      for (var y = 4; y < HH; y += 4)
        for (var x = 4; x < W; x += 4) {
          var ws = [0, 0, 0, 0, 0],
            nb = [null, null, null, null, null],
            nd = [1e9, 1e9, 1e9, 1e9, 1e9];
          NS.forEach(function (n) {
            var d2 = (n.x - x) * (n.x - x) + (n.y - y) * (n.y - y);
            ws[n.e] += Math.exp(-d2 / 1352);
            d2 < nd[n.e] && ((nd[n.e] = d2), (nb[n.e] = n));
          });
          rib.forEach(function (r) {
            var dx = r[2] - r[0],
              dy = r[3] - r[1],
              t = Math.max(0, Math.min(1, ((x - r[0]) * dx + (y - r[1]) * dy) / (dx * dx + dy * dy || 1))),
              d2 = Math.pow(r[0] + t * dx - x, 2) + Math.pow(r[1] + t * dy - y, 2);
            ws[3] += 2.4 * Math.exp(-d2 / 128);
          });
          var tot = ws[0] + ws[1] + ws[2] + ws[3] + ws[4];
          if (sst(0.04, 0.5, tot) < 0.3) continue;
          cells++;
          var o = [0, 1, 2, 3, 4].sort(function (a, b) {
              return ws[b] - ws[a];
            }),
            k1 = o[0],
            k2 = o[1];
          if (
            Math.abs(RKE[k1] - RKE[k2]) < 2 ||
            RKE[k1] === 1 ||
            RKE[k2] === 1 ||
            ws[k2] < 0.03 ||
            sst(0.22, 0.42, ws[k2] / (ws[k1] + ws[k2])) <= 0.5
          )
            continue;
          rk++;
          var a = nb[k1],
            b = nb[k2];
          if (!a || !b) continue;
          var key = Math.min(a.k, b.k) + "|" + Math.max(a.k, b.k),
            f = by[key] || (by[key] = { a: a, b: b, d: Math.abs(RKE[a.e] - RKE[b.e]), c: [] });
          f.c.push([x, y]);
        }
      var L = Object.keys(by)
        .map(function (k) {
          return by[k];
        })
        .sort(function (p, q) {
          return q.c.length * q.d - p.c.length * p.d;
        });
      L.forEach(function (f) {
        var cx = 0,
          cy = 0;
        f.c.forEach(function (c) {
          cx += c[0];
          cy += c[1];
        });
        cx /= f.c.length;
        cy /= f.c.length;
        f.at = f.c.slice().sort(function (p, q) {
          return Math.hypot(p[0] - cx, p[1] - cy) - Math.hypot(q[0] - cx, q[1] - cy);
        })[0];
        /* uphill is toward acceptance: name the lower emotion first when telling the climb */
        f.lo = RKE[f.a.e] > RKE[f.b.e] ? f.a : f.b;
        f.hi = f.lo === f.a ? f.b : f.a;
      });
      return { share: cells ? rk / cells : 0, faces: L };
    }
    function rockReading(R) {
      if (PLACE) return;
      var rf = rockFaces(),
        fall = null;
      R.forEach(function (r) {
        r.kind === "fall" && (fall = r);
      });
      var same = function (f) {
          return FALLPAIR && ((f.a.k === FALLPAIR[0] && f.b.k === FALLPAIR[1]) || (f.a.k === FALLPAIR[1] && f.b.k === FALLPAIR[0]));
        },
        f = rf.faces.filter(function (f) {
          return !same(f);
        })[0];
      if (fall && rf.faces.some(same))
        fall.more +=
          " The ground between them is bare rock, the costliest crossing on the map.";
      if (!f) return;
      var lo = EMO[f.lo.e][0].toLowerCase(),
        hi = EMO[f.hi.e][0].toLowerCase(),
        ind = nn(f.at[0], f.at[1], [3]),
        sh = Math.round(rf.share * 100);
      R.push({
        grp: 2,
        kind: "rock",
        title: "Bare rock between N" + f.hi.k + " and N" + f.lo.k,
        short:
          "Here " + hi + " (N" + f.hi.k + ") meets " + lo + " (N" + f.lo.k + ") with no indifference between them, so the ground turns to bare rock.",
        more:
          "Bare rock marks the costliest moves on the map. Every move between emotions takes energy in either direction, and the farther apart the two emotions are, the more it takes; these are " +
          STEPW[f.d] +
          " apart. The climb from " +
          lo +
          " up to " +
          hi +
          " is the hard one; the drop the other way is easy, so " +
          hi +
          " beside bare rock needs tending. Most moves go through indifference (Vigneaux, 2026), so the feasible way across goes around" +
          (ind ? ", by N" + ind.k : ", through indifference") +
          "." +
          (sh ? " About " + sh + "% of the colored ground is bare rock." : ""),
        cap:
          "Here " + hi + " (N" + f.hi.k + ") meets " + lo + " (N" + f.lo.k + ") with no indifference between them, so the ground turns to bare rock. Crossing it is the costliest move on the map; the feasible way goes around" +
          (ind ? ", by the indifference at N" + ind.k : ", through indifference") +
          ".",
        at: f.at,
      });
    }
    function introStops(primer) {
      /* the tour's opening (Pattern Synthesis) and the whole of the Pattern Analysis tour; Claude's wording */
      var act = "READING THE GROUND",
        N = terr.notes.filter(function (n) {
          return null != n.e;
        }),
        out = [],
        cost =
          "Every move between emotions takes energy. Climbing takes far more than falling, and the farther apart two emotions are, the more a move costs. Most moves go through indifference. From acceptance and indifference, change can start now; from distrust, aggression, and defiance, it is unlikely in the short or medium term (Vigneaux, 2026).";
      if (PLACE) {
        out.push({ act: act, title: "How to read this map", cap: "Each color is an emotion your notes carry, painted where you placed them; the ground is the real terrain. Where it has no color, no notes are nearby, so there is no information there.", at: null });
        out.push({ act: act, title: "What a move costs", cap: cost, at: null });
        return out;
      }
      out.push({
        act: act,
        title: "How to read this ground",
        cap: "Each color is an emotion your notes carry. Height follows the order in Vigneaux (2026): acceptance is the high ground, indifference a ridge, then distrust, aggression, and defiance, the deepest ground.",
        at: null,
      });
      if (!primer) {
        out.push({ act: act, title: "What a move costs", cap: cost + " Gray bare rock is where distant emotions meet with no indifference between them: the costliest crossing.", at: null });
        return out;
      }
      var by = function (e) {
          return N.filter(function (n) {
            return n.e === e;
          }).sort(function (a, b) {
            return hAt(b.x, b.y) - hAt(a.x, a.y);
          });
        },
        acc = by(1),
        ind = by(3),
        low = N.slice().sort(function (a, b) {
          return hAt(a.x, a.y) - hAt(b.x, b.y);
        })[0];
      acc.length &&
        out.push({
          act: act,
          title: "The high ground: acceptance",
          cap: "N" + acc[0].k + " sits on the highest ground. Acceptance is where the goal already has people with it, the place to build from first.",
          at: [acc[0].x, acc[0].y],
        });
      ind.length &&
        out.push({
          act: act,
          title: "The ridge: indifference",
          cap:
            nks(
              ind
                .slice(0, 5)
                .map(function (n) {
                  return n.k;
                })
                .sort(function (a, b) {
                  return a - b;
                }),
            ) +
            (ind.length > 1 ? " are" : " is") +
            " indifference, the emotion of transition (Vigneaux, 2026). No one here is for or against the goal yet. Most moves between emotions go along a ridge like this.",
          at: [ind[0].x, ind[0].y],
        });
      var rf = rockFaces().faces[0];
      rf &&
        out.push({
          act: act,
          title: "Bare rock",
          cap:
            "Where " +
            EMO[rf.hi.e][0].toLowerCase() +
            " (N" +
            rf.hi.k +
            ") meets " +
            EMO[rf.lo.e][0].toLowerCase() +
            " (N" +
            rf.lo.k +
            ") with no indifference between them, the ground turns to gray bare rock. A move across costs the most energy, in either direction.",
          at: rf.at,
        });
      low &&
        hAt(low.x, low.y) < -0.1 &&
        out.push({
          act: act,
          title: "The deepest ground: " + EMO[low.e][0].toLowerCase(),
          cap:
            "N" +
            low.k +
            " sits on the deepest ground. The way up from here to acceptance is the longest climb on the map, and the rarest move.",
          at: [low.x, low.y],
        });
      out.push({ act: act, title: "What a move costs", cap: cost + " Pattern Synthesis reads this ground in full.", at: null });
      return out;
    }
    function firstSentence(t) {""",
    )
    # 4: the fall reading is marked so the rock reading can find it; the pair is kept
    rep(
        """        if (top && low)
          R.push({
            grp: 0,
            title: "Where it is easiest to fall from",""",
        """        if (top && low) FALLPAIR = [top.k, low.k];
        if (top && low)
          R.push({
            grp: 0,
            kind: "fall",
            title: "Where it is easiest to fall from",""",
    )
    rep(
        """      moreReadings(R);
      R = R.filter(function (r) {
        return r.at;
      });""",
        """      FALLPAIR = null;
      moreReadings(R);
      try {
        rockReading(R);
      } catch (e) {}
      R = R.filter(function (r) {
        return r.at;
      });""",
    )
    rep("      READ = R.slice(0, 12);", "      READ = R.slice(0, 13);")
    # 3 + 4: captions use a reading's own caption when it has one; the introduction goes to the 3D
    rep(
        """            return { at: r.at, title: r.title, text: r.short + (r.more ? " " + r.more : ""), grp: r.grp, cap: c.join(" ") };
          });
          D.groups = GROUPS;""",
        """            return { at: r.at, title: r.title, text: r.short + (r.more ? " " + r.more : ""), grp: r.grp, cap: r.cap || c.join(" ") };
          });
          D.groups = GROUPS;
          try {
            D.intro = introStops(false);
          } catch (e) {}""",
    )
    rep(
        """        } else if (ANH && !PAR) {
          D.read = [];
        }""",
        """        } else if (ANH && !PAR) {
          D.read = [];
          /* 6: Pattern Analysis gets its own short tour: how to read this map */
          try {
            D.intro = introStops(true);
          } catch (e) {}
        }""",
    )
    s = s.replace('t.textContent = "v209"', 't.textContent = "v210"')
    assert 't.textContent = "v210"' in s
open(P, "w").write(s)
