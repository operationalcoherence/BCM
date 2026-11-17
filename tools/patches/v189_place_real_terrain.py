"""v189: on a place map the ground is the real terrain, true to scale. The engine waits for the relief module to
fetch elevation (gsmRelief.prep) before it builds the 3D scene; emotion shows only as color on a place."""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:80]); s = s.replace(a, b)
rep("""      function go() {
        relLoad()
          .then(function () {
            if (!host.isConnected || host._rel) return;""", """      function go() {
        relLoad()
          .then(function () {
            return PLACE && window.gsmRelief && window.gsmRelief.prep ? window.gsmRelief.prep(PLACE) : null;
          })
          .then(function () {
            if (!host.isConnected || host._rel) return;""")
rep('t.textContent = "v188"', 't.textContent = "v189"')
open(P, "w").write(s)
