"""v185: Taking Action's legends go back to how they were before v184 (inside each card's map, programs too);
the legend drawer of full-screen Pattern Synthesis now opens when a strategy card goes full screen (in gsm-relief.js)."""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:80]); s = s.replace(a, b)

rep("""            stg.style.display = "none";
            /* legend: kept outside the 3D box on strategy cards, so it stays while the map is parked; none on programs */
            (function () {
              var lg = box.querySelector(".grleg");
              if (!lg || !CARDH) return;
              var cm = CARDS && null != COURSE && CARDS[COURSE] ? CARDS[COURSE].mode : "";
              lg.style.display = "none";
              if ("PROGRAM" === cm) return;
              host._legKeep && host._legKeep.remove();
              host._legKeep = lg.cloneNode(!0);
              host._legKeep.style.display = "";
              box.parentNode.insertBefore(host._legKeep, box.nextSibling);
            })();
""", """            stg.style.display = "none";
""")
rep('t.textContent = "v184"', 't.textContent = "v185"')
open(P, "w").write(s)
