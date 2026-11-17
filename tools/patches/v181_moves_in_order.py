"""v181: T6, Synthesis -> Action handoff. Each strategy card with two or more ways gets MOVES, IN ORDER,
built from the ways' ground (easy way, indifference crossings, the harder way's resistance) and the action grid."""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:80]); s = s.replace(a, b)
# expose the grid's points for Taking Action
rep("""                    pts.forEach(function (p) {
                      p.any = p.reach / mr;
                    });""", """                    pts.forEach(function (p) {
                      p.any = p.reach / mr;
                    });
                    window.gsmGridPts = pts;""")
rep("""          out.push({
            k: "",
            title: "When to stop and readjust",""", r"""          (function () {
            var G = window.gsmGridPts || [],
              ids = (cd.ids || []).map(function (x) {
                return String(x).replace(/^(?:note\s*)/i, "N");
              }),
              mine = G.filter(function (p) {
                return ids.indexOf(p.id) >= 0;
              }),
              pick = function (f) {
                return mine.filter(f).map(function (p) {
                  return p.id;
                });
              },
              ea = pick(function (p) {
                return p.d < 0.5 && p.any >= 0.5;
              }),
              eh = pick(function (p) {
                return p.d < 0.5 && p.any < 0.5;
              }),
              hd = pick(function (p) {
                return p.d >= 0.5;
              }),
              mv = [],
              start = ea.length ? ea : eh.length ? eh : easy.st.acc.slice(0, 2).map(function (k) {
                return "N" + k;
              }),
              cross = [];
            ROUTES.forEach(function (R) {
              R.st.ind.forEach(function (k) {
                cross.indexOf("N" + k) < 0 && cross.push("N" + k);
              });
            });
            start.length &&
              mv.push(
                "Start with " +
                  list(start.slice(0, 3)) +
                  (ea.length
                    ? (start.length > 1 ? ": easy to take, and their words reach" : ": easy to take, and its words reach") + " across the workbook (the action grid on In Parallel)."
                    : eh.length
                      ? (start.length > 1 ? ": easy to take, though they act in one place; begin there." : ": easy to take, though it acts in one place; begin there.")
                      : ", on the ground way " + easy.key + " passes, where acceptance already is.") +
                  (start.length > 1 ? " Keep them small and visible." : " Keep it small and visible."),
              );
            cross.length &&
              mv.push(
                "Next, work with " +
                  list(cross.slice(0, 3)) +
                  ": indifference, where most moves between emotions cross. Win it over before it tips the other way.",
              );
            hardW.st.hard.length &&
              mv.push(
                "Then take way " +
                  hardW.key +
                  " to " +
                  list(
                    hardW.st.hard.slice(0, 3).map(function (k) {
                      return "N" + k;
                    }),
                  ) +
                  ", behaviors first: bring something to do that fits what people there already value, not an argument." +
                  (hd.length ? " " + list(hd.slice(0, 2)) + " belong" + (hd.length > 1 ? "" : "s") + " here: difficult actions, taken last." : ""),
              );
            mv.push("After each move, update the notes you passed and read the ground again before the next.");
            out.push({
              k: "",
              title: "Moves, in order",
              text: mv
                .map(function (t, i) {
                  return i + 1 + ". " + t;
                })
                .join(" "),
            });
          })();
          out.push({
            k: "",
            title: "When to stop and readjust",""")
rep('t && (t.textContent = "v180");', 't && (t.textContent = "v181");')
open(P, "w").write(s); print("v181 ok")
