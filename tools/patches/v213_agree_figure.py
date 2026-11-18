"""v213: the In Parallel figure (review 5a, 5b; decided 11-18 as mockup 2 with mockup 3's piece).
1. THE TWO PICTURES, SIDE BY SIDE closes Pattern Synthesis: the words Pattern Analysis reports in its own column at
   left, and hoses carrying each one onto the Synthesis ground, to the notes that use it. A black hose: the ground
   agrees with what Analysis found. A white hose: the ground raises a question about it. The ground is painted with
   the 3D relief's own rule (each note's emotion spreads around it, the nearest strong emotion wins, indifference
   reads as one band, bare rock where distant emotions meet, plain ground where there are no notes), shaded by height.
   Words and verdicts are the ones In Parallel reports (WHERE BOTH PICTURES AGREE and WHERE THEY DIFFER), named by
   their repeated phrase where the workbook has one. Line maps only (place maps have no shared ground coordinates).
2. Tapping a word lights its hoses, says in one sentence what both pictures say about it, and draws its hoses as
   tubes on the 3D relief above (black or white, as ways are drawn on Taking Action). "See it on the 3D map" scrolls
   up to it. Tapping the word again clears it.
3. In Parallel's own 3D (Both pictures on one map) is folded away behind THE EARLIER 3D VIEW; the code is unchanged.
Wording is Claude's (the figure's lead line follows the mockup he chose).
Usage: python3 v213_agree_figure.py tools/relief/relief.js --relief   and   python3 v213_agree_figure.py gsm-readable.js"""
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
        "  let selWay = null, hovWay = null;",
        """  /* v213: a word's hoses from the agreement figure, drawn as the ways are (black: the ground agrees; white: it asks) */
  const HOSES = new THREE.Group(); scene.add(HOSES); let hoseN = 0;
  function hoses(h) { while (HOSES.children.length) { const m = HOSES.children.pop(); m.geometry.dispose(); m.material.dispose(); } hoseN = 0;
    if (h && h.pts && h.pts.length > 1) { const P = h.pts, white = !!h.ask;
      for (let i = 1; i < P.length; i++) { const a = P[i - 1], b = P[i], n = Math.max(8, Math.ceil(Math.hypot(b[0] - a[0], b[1] - a[1]) / 3)), pts = [];
        for (let k = 0; k <= n; k++) { const t = k / n, x = a[0] + (b[0] - a[0]) * t, y = a[1] + (b[1] - a[1]) * t; pts.push(new THREE.Vector3(X(x), gH(x, y) + 2 + Math.sin(Math.PI * t) * 4, Z(y))); }
        const c = new THREE.CatmullRomCurve3(pts), tube = new THREE.Mesh(new THREE.TubeGeometry(c, n * 4, 1.5, 8), new THREE.MeshStandardMaterial({ color: white ? '#f4f4f4' : '#111111', roughness: 0.45, emissive: white ? '#ffffff' : '#000000', emissiveIntensity: white ? 0.35 : 0 }));
        tube.castShadow = true; HOSES.add(tube); hoseN++;
        if (white) HOSES.add(new THREE.Mesh(new THREE.TubeGeometry(c, n * 4, 1.9, 8), new THREE.MeshStandardMaterial({ color: '#222', side: THREE.BackSide }))); } }
    dirty = true; }
  let selWay = null, hovWay = null;""",
    )
    rep(
        "  return { loops, focusQ, tour: startTour,",
        "  return { loops, hoses, hoseCount() { return hoseN; }, focusQ, tour: startTour,",
    )
else:
    # the Synthesis relief is reachable from the figure
    rep(
        "              host._rel = window.gsmRelief.mount(box, data());",
        "              host._rel = window.gsmRelief.mount(box, data());\n              if (!ANH && !PAR && !CARDH) {\n                window.gsmSynRel = host._rel;\n                window.gsmSynHost = host;\n              }",
    )
    # 3: In Parallel's own 3D folds away
    rep(
        """? gsmGrid() + '<div class="intsub" style="margin:4px 0 8px">Both pictures on one map.""",
        """? gsmGrid() + '<details class="fold parold" style="margin:14px 0 18px"><summary>THE EARLIER 3D VIEW</summary><div class="intsub" style="margin:4px 0 8px">The two pictures now meet at the end of Pattern Synthesis, in THE TWO PICTURES, SIDE BY SIDE. This earlier view is kept here. Both pictures on one map.""",
    )
    rep(
        """<div class="gterr-host" data-an="1" data-par="1"></div>'""",
        """<div class="gterr-host" data-an="1" data-par="1"></div></details>'""",
    )
    # 1: the items, from the same lists that write WHERE BOTH PICTURES AGREE and WHERE THEY DIFFER
    rep(
        """                    a
                      ? (Rt.insertBefore(ct, a), Rt.insertBefore(ut, a), Rt.insertBefore(lt, a))
                      : (Rt.appendChild(ct), Rt.appendChild(ut), Rt.appendChild(lt)),""",
        """                    a
                      ? (Rt.insertBefore(ct, a), Rt.insertBefore(ut, a), Rt.insertBefore(lt, a))
                      : (Rt.appendChild(ct), Rt.appendChild(ut), Rt.appendChild(lt)),
                    (function () {
                      var AGI = [];
                      [
                        [p, 1, "c"],
                        [g, 1, "g"],
                        [m, 1, "u"],
                        [v, 0, "p"],
                        [y, 0, "y"],
                        [w, 0, "w"],
                      ].forEach(function (z) {
                        z[0].slice(0, 2).forEach(function (k) {
                          AGI.some(function (o) {
                            return o.k === k;
                          }) || AGI.push({ k: k, ok: z[1], kind: z[2] });
                        });
                      });
                      var AG = null;
                      try {
                        var AGa = AGI.filter(function (o) {
                            return o.ok;
                          }),
                          AGq = AGI.filter(function (o) {
                            return !o.ok;
                          }).slice(0, 3);
                        AGI = AGa.slice(0, 9 - AGq.length).concat(AGq);
                        AG = AGI.length ? gsmAgreeFig(AGI) : null;
                      } catch (e) {
                        window.console && console.warn("agree figure", e);
                      }
                      if (AG) {
                        var AH = document.createElement("div");
                        AH.className = "plab";
                        AH.textContent = "THE TWO PICTURES, SIDE BY SIDE";
                        Rt.insertBefore(AH, ct);
                        Rt.insertBefore(AG, ct);
                      }
                    })(),""",
    )
    # the figure itself
    rep(
        """  function gsmPhNameH(key, ctx) {""",
        r'''  // v213: THE TWO PICTURES, SIDE BY SIDE (closes Pattern Synthesis)
  function gsmAgreeFig(items) {
    var D = window.gsmData ? window.gsmData() : { m: [] },
      M = (D.m || []).filter(function (r) {
        return r && null != r[1] && null != r[2];
      });
    if (!M.length || D.place) return null;
    var NS = (D.m || [])
        .map(function (r, i) {
          return r && null != r[1] ? { k: i + 1, x: +r[1], y: +r[2], e: null == r[5] ? null : r[5], t: r[3] || "", q: r[0] } : null;
        })
        .filter(Boolean),
      EC = [
        [200, 53, 46],
        [42, 157, 143],
        [164, 143, 208],
        [230, 190, 79],
        [27, 42, 143],
      ],
      EN = ["aggression", "acceptance", "distrust", "indifference", "defiance"],
      RK = [3, 0, 2, 1, 4],
      HK = [-0.7, 1, -0.45, 0.35, -1];
    function vivid(c, deep) {
      var r = c[0] / 255, g = c[1] / 255, b = c[2] / 255, mx = Math.max(r, g, b), mn = Math.min(r, g, b), l = (mx + mn) / 2, sa = 0, h = 0, d = mx - mn;
      if (d > 1e-6) {
        sa = l > 0.5 ? d / (2 - mx - mn) : d / (mx + mn);
        h = mx === r ? (g - b) / d + (g < b ? 6 : 0) : mx === g ? (b - r) / d + 2 : (r - g) / d + 4;
        h /= 6;
      }
      sa = Math.min(1, sa * 1.5 + 0.08);
      l = deep ? Math.min(0.36, Math.max(0.24, l)) : Math.min(0.62, Math.max(0.42, l));
      var q = l < 0.5 ? l * (1 + sa) : l + sa - l * sa, pp = 2 * l - q, f = function (t) {
          t = (t + 1) % 1;
          return t < 1 / 6 ? pp + (q - pp) * 6 * t : t < 0.5 ? q : t < 2 / 3 ? pp + (q - pp) * (2 / 3 - t) * 6 : pp;
        };
      return [f(h + 1 / 3) * 255, f(h) * 255, f(h - 1 / 3) * 255];
    }
    var VC = EC.map(function (c, k) {
        return vivid(c, 4 === k);
      }),
      sst = function (a, b, x) {
        var t = Math.max(0, Math.min(1, (x - a) / (b - a)));
        return t * t * (3 - 2 * t);
      },
      mix = function (a, b, t) {
        return [a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t, a[2] + (b[2] - a[2]) * t];
      },
      EM = NS.filter(function (n) {
        return null != n.e;
      }),
      rib = [];
    // indifference reads as one band, as on the relief
    (function () {
      var P = EM.filter(function (n) {
          return 3 === n.e;
        }),
        par = P.map(function (_, i) {
          return i;
        }),
        top = function (i) {
          return par[i] === i ? i : (par[i] = top(par[i]));
        },
        E = [];
      for (var i = 0; i < P.length; i++) for (var j = i + 1; j < P.length; j++) E.push([Math.hypot(P[i].x - P[j].x, P[i].y - P[j].y), i, j]);
      E.sort(function (a, b) {
        return a[0] - b[0];
      }).forEach(function (e) {
        if (e[0] > 95 || top(e[1]) === top(e[2])) return;
        par[top(e[1])] = top(e[2]);
        rib.push([P[e[1]].x, P[e[1]].y, P[e[2]].x, P[e[2]].y]);
      });
    })();
    // the ground, painted by the relief's rule
    var GW = 170, GHh = 115, cv = document.createElement("canvas");
    cv.width = GW;
    cv.height = GHh;
    var cx = cv.getContext("2d"), img = cx.createImageData(GW, GHh), HT = new Float32Array(GW * GHh), CL = [];
    for (var j = 0; j < GHh; j++)
      for (var i = 0; i < GW; i++) {
        var x = ((i + 0.5) / GW) * 340, yy = ((j + 0.5) / GHh) * 230, ws = [0, 0, 0, 0, 0];
        EM.forEach(function (n) {
          ws[n.e] += Math.exp(-((n.x - x) * (n.x - x) + (n.y - yy) * (n.y - yy)) / 1352);
        });
        rib.forEach(function (r) {
          var dx = r[2] - r[0], dy = r[3] - r[1], t = Math.max(0, Math.min(1, ((x - r[0]) * dx + (yy - r[1]) * dy) / (dx * dx + dy * dy || 1)));
          ws[3] += 2.4 * Math.exp(-(Math.pow(r[0] + t * dx - x, 2) + Math.pow(r[1] + t * dy - yy, 2)) / 128);
        });
        var tot = ws[0] + ws[1] + ws[2] + ws[3] + ws[4], pw = 0, cc = [0, 0, 0], hh = 0, k;
        for (k = 0; k < 5; k++) {
          var v = Math.pow(ws[k] * (4 === k ? 1.6 : 1), 2.2);
          pw += v;
          cc = [cc[0] + VC[k][0] * v, cc[1] + VC[k][1] * v, cc[2] + VC[k][2] * v];
          hh += ws[k] * HK[k];
        }
        pw && (cc = [cc[0] / pw, cc[1] / pw, cc[2] / pw]);
        var o = [0, 1, 2, 3, 4].sort(function (a, b) {
            return ws[b] - ws[a];
          }),
          gap = Math.abs(RK[o[0]] - RK[o[1]]) < 2 || 1 === RK[o[0]] || 1 === RK[o[1]] || ws[o[1]] < 0.03 ? 0 : sst(0.22, 0.42, ws[o[1]] / (ws[o[0]] + ws[o[1]])),
          sc = sst(0.04, 0.5, tot),
          col = mix([116, 122, 74], [cc[0] * 0.92, cc[1] * 0.92, cc[2] * 0.92], 0.62 * sc);
        gap > 0.01 && (col = mix(col, [140, 135, 127], gap * 0.85));
        HT[j * GW + i] = (hh / Math.max(0.25, tot)) * sc;
        CL.push(col);
      }
    for (j = 0; j < GHh; j++)
      for (i = 0; i < GW; i++) {
        var a0 = HT[Math.max(0, j - 1) * GW + Math.max(0, i - 1)], a1 = HT[Math.min(GHh - 1, j + 1) * GW + Math.min(GW - 1, i + 1)],
          lum = 1.04 + Math.max(-0.32, Math.min(0.32, (a0 - a1) * 2.2)) + 0.08 * HT[j * GW + i],
          c = CL[j * GW + i], q = 4 * (j * GW + i);
        img.data[q] = Math.min(255, c[0] * lum);
        img.data[q + 1] = Math.min(255, c[1] * lum);
        img.data[q + 2] = Math.min(255, c[2] * lum);
        img.data[q + 3] = 255;
      }
    cx.putImageData(img, 0, 0);
    // the words and the notes they reach
    var IT = items.map(function (o) {
        var st = String(o.k).split(" "), nm = gsmPhName(o.k).ph;
        var hit = phKeep(function () {
          return NS.filter(function (n) {
            return phIn(st, n.t);
          });
        });
        return { k: o.k, ok: o.ok, kind: o.kind, nm: nm, ns: hit };
      }),
      SVGN = "http://www.w3.org/2000/svg",
      X0 = 186, SX = 494 / 340, GHt = 230 * SX, TOPY = 26, VH = TOPY + GHt + 26,
      mk = function (tag, at, par) {
        var e = document.createElementNS(SVGN, tag);
        for (var k in at) e.setAttribute(k, at[k]);
        par && par.appendChild(e);
        return e;
      },
      gx = function (x) {
        return X0 + x * SX;
      },
      gy = function (y) {
        return TOPY + y * SX;
      };
    var wrap = document.createElement("div");
    wrap.className = "agfig";
    wrap.innerHTML =
      '<div class="agsub">Pattern Analysis keeps its own column; the hoses carry each of its words onto the Synthesis ground, to the notes that use it. A <b>black hose</b>: the ground agrees with what Analysis found. A <b>white hose</b>: the ground raises a question about it. Tap a word to follow it here and on the 3D map above.</div>';
    var svg = mk("svg", { viewBox: "0 0 680 " + VH.toFixed(0), role: "img", "aria-label": "Pattern Analysis words in a column, joined by hoses to their notes on the Pattern Synthesis ground" }, wrap);
    mk("rect", { x: 0, y: 0, width: 176, height: VH, fill: "#fafafa" }, svg);
    var t0 = mk("text", { x: 10, y: 16, "font-size": 10.5, "letter-spacing": 1.4, fill: "#555" }, svg);
    t0.textContent = "PATTERN ANALYSIS";
    mk("rect", { x: 10, y: VH - 30, width: 12, height: 9, fill: "#111" }, svg);
    mk("text", { x: 27, y: VH - 22, "font-size": 10, fill: "#333" }, svg).textContent = "the ground agrees";
    mk("rect", { x: 10, y: VH - 16, width: 12, height: 9, fill: "#fff", stroke: "#111" }, svg);
    mk("text", { x: 27, y: VH - 8, "font-size": 10, fill: "#333" }, svg).textContent = "the ground asks";
    mk("image", { href: cv.toDataURL(), x: X0, y: TOPY, width: 494, height: GHt.toFixed(1), preserveAspectRatio: "none" }, svg);
    mk("rect", { x: X0, y: TOPY, width: 494, height: GHt.toFixed(1), fill: "none", stroke: "#ccc" }, svg);
    mk("line", { x1: X0, y1: gy(118), x2: X0 + 494, y2: gy(118), stroke: "#111", "stroke-width": 1, "stroke-dasharray": "6 5", opacity: 0.55 }, svg);
    [["HELP", -6], ["HINDER", 14]].forEach(function (z) {
      var t = mk("text", { x: gx(305) - 22, y: gy(118) + z[1], "font-size": 10.5, "letter-spacing": 1.4, "text-anchor": "end", fill: "#111", stroke: "rgba(255,255,255,.75)", "stroke-width": 3, "paint-order": "stroke" }, svg);
      t.textContent = z[0];
    });
    mk("rect", { x: gx(305) - 6, y: gy(118) - 6, width: 12, height: 12, fill: "#111", transform: "rotate(45 " + gx(305) + " " + gy(118) + ")" }, svg);
    var tg = mk("text", { x: gx(305), y: gy(118) - 11, "font-size": 10.5, "letter-spacing": 1.4, "text-anchor": "middle", fill: "#111" }, svg);
    tg.textContent = "GOAL";
    var t1 = mk("text", { x: X0 + 247, y: VH - 8, "font-size": 10.5, "letter-spacing": 1.4, fill: "#555", "text-anchor": "middle" }, svg);
    t1.textContent = "PATTERN SYNTHESIS";
    var HG = mk("g", {}, svg), DG = mk("g", {}, svg), WG = mk("g", {}, svg),
      step = Math.min(60, (GHt - 24) / Math.max(1, IT.length)),
      reach = {};
    IT.forEach(function (o, i) {
      o.y = TOPY + 4 + step * i + step / 2;
      o.g = mk("g", {}, HG);
      o.ns.forEach(function (n) {
        reach[n.k] = 1;
        var sx = gx(n.x), sy = gy(n.y), c1x = 168 + (sx - 168) * 0.45, c1y = o.y + (sy - o.y) * 0.85,
          d = "M168 " + o.y.toFixed(1) + " Q" + c1x.toFixed(1) + " " + c1y.toFixed(1) + " " + sx.toFixed(1) + " " + sy.toFixed(1);
        mk("path", { d: d, transform: "translate(2 3)", stroke: "#000", "stroke-opacity": 0.22, "stroke-width": 6, fill: "none", "stroke-linecap": "round" }, o.g);
        o.ok
          ? mk("path", { d: d, stroke: "#1a1a1a", "stroke-width": 4.2, fill: "none", "stroke-linecap": "round" }, o.g)
          : (mk("path", { d: d, stroke: "#222", "stroke-width": 6, fill: "none", "stroke-linecap": "round" }, o.g),
            mk("path", { d: d, stroke: "#f4f4f4", "stroke-width": 3.8, fill: "none", "stroke-linecap": "round" }, o.g));
        mk("path", { d: d, transform: "translate(-.8 -1.2)", stroke: "#fff", "stroke-opacity": o.ok ? 0.3 : 0.9, "stroke-width": 1.2, fill: "none", "stroke-linecap": "round" }, o.g);
      });
    });
    NS.forEach(function (n) {
      mk("circle", { cx: gx(n.x), cy: gy(n.y), r: reach[n.k] ? 5 : 3, fill: null == n.e ? "#fff" : "rgb(" + EC[n.e].join(",") + ")", stroke: reach[n.k] ? "#fff" : "#333", "stroke-width": reach[n.k] ? 1.5 : 0.6 }, DG);
      if (reach[n.k]) {
        var tl = mk("text", { x: gx(n.x) + 7, y: gy(n.y) + 3.5, "font-size": 9.5, "font-weight": 700, fill: "#111", stroke: "#fff", "stroke-width": 2.6, "paint-order": "stroke" }, DG);
        tl.textContent = "N" + n.k;
      }
    });
    var rd = document.createElement("div");
    rd.className = "agread";
    var SEL = -1;
    function wrapTxt(t, n) {
      var w = String(t).split(/\s+/), L = [""];
      w.forEach(function (x) {
        (L[L.length - 1] + " " + x).trim().length > n && L[L.length - 1] ? L.push(x) : (L[L.length - 1] = (L[L.length - 1] + " " + x).trim());
      });
      return L.slice(0, 2).map(function (l, i, a) {
        return i === 1 && L.length > 2 ? l + "…" : l;
      });
    }
    function nl(a) {
      a = a.map(function (n) {
        return "N" + n.k;
      });
      return a.length > 5 ? a.slice(0, 5).join(", ") + ", and " + (a.length - 5) + " more" : phList(a);
    }
    function reading(o) {
      var up = o.ns.filter(function (n) {
          return n.y < 118;
        }),
        dn = o.ns.filter(function (n) {
          return n.y > 118;
        }),
        nm = "“" + o.nm + "”",
        on = o.ns.length ? " Its notes: " + nl(o.ns) + "." : " No note on the ground uses it yet.";
      return {
        c:
          nm + ": Analysis finds it both resisted and supported, and the ground agrees" +
          (up.length && dn.length ? ": its notes sit above the line (" + nl(up) + ") and below it (" + nl(dn) + ")." : ".") +
          " This is where the work is decided.",
        g: nm + ": Analysis finds nothing you would design takes it up, and the ground agrees: it stays in the context you have grasped." + on + " The clearest gap.",
        u: nm + ": support already at work that nothing you would design draws on yet, and the ground agrees." + on + " The easiest place to build.",
        p: nm + ": you would design for it, but neither picture shows what it answers." + on + " The ground asks: what does it answer?",
        y: nm + ": Analysis says nothing you would design reaches it, but its words run on into what you would design." + on + " The ground asks: is it reached after all?",
        w: nm + ": the threads keep it in the context you have grasped, though Analysis does not list it as a gap." + on + " The ground asks: is it answered in other words?",
      }[o.kind];
    }
    function chain(ns) {
      var L = ns.slice().sort(function (a, b) {
          return a.x - b.x;
        }),
        out = L.length ? [L.shift()] : [];
      while (L.length) {
        var l = out[out.length - 1], bi = 0, bd = 1e9;
        L.forEach(function (n, i) {
          var d = Math.hypot(n.x - l.x, n.y - l.y);
          d < bd && ((bd = d), (bi = i));
        });
        out.push(L.splice(bi, 1)[0]);
      }
      return out.map(function (n) {
        return [n.x, n.y];
      });
    }
    function pick(i) {
      SEL = SEL === i ? -1 : i;
      IT.forEach(function (o, k) {
        o.g.setAttribute("opacity", SEL < 0 || SEL === k ? 1 : 0.1);
        o.box.setAttribute("stroke-width", SEL === k ? 3 : 1.5);
        o.gw.setAttribute("aria-pressed", SEL === k ? "true" : "false");
      });
      rd.textContent = "";
      if (SEL < 0) {
        rd.textContent = "Tap a word to read what both pictures say about it.";
        window.gsmSynRel && window.gsmSynRel.hoses && window.gsmSynRel.hoses(null);
        return;
      }
      var o = IT[SEL];
      rd.appendChild(document.createTextNode(reading(o) + " "));
      if (window.gsmSynRel && window.gsmSynRel.hoses && o.ns.length > 1) {
        window.gsmSynRel.hoses({ pts: chain(o.ns), ask: !o.ok });
        var bt = document.createElement("button");
        bt.type = "button";
        bt.className = "lnk";
        bt.textContent = "See it on the 3D map ↑";
        bt.onclick = function () {
          window.gsmSynHost && window.gsmSynHost.scrollIntoView({ behavior: "smooth", block: "center" });
        };
        rd.appendChild(bt);
      } else window.gsmSynRel && window.gsmSynRel.hoses && window.gsmSynRel.hoses(null);
    }
    IT.forEach(function (o, i) {
      var gw = mk("g", { role: "button", tabindex: 0, "aria-pressed": "false", style: "cursor:pointer" }, WG), L = wrapTxt(o.nm, 19), bh = 10 + 14 * L.length;
      o.gw = gw;
      o.box = mk("rect", { x: 8, y: o.y - bh / 2, width: 160, height: bh, rx: 2, fill: o.ok ? "#111" : "#fff", stroke: "#111", "stroke-width": 1.5 }, gw);
      L.forEach(function (l, k) {
        var t = mk("text", { x: 16, y: o.y - bh / 2 + 17 + 14 * k, "font-size": 12.5, fill: o.ok ? "#fff" : "#111" }, gw);
        t.textContent = l;
      });
      mk("title", {}, gw).textContent = o.ok ? "The ground agrees" : "The ground asks";
      gw.addEventListener("click", function () {
        pick(i);
      });
      gw.addEventListener("keydown", function (e) {
        ("Enter" !== e.key && " " !== e.key) || (e.preventDefault(), pick(i));
      });
    });
    rd.textContent = "Tap a word to read what both pictures say about it.";
    wrap.appendChild(rd);
    var st = document.createElement("style");
    st.textContent =
      "#gsm .agfig svg{display:block;width:100%;height:auto;border:1px solid #ddd;font-family:Questrial,Helvetica,Arial,sans-serif}#gsm .agsub{font-size:14px;line-height:1.5;color:#333;margin:0 0 10px}#gsm .agread{font-size:15px;line-height:1.5;margin:10px 0 18px;min-height:44px;border-left:3px solid #222;padding-left:12px}#gsm .agread .lnk{margin-left:4px}";
    wrap.appendChild(st);
    return wrap;
  }
  function gsmPhNameH(key, ctx) {''',
    )
    rep(
        '''                          "THE TWO PICTURES TOGETHER" === r ||''',
        '''                          "THE TWO PICTURES TOGETHER" === r ||
                          "THE TWO PICTURES, SIDE BY SIDE" === r ||''',
    )
    s = s.replace('t.textContent = "v212"', 't.textContent = "v213"')
    assert 't.textContent = "v213"' in s
open(P, "w").write(s)
