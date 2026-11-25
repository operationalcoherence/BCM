# v277: Risk After the Goal, item 3 in his order (queue 11-20; his "do it", 25 Nov 2026 15:32).
# RISK AFTER THE GOAL, a card under WHY IT BEHAVES THIS WAY on Pattern Analysis: the low ground that waits
# close to the goal on the side that hinders, where the change can be counted as done and still be undone.
# It says how (by emotion), whether what you would do reaches it, and any weight you put on it yourself
# ("the most dangerous"). It goes on: a row in Taking Action's THE TEST, and the map's number for a hollow
# at the goal says what it is. Line maps only. Inactive unless two or more notes on distrust, aggression,
# or defiance sit close to the goal on the side that hinders.
p = 'gsm-readable.js'
s = open(p, encoding='utf-8').read()

def rep(old, new, n=1):
    global s
    c = s.count(old)
    assert c == n, (c, old[:100])
    s = s.replace(old, new)

# 1. the card, after WHO STANDS WHERE
rep('''    } catch (e) {}
    return R.length >= 1 ? '<div class="plab">WHY IT BEHAVES THIS WAY</div><div class="sreads">' + R.join("") + "</div>" : "";''',
'''    } catch (e) {}
    /* v277: RISK AFTER THE GOAL */
    try {
      var AG = gsmAfterGoal();
      if (AG) {
        SS.after = AG.ns.map(function (n) {
          return n.ref;
        });
        card(
          "RISK AFTER THE GOAL",
          AG.say.map(function (t) {
            return "<p>" + t + "</p>";
          }).join(""),
          AG.ns
            .map(function (n) {
              return "<div><i>" + E[n.em] + "</i>: " + gsmStQ(n, null, AG.wk[n.ref]) + "</div>";
            })
            .join(""),
        );
      }
    } catch (e) {}
    return R.length >= 1 ? '<div class="plab">WHY IT BEHAVES THIS WAY</div><div class="sreads">' + R.join("") + "</div>" : "";''')

# 2. the reading
rep('''  function gsmCap(t) {''', r'''  /* v277: the low ground close to the goal. Close = the last third of the way (x past 225, as the stories
     read it); low = distrust, aggression, or defiance on the side that hinders. Each emotion undoes an
     arrived change its own way (Vigneaux, 2026): defiance keeps the old way in practice, aggression pushes
     the change back, distrust holds back from it or leaves. */
  var GSMWEIGHT = /\b(?:the\s+)?(?:most|single\s+most)\s+(dangerous|important|critical|serious|damaging|worrying)\b|\b(?:the\s+)?(?:biggest|greatest|main|largest|worst)\s+(?:risk|danger|threat|problem|obstacle)\b|\bcritical(?:ly)?\b|\bcrucial\b/i;
  function gsmAfterGoal() {
    if (!C.m || !C.m.length) return null;
    var E = GSMEMO,
      ns = [];
    C.m.forEach(function (t, i) {
      if (!t || !String(t[3] || "").trim() || "number" != typeof t[1] || "number" != typeof t[2]) return;
      var e = "number" == typeof t[5] ? t[5] : null;
      t[1] > 225 && t[2] > 118 && (0 === e || 2 === e || 4 === e) && ns.push({ ref: "note " + (i + 1), lab: "N" + (i + 1), txt: t[3], em: e, x: t[1], id: t[8], note: 1, side: -1 });
    });
    /* activation by a low ground, not by presence: where the map is big enough to have low grounds of its
       own (gsmSystems), only the notes of a low ground centred close to the goal count; on a small map,
       two such notes are enough */
    try {
      var Y = gsmSystems();
      if (Y.pts.length >= 12) {
        var inH = {};
        Y.low
          .filter(function (g) {
            return g.x > 225;
          })
          .forEach(function (g) {
            g.n.forEach(function (p) {
              inH[p.ref] = 1;
            });
          });
        ns = ns.filter(function (n) {
          return inH[n.ref];
        });
      }
    } catch (e) {}
    if (ns.length < 2) return null;
    var c = [0, 0, 0, 0, 0];
    ns.forEach(function (n) {
      c[n.em]++;
    });
    var ems = [4, 0, 2]
        .filter(function (e) {
          return c[e];
        })
        .sort(function (a, b) {
          return c[b] - c[a];
        }),
      HOW = {
        4: "defiance keeps the old way going in practice under the new name",
        0: "aggression pushes the change back once it has arrived",
        2: "distrust holds back from it, or leaves, once it has arrived",
      },
      say = [],
      wk = {};
    ns.sort(function (a, b) {
      return ems.indexOf(a.em) - ems.indexOf(b.em) || a.x - b.x;
    });
    say.push(
      "Close to the goal, on the side that hinders, the ground drops into " + gsmMeanList(ems.map(function (e) {
          return E[e];
        })) + gsmStNB(ns) +
        ". This is where the change would already count as done, so it can be undone after it looks finished: " +
        gsmMeanList(ems.map(function (e) {
          return HOW[e];
        })) + ".",
    );
    /* the author's own weight: words like "the most dangerous" in these notes */
    var hv = ns.filter(function (n) {
      var m = n.txt.match(GSMWEIGHT);
      return m && (wk[n.ref] = m[0].replace(/^the\s+/i, "").split(/\s+/).pop().toLowerCase().slice(0, 5));
    });
    hv.length &&
      say.push(
        "You put your own weight on it: " +
          hv
            .slice(0, 2)
            .map(function (n) {
              return "you called " + gsmStRef(n) + " “" + Gt(n.txt.match(GSMWEIGHT)[0].trim()) + "”";
            })
            .join(", and ") +
          ".",
      );
    /* does what you would do reach it? */
    var by = {},
      met = [],
      un = [];
    ns.forEach(function (n) {
      var b = gsmAfterReach(n);
      b.length ? (met.push(n), (by[n.lab] = b)) : un.push(n);
    });
    say.push(
      !un.length
        ? "What you would do (Q.5–Q.7) reaches each of them: " +
            gsmMeanList(
              met.map(function (n) {
                return gsmStRef(n) + " through " + Gt(by[n.lab].slice(0, 2).join(" and "));
              }),
            ) +
            ". Check that it reaches them in practice, not only in the same words."
        : !met.length
          ? "Nothing you would do (Q.5–Q.7) reaches them yet, so the plan stops where they begin."
          : "What you would do (Q.5–Q.7) reaches some of them, but not" + gsmStNB(un) + ", so part of this ground lies past where the plan stops.",
    );
    say.push(
      "Arrival here can't be read from what is announced. Decide early what the goal looks like in how people work, and count it reached only when that shows.",
    );
    return { ns: ns, say: say, wk: wk };
  }
  window.gsmAfterGoal = gsmAfterGoal;
  /* v277: what reaches a note at the goal: a design answer or note (Q.5-Q.7) sharing one of its words (the
     same words NOTHING YOU WOULD DO ANSWERS THESE YET reads), or a link you drew; your "No" to DOES THIS
     ANSWER IT? overrides. A note that itself hinders on distrust, aggression, or defiance never counts as
     reaching it, though it sits in Q.5-Q.7. Pattern Analysis and Taking Action both read this. */
  function gsmAfterReach(n) {
    var NR = window.gsmNR,
      i = +String(n.ref || "").replace(/\D/g, "") - 1,
      r = C.m && C.m[i];
    if (!NR || !NR.rw || !r) return [];
    if ("n" === (C.asks || {})["resp|" + r[8]]) return [];
    var bad = {};
    C.m.forEach(function (t, j) {
      t && t[2] > 118 && (0 === t[5] || 2 === t[5] || 4 === t[5]) && (bad["N" + (j + 1)] = 1);
    });
    var me = "N" + (i + 1),
      out = [];
    Object.keys(Ht(r[3] || "").k).forEach(function (k) {
      !(NR.cm || {})[k] &&
        (NR.rw[k] || []).forEach(function (l) {
          l !== me && !bad[l] && out.indexOf(l) < 0 && out.push(l);
        });
    });
    (C.links || []).some(function (l) {
      return (l.f === r[8] && (NR.ri || {})[l.t]) || (l.t === r[8] && (NR.ri || {})[l.f]);
    }) && out.push("a link you drew");
    return out;
  }
  window.gsmAfterReach = gsmAfterReach;
  function gsmCap(t) {''')

# 3. say once: the card says the closing line of the CLOSE TO THE GOAL chapter
rep('''      "goal" === wh && S.push("Near the goal, the way out also means judging the change by what people do, not by what has been declared.");''',
'''      "goal" === wh && !(window.gsmStructSum || {}).after && S.push("Near the goal, the way out also means judging the change by what people do, not by what has been declared.");''')

# 4. Taking Action: a row in THE TEST
rep('''              row("Where it can shift", shift) +''',
'''              row("Where it can shift", shift) +
              (function () {
                /* v277: RISK AFTER THE GOAL, tested like the rest */
                var AX = IT(SS.after);
                if (AX.length < 2) return "";
                var tA = { met: [], not: [] };
                AX.forEach(function (x) {
                  (gsmAfterReach({ ref: x.id }).length ? tA.met : tA.not).push(x);
                });
                tA.v = tA.not.length ? (tA.met.length ? "partly" : "not yet") : "yes";
                return row(
                  "After the goal",
                  "<div>" +
                    VL(tA) +
                    " " +
                    NAMES(AX) +
                    " wait close to the goal, on the side that hinders, where the change could be counted as done and still come undone." +
                    IDS(AX, 1) +
                    " " +
                    (tA.met.length
                      ? tA.not.length
                        ? "The proposed actions reach " + gsmStCount(tA.met.length, "").split(" ")[0] + " of them, but not yet " + phList(tA.not.map(NB)) + "."
                        : "The proposed actions reach all of them."
                      : "The proposed actions don\\u2019t reach them yet.") +
                    " Count the goal reached by how people work, not by what is announced.</div>",
                );
              })() +''')

# 5. the map: a hollow at the goal says what it is
rep('''            nearGoal && onLine
              ? "A drop just before the goal"
              : k === 0''',
'''            nearGoal && onLine
              ? "A drop just before the goal"
              : nearGoal && y > 118
                ? "Where it can come undone at the goal"
                : k === 0''')
rep('''          more:
            "Getting out toward the goal means a climb of " +''',
'''          more:
            (nearGoal && y > 118 && !onLine ? "This low ground waits where the change would already count as done (RISK AFTER THE GOAL). " : "") +
            "Getting out toward the goal means a climb of " +''')

rep('t && (t.textContent = "v276")', 't && (t.textContent = "v277")')
open(p, 'w', encoding='utf-8').write(s)
print('ok')
