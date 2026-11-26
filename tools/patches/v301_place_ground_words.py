"""v301: Broadview visual checks (v293 to v300).

1. The map placeholder read "Building the land" plus a broken character: a CSS escape lost its backslash
   inside the JS string. Every workbook.
2. Opened story folds ("Your story in greater detail", "The whole workbook read as one story") showed their
   text dark red and underlined: a rule for small "read more" links also caught these folds. Every workbook.
3. Place-only workbooks: Pattern Analysis and the Taking Action summary still spoke of ridges, high ground,
   low ground and bare rock. They now name emotions, as the cards have since v300. Line maps unchanged.
4. DOES THIS ANSWER THE GOAL?: no ". after a quote that already ends in a period. Every workbook.
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


PO = "gsmPlaceOnly()"

# 1. placeholder escape
rep("content:'Building the land\\2026'", "content:'Building the land\\\\2026'")

# 2. read-more rule no longer reaches the story folds
rep(".gterr .more{color:#7a1d12;", ".gterr .more:not(details){color:#7a1d12;")

# 3a. Taking Action summary: where it can shift
rep(
    '" Most shifts happen on the ridge of indifference, where people are not yet for or against: " +',
    '(' + PO + ' ? " Most shifts pass through indifference, where people are not yet for or against: " : " Most shifts happen on the ridge of indifference, where people are not yet for or against: ") +',
)
rep(
    ': "<div>" + VL({ v: "not yet" }) + " No one is mapped as not yet for or against, so there is no ridge of indifference: every shift is a climb over bare rock. Ask who is not yet for or against.</div>",',
    ': "<div>" + VL({ v: "not yet" }) + (' + PO + ' ? " No one is mapped as not yet for or against, so there is no indifference to pass through: every shift is a big jump. Ask who is not yet for or against.</div>" : " No one is mapped as not yet for or against, so there is no ridge of indifference: every shift is a climb over bare rock. Ask who is not yet for or against.</div>"),',
)

# 3b. THE CHEAPEST FIRST MOVE (also read by the one-story fold)
rep(
    "FT = (pr || st || {}).title || \"\";\n                return pr && st",
    "FT = (pr || st || {}).title || \"\";\n                var PL = " + PO + ",\n                  HG = PL ? \"it already stands in acceptance\" : \"it stands on high ground\",\n                  RG = PL ? \"through indifference\" : \"through the ridge\";\n                return pr && st",
)
rep(
    '"”: it stands on high ground and asks for no crossing. Then take up the strategy “" + Gt(st.title) + "”, crossing where it is cheapest, through the ridge."',
    '"”: " + HG + " and asks for no crossing. Then take up the strategy “" + Gt(st.title) + "”, crossing where it is cheapest, " + RG + "."',
)
rep(
    '? "Start with the strategy “" + Gt(st.title) + "”, crossing where it is cheapest, through the ridge."',
    '? "Start with the strategy “" + Gt(st.title) + "”, crossing where it is cheapest, " + RG + "."',
)
rep(
    '? "Start with the program “" + Gt(pr.title) + "”: it stands on high ground and asks for no crossing."',
    '? "Start with the program “" + Gt(pr.title) + "”: " + HG + " and asks for no crossing."',
)

# 3c. THE OPPORTUNITY
rep(
    '? " It stands on the high ground of acceptance, the ground with the most promise, but acceptance doesn’t hold on its own: what isn’t reinforced can slip."',
    '? (' + PO + ' ? " It already stands in acceptance, the emotion with the most promise, but acceptance doesn’t hold on its own: what isn’t reinforced can slip." : " It stands on the high ground of acceptance, the ground with the most promise, but acceptance doesn’t hold on its own: what isn’t reinforced can slip.")',
)

# 3d. THE BARE LANDSCAPE: what can move now
rep(
    '"%: acceptance on the helping side and the ridge of indifference. " +\n            (by[bI].n\n              ? "The ridge holds " +',
    '(' + PO + ' ? "%: acceptance on the helping side and indifference. " : "%: acceptance on the helping side and the ridge of indifference. ") +\n            (by[bI].n\n              ? (' + PO + ' ? "Indifference holds " : "The ridge holds ") +',
)
rep(
    '"% of that tilts against the goal. That is ground that can still be explored and possibly constructively engaged with, and it is the crossing most other moves have to use."\n              : "No note carries indifference, so there is no ridge to cross by.") +',
    '(' + PO + ' ? "% of that tilts against the goal. That can still be explored and possibly constructively engaged with, and it is the step most other moves have to pass through." : "% of that tilts against the goal. That is ground that can still be explored and possibly constructively engaged with, and it is the crossing most other moves have to use.")\n              : ' + PO + ' ? "No note carries indifference, so there is no middle step to move through." : "No note carries indifference, so there is no ridge to cross by.") +',
)
# 3e. THE BARE LANDSCAPE: where understanding turns into doing
rep(
    '? "Your plans sit on " +\n                  (la > lc ? "lower" : "higher") +\n                  " ground than the situation does (" +',
    '? (' + PO + ' ? "Your plans carry " + (la > lc ? "more" : "less") + " resistance than the situation does (" : "Your plans sit on " + (la > lc ? "lower" : "higher") + " ground than the situation does (") +',
)

# 3f. YOUR LANDSCAPE: what this suggests
rep(
    '(t += " The high ground belongs mostly to <b>Q." + hi.q',
    '(t += (' + PO + ' ? " Acceptance belongs mostly to <b>Q." : " The high ground belongs mostly to <b>Q.") + hi.q',
)
rep(
    '" The lowest ground belongs to <b>Q." +\n            lo.q +',
    '(' + PO + ' ? " Aggression and defiance belong mostly to <b>Q." : " The lowest ground belongs to <b>Q.") +\n            lo.q +',
)
rep(
    '" something you would do, placed in hard ground. Those actions will meet the emotion there before they reach the goal.");',
    '(' + PO + ' ? " something you would do, placed among resistance. Those actions will meet the emotion there before they reach the goal." : " something you would do, placed in hard ground. Those actions will meet the emotion there before they reach the goal."));',
)
rep(
    '" indifference: the ridge, where most moves between emotions cross.");',
    '(' + PO + ' ? " indifference, the step most moves between emotions pass through." : " indifference: the ridge, where most moves between emotions cross."));',
)

# 3g. YOUR LANDSCAPE legend: on a place map the land is real, so emotions are named, not ground
rep(
    '        var txt = R\n          ? e[0] + ": " + (i === 1 ? "cuts a channel" : i === 3 ? "a ridge" : "rises as a wall")\n          : o[1];',
    '        var txt = R\n          ? e[0] + ": " + (i === 1 ? "cuts a channel" : i === 3 ? "a ridge" : "rises as a wall")\n          : ' + PO + '\n            ? e[0]\n            : o[1];',
)
rep(
    "      row(\n        '<svg width=\"30\" height=\"14\"><rect x=\"1\" y=\"2\" width=\"28\" height=\"10\" rx=\"2\" fill=\"rgb(140,135,127)\" stroke=\"#bbb\"/></svg>',\n        \"Bare rock face: two distant emotions meet",
    "      " + PO + " || row(\n        '<svg width=\"30\" height=\"14\"><rect x=\"1\" y=\"2\" width=\"28\" height=\"10\" rx=\"2\" fill=\"rgb(140,135,127)\" stroke=\"#bbb\"/></svg>',\n        \"Bare rock face: two distant emotions meet",
)

# 4. no ". after a quote that already ends in a period
rep(
    '                                  return (a0 > 0 ? "…" : "") + x.slice(a0, b0) + (b0 < x.length ? "…" : "");\n                                })(sn),\n                              ) +\n                              "”"\n                            : "") +\n                          ". Does " +',
    '                                  return (a0 > 0 ? "…" : "") + (b0 < x.length ? x.slice(a0, b0) + "…" : x.slice(a0, b0).replace(/\\.\\s*$/, ""));\n                                })(sn),\n                              ) +\n                              "”"\n                            : "") +\n                          ". Does " +',
)

# 5. the terrain block is its own scope: share the helper with it
rep(
    '  function gsmPlaceOnly() {\n    return (\n      !(C.m || []).some(function (t) {\n        return Array.isArray(t) && String(t[3] || "").trim();\n      }) && !!((C.p && C.p.m) || []).length\n    );\n  }\n',
    '  function gsmPlaceOnly() {\n    return (\n      !(C.m || []).some(function (t) {\n        return Array.isArray(t) && String(t[3] || "").trim();\n      }) && !!((C.p && C.p.m) || []).length\n    );\n  }\n  window.gsmPlaceOnly = gsmPlaceOnly; /* v301: the terrain block below reads it too */\n',
)
rep(
    '/* ---- Pattern Synthesis terrain (layer: the ground ahead) ---- */\n!(function () {\n',
    '/* ---- Pattern Synthesis terrain (layer: the ground ahead) ---- */\n!(function () {\n  /* v301: a place-only workbook, from the main block (a ReferenceError here was swallowed and blanked the bare landscape) */\n  var gsmPlaceOnly = function () {\n    return !!(window.gsmPlaceOnly && window.gsmPlaceOnly());\n  };\n',
)

open(P, "w", encoding="utf-8").write(s)
print("ok")
