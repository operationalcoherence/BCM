"""v224: YOUR STORY SO FAR panel on Pattern Analysis gets a white background (his 11-18 19:21 note).
Usage: python3 v224_story_white.py gsm-readable.js"""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:90]); s = s.replace(a, b)
rep('#gsm .storylead>details.fold{border:2px solid #111;background:#faf8f3;', '#gsm .storylead>details.fold{border:2px solid #111;background:#fff;')
rep('t && (t.textContent = "v223");', 't && (t.textContent = "v224");')
open(P, "w").write(s)
print("ok")
