"""v206: YOUR STORY SO FAR told as a story (review 3e).
The opening no longer leads with the workbook's most-used word. It tells the context in order, quoting
the user's own notes: where it starts (Q.1, why the goal has not taken root), what holds the goal back and
what already helps now, and what waits further on toward the goal, by where the notes sit on the line map
(left = now, toward the goal = later; above the line helps, below hinders). Only the context grasped
(Q.1-Q.4) tells the story; what the user would design stays in WHAT YOU WOULD DO. On place maps, where
position says nothing about time, the questions carry it (Q.2 holds back, Q.3 helps, Q.4 is what has to
come true). The word that does two jobs closes the story in one sentence. WHAT STANDS IN THE WAY is kept.
Usage: python3 v206_story.py gsm-readable.js"""
import sys

P = sys.argv[1]
s = open(P).read()

A = "              /* opening: what the workbook turns on */\n"
B = "              /* what stands in the way */\n"
i, j = s.index(A), s.index(B)
assert s.count(A) == 1 and s.count(B) == 1 and i < j
old = s[i:j]
assert "Your workbook turns on" in old

new = r"""              /* opening: the story of the context grasped, in the user's own words (v206) */
              (function () {
                function qt(t) {
                  var x = String(t || "").replace(/\s+/g, " ").trim(),
                    p = x.split(/(?<=[.!?])\s+(?=[A-Z0-9“"(])/),
                    k;
                  for (k = 0; k < p.length; k++)
                    if (p[k].split(" ").length >= 4) {
                      x = p[k];
                      break;
                    }
                  x.length > 110 && (x = x.slice(0, 110).replace(/\s+\S*$/, "") + "…");
                  return "“" + Gt(x.replace(/[\s.;:,]+$/, "")) + "”";
                }
                function cite(o) {
                  var l = /place/.test(o.lab) ? "place " + o.lab.replace(/\s*\(place\)/, "") : o.lab;
                  return qt(o.r[3]) + " (" + l + (null != o.r[5] ? ", " + EN[o.r[5]] : "") + ")";
                }
                function w(o) {
                  return String(o.r[3] || "").trim().split(/\s+/).length;
                }
                var HARD = { 4: 5, 0: 4, 2: 3, 3: 2, 1: 1 },
                  SOFT = { 1: 5, 3: 3, 2: 2, 0: 2, 4: 1 },
                  ctx = live.filter(function (o) {
                    return o.r[0] >= 1 && o.r[0] <= 4;
                  }),
                  line = ctx.filter(function (o) {
                    return !/place/.test(o.lab) && "number" == typeof o.r[1] && "number" == typeof o.r[2];
                  }),
                  S = [],
                  Q1 = (function () {
                    /* the Q.1 sentence that shares the most words with the goal and the other answers */
                    var a = String((C.a || [])[0] || "").replace(/\s+/g, " ").trim();
                    if (!a || /^(yes|no)\W*$/i.test(a)) return "";
                    var rest = (String(C.goal || "") + " " + (C.a || []).slice(1).join(" ")).toLowerCase(),
                      best = "",
                      bs = -1;
                    a.split(/(?<=[.!?])\s+(?=[A-Z0-9“"(])/).forEach(function (z) {
                      if (z.split(" ").length < 6) return;
                      var seen = {},
                        n = 0;
                      (z.toLowerCase().match(/[a-z][a-z'-]{4,}/g) || []).forEach(function (t) {
                        !seen[t] && rest.indexOf(t) >= 0 && (n++, (seen[t] = 1));
                      });
                      n > bs && ((bs = n), (best = z));
                    });
                    best = (best || a).replace(/^(however|but|and|also|so|yet|still|then|thus|therefore|moreover|instead)\b,?\s+/i, "");
                    best = best.charAt(0).toUpperCase() + best.slice(1);
                    return best.length > 160 ? best.slice(0, 160).replace(/\s+\S*$/, "") + "…" : best;
                  })();
                Q1 && S.push("It starts with why the goal has not taken root: “" + Gt(Q1.replace(/[\s.;:,]+$/, "")) + "” (Q.1).");
                function pick(L, n, wt, far) {
                  return L.slice()
                    .sort(function (a, b) {
                      return (
                        (w(b) >= 3) - (w(a) >= 3) ||
                        (far ? far(b) - far(a) : 0) ||
                        (wt[b.r[5]] || 0) - (wt[a.r[5]] || 0)
                      );
                    })
                    .slice(0, n);
                }
                function list(L) {
                  return and(L.map(cite));
                }
                if (line.length >= 3) {
                  var up = function (o) {
                      return o.r[2] < 118;
                    },
                    now = function (o) {
                      return o.r[1] < 157;
                    },
                    far = function (o) {
                      return Math.abs(o.r[2] - 118);
                    },
                    hn = line.filter(function (o) {
                      return !up(o) && now(o);
                    }),
                    pn = line.filter(function (o) {
                      return up(o) && now(o);
                    }),
                    hl = line.filter(function (o) {
                      return !up(o) && !now(o);
                    }),
                    pl = line.filter(function (o) {
                      return up(o) && !now(o);
                    });
                  hn.length &&
                    S.push(
                      "In the present, close at hand, " +
                        (hn.length > 1 ? "these hold it back: " : "this holds it back: ") +
                        list(pick(hn, 2, HARD, far)) +
                        ".",
                    );
                  pn.length &&
                    S.push(
                      (hn.length ? "On the same ground, where things help, you placed " : "In the present, where things help, you placed ") +
                        list(pick(pn, pn.length > 1 ? 2 : 1, SOFT, far)) +
                        ".",
                    );
                  (hl.length || pl.length) &&
                    S.push(
                      "Further on, toward the goal, " +
                        (hl.length ? list(pick(hl, 1, HARD, far)) + " waits on the side that hinders" : "") +
                        (hl.length && pl.length ? ", and " : "") +
                        (pl.length ? list(pick(pl, 1, SOFT, far)) + " on the side that helps" : "") +
                        ".",
                    );
                  var H = hn.length + hl.length,
                    U = pn.length + pl.length;
                  H >= 3 &&
                    U >= 3 &&
                    S.push(
                      (hn.length * 2 > H && pl.length * 2 > U
                        ? "Most of what hinders sits in the present (" + hn.length + " of " + H + "), and most of what helps lies further on (" + pl.length + " of " + U + "): the help is still ahead of the trouble."
                        : hl.length * 2 > H && pn.length * 2 > U
                          ? "Most of what helps is already here (" + pn.length + " of " + U + "), and most of what hinders lies further on (" + hl.length + " of " + H + "): the trouble is still ahead, which leaves time to meet it."
                          : hn.length * 2 > H && pn.length * 2 > U
                            ? "Most of what hinders (" + hn.length + " of " + H + ") and most of what helps (" + pn.length + " of " + U + ") sit in the present, so little of the context you have grasped yet reaches toward the goal."
                            : "What hinders and what helps are spread from the present toward the goal (" + hn.length + " of " + H + " hindering, and " + pn.length + " of " + U + " helping, sit in the present)."),
                    );
                } else {
                  var q2 = byQ([2]),
                    q3 = byQ([3]),
                    q4 = byQ([4]);
                  q2.length &&
                    S.push((q2.length > 1 ? "Today, these hold it back: " : "Today, this holds it back: ") + list(pick(q2, 2, HARD)) + ".");
                  q3.length && S.push("On the side that helps, you name " + list(pick(q3, 1, SOFT)) + ".");
                  q4.length && S.push("For the goal to take root, " + list(pick(q4, 1, SOFT)) + " has to come true.");
                }
                /* the word that does two jobs closes the story */
                if (mk) {
                  var M = MED[mk],
                    sides = { 1: [], "-1": [], 0: [] };
                  M.subs
                    .slice()
                    .sort(function (a, b) {
                      return M.cnt[b] - M.cnt[a];
                    })
                    .forEach(function (b) {
                      var u = 0,
                        d = 0;
                      live.forEach(function (o) {
                        var t = (o.tk = o.tk || Ht(o.r[3])).b;
                        t[b] && (o.r[2] < 118 ? u++ : d++);
                      });
                      sides[u > d ? 1 : d > u ? -1 : 0].push(b);
                    });
                  sides[1].length &&
                    sides[-1].length &&
                    S.push(
                      "Underneath it all, you use <b>“" +
                        Gt(jt(mk)) +
                        "”</b> on both sides: where things help, it is " +
                        q(sides[1].slice(0, 2)) +
                        "; where they hinder, " +
                        q(sides[-1].slice(0, 2)) +
                        ". The line between the two is the line your work has to draw for other people.",
                    );
                }
                S.length && (out += "<p>" + S.join(" ") + "</p>");
              })();
"""
s = s[:i] + new + s[j:]
s = s.replace('t.textContent = "v205"', 't.textContent = "v206"')
assert 't.textContent = "v206"' in s
open(P, "w").write(s)
