"""v216: In Parallel cut to the figure (review 5c-5e; his note 11-18 14:52: "The In Parallel page is very wrong still").
Under THE TWO PICTURES, SIDE BY SIDE the tab now reads, in order:
1. Where to start (one line).
2. MORE FROM BOTH PICTURES, a closed fold: Read together, Closest and farthest from the goal, Emotion, Voices,
   Patterns worth a second look, What might relate to what. Nothing is deleted; it is out of the way.
3. THE EARLIER 3D VIEW (closed), now last.
"Where both pictures agree" and "Where they differ" are removed when the figure is shown: the figure says the same
thing word by word (tap a word), including "wildfire risk", the word 5c asked to explain. Where the figure cannot be
drawn (place maps), they stay as before.
Usage: python3 v216_in_parallel_cut.py gsm-readable.js   (no relief change; --relief is a no-op)"""
import sys
P = sys.argv[1]
if "--relief" in sys.argv:
    sys.exit(0)
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:90]); s = s.replace(a, b)
rep("""                      E.map(function (t) {
                        return (
                          '<div class="intl"><b>' +""",
    """                      gsmIntOrder(E, function (t) {
                        return (
                          '<div class="intl"><b>' +""")
rep("""                          "</div>"
                        );
                      }).join("") +
                      '<div class="pby">The Bear Canyon Method delivers""",
    """                          "</div>"
                        );
                      }) +
                      '<div class="pby">The Bear Canyon Method delivers""")
rep("""                      var SL = lt.querySelector(".agslot");
                      AG && SL && SL.appendChild(AG);""",
    """                      var SL = lt.querySelector(".agslot"),
                        PO = lt.querySelector("details.parold"),
                        PB = lt.querySelector(".pby");
                      if (AG && SL) {
                        SL.appendChild(AG);
                        lt.querySelectorAll("[data-dup]").forEach(function (x) {
                          x.parentNode.removeChild(x);
                        });
                      }
                      PO && PB && lt.insertBefore(PO, PB);""")
rep("""  // v213: THE TWO PICTURES, SIDE BY SIDE (closes Pattern Synthesis)""",
    """  // v216: In Parallel under the figure: where to start, then the rest folded away
  function gsmIntOrder(E, f) {
    var top = [],
      dup = [],
      rest = [];
    E.forEach(function (t) {
      "Where to start" === t[0]
        ? top.push(f(t))
        : "Where both pictures agree" === t[0] || "Where they differ" === t[0]
          ? dup.push(f(t).replace('<div class="intl">', '<div class="intl" data-dup="1">'))
          : rest.push(f(t));
    });
    return (
      top.join("") +
      dup.join("") +
      (rest.length
        ? '<details class="fold parmore" style="margin:14px 0"><summary>MORE FROM BOTH PICTURES</summary>' + rest.join("") + "</details>"
        : "")
    );
  }
  // v213: THE TWO PICTURES, SIDE BY SIDE (closes Pattern Synthesis)""")
s = s.replace('t.textContent = "v215"', 't.textContent = "v216"'); assert 't.textContent = "v216"' in s
open(P, "w").write(s)
