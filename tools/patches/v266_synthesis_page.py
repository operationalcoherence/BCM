# v266: the simple Pattern Synthesis page (his call, 11-24: "build only the relationship graph, shape detection,
# and a simple page using those outputs"; then 20:43: "then, build the simple page").
# Two blocks at the top of the Pattern Synthesis tab, from tools/graph/graph.js, shapes.js and page.js:
# WHAT CHANGED WHAT (the strongest relationship) and WHAT KEEPS ITSELF GOING / WHAT HOLDS IT IN PLACE /
# WHERE IT IS HEADING (the strongest shape). No question block: the question engine waits.
# Everything already on the tab stays, under the new blocks.
# The three modules are bundled ahead of the engine at build time (see README):
#   cat tools/graph/graph.js tools/graph/shapes.js tools/graph/page.js gsm-readable.js | npx esbuild@0.24 --minify > gsm-preview.js
p = "gsm-readable.js"; s = open(p, encoding="utf-8").read()
# 1. the engine hands its own stopwords and -ly exceptions to the graph, so both read words the same way
old = "  };\n  function Nt(t) {\n    var e = t;"
assert s.count(old) == 1
s = s.replace(old, "  };\n  try { window.gsmLexicon = { stop: Ot, ly: At }; } catch (e) {}\n  function Nt(t) {\n    var e = t;", 1)
# 2. the page goes in right after Synthesis renders, before note numbers become links
old = "(Rt.innerHTML = Ot),"
assert s.count(old) == 1
s = s.replace(old, old + "\n          (function () { try { window.gsmPSPage && window.gsmPSPage(Rt, C); } catch (e) {} })(),", 1)
assert s.count('t.textContent = "v265"') == 1
s = s.replace('t.textContent = "v265"', 't.textContent = "v266"')
open(p, "w", encoding="utf-8").write(s)
