"""v174: Taking Action cards get their 3D back (v171 removed a part the card code reads); two references corrected by Gregory."""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:80]); s = s.replace(a, b)
rep('''      if (data && data.card) {
        how.remove();
        return;
      }''', '''      if (data && data.card) {
        how.style.display = "none";
        return;
      }''')
rep("<i>Context changes everything: How constraints create change.</i>", "<i>Context changes everything: How constraints create coherence.</i>")
rep("<i>The emerging science at the edge of order and chaos.</i> New York, NY: Touchstone.", "<i>Complexity: The emerging science at the edge of order and chaos.</i> New York, NY: Touchstone.")
rep("<i>The emerging science at the edge of order and chaos</i>. New York, NY: Touchstone.", "<i>Complexity: The emerging science at the edge of order and chaos</i>. New York, NY: Touchstone.")
rep('t && (t.textContent = "v173");', 't && (t.textContent = "v174");')
open(P, "w").write(s); print("v174 ok")
