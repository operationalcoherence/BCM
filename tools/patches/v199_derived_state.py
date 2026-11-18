"""v199: one derived-state pass (review plan, Phase 1 step 3; P2).
The action points that Taking Action reads (MOVES, IN ORDER) were computed inside In Parallel's drawing, and only
when In Parallel's figures existed. They are now computed in gsmDerive(), from the workbook alone, on every pass
the page makes after an edit (every save schedules one), before anything is drawn. In Parallel's action grid draws
from the same points instead of computing its own. The pass leaves the word tallies as it found them, so no label
changes. window.gsmDV counts the passes, so a test can see one ran.
Nothing on screen changes for a workbook that already had In Parallel's figures.
Usage: python3 v199_derived_state.py gsm-readable.js"""
import sys

P = sys.argv[1]
s = open(P).read()


def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, (c, a[:90])
    s = s.replace(a, b)


# 1. the pass itself, next to gsmData (Ht is a hoisted declaration in the same scope)
DERIVE = r'''  window.gsmDV = 0;
  window.gsmDerive = function () {
    // reading the notes must not change which spelling of a word the pages show: keep the tallies as they were
    var SV = [Mt, NmK, NmD].map(function (o) {
        return JSON.stringify(o);
      }),
      M = (window.gsmData ? window.gsmData().m || [] : [])
        .map(function (r, i) {
          return { r: r, id: "N" + (i + 1), k: i + 1, t: Ht(r[3] || "") };
        })
        .filter(function (o) {
          return String(o.r[3] || "").trim();
        }),
      HARD = [3, 0, 2, 1, 4],
      MED = window.gsmMED || {},
      pts = M.map(function (o) {
        var e = o.r[5],
          d = (null == e ? 2 : HARD[e]) + ((null != o.r.hd ? o.r.hd : o.r[2] >= 118) ? 1 : 0),
          emo = {},
          shared = 0;
        M.forEach(function (p) {
          if (p === o) return;
          var hit = Object.keys(o.t.k).some(function (k) {
            return !MED[k] && p.t.k[k];
          });
          hit && (shared++, null != p.r[5] && (emo[p.r[5]] = 1));
        });
        return { id: o.id, k: o.k, q: o.r[0], act: o.r[0] >= 5, d: d / 5, reach: Object.keys(emo).length, shared: shared, e: e };
      }),
      mr = Math.max.apply(null, pts.map(function (p) { return p.reach; }).concat([1]));
    pts.forEach(function (p) {
      p.any = p.reach / mr;
    });
    [Mt, NmK, NmD].forEach(function (o, i) {
      for (var k in o) delete o[k];
      var v = JSON.parse(SV[i]);
      for (k in v) o[k] = v[k];
    });
    window.gsmGridAll = pts;
    window.gsmGridPts = pts.filter(function (p) {
      return p.act;
    });
    window.gsmDV++;
  };
'''
rep("  window.gsmData = function () {\n", DERIVE + "  window.gsmData = function () {\n")

# 2. run it on every pass, right after the saturated words (MED) it depends on are known
rep("          window.gsmMED = MED;\n        })(),", "          window.gsmMED = MED;\n          window.gsmDerive();\n        })(),")

# 3. In Parallel's grid draws from the derived points
a = s.index("                  function gsmGrid() {\n")
b = s.index("                    window.gsmGridPts = pts.filter(function (p) {\n                      return p.act;\n                    });\n", a)
e = b + len("                    window.gsmGridPts = pts.filter(function (p) {\n                      return p.act;\n                    });\n")
assert "var HARD = [3, 0, 2, 1, 4]" in s[a:e]
s = (
    s[:a]
    + "                  function gsmGrid() {\n"
    + "                    var pts = window.gsmGridAll || [];\n"
    + "                    if (pts.filter(function (p) {\n"
    + "                        return p.act;\n"
    + "                      }).length < 2) return \"\";\n"
    + "                    var ms = Math.max.apply(null, pts.map(function (p) { return p.shared; }).concat([1]));\n"
    + s[e:]
)

s = s.replace('t.textContent = "v198"', 't.textContent = "v199"')
assert 't.textContent = "v199"' in s
open(P, "w").write(s)
