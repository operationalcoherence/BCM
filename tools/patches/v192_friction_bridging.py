"""v192 (F3 + F5): the ways forward feel the emotional ground they cross.
F3 friction: each step of a way costs by the emotion holding the ground there (acceptance least, then indifference,
distrust, aggression, defiance most), weighted by how strongly notes hold it. Boomerang risk: the way enters
aggression or defiance directly, without passing indifference first.
F5 bridging: each bare rock face a way crosses (two distant emotions meeting with no indifference between them)
costs by how far apart the two emotions are; the reading names the notes on either side.
Effort = climb + 0.15 x length ratio + 0.6 x friction + 0.5 x bridging."""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:80]); s = s.replace(a, b)

rep("""      var mk = Object.keys(met),
        hard = mk.filter(function (k) {
          return 0 === met[k] || 2 === met[k] || 4 === met[k];
        }),""", """      /* F3 friction and F5 rock faces, from the same emotion field the ground is colored by */
      var FRK = [0.2, 0.5, 1.0, 1.4, 1.8],
        RKE = [3, 0, 2, 1, 4],
        NS = terr && terr.notes ? terr.notes : [],
        sst = function (a, b, x) {
          var t = Math.max(0, Math.min(1, (x - a) / (b - a)));
          return t * t * (3 - 2 * t);
        },
        emoAt = function (x, y) {
          var ws = [0, 0, 0, 0, 0];
          NS.forEach(function (n) {
            if (null == n.e) return;
            var dx = n.x - x,
              dy = n.y - y,
              d2 = dx * dx + dy * dy;
            d2 < 10816 && (ws[n.e] += Math.exp(-d2 / 1352));
          });
          var k1 = 0,
            k2 = -1,
            tot = ws[0] + ws[1] + ws[2] + ws[3] + ws[4];
          for (var a = 1; a < 5; a++) ws[a] > ws[k1] && (k1 = a);
          for (var b = 0; b < 5; b++) b !== k1 && (k2 < 0 || ws[b] > ws[k2]) && (k2 = b);
          var g =
            Math.abs(RKE[k1] - RKE[k2]) < 2 || 1 === RKE[k1] || 1 === RKE[k2] || ws[k2] < 0.03
              ? 0
              : sst(0.22, 0.42, ws[k2] / (ws[k1] + ws[k2]));
          return { k1: k1, k2: k2, s: sst(0.04, 0.5, tot), g: g };
        },
        near = function (e, x, y) {
          var bk = null,
            bd = 1e9;
          NS.forEach(function (n) {
            if (n.e !== e) return;
            var d = Math.hypot(n.x - x, n.y - y);
            d < bd && ((bd = d), (bk = n.k));
          });
          return bk;
        },
        fric = 0,
        boom = [],
        rocks = [],
        bridge = 0,
        lastR = -1,
        inH = !1,
        inRk = !1;
      for (var i3 = 1; i3 < R.length; i3++) {
        var mx3 = (R[i3][0] + R[i3 - 1][0]) / 2,
          my3 = (R[i3][1] + R[i3 - 1][1]) / 2,
          dl3 = Math.hypot(R[i3][0] - R[i3 - 1][0], R[i3][1] - R[i3 - 1][1]),
          E3 = emoAt(mx3, my3),
          r3 = RKE[E3.k1];
        fric += dl3 * (0.3 * (1 - E3.s) + E3.s * FRK[r3]);
        if (E3.s > 0.45 && r3 >= 3) {
          if (!inH) {
            inH = !0;
            if (1 !== lastR) {
              var bk3 = near(E3.k1, mx3, my3);
              null != bk3 && boom.indexOf(bk3) < 0 && boom.push(bk3);
            }
          }
        } else (inH = !1), E3.s > 0.35 && (lastR = r3);
        if (E3.g > 0.5 && !inRk) {
          inRk = !0;
          var ra = near(E3.k1, mx3, my3),
            rb = near(E3.k2, mx3, my3),
            dd = Math.abs(RKE[E3.k1] - RKE[E3.k2]);
          rocks.some(function (r) {
            return (r.a === ra && r.b === rb) || (r.a === rb && r.b === ra);
          }) || rocks.push({ a: ra, b: rb, ea: E3.k1, eb: E3.k2, d: dd });
          bridge += dd;
        } else E3.g < 0.2 && (inRk = !1);
      }
      fric /= Math.max(1, straight);
      var mk = Object.keys(met),
        hard = mk.filter(function (k) {
          return 0 === met[k] || 2 === met[k] || 4 === met[k];
        }),""")
rep("""        effort: climb + 0.15 * (L / straight),
        impact: hard.length + 0.5 * Object.keys(emos).length,""", """        fric: fric,
        boom: boom,
        rocks: rocks,
        rock: bridge,
        effort: climb + 0.15 * (L / straight) + 0.6 * fric + 0.5 * bridge,
        impact: hard.length + 0.5 * Object.keys(emos).length,""")
rep("""            out.push({ k: "", title: R.key + ": why choose it", text: R.key + " is " + why });""", """            var en3 = function (e) {
                return EMO[e] ? String(EMO[e][0]).toLowerCase() : "";
              },
              xtra =
                (S.rocks && S.rocks.length
                  ? " It crosses " +
                    (1 === S.rocks.length ? "a bare rock face" : S.rocks.length + " bare rock faces") +
                    " (" +
                    S.rocks
                      .slice(0, 3)
                      .map(function (r) {
                        return (null != r.a ? "N" + r.a + ", " : "") + en3(r.ea) + ", against " + (null != r.b ? "N" + r.b + ", " : "") + en3(r.eb);
                      })
                      .join("; ") +
                    "), where two distant emotions meet with no indifference between them. That is the costliest ground to act on. A bridge there would be something both sides can first be indifferent to."
                  : "") +
                (S.boom && S.boom.length
                  ? " Boomerang risk: it goes straight into " +
                    list(
                      S.boom.slice(0, 3).map(function (k) {
                        var n = NSK[k];
                        return (n ? en3(n.e) + " at " : "") + "N" + k;
                      }),
                    ) +
                    " without passing indifference first, so pushing there can turn people further against the goal."
                  : "");
            out.push({ k: "", title: R.key + ": why choose it", text: R.key + " is " + why + xtra });""")
rep("""          ROUTES.forEach(function (R) {
            var S = R.st,
              why =""", """          var NSK = {};
          (terr && terr.notes ? terr.notes : []).forEach(function (n) {
            NSK[n.k] = n;
          });
          ROUTES.forEach(function (R) {
            var S = R.st,
              why =""")
rep("""          ["Effort", "effort", "How much climbing the way does: the energy it takes."],""", """          ["Effort", "effort", "The energy it takes: climbing, friction and rock faces together."],
          ["Friction", "fric", "How hard the emotional ground is to act on along the way: acceptance costs least, defiance most."],
          ["Rock faces", "rock", "Bare rock faces the way crosses, weighted by how far apart the two emotions are."],""")
rep('t.textContent = "v191"', 't.textContent = "v192"')
open(P, "w").write(s)
