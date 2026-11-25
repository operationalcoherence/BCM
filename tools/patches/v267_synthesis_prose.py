# v267: the Pattern Synthesis blocks rewritten as prose (his note 11-24 21:01: "the writing is really dry").
# The change is in tools/graph/page.js; this script only bumps the label.
p = "gsm-readable.js"; s = open(p, encoding="utf-8").read()
assert s.count('t.textContent = "v266"') == 1
s = s.replace('t.textContent = "v266"', 't.textContent = "v267"'); open(p, "w", encoding="utf-8").write(s)
