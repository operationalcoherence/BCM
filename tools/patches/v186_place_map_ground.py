"""v186: a place-map-only workbook gets the 3D ground. Its place notes are projected (Web Mercator) into the
340 x 230 frame around the notes and the location; the goal stands at the location. Analysis, Synthesis,
In Parallel and the Taking Action cards all use it. Help or hinder for a place note comes from its question
(Q.1 and Q.2 hinder), since a place map has no line. The ground itself (Esri imagery) is drawn in gsm-relief.js."""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:80]); s = s.replace(a, b)

# 1) gsmData: projected place notes when there are no line notes
rep("""  window.gsmData = function () {
    return { m: C.m, a: Q(), goal: C.goal };
  };""", """  function gsmPlaceView() {
    var has = function (t) {
      return Array.isArray(t) && String(t[3] || "").trim();
    };
    if (C.m.some(has)) return null;
    var P = (C.p && C.p.m) || [];
    if (
      !P.some(function (t) {
        return has(t) && isFinite(+t[1]) && isFinite(+t[2]);
      })
    )
      return null;
    function mp(la, ln) {
      la = Math.max(-85, Math.min(85, +la));
      var s = Math.sin((la * Math.PI) / 180);
      return [((+ln + 180) / 360) * 256, (0.5 - Math.log((1 + s) / (1 - s)) / (4 * Math.PI)) * 256];
    }
    var L = C.p.loc && isFinite(+C.p.loc.lat) && isFinite(+C.p.loc.lng) ? [+C.p.loc.lat, +C.p.loc.lng] : null,
      pts = [],
      lat0 = null;
    P.forEach(function (t) {
      if (!has(t) || !isFinite(+t[1]) || !isFinite(+t[2])) return;
      null == lat0 && (lat0 = +t[1]);
      pts.push(mp(t[1], t[2]));
      Array.isArray(t[4]) &&
        t[4].forEach(function (v) {
          Array.isArray(v) && isFinite(+v[0]) && isFinite(+v[1]) && pts.push(mp(v[0], v[1]));
        });
    });
    var g = L ? mp(L[0], L[1]) : null;
    g && (pts.push(g), (lat0 = L[0]));
    var x0 = 1e9, x1 = -1e9, y0 = 1e9, y1 = -1e9;
    pts.forEach(function (q) {
      x0 = Math.min(x0, q[0]); x1 = Math.max(x1, q[0]); y0 = Math.min(y0, q[1]); y1 = Math.max(y1, q[1]);
    });
    /* at least about 250 m across; a margin so flags and labels stay on the ground */
    var minS = 250 / (156543.03392 * Math.cos((lat0 * Math.PI) / 180)),
      sx = Math.max(x1 - x0, minS) * 1.4,
      sy = Math.max(y1 - y0, minS * 0.6) * 1.4,
      A = 340 / 230;
    sx / sy < A ? (sx = sy * A) : (sy = sx / A);
    var X0 = (x0 + x1) / 2 - sx / 2,
      Y0 = (y0 + y1) / 2 - sy / 2,
      k = 340 / sx,
      fr = function (q) {
        return [(q[0] - X0) * k, (q[1] - Y0) * k];
      },
      areas = [],
      rows = P.map(function (t, i) {
        var r = t.slice();
        if (isFinite(+t[1]) && isFinite(+t[2])) {
          var f = fr(mp(t[1], t[2]));
          r[1] = f[0];
          r[2] = f[1];
        }
        r.hd = t[0] <= 2;
        Array.isArray(t[4]) &&
          t[4].length > 2 &&
          has(t) &&
          areas.push({
            k: i + 1,
            e: null != t[5] ? t[5] : null,
            pts: t[4]
              .filter(function (v) {
                return Array.isArray(v) && isFinite(+v[0]) && isFinite(+v[1]);
              })
              .map(function (v) {
                return fr(mp(v[0], v[1]));
              }),
          });
        return r;
      }),
      gf = g ? fr(g) : [170, 115];
    return {
      m: rows,
      place: { X0: X0, Y0: Y0, k: k, goal: gf, areas: areas, name: String(C.p.name || (C.p.loc && C.p.loc.name) || "") },
    };
  }
  window.gsmData = function () {
    var pv = gsmPlaceView();
    return { m: pv ? pv.m : C.m, a: Q(), goal: C.goal, place: pv ? pv.place : null };
  };""")

# 2) Synthesis and Analysis: a ground exists when line notes or (place-only) place notes have text
rep("""            (ye += C.m.some(function (t) {
              return (t[3] || "").trim();
            })
              ? ((window.gsmTD = { m: C.m, a: Q(), goal: C.goal }),""", """            (ye += window.gsmData().m.some(function (t) {
              return (t[3] || "").trim();
            })
              ? ((window.gsmTD = window.gsmData()),""")
rep("""          (C.m.some(function (t) {
            return (t[3] || "").trim();
          })
            ? '<div class="plab">YOUR LANDSCAPE, ONE QUESTION AT A TIME</div><div class="gterr-host" data-an="1"></div>'""",
"""          (window.gsmData().m.some(function (t) {
            return (t[3] || "").trim();
          })
            ? '<div class="plab">YOUR LANDSCAPE, ONE QUESTION AT A TIME</div><div class="gterr-host" data-an="1"></div>'""")

# 3) Taking Action cards: place notes stand in for line notes when the workbook is place-only
rep("""                (function (t, e, stp) {
                  var n = e
                    .filter(function (t) {
                      return t.line;
                    })
                    .map(function (t) {
                      return [+t.line[1], +t.line[2], t.id];
                    })""", """                (function (t, e, stp) {
                  var PV = window.gsmData().place ? window.gsmData().m : null,
                    pl = function (t) {
                      return t.line || (PV && t.place && PV[+String(t.id).replace(/\\D/g, "") - 1]) || null;
                    };
                  var n = e
                    .filter(function (t) {
                      return pl(t);
                    })
                    .map(function (t) {
                      var L = pl(t);
                      return [+L[1], +L[2], t.id];
                    })""")
rep("""                    f =
                      "Crosses the help and hinder line " +""", """                    f = PV
                      ? ""
                      : "Crosses the help and hinder line " +""")
rep("""                    g = t
                      ? u < 1.25 && l <= 1""", """                    g = PV
                      ? ""
                      : t
                      ? u < 1.25 && l <= 1""")
rep("""                      e
                        .filter(function (x) {
                          return x.line;
                        })""", """                      e
                        .filter(function (x) {
                          return pl(x);
                        })""")

# 4) the module: place ids, goal at the location, start at the note farthest from it, hinder from the question
rep("""var m = /^(?:note\\s*|N)(\\d+)$/i.exec(x);""", """var m = /^(?:note\\s*|N|P)(\\d+)$/i.exec(x);""")
rep("""          mount(h, {
            m: d.m || [],
            a: d.a || [],
            goal: d.goal || "",
            card: 1,""", """          mount(h, {
            m: d.m || [],
            a: d.a || [],
            goal: d.goal || "",
            place: d.place || null,
            card: 1,""")
rep("""    var CARDH = !!data.card,
      ANH = !!data.an,""", """    var CARDH = !!data.card,
      PLACE = data.place || null,
      ANH = !!data.an,""")
rep("""          e: e,
          v: n[7] ? String(n[7]) : "",
        });""", """          e: e,
          v: n[7] ? String(n[7]) : "",
          hd: null != n.hd ? !!n.hd : y > 118,
        });""")
rep("""            var nearL = Math.exp(-Math.pow((y - 118) / 40, 2)),""", """            var nearL = PLACE ? 0 : Math.exp(-Math.pow((y - 118) / 40, 2)),""")
rep("""      var notes = prep(raw);
      $("msg").textContent = "";""", """      var notes = prep(raw);
      if (PLACE) {
        GOAL.x = Math.max(8, Math.min(W - 8, PLACE.goal[0]));
        GOAL.y = Math.max(8, Math.min(HH - 8, PLACE.goal[1]));
        var far = null,
          fd = -1;
        notes.forEach(function (n) {
          var d = Math.hypot(n.x - GOAL.x, n.y - GOAL.y);
          d > fd && ((fd = d), (far = n));
        });
        START.x = far ? far.x : 10;
        START.y = far ? far.y : 118;
      }
      $("msg").textContent = "";""")
rep("""            (n.y > 118 ? ", on the hinder side" : "") +""", """            (n.hd ? ", on the hinder side" : "") +""")
rep("""          o.r[2] < 118 && up++;""", """          (null != o.r.hd ? !o.r.hd : o.r[2] < 118) && up++;""")
rep("""          notes: terr.notes.map(function (n) {
            return { k: n.k, x: n.x, y: n.y, e: n.e, q: n.q, t: n.t };
          }),
          goalText: GOALTEXT,
        };""", """          notes: terr.notes.map(function (n) {
            return { k: n.k, x: n.x, y: n.y, e: n.e, q: n.q, t: n.t };
          }),
          goalText: GOALTEXT,
          place: PLACE,
        };""")
rep("""d = (null == e ? 2 : HARD[e]) + (o.r[2] >= 118 ? 1 : 0),""", """d = (null == e ? 2 : HARD[e]) + ((null != o.r.hd ? o.r.hd : o.r[2] >= 118) ? 1 : 0),""")
rep('t.textContent = "v185"', 't.textContent = "v186"')
open(P, "w").write(s)
