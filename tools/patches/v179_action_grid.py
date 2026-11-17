"""v179: T4, the action grid (after axis.png): every action note (Q.5-Q.7) plotted by how hard it is to take
(the emotion and side of the line it sits in) and how far it reaches (act here: tied to one kind of ground;
act anywhere: its words run through notes in many emotions). On In Parallel, feeding Taking Action."""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:80]); s = s.replace(a, b)

GRID = r'''
                  function gsmGrid() {
                    var M = (window.gsmData ? window.gsmData().m || [] : []).map(function (r, i) {
                        return { r: r, id: "N" + (i + 1), t: Ht(r[3] || "") };
                      }).filter(function (o) {
                        return String(o.r[3] || "").trim();
                      }),
                      A = M.filter(function (o) {
                        return o.r[0] >= 5;
                      });
                    if (A.length < 2) return "";
                    var HARD = [3, 0, 2, 1, 4], /* emotion index -> difficulty rank: acceptance 0 ... defiance 4 */
                      MED = window.gsmMED || {},
                      pts = A.map(function (o) {
                        var e = o.r[5],
                          d = (null == e ? 2 : HARD[e]) + (o.r[2] >= 118 ? 1 : 0),
                          emo = {},
                          shared = 0;
                        M.forEach(function (p) {
                          if (p === o) return;
                          var hit = Object.keys(o.t.k).some(function (k) {
                            return !MED[k] && p.t.k[k];
                          });
                          hit && (shared++, null != p.r[5] && (emo[p.r[5]] = 1));
                        });
                        return { id: o.id, q: o.r[0], d: d / 5, reach: Object.keys(emo).length, shared: shared, e: e };
                      }),
                      mr = Math.max.apply(
                        null,
                        pts.map(function (p) {
                          return p.reach;
                        }).concat([1]),
                      );
                    pts.forEach(function (p) {
                      p.any = p.reach / mr;
                    });
                    var W = 520,
                      H = 360,
                      cx = W / 2,
                      cy = H / 2,
                      col = ["#c8352e", "#2a9d8f", "#a48fd0", "#e6be4f", "#1b2a8f"],
                      used = {},
                      dots = pts
                        .map(function (p) {
                          var x = 70 + p.d * (W - 140),
                            y = 40 + p.any * (H - 80),
                            k = Math.round(x / 14) + "," + Math.round(y / 14);
                          while (used[k]) {
                            y += 13;
                            k = Math.round(x / 14) + "," + Math.round(y / 14);
                          }
                          used[k] = 1;
                          return (
                            '<g><circle cx="' + x.toFixed(1) + '" cy="' + y.toFixed(1) + '" r="7" fill="' +
                            (null == p.e ? "#fff" : col[p.e]) +
                            '" stroke="#111" stroke-width="1.2"/><text x="' + (x + 10).toFixed(1) + '" y="' + (y + 4).toFixed(1) +
                            '" font-size="12" font-family="Questrial,Helvetica,Arial,sans-serif" fill="#111">' + p.id + "</text></g>"
                          );
                        })
                        .join(""),
                      svg =
                        '<svg viewBox="0 0 ' + W + " " + H + '" style="display:block;width:100%;max-width:560px;height:auto;margin:6px auto;background:#fff" role="img" aria-label="Actions by ease and reach">' +
                        '<line x1="' + cx + '" y1="24" x2="' + cx + '" y2="' + (H - 24) + '" stroke="#111" stroke-width="1"/>' +
                        '<line x1="40" y1="' + cy + '" x2="' + (W - 40) + '" y2="' + cy + '" stroke="#111" stroke-width="1"/>' +
                        '<g font-family="Questrial,Helvetica,Arial,sans-serif" font-size="15" fill="#111" text-anchor="middle">' +
                        '<text x="' + cx + '" y="16">Act Here</text><text x="' + cx + '" y="' + (H - 6) + '">Act Anywhere</text>' +
                        '<text x="34" y="' + (cy - 8) + '" text-anchor="start">Easy</text><text x="' + (W - 34) + '" y="' + (cy - 8) + '" text-anchor="end">Difficult</text></g>' +
                        dots +
                        "</svg>",
                      q4 = function (f) {
                        return pts.filter(f).map(function (p) {
                          return p.id;
                        });
                      },
                      li = function (a) {
                        return a.length > 1 ? a.slice(0, -1).join(", ") + " and " + a[a.length - 1] : a[0];
                      },
                      ea = q4(function (p) {
                        return p.d < 0.5 && p.any >= 0.5;
                      }),
                      eh = q4(function (p) {
                        return p.d < 0.5 && p.any < 0.5;
                      }),
                      da = q4(function (p) {
                        return p.d >= 0.5 && p.any >= 0.5;
                      }),
                      dh = q4(function (p) {
                        return p.d >= 0.5 && p.any < 0.5;
                      }),
                      tx = [];
                    ea.length &&
                      tx.push("<b>Easy, and they act anywhere:</b> " + li(ea) + ". Little energy, and their words run through notes in many emotions, so they travel. Start here.");
                    eh.length &&
                      tx.push("<b>Easy, but they act here:</b> " + li(eh) + ". Cheap to take, but tied to one kind of ground. Good first steps in that place, not everywhere.");
                    da.length &&
                      tx.push("<b>Difficult, but they act anywhere:</b> " + li(da) + ". They cost energy, yet what they touch runs through the whole workbook. Worth the effort once something is moving.");
                    dh.length &&
                      tx.push("<b>Difficult, and they act here:</b> " + li(dh) + ". Costly and local. Take them only where that ground is what stands between you and the goal, and watch them closely.");
                    return (
                      '<div class="intl"><b>Actions by ease and reach.</b> Every note you placed as something to design, redesign or reinforce (Q.5–Q.7). Left to right: how hard it is to take, from the emotion it sits in and whether it is above or below the line. Top to bottom: how far it reaches, from acting here (its words meet notes in few emotions) to acting anywhere (its words run through notes in many). Colors are the emotions.</div>' +
                      svg +
                      '<div class="intl">' + tx.join("<br>") + "</div>"
                    );
                  }
'''
rep("""                  var st = function (t) {
                      var e = t.cloneNode(!0);""", GRID + """                  var st = function (t) {
                      var e = t.cloneNode(!0);""")
rep("""                        ? '<div class="intsub" style="margin:4px 0 8px">Both pictures on one map.""", """                        ? gsmGrid() + '<div class="intsub" style="margin:4px 0 8px">Both pictures on one map.""")
rep('t && (t.textContent = "v178");', 't && (t.textContent = "v179");')
open(P, "w").write(s); print("v179 ok")
