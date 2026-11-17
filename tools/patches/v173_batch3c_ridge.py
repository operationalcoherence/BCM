"""v173 batch 3c: B3, the indifference ridge stands proud all along its notes, even where they sit in another emotion's ground."""
import sys
P = sys.argv[1]
s = open(P).read()
a = "              hgt = crest - st * Math.max(0, dm - flat * rs);"
assert s.count(a) == 1
s = s.replace(a, "              hgt = Math.max(\n                crest - st * Math.max(0, dm - flat * rs),\n                hs[qb] + PROM * 0.9 * Math.max(0, 1 - dm / (0.45 * sigma)),\n              );")
open(P, "w").write(s)
print("batch3c ok")
