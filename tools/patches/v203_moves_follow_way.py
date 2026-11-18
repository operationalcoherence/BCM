"""v203: FIRST MOVES follows the selected way (review plan, Phase 1 step 5; P3; review 6c; decision E9).
Choosing a way on a card's map (its button, its row, or on the 3D) adds a line under FIRST MOVES (or THE SEQUENCE):
where that way starts, the indifference it passes, and whether it meets what resists the goal or goes around it.
"All ways" takes the line away. So the words follow the way that is drawn.
E9 said way A would follow FIRST MOVES instead. Tried both ways of doing that (start where FIRST MOVES starts, then
left to right; or a nearest-note order that avoids crossing the line): both made ways far longer (6.2x to 38.2x a
straight run on the 200-note workbook), and the first didn't reduce crossings. So the drawing is unchanged and the
words follow it. Way A's left-to-right zigzag is still there.
Usage: python3 v203_moves_follow_way.py gsm-readable.js"""
import sys

P = sys.argv[1]
s = open(P).read()


def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, (c, a[:90])
    s = s.replace(a, b)


# 2. FIRST MOVES follows the selected way
rep(
    "    function render(st) {\n      if (host._rel) {",
    """    var FMK;
    function wayMoves(k) {
      if (k === FMK) return;
      FMK = k;
      var card = host.closest && host.closest(".coa");
      if (!card) return;
      var sec = [].slice.call(card.querySelectorAll(".csec")).filter(function (c) {
        var l = c.querySelector(".csl");
        return l && /^(FIRST MOVES|THE SEQUENCE)$/.test(l.textContent.trim());
      })[0];
      if (!sec) return;
      var old = sec.querySelector(".fmway");
      old && old.parentNode.removeChild(old);
      var R = k
        ? ROUTES.filter(function (r) {
            return r.key === k;
          })[0]
        : null;
      if (!R || !R.st) return;
      var st = R.st,
        N = function (a) {
          return list(
            a.slice(0, 3).map(function (q) {
              return "N" + q;
            }),
          );
        },
        t = [];
      t.push((st.acc || []).length ? "it runs through acceptance at " + N(st.acc) : "it passes no acceptance");
      (st.ind || []).length && t.push("through the indifference at " + N(st.ind) + " (win it over before it tips the other way)");
      (st.hard || []).length
        ? t.push("and meets what resists the goal at " + N(st.hard) + " (bring something to do, not an argument)")
        : t.push("and goes around what resists the goal, which stays as it is");
      var d = document.createElement("div");
      d.className = "fmway";
      d.style.borderLeftColor = "B" === R.key ? "#111" : (RCOL && RCOL[R.key]) || "#111";
      d.innerHTML = "<b>Following way " + R.key + ":</b> " + t.join(", ") + ".";
      sec.appendChild(d);
    }
    function render(st) {
      CARDH && wayMoves(ROUTESEL);
      if (host._rel) {""",
)
rep(
    "#gsm .coacall .gsmmode{",
    "#gsm .fmway{font-size:13.5px;line-height:1.45;margin:8px 0 2px;padding:6px 8px;border-left:3px solid #111;background:#f6f5f1}#gsm .coacall .gsmmode{",
)

s = s.replace('t.textContent = "v202"', 't.textContent = "v203"')
assert 't.textContent = "v203"' in s
open(P, "w").write(s)
