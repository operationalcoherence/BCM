"""v240: direction arrows on the ways (his ask 11-19 10:26: "the hoses are great, but I think they need directional
arrows so you know which way to go, even when it isn't muddled like this").
The 3D part is in tools/relief/relief.js (edited directly): along each way on a card, arrowheads every ~42 units
(2 to 14 a way), pointing the way it runs (present to goal), skipping the letter badge. Each arrowhead is in the
way's own color with a contrasting outline (white around A and C, dark around B), and dims with its way.
Ways exist only on Taking Action cards, so no other view changes. This script only bumps the label.
Usage: python3 v240_way_arrows.py gsm-readable.js"""
import sys
P = sys.argv[1]
s = open(P).read()
a, b = 't.textContent = "v239"', 't.textContent = "v240"'
assert s.count(a) == 1; s = s.replace(a, b)
open(P, 'w').write(s)
print("v240 applied")
