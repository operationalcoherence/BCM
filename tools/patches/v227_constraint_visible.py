"""v227: the constraint loop made visible (his 11-18 21:31 yes).
1. The Q.4 / Q.6 / Q.7 buttons under each constraint field always show; grayed out until something is written.
2. A note on Mapping Landscape (line map and place map) shows the constraint named for it on Taking Action, and
   which answer it was added to; it updates as the constraint is typed.
Usage: python3 v227_constraint_visible.py gsm-readable.js"""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:90]); s = s.replace(a, b)

rep('''      '"' +
      (v ? "" : ' style="display:none"') +
      ">Add it to " +''', '''      '"' +
      ">" +
      (v ? "Add it to " : "Once written, add it to ") +''')
rep('''            '" data-cq="' +
            b[0] +''', '''            '"' +
            (v ? "" : " disabled") +
            ' data-cq="' +
            b[0] +''')
rep('''#gsm .consq .ech{font-size:12.5px;margin:3px 4px 0 0}''', '''#gsm .consq .ech{font-size:12.5px;margin:3px 4px 0 0}#gsm .consq .ech[disabled]{opacity:.4;cursor:default}#gsm .ncons{font-size:13.5px;color:#333;line-height:1.45}#gsm .ncons:not(:empty){margin:6px 0 2px;padding:4px 0 4px 9px;border-left:3px solid #111}#gsm .ncons b{font-size:11px;letter-spacing:.12em;color:#555}''')
# the note shows its constraint
rep('''                b(t) +
                "</div></div>"''', '''                b(t) +
                gsmNoteCons(t) +
                "</div></div>"''')
rep('''            b(t) +
            "</div></div>"''', '''            b(t) +
            gsmNoteCons(t) +
            "</div></div>"''')
rep('''  function gsmConsQ(key, v) {''', '''  function gsmNoteConsIn(id) {
    var x = String((C.asks || {})["cons|" + id] || "").trim();
    if (!x) return "";
    var inq = [3, 5, 6]
      .filter(function (i) {
        return String(C.a[i] || "").indexOf(x) >= 0;
      })
      .map(function (i) {
        return "Q." + (i + 1);
      });
    return (
      "<b>WHAT HOLDS IT, AS YOU NAMED IT ON TAKING ACTION</b><div>\\u201c" +
      Gt(x) +
      "\\u201d " +
      (inq.length ? "(in " + inq.join(", ") + ")" : "(not yet in Q.4, Q.6, or Q.7)") +
      "</div>"
    );
  }
  function gsmNoteCons(t) {
    return t && t[8] ? '<div class="ncons" data-ncid="' + Gt(String(t[8])) + '">' + gsmNoteConsIn(String(t[8])) + "</div>" : "";
  }
  function gsmConsQ(key, v) {''')
rep('''    document.querySelectorAll(".consq[data-cqfor]").forEach(function (q) {
      q.getAttribute("data-cqfor") === id && (q.outerHTML = gsmConsQ(id, t.value));
    });''', '''    document.querySelectorAll(".consq[data-cqfor]").forEach(function (q) {
      q.getAttribute("data-cqfor") === id && (q.outerHTML = gsmConsQ(id, t.value));
    });
    document.querySelectorAll(".ncons[data-ncid]").forEach(function (q) {
      q.getAttribute("data-ncid") === id && (q.innerHTML = gsmNoteConsIn(id));
    });''')
# after a one-tap add, the notes update too
rep('''      qa.classList.add("has");
    }
    P();''', '''      qa.classList.add("has");
    }
    document.querySelectorAll(".ncons[data-ncid]").forEach(function (q) {
      q.getAttribute("data-ncid") === id && (q.innerHTML = gsmNoteConsIn(id));
    });
    P();''')
rep('''t.textContent = "v226"''', '''t.textContent = "v227"''')
open(P, "w").write(s)
print("ok")
