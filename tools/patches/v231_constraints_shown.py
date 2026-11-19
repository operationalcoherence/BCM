"""v231: the constraint boxes on Taking Action show again (his 11-18 22:29 report).
v228 folded every empty constraint box into a "Name what holds it" link, which hid the field and the grayed
Q.4 / Q.6 / Q.7 buttons he approved in v227 ("always show, grayed out until something is written").
This removes that fold: every box shows its field, its one-line help, and its grayed buttons, wherever the box sits.
Usage: python3 v231_constraints_shown.py gsm-readable.js"""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:90]); s = s.replace(a, b)
rep('''    w.querySelectorAll(".ccons").forEach(function (cc) {
      var t = cc.querySelector("textarea");
      if (!t || t.value.trim() || cc.querySelector(".tanb")) return;
      cc.classList.add("cempty");
      var q = cc.querySelector(".cq"),
        b = document.createElement("button");
      b.type = "button";
      b.className = "lnk sm tanb";
      b.textContent = "Name what holds it";
      q ? q.parentNode.insertBefore(b, q.nextSibling) : cc.insertBefore(b, cc.firstChild);
    });
''', '')
rep('t && (t.textContent = "v230");', 't && (t.textContent = "v231");')
open(P, "w").write(s)
print("ok")
