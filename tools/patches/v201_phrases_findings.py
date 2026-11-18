"""v201: the phrase-and-meaning layer, second half (review plan, Phase 1 step 4; P1): Pattern Analysis and Synthesis.
1. WHAT YOU WOULD DO (Analysis, 3f): no "causes", no counts. It says plainly which things that stand in the way in
   the context you've grasped nothing you would design, redesign, or reinforce deals with yet, as phrases, each
   with the notes it comes from (each note number links to the map).
2. WHAT IT MIGHT MEAN (Synthesis, 4i): every list names phrases, not bare words, with the notes behind each, so
   each item links back to the map.
3. IN YOUR ANSWERS, NOT ON THE MAP (Synthesis, 4h): a single word is never shown as a theme. A word the workbook
   uses inside a phrase is shown as that phrase; a word with no phrase around it is left out.
4. POSSIBLE PATTERNS (Analysis, 3l): "What you talk about most may be what you have planned least" now counts the
   notes written under Q.5–Q.7 as planning, not only the answers; every finding there names its phrase.
5. ONE WORD, SEVERAL MEANINGS (Analysis, 3i): under each saturated word, a fold, EACH MEANING IN YOUR WORDS, that
   opens every meaning into its phrase and the sentences that carry it, with their notes; and the actions written
   around the word ("managing unplanned fires," "putting fire") are listed as meanings of their own.
Engine only, for every workbook. Needs v200's helpers.
Usage: python3 v201_phrases_findings.py gsm-readable.js"""
import sys

P = sys.argv[1]
s = open(P).read()


def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, (c, a[:90])
    s = s.replace(a, b)


HELP = r'''  // does a text carry all the stems in one sentence?
  function phIn(stems, text) {
    var S = phSet(stems);
    return phSents(text).some(function (sen) {
      var T = phToks(sen);
      return stems.every(function (k) {
        return T.some(function (o) {
          return !o.cap && phHas(o, k) && S[k];
        });
      });
    });
  }
  // a finding's name: the phrase the workbook uses around a key, and the notes that carry it.
  // ctx: only the context grasped (Q.1–Q.4 answers and notes)
  var PhNm = {};
  function gsmPhName(key, ctx) {
    var ck = key + (ctx ? "|c" : "");
    if (ck in PhNm) return PhNm[ck];
    return (PhNm[ck] = phKeep(function () {
      var stems = String(key).split(" "),
        all = phAll(),
        use = all.filter(function (x) {
          return !ctx || (x.q >= 1 && x.q <= 4);
        }),
        b = phBest(stems, use),
        ids = use
          .filter(function (x) {
            return /^N/.test(x.src) && phIn(stems, x.t);
          })
          .map(function (x) {
            return x.src;
          });
      // a finding names a phrase only when the workbook repeats it, or the goal uses it
      var B = b
        ? [b].concat(b.alt || []).filter(function (x) {
            return x.n >= 2 && (x.k >= 2 || x.g);
          })[0]
        : null;
      return { ph: B ? B.ph : jt(key), multi: !!B || stems.length > 1, ids: ids };
    }));
  }
  function gsmPhNameH(key, ctx) {
    var m = gsmPhName(key, ctx);
    return Gt(m.ph) + (m.ids.length ? " (" + phList(m.ids.slice(0, 3)) + ")" : "");
  }
  // the meanings of a saturated word, opened into phrases and sentences (ONE WORD, SEVERAL MEANINGS)
  function gsmSenses(w, subs) {
    return phKeep(function () {
      var all = phAll(),
        out = [],
        seen = {};
      subs.slice(0, 8).forEach(function (b) {
        var stems = String(b).split(" "),
          it = all.filter(function (x) {
            return "goal" !== x.src && phClause(stems, x.t, 18, stems.length > 1);
          }),
          best = phBest(stems, it),
          lines = [];
        if (!best) return;
        it.slice(0, 3).forEach(function (x) {
          var c = phClause(stems, x.t, 18, stems.length > 1);
          if (!c) return;
          // up to six words before it, within its clause, for context
          var at = c.sent.toLowerCase().indexOf(c.cl.replace(/…$/, "").toLowerCase()),
            pre = at > 0 ? c.sent.slice(0, at).split(/[,;:()]/).pop() : "",
            pw = pre.trim().split(/\s+/).filter(Boolean),
            lead = pw.slice(-6).join(" ");
          lines.push("“" + (pw.length > 6 ? "…" : "") + Gt((lead ? lead + " " : "") + c.cl) + "” (" + x.src + ")");
        });
        var k = best.ph.toLowerCase();
        seen[k] || ((seen[k] = 1), out.push("<p><b>" + Gt(best.ph) + "</b>: " + lines.join("; ") + "</p>"));
      });
      // actions written around the word: an -ing word just before it ("managing unplanned fires")
      var act = {};
      all.forEach(function (x) {
        if ("goal" === x.src) return;
        phSents(x.t).forEach(function (sen) {
          var T = phToks(sen);
          T.forEach(function (o, j) {
            if (o.cap || !phHas(o, w)) return;
            for (var a = j - 1; a >= 0 && a >= j - 2; a--) {
              if (!/^[\s\-–]*$/.test(phGap(sen, T, a, a + 1))) break;
              if (/ing$/i.test(T[a].w) && T[a].c) {
                var ph = phLow(sen.slice(T[a].i, o.e), T[a]),
                  kk = ph.toLowerCase();
                (act[kk] = act[kk] || { ph: ph, ids: [] }).ids.indexOf(x.src) < 0 && act[kk].ids.push(x.src);
                break;
              }
              if (!T[a].c) break;
            }
          });
        });
      });
      var A = Object.keys(act)
        .filter(function (k) {
          return !seen[k];
        })
        .sort(function (p, q) {
          return act[q].ids.length - act[p].ids.length || act[q].ph.split(" ").length - act[p].ph.split(" ").length;
        })
        .slice(0, 6)
        .map(function (k) {
          return "<b>" + Gt(act[k].ph) + "</b> (" + phList(act[k].ids.slice(0, 3)) + ")";
        });
      A.length && out.push("<p>Written as an action: " + phList(A) + ".</p>");
      return out.length
        ? '<details class="more"><summary>Each meaning, in your words</summary><div class="mtext">' + out.join("") + "</div></details>"
        : "";
    });
  }
'''
rep("  var PhTi = {};\n  function gsmPhTitle(key) {\n", HELP + "  var PhTi = {};\n  function gsmPhTitle(key) {\n")
rep("    PhUsed = {};\n    PhTi = {};\n", "    PhUsed = {};\n    PhTi = {};\n    PhNm = {};\n")

# sentences: abbreviations such as U.S. and a.m. do not end one
rep(
    "  function phSents(t) {\n    return (String(t || \"\").match(/[^.!?\\n]+[.!?]*/g) || [])\n      .map(function (x) {\n        return x.trim();\n      })",
    "  function phSents(t) {\n    return (String(t || \"\")\n      .replace(/\\b(?:[A-Za-z]\\.){2,}/g, function (m) {\n        return m.replace(/\\./g, \"\\u2024\");\n      })\n      .match(/[^.!?\\n]+[.!?]*/g) || [])\n      .map(function (x) {\n        return x.trim().replace(/\\u2024/g, \".\");\n      })",
)

# phClause: an optional fourth argument, near, asks for the stems side by side (within three words)
rep("  function phClause(stems, text, cap) {\n    cap = cap || 16;", "  function phClause(stems, text, cap, near) {\n    cap = cap || 16;")
rep(
    "      var a = hits.filter(covers).pop(),\n        last = hits[hits.length - 1],",
    "      var a = hits.filter(covers).pop(),\n        last = hits[hits.length - 1];\n"
    "      if (near) {\n"
    "        var cl0 = hits.filter(function (j) {\n"
    "          return stems.every(function (k) {\n"
    "            return hits.some(function (h) {\n"
    "              return h >= j && h <= j + 3 && phHas(T[h], k);\n"
    "            });\n"
    "          });\n"
    "        })[0];\n"
    "        if (null == cl0) return !1;\n"
    "        a = cl0;\n"
    "        last = Math.max.apply(null, hits.filter(function (h) {\n"
    "          return h >= a && h <= a + 3;\n"
    "        }));\n"
    "      }\n"
    "      var",
)

# 1. WHAT YOU WOULD DO
rep(
    """                un.length + an.length &&
                  (s4 +=
                    " Of the words and phrases you use for causes, opposition, and conditions, " +
                    an.length +
                    " also turn up in what you would do and " +
                    un.length +
                    " do not" +
                    (un.length ? ", among them " + q(un.slice(0, 3)) : "") +
                    "." +""",
    """                un.length &&
                  (s4 +=
                    " Nothing you would design, redesign, or reinforce deals yet with " +
                    phList(
                      un.slice(0, 3).map(function (k) {
                        return gsmPhNameH(k, 1);
                      }),
                    ) +
                    (un.length > 3 ? ", among other things" : "") +
                    " that stand in the way in the context you’ve grasped." +""",
)

# 2. WHAT IT MIGHT MEAN: phrases, with the notes behind each
rep(
    """                  e
                    .slice(0, 4)
                    .map(function (t) {
                      return Gt(jt(t));
                    })
                    .join(", ") +
                  (e.length > 4 ? ", and " + (e.length - 4) + " more" : "") +
                  ". " +
                  (e.length > 1 ? rt[t][1] : rt[t][2]) +""",
    """                  e
                    .slice(0, 4)
                    .map(function (k) {
                      return gsmPhNameH(k, "unanswered" === t || "condition" === t);
                    })
                    .join("; ") +
                  (e.length > 4 ? "; and " + (e.length - 4) + " more" : "") +
                  ". " +
                  (e.length > 1 ? rt[t][1] : rt[t][2]) +""",
)

# 3. IN YOUR ANSWERS, NOT ON THE MAP: no single word as a theme
rep(
    """          if (!SH.length && !WQ.length && !WD.length) return;
          function srt(x, y) {""",
    """          var one = function (c) {
            return c.key.indexOf(" ") < 0 && !gsmPhName(c.key).multi;
          };
          SH = SH.filter(function (c) {
            return !one(c);
          });
          WD = WD.filter(function (c) {
            return !one(c);
          });
          if (!SH.length && !WQ.length && !WD.length) return;
          function srt(x, y) {""",
)
rep(
    """                    '<div class="csl">“' +
                    Gt(jt(c.key)) +
                    '”</div><div class="cq">In ' +""",
    """                    '<div class="csl">“' +
                    Gt(gsmPhName(c.key).ph) +
                    '”</div><div class="cq">In ' +""",
)
rep(
    """              (WD.length > 1 ? "These single words also run" : "This single word also runs") +
              " through three or more of your answers and " +
              (WD.length > 1 ? "appear" : "appears") +
              " in one note at most. A word can be a theme or just wording, and Patterns cannot tell which, so it asks.</p>" +
              window.gsmTHW
                .map(function (c, i) {
                  return (
                    '<div style="margin:6px 0 10px">“' +
                    Gt(jt(c.key)) +""",
    """              (WD.length > 1 ? "These phrases also run" : "This phrase also runs") +
              " through three or more of your answers and " +
              (WD.length > 1 ? "appear" : "appears") +
              " in one note at most. A phrase can be a theme or just wording, and Patterns cannot tell which, so it asks.</p>" +
              window.gsmTHW
                .map(function (c, i) {
                  return (
                    '<div style="margin:6px 0 10px">“' +
                    Gt(gsmPhName(c.key).ph) +""",
)
# the header counts phrases only now
rep(
    """              nn = nw && nw < SH.length ? "phrases and words" : nw ? "words" : "phrases",
              n1 = nw ? "word" : "phrase";""",
    """              nn = "phrases",
              n1 = "phrase";""",
)

# 4. POSSIBLE PATTERNS: notes under Q.5–Q.7 count as planning; names are phrases
rep(
    """          var b = lo(
            Object.keys(g).filter(function (t) {
              return (
                g[t] >= 2 &&
                t.indexOf(" ") < 0 &&
                [0, 1, 2, 3].some(function (e) {
                  return s[e] && i[e].k[t];
                }) &&
                ![4, 5, 6].some(function (e) {
                  return i[e].k[t];
                })
              );
            }),
          );""",
    """          var NK5 = phKeep(function () {
              var o = {};
              ((window.gsmData ? window.gsmData().m : []) || []).forEach(function (r) {
                r[0] >= 5 && r[0] <= 7 && Object.assign(o, Ht(r[3] || "").k);
              });
              return o;
            }),
            b = lo(
            Object.keys(g).filter(function (t) {
              return (
                g[t] >= 2 &&
                t.indexOf(" ") < 0 &&
                [0, 1, 2, 3].some(function (e) {
                  return s[e] && i[e].k[t];
                }) &&
                ![4, 5, 6].some(function (e) {
                  return i[e].k[t];
                }) &&
                !NK5[t]
              );
            }),
          );""",
)
rep(
    """                    t[3]
                      ? (n = t[3].map(function (t) {
                          return jt(t);
                        }))""",
    """                    t[3]
                      ? (n = t[3].map(function (t) {
                          return gsmPhName(t).ph;
                        }))""",
)
rep(
    '                        " comes up often, but none of your actions (Q.5–Q.7) mention it. What you talk about most may be what you have planned least."',
    '                        " comes up often, but nothing you would design, redesign, or reinforce (Q.5–Q.7, answers or notes) mentions it. What you talk about most may be what you have planned least."',
)

# 5. ONE WORD, SEVERAL MEANINGS: each meaning opened, and the actions around the word
i = s.index(" Patterns reads these as separate ideas from here on and no longer reports the bare word by itself.")
j = s.index("              M.subs,\n              null,\n            );", i)
assert s.count("              M.subs,\n              null,\n            );") == 1
s = s[:j].rstrip().rstrip(",") + "\n                +\n                gsmSenses(w, rows.map(function (x) {\n                  return x.b;\n                })),\n" + s[j:]


rep("    var K = Object.keys(cnt).sort(function (p, q) {", "    for (var kk in ex) ex[kk].k = cnt[kk];\n    var K = Object.keys(cnt).sort(function (p, q) {")

s = s.replace('t.textContent = "v200"', 't.textContent = "v201"')
assert 't.textContent = "v201"' in s
open(P, "w").write(s)
