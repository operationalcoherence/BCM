"""v217: the patterns row (v212) shows only on Pattern Synthesis. The map template is shared, so it also appeared
above YOUR LANDSCAPE on Pattern Analysis (and on In Parallel's earlier 3D), where the map draws no patterns and the
buttons did nothing (his note, 11-18 15:07: "none of these links do anything").
Usage: python3 v217_laybar_synthesis_only.py gsm-readable.js   (no relief change; --relief is a no-op)"""
import sys
P = sys.argv[1]
if "--relief" in sys.argv:
    sys.exit(0)
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:90]); s = s.replace(a, b)
rep("""      lb.innerHTML = "";
      if (!terr || !terr.threads.length) return;""",
    """      lb.innerHTML = "";
      if (ANH || PAR || CARDH || !terr || !terr.threads.length) return;""")
s = s.replace('t.textContent = "v216"', 't.textContent = "v217"'); assert 't.textContent = "v217"' in s
open(P, "w").write(s)
