"""v195 (F7): lexical world-making and a perturbation audit, folded into one item on Pattern Analysis
(IN THE WORDS): WORDS THAT MAKE THE WORLD.
1. For each word used everywhere (the E2 saturation words), the answers and notes that use it bare, with nothing beside
   it to say which kind, and the kinds already written elsewhere. Nothing is rewritten; the reframing is his to do.
2. Notes from other voices are tested against the ground his own notes make: where one carries an emotion two or more
   steps from his nearby notes, it is a perturbation to test, not an instruction (Maturana & Varela)."""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:80]); s = s.replace(a, b)

rep("""          var E = Object.keys(r.k).filter(function (t) {
            return (
              !k[t] &&""", """          (function () {
            var EN = ["aggression", "acceptance", "distrust", "indifference", "defiance"],
              RK = [3, 0, 2, 1, 4],
              parts = [],
              lst = function (a) {
                return a.length > 1 ? a.slice(0, -1).join(", ") + " and " + a[a.length - 1] : a[0] || "";
              };
            Object.keys(window.gsmMED || {})
              .sort(function (x, y) {
                return window.gsmMED[y].n - window.gsmMED[x].n;
              })
              .slice(0, 3)
              .forEach(function (w) {
                var M = window.gsmMED[w],
                  re = new RegExp("\\\\b" + String(w).replace(/[^a-z0-9]/gi, "").toLowerCase() + "\\\\b"),
                  bare = n
                    .filter(function (pc) {
                      return (
                        "GOAL" !== pc.id &&
                        re.test(pc.raw || "") &&
                        !(M.subs || []).some(function (b) {
                          return pc.t && pc.t.b && pc.t.b[b];
                        })
                      );
                    })
                    .map(function (pc) {
                      return o(pc.id);
                    }),
                  kinds = (M.subs || [])
                    .slice()
                    .sort(function (x, y) {
                      return (M.cnt[y] || 0) - (M.cnt[x] || 0);
                    })
                    .slice(0, 4)
                    .map(function (b) {
                      return "<b>" + Gt(jt(b)) + "</b>";
                    });
                bare.length &&
                  parts.push(
                    "<p><b>“" +
                      Gt(jt(w)) +
                      "”</b> stands alone in " +
                      lst(bare.slice(0, 8)) +
                      (bare.length > 8 ? " and " + (bare.length - 8) + " more" : "") +
                      ": nothing beside it says which " +
                      Gt(jt(w)) +
                      "." +
                      (kinds.length ? " Elsewhere you write " + lst(kinds) + "." : "") +
                      " Naming the kind changes what a reader sees, and what Patterns can read.</p>",
                  );
              });
            var D = window.gsmData ? window.gsmData() : { m: [] },
              own = function (r) {
                return !r[7] || "Mine" === r[7] || r[7] === (C.who || "").trim();
              },
              pl = !!D.place,
              lab = function (i) {
                return "N" + (i + 1) + (C.m.length && C.p.m.length ? (pl ? " (place)" : " (line)") : "");
              },
              rows = (D.m || []).map(function (r, i) {
                return { r: r, i: i };
              }).filter(function (x) {
                return Array.isArray(x.r) && String(x.r[3] || "").trim() && null != x.r[5] && isFinite(+x.r[1]) && isFinite(+x.r[2]);
              }),
              pert = [];
            rows.forEach(function (x) {
              if (own(x.r)) return;
              var nb = rows
                .filter(function (y) {
                  return own(y.r);
                })
                .map(function (y) {
                  return { y: y, d: Math.hypot(+y.r[1] - +x.r[1], +y.r[2] - +x.r[2]) };
                })
                .filter(function (z) {
                  return z.d < 60;
                })
                .sort(function (a, b) {
                  return a.d - b.d;
                })
                .slice(0, 3);
              if (!nb.length) return;
              var cnt = {};
              nb.forEach(function (z) {
                cnt[z.y.r[5]] = (cnt[z.y.r[5]] || 0) + 1;
              });
              var maj = +Object.keys(cnt).sort(function (a, b) {
                return cnt[b] - cnt[a];
              })[0];
              Math.abs(RK[x.r[5]] - RK[maj]) >= 2 &&
                pert.push(
                  lab(x.i) +
                    " (" +
                    Gt(String(x.r[7])) +
                    ") carries " +
                    EN[x.r[5]] +
                    " where your own notes near it (" +
                    lst(
                      nb.map(function (z) {
                        return lab(z.y.i);
                      }),
                    ) +
                    ") carry " +
                    EN[maj],
                );
            });
            pert.length &&
              parts.push(
                "<p>Notes from other voices perturb the ground your notes make; they do not instruct it (Maturana &amp; Varela). " +
                  lst(pert.slice(0, 5)) +
                  ". Test each one: what would have to be true for both to hold? If it holds up, change the map; if not, keep it as a voice.</p>",
              );
            parts.length &&
              c(
                "WORDS THAT MAKE THE WORLD",
                '<details class="f7"><summary style="cursor:pointer;text-decoration:underline">Which words, and whose voices, shape this map (' +
                  parts.length +
                  ")</summary>" +
                  parts.join("") +
                  '<p style="color:#666;font-size:13px">Language brings forth the world it speaks of (Winograd &amp; Flores, 1986). Nothing here rewrites your words.</p></details>',
                [],
                null,
              );
          })();
          var E = Object.keys(r.k).filter(function (t) {
            return (
              !k[t] &&""")
rep('t.textContent = "v194"', 't.textContent = "v195"')
open(P, "w").write(s)
