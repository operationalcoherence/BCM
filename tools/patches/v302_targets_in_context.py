"""v302, his asks 26 Nov 2026 07:55.

1. Aggression (or any emotion) "is not one thing": each target is now named in the note's own phrase, quoted, not a
   trimmed keyword ("supporters" -> "supporters of the transition"; "complex adaptive system" -> "the complex adaptive
   system idea"), and who holds it when the note says ("among supporters"). Grouping still uses the keyword.
2. WHAT HOLDS THE SITUATION IN PLACE: "Most of it sits on X" only when X really is the most; a tie is named as a tie.
   On a place-only workbook it names no ground.
3. A card title quoted inside a sentence uses single quotes for its own inner quotes.
"""
import sys

P = "gsm-readable.js"
s = open(P, encoding="utf-8").read()


def rep(old, new, n=1):
    global s
    c = s.count(old)
    if c != n:
        sys.exit("expected %d, found %d: %r" % (n, c, old[:90]))
    s = s.replace(old, new)


# 1a. gsmTarget keeps the note's whole phrase (full) and who holds it (by)
rep(
    "  function gsmTarget(n) {\n    var W = GSMEMW[n.em];",
    """  /* v302: the target as the note says it, up to the end of its clause; a list ("defiant, aggressive, or distrustful
     of ...") is kept whole. At most 12 words. */
  function gsmTargetFull(tail) {
    var sg = String(tail).split(","),
      j = 0;
    for (var k = 1; k < sg.length && k <= 3; k++)
      if (/^\\s*(and|or)\\s/i.test(sg[k])) {
        j = k;
        break;
      }
    var mid = sg.slice(1, j).every(function (x) {
        return x.trim().split(/\\s+/).length <= 3;
      }),
      f = (j && mid && (j >= 2 || sg[j].trim().split(/\\s+/).length <= 4) ? sg.slice(0, j + 1).join(",") : sg[0]).replace(/\\s+/g, " ").trim().replace(/[\\s,]+$/, ""),
      w = f.split(" ");
    if (w.length > 12) {
      w = w.slice(0, 12);
      while (w.length > 3 && /^(and|or|the|a|an|of|to|in|on|at|for|with|by|they|it|are|is|was|now|that|any|other)$/i.test(w[w.length - 1])) w.pop();
      f = w.join(" ") + "…";
    }
    return f;
  }
  function gsmTarget(n) {
    var W = GSMEMW[n.em];""",
)
rep(
    """      var th = /^(those|people|anyone|others)\\s+who\\s+(?:are|were|is)\\s+([a-z-]+)/i.exec(m[3]);
      if (th) return { key: [th[2].toLowerCase()], show: th[1].toLowerCase() + " who are " + th[2].toLowerCase(), art: "" };""",
    """      var th = /^(those|people|anyone|others)\\s+who\\s+(?:are|were|is)\\s+([a-z-]+)/i.exec(m[3]),
        hb = /^\\s*((?:among|amongst|within|from)\\s+[a-z'-]+(?:\\s+[a-z'-]+)?)\\s*$/i.exec(m[1] || ""),
        FULL = gsmTargetFull(tail),
        BY = hb ? hb[1].toLowerCase().replace(/^amongst/, "among") : "";
      if (th) return { key: [th[2].toLowerCase()], show: th[1].toLowerCase() + " who are " + th[2].toLowerCase(), art: "", full: gsmTargetFull(m[3]), by: BY };""",
)
rep(
    '      if (key.length) return { key: key, show: art + out.join(" "), art: art };\n    }\n    return null;\n  }',
    '      if (key.length) return { key: key, show: art + out.join(" "), art: art, full: FULL, by: BY };\n    }\n    return null;\n  }',
)
# 1b. the groups carry the first note's phrase and holder
rep(
    ": G.push({ key: x.t.key.slice(), show: x.t.show, notes: [x.n] });",
    ": G.push({ key: x.t.key.slice(), show: x.t.show, full: x.t.full || x.t.show, by: x.t.by || \"\", notes: [x.n] });",
)
# 1c. the sentence names each target in the note's words
rep(
    '            return "<b>" + Gt(g.show) + "</b>" + gsmStNB(g.notes);',
    '            return "“<b>" + Gt(g.full || g.show) + "</b>”" + (g.by ? " (" + Gt(g.by) + ")" : "") + gsmStNB(g.notes);',
)
rep(
    'say = gsmCap(e) + " here is not one thing. It is aimed at " + list + (most ? ", and " + Gt(G[0].show) + " draws the most of it." : ".");',
    'say = gsmCap(e) + " here is not one thing. It is aimed at " + list + (most ? ", and “" + Gt(G[0].full || G[0].show) + "” draws the most of it." : ".");',
)

# 2. "Most of it" only when it is the most
rep(
    """      o.length &&
        ([0, 4].indexOf(o[0]) >= 0 && [0, 4].indexOf(o[1]) >= 0""",
    """      /* v302: a tie at the top is named as a tie, never as "most" */
      var TIE = o.length > 1 && em.c[o[0]] === em.c[o[1]]
        ? o.filter(function (i) {
            return em.c[i] === em.c[o[0]];
          })
        : null;
      TIE
        ? (function () {
            var lo = TIE.filter(function (i) {
                return [0, 2, 4].indexOf(i) >= 0;
              }),
              nm = gsmStList(
                TIE.map(function (i) {
                  return E[i];
                }),
                5,
              );
            g =
              "It carries " +
              nm +
              " in equal measure" +
              (lo.length && TIE.indexOf(3) >= 0
                ? ": the " + gsmStList(lo.map(function (i) { return E[i]; }), 5) + (lo.length > 1 ? " hold" : " holds") + " it in place, while the indifference could tip either way."
                : lo.length === TIE.length
                  ? ", which is why it holds: from there, change is unlikely in the short or medium term."
                  : ".");
          })()
        : o.length &&
        ([0, 4].indexOf(o[0]) >= 0 && [0, 4].indexOf(o[1]) >= 0""",
)
rep(
    """                  : (g = "Most of it carries acceptance: the people inside it are content with it, which is its own kind of hold."));""",
    """                  : (g = "Most of it carries acceptance: the people inside it are content with it, which is its own kind of hold."));
      gsmPlaceOnly() &&
        (g = g
          .replace(", the lowest ground and the longest road to acceptance,", ", the longest road to acceptance,")
          .replace(", the lowest ground,", ",")
          .replace(", low ground that can slide into defiance,", ", which can slide into defiance,")
          .replace(", low ground where trust", ", where trust"));""",
)

# 3. nested quotes in quoted card titles
rep(
    "                var PL = gsmPlaceOnly(),",
    "                var Q1 = function (t) {\n                    return Gt(String(t).replace(/[“\"]([^”\"]*)[”\"]/g, \"‘$1’\"));\n                  },\n                  PL = gsmPlaceOnly(),",
)
rep('“" + Gt(pr.title) + "”', '“" + Q1(pr.title) + "”', 2)
rep('“" + Gt(st.title) + "”', '“" + Q1(st.title) + "”', 2)

# 3b. the first move's titles are swapped for the cards' action titles after the cards are built
rep(
    'join("\\u201c" + Gt(a.textContent) + "\\u201d"));',
    'join("\\u201c" + Gt(a.textContent.replace(/\\u201c/g, "\\u2018").replace(/\\u201d/g, "\\u2019")) + "\\u201d"));',
)

rep('t && (t.textContent = "v301");', 't && (t.textContent = "v302");')

open(P, "w", encoding="utf-8").write(s)
print("ok")
