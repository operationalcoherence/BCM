# v279: Same Emotion, Different Targets, item 5 in his order of the second generation of insight types
# (queue 11-20; his call 25 Nov 2026 16:04). ONE EMOTION, SEVERAL TARGETS, a card under WHY IT BEHAVES THIS WAY
# on Pattern Analysis, after WHO STANDS WHERE. Where a note names its own emotion and what it is aimed at
# ("distrust in leadership", "aggression toward supporters"), the target is read from the words after it.
# One emotion aimed at two or more different targets, across three or more notes, is said to be several
# things, each needing its own response. Targets are told apart by the person's own words, never merged:
# two targets are one only when they share a word that is not generic ("idea", "concept", "way").
# Second piece: an emotion word alone no longer pairs a hindrance with a response under NO RESPONSE YET and
# DOES THIS ANSWER IT? ("distrust" in both does not mean one answers the other).
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
    /* v279: ONE EMOTION, SEVERAL TARGETS */
    try {
      var TG = gsmTargets(src);
      SS.targets = TG;
      TG.length &&
        card(
          "ONE EMOTION, SEVERAL TARGETS",
          TG.map(function (t) {
            return "<p>" + t.say + "</p>";
          }).join(""),
          TG.map(function (t) {
            return t.groups
              .map(function (g) {
                return g.notes
                  .map(function (n) {
                    return "<div><i>" + E[n.em] + " at " + Gt(g.show) + (n.side > 0 ? ", helps" : n.side < 0 ? ", hinders" : "") + "</i>: " + gsmStQ(n, null, g.key[0]) + "</div>";
                  })
                  .join("");
              })
              .join("");
          }).join(""),
        );
    } catch (e) {}
    return R.length >= 1 ? '<div class="plab">WHY IT BEHAVES THIS WAY</div><div class="sreads">' + R.join("") + "</div>" : "";''')

# 2. the target reader
rep('''  function gsmCap(t) {''', r'''  /* v279: what a note's own emotion is aimed at. The note must name its emotion ("distrust", "aggressive",
     "defiance"...) and a preposition must follow within three words; the target is the words after it, up to
     the first clause break, with determiners and generic heads ("the idea of") taken off. General words only. */
  var GSMEMW = [
    "aggression|aggressive(?:ness)?|hostility|hostile|anger|angry",
    "acceptance|accepting",
    "distrust(?:s|ed|ing|ful)?|mistrust(?:s|ed|ing|ful)?|suspicion|suspicious",
    "indifference|indifferent|apathy|apathetic",
    "defiance|defiant|rebellion|rebellious",
  ];
  var GSMTGEN = /^(idea|ideas|concept|concepts|notion|way|ways|thing|things|kind|sort|type|part|whole|lot|level|degree|sense|matter|issue|aspect|form)$/;
  var GSMTDET = /^(the|a|an|what|how|its|their|our|his|her|this|that|these|any|all|some|such|being|it|them|him|me|us|you)$/;
  var GSMTCUT = /^(to|that|which|who|whom|will|would|is|are|was|were|be|been|can|could|should|may|might|must|has|have|had|does|do|did|but|or|as|when|while|for|with|by|in|of|on|at|from|over|into|about|because|if|than|so|not|and|since|after|before|until|during|especially|where|whenever|despite|without|through|among|amongst|within|toward|towards|against|under|between|now|then|again|too|also|even|only|just|still|yet|very|more|most|less)$/;
  function gsmTarget(n) {
    var W = GSMEMW[n.em];
    if (!W) return null;
    var t = String(n.txt || "").replace(/\s+/g, " "),
      rx = new RegExp("\\b(?:" + W + ")\\b((?:\\s+[a-z'-]+){0,3}?)\\s+(toward|towards|against|in|of|at|over|about)\\s+([^.;:!?()]+)", "gi"),
      /* a verb takes its target straight after it: "staff distrust the new system", "they accept the old way" */
      vb = [null, "accepts?|accepted", "distrusts?|distrusted|mistrusts?|mistrusted", null, "defy|defies|defied"][n.em],
      vx = vb ? new RegExp("\\b(?:" + vb + ")\\s+()()((?:the|a|an|their|its|our|this|these|those)\\s+[^.;:!?()]+)", "i").exec(t) : null,
      M = [],
      m;
    while ((m = rx.exec(t))) M.push(m);
    vx && M.push(vx);
    for (var mi = 0; mi < M.length; mi++) {
      m = M[mi];
      var tail = m[3];
      /* "toward and rejection of ...": read from the next preposition */
      var nx = /^\s*and\s+(?:[a-z'-]+\s+){0,2}?(?:toward|towards|against|in|of|at|over|about)\s+(.+)$/i.exec(tail);
      nx && (tail = nx[1]);
      var w = tail.split(",")[0].split(/\s+/).filter(Boolean),
        out = [],
        art = "",
        i = 0;
      /* "those who are defiant": people named by what they do */
      var th = /^(those|people|anyone|others)\s+who\s+(?:are|were|is)\s+([a-z-]+)/i.exec(m[3]);
      if (th) return { key: [th[2].toLowerCase()], show: th[1].toLowerCase() + " who are " + th[2].toLowerCase(), art: "" };
      while (i < w.length && GSMTDET.test(w[i].toLowerCase())) (art = /^(the|a|an)$/i.test(w[i]) ? w[i].toLowerCase() + " " : art), i++;
      if (i < w.length && "and" === w[i].toLowerCase()) continue; /* "toward and rejection of ...": the next one */
      while (i + 1 < w.length && GSMTGEN.test(w[i].toLowerCase()) && /^(of|for)$/i.test(w[i + 1])) {
        i += 2;
        art = "";
        while (i < w.length && GSMTDET.test(w[i].toLowerCase())) (art = /^(the|a|an)$/i.test(w[i]) ? w[i].toLowerCase() + " " : art), i++;
      }
      for (; i < w.length && out.length < 4; i++) {
        var x = w[i].replace(/[^A-Za-z'-]/g, ""),
          lx = x.toLowerCase();
        if (!lx) break;
        if (GSMTCUT.test(lx) && !("and" === lx && out.length && w[i + 1] && !GSMTDET.test(w[i + 1].toLowerCase()) && !GSMTCUT.test(w[i + 1].toLowerCase()))) break;
        if (/'s$/.test(lx)) {
          out.push(x.replace(/'s$/i, ""));
          break;
        }
        out.push(x);
      }
      while (out.length && GSMTGEN.test(out[out.length - 1].toLowerCase())) out.pop();
      var key = out
        .map(function (x) {
          return x.toLowerCase();
        })
        .filter(function (x) {
          return "and" !== x && !GSMTGEN.test(x) && x.length > 2;
        });
      if (key.length) return { key: key, show: art + out.join(" "), art: art };
    }
    return null;
  }
  function gsmTargets(src) {
    var E = GSMEMO,
      by = {},
      out = [];
    src.forEach(function (n) {
      if (!n.note || null == n.em) return;
      var t = gsmTarget(n);
      t && (by[n.em] = by[n.em] || []).push({ n: n, t: t });
    });
    Object.keys(by).forEach(function (em) {
      var L = by[em],
        G = [];
      if (L.length < 3) return;
      L.forEach(function (x) {
        var g = G.filter(function (g) {
          return x.t.key.some(function (k) {
            return g.key.indexOf(k) >= 0;
          });
        })[0];
        g ? (g.notes.push(x.n), x.t.key.forEach(function (k) { g.key.indexOf(k) < 0 && g.key.push(k); })) : G.push({ key: x.t.key.slice(), show: x.t.show, notes: [x.n] });
      });
      if (G.length < 2) return;
      /* people or something else: a target is people when it is a group word (v276) or "those who are ..." */
      G.forEach(function (g) {
        g.ppl = /^(those|people|anyone|others) who/.test(g.show) || GSMGRP.some(function (R) {
          return new RegExp("^(?:" + R[0] + ")$", "i").test(g.key[g.key.length - 1]) || new RegExp("^(?:" + R[0] + ")$", "i").test(g.key[0]);
        });
        g.side = g.notes.reduce(function (a, n) {
          return a + (n.side || 0);
        }, 0);
      });
      G.sort(function (a, b) {
        return b.notes.length - a.notes.length;
      });
      var e = E[em],
        list = gsmStList(
          G.map(function (g) {
            return "<b>" + Gt(g.show) + "</b>" + gsmStNB(g.notes);
          }),
          6,
        ),
        P = G.filter(function (g) {
          return g.ppl;
        }),
        O = G.filter(function (g) {
          return !g.ppl;
        }),
        H = G.filter(function (g) {
          return g.side > 0;
        }),
        N = G.filter(function (g) {
          return g.side < 0;
        }),
        most = G[0].notes.length >= 2 && G[0].notes.length > G[1].notes.length,
        say = gsmCap(e) + " here is not one thing. It is aimed at " + list + (most ? ", and " + Gt(G[0].show) + " draws the most of it." : ".");
      say +=
        P.length && O.length
          ? " " + gsmCap(e) + " aimed at people moves with what those people are seen to do; aimed at an idea or a thing, it moves with what people see of it at work."
          : P.length
            ? " Each group it is aimed at is its own relationship, and each moves with what that group is seen to do."
            : " Each moves with what people see of what it is aimed at.";
      say += " So no single answer to " + e + " will reach it: there are " + ["two", "three", "four", "five", "six", "seven"][Math.min(G.length, 7) - 2] + " things to answer, each where it points.";
      out.push({ em: +em, say: say, groups: G, n: L.length });
    });
    return out
      .sort(function (a, b) {
        return b.groups.length - a.groups.length || b.n - a.n;
      })
      .slice(0, 2);
  }
  function gsmCap(t) {''')

# 3. an emotion word alone does not pair a hindrance with a response
rep('''            var own = Object.keys(Ht(tx).k).filter(function (k) {
                return (
                  !CM[k] &&''',
'''            var own = Object.keys(Ht(tx).k).filter(function (k) {
                return (
                  !CM[k] &&
                  !/^(aggres|hostil|anger|angry|accept|distru|mistru|suspic|indiff|apath|defian|defiant|rebel)/.test(k) &&''')

rep('t && (t.textContent = "v278")', 't && (t.textContent = "v279")')
open(p, 'w', encoding='utf-8').write(s)
print('ok')
