"""v215: his call (11-18, 14:30): "I don't want the grid anywhere near this project," and In Parallel is the
two-pictures figure.
1. In Parallel opens with THE TWO PICTURES, SIDE BY SIDE (the figure with lines, v214). It is no longer placed at the
   end of Pattern Synthesis; "See the two pictures together" there leads to it.
2. The action grid (Actions by ease and reach; Act Here / Act Anywhere) is gone: removed from In Parallel and its
   drawing code deleted. (gsmDerive still computes each note's ease for MOVES, IN ORDER; nothing is drawn from it.)
3. MOVES, IN ORDER on Taking Action no longer speaks of reach or the grid: it starts with the notes the way passes
   that are easy to take (the emotion they sit in, and their side of the line), else with the acceptance the way
   passes. "(the action grid on In Parallel)" and "acts in one place" are gone.
4. Tapping a word still draws its lines on the Pattern Synthesis 3D; "See it on the Pattern Synthesis 3D map" goes
   there. In Parallel's own old 3D stays folded under THE EARLIER 3D VIEW.
Usage: python3 v215_in_parallel_figure.py gsm-readable.js   (no relief change; --relief is a no-op)"""
import sys
P = sys.argv[1]
if "--relief" in sys.argv:
    sys.exit(0)
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:90]); s = s.replace(a, b)
# 2 + 1: no grid; a slot for the figure at the top of In Parallel
rep("""? gsmGrid() + '<details class="fold parold" style="margin:14px 0 18px"><summary>THE EARLIER 3D VIEW</summary><div class="intsub" style="margin:4px 0 8px">The two pictures now meet at the end of Pattern Synthesis, in THE TWO PICTURES, SIDE BY SIDE. This earlier view is kept here. Both pictures on one map.""",
    """? '<div class="agslot"></div><details class="fold parold" style="margin:14px 0 18px"><summary>THE EARLIER 3D VIEW</summary><div class="intsub" style="margin:4px 0 8px">Both pictures on one map.""")
rep("""                      if (AG) {
                        var AH = document.createElement("div");
                        AH.className = "plab";
                        AH.textContent = "THE TWO PICTURES, SIDE BY SIDE";
                        Rt.insertBefore(AH, ct);
                        Rt.insertBefore(AG, ct);
                      }""",
    """                      var SL = lt.querySelector(".agslot");
                      AG && SL && SL.appendChild(AG);""")
# 4: the 3D lines are on Pattern Synthesis
rep("""Tap a word to follow it here and on the 3D map above.""",
    """Tap a word to follow it here and on the Pattern Synthesis 3D map.""")
rep("""        bt.textContent = "See it on the 3D map ↑";""",
    """        bt.textContent = "See it on the Pattern Synthesis 3D map";""")
rep("""          window.gsmSynHost && window.gsmSynHost.scrollIntoView({ behavior: "smooth", block: "center" });""",
    """          window.gsmTab && window.gsmTab(3);
          setTimeout(function () {
            window.gsmSynHost && window.gsmSynHost.scrollIntoView({ behavior: "smooth", block: "center" });
          }, 300);""")
# 3: MOVES, IN ORDER without the grid
rep("""                  (ea.length
                    ? (start.length > 1 ? ": easy to take, and their words reach" : ": easy to take, and its words reach") + " across the workbook (the action grid on In Parallel)."
                    : eh.length
                      ? (start.length > 1 ? ": easy to take, though they act in one place; begin there." : ": easy to take, though it acts in one place; begin there.")
                      : ", on the ground way " + easy.key + " passes, where acceptance already is.") +""",
    """                  (ea.length || eh.length
                    ? (start.length > 1 ? ": easy to take, on ground that already holds; begin there." : ": easy to take, on ground that already holds; begin there.")
                    : ", on the ground way " + easy.key + " passes, where acceptance already is.") +""")
rep("""              start = ea.length ? ea : eh.length ? eh : easy.st.acc.slice(0, 2).map(function (k) {""",
    """              start = ea.length || eh.length ? ea.concat(eh) : easy.st.acc.slice(0, 2).map(function (k) {""")
# 2: the grid's drawing code is removed, not only uncalled
i = s.index("                  function gsmGrid() {")
j = s.index("{", i); d = 0; k = j
while True:
    ch = s[k]
    if ch == "{": d += 1
    elif ch == "}":
        d -= 1
        if d == 0: break
    k += 1
assert "Act Anywhere" in s[i:k] and s.count("function gsmGrid()") == 1
s = s[:i] + "                  /* v215: the action grid is gone (his call, 11-18) */" + s[k + 1:]
# lines wait for the Synthesis 3D if it has not mounted yet
rep("""      if (window.gsmSynRel && window.gsmSynRel.hoses && o.ns.length > 1) {
        window.gsmSynRel.hoses({ pts: chain(o.ns), ask: !o.ok });""",
    """      window.gsmSynPend = o.ns.length > 1 ? { pts: chain(o.ns), ask: !o.ok } : null;
      if (o.ns.length > 1) {
        window.gsmSynRel && window.gsmSynRel.hoses && window.gsmSynRel.hoses(window.gsmSynPend);""")
rep("""        window.gsmSynRel && window.gsmSynRel.hoses && window.gsmSynRel.hoses(null);
        return;""",
    """        window.gsmSynPend = null;
        window.gsmSynRel && window.gsmSynRel.hoses && window.gsmSynRel.hoses(null);
        return;""")
rep("""                window.gsmSynRel = host._rel;
                window.gsmSynHost = host;""",
    """                window.gsmSynRel = host._rel;
                window.gsmSynHost = host;
                window.gsmSynPend && host._rel.hoses && host._rel.hoses(window.gsmSynPend);""")
s = s.replace('t.textContent = "v214"', 't.textContent = "v215"'); assert 't.textContent = "v215"' in s
open(P, "w").write(s)
