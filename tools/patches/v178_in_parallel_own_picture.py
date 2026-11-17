"""v178: In Parallel gets its own picture (numbered readings + each question's spokes to its notes);
the In Parallel flag is read once (inside data() the name `data` is the function, so data.par was never seen)."""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:80]); s = s.replace(a, b)
rep("      ANH = !!data.an,\n      AQ = 0;", "      ANH = !!data.an,\n      PAR = !!data.par,\n      AQ = 0;")
rep("          if (!data.par) return;", "          if (!PAR) return;")
rep("          t && !data.par && (t.innerHTML = say(q));", "          t && !PAR && (t.innerHTML = say(q));")
rep("      if (data.par) {", "      if (PAR) {")
rep("      data.par || stg0.parentNode.insertBefore(hd, sy);", "      PAR || stg0.parentNode.insertBefore(hd, sy);")
rep("        } else if (ANH && !data.par) {", "        } else if (ANH && !PAR) {")
rep("""        return D;
      }""", """        PAR && (D.spokes = 1);
        return D;
      }""")
rep("One map for both pictures: the buttons show each question’s notes on the ground (Analysis); the ground itself, its heights, colors and ridges, is what the notes say together (Synthesis).",
    "Both pictures on one map. From each question’s flag, thin lines run to its notes: how your thinking spreads across the ground (Analysis). The numbers are what the ground says, read on Pattern Synthesis (Synthesis). Where a question’s lines reach a numbered place, the two pictures meet. Use the buttons to follow one question at a time.")
rep("""      if (PAR) {
        sy.innerHTML = "";
        sy.style.display = "none";
      }""", r"""      if (PAR) {
        sy.innerHTML = (function () {
          var rad = 1.3 * ((terr && terr.sigma) || 18),
            out = [];
          (READ || []).forEach(function (r, i) {
            if (!r.at) return;
            var qs = {};
            (terr.notes || []).forEach(function (n) {
              n.q && Math.hypot(n.x - r.at[0], n.y - r.at[1]) < rad && (qs[n.q] = (qs[n.q] || 0) + 1);
            });
            var qk = Object.keys(qs).map(Number).sort(function (a, b) {
                return a - b;
              }),
              grasp = qk.filter(function (q) {
                return q <= 4;
              }),
              act = qk.filter(function (q) {
                return q >= 5;
              });
            if (qk.length < 2) return;
            var nmq = function (L) {
                var a = L.map(function (q) {
                  return "Q." + q + " (" + RL[q - 1] + ")";
                });
                return a.length > 1 ? a.slice(0, -1).join(", ") + " and " + a[a.length - 1] : a[0];
              },
              low = 1 === r.grp,
              high = 0 === r.grp,
              t = "<b>" + (i + 1) + " · " + String(r.title).replace(/[&<>"]/g, function (c) { return "&#" + c.charCodeAt(0) + ";"; }) + ".</b> Notes from " + nmq(qk) + " gather here. ";
            t +=
              low && act.length && grasp.length
                ? "What you would do sits in the same low ground as " +
                  nmq(grasp) +
                  ": these actions will meet the emotions there before they reach the goal, so start them where they can be seen to work."
                : low && grasp.length
                  ? "Several kinds of problem share one low place. Nothing you would do is placed here yet, so this is where the ground can hold you back unanswered."
                  : high && qs[2]
                    ? "Opposition stands on high ground here, next to what helps: resistance that may be easier to meet than it sounds."
                    : high && act.length
                      ? "What you would do stands on ground that holds: a place to start and be seen."
                      : 2 === r.grp
                        ? "These questions share a crossing: a place where people can move either way."
                        : "Two parts of your thinking land on the same ground, so what changes one will touch the other.";
            var key = qk.join(",") + "|" + r.grp;
            out.some(function (o) {
              return o[2] === key;
            }) || out.push([qk.length + (act.length && grasp.length ? 2 : 0), t, key]);
          });
          out.sort(function (a, b) {
            return b[0] - a[0];
          });
          return out.length
            ? out
                .slice(0, 5)
                .map(function (x) {
                  return '<p style="margin:0 0 8px">' + x[1] + "</p>";
                })
                .join("")
            : "No numbered place on the ground gathers notes from more than one question yet.";
        })();
      }""")
rep("""      PAR || stg0.parentNode.insertBefore(hd, sy);""", """      PAR && (hd.textContent = "WHERE THE TWO PICTURES MEET");
      stg0.parentNode.insertBefore(hd, sy);""")
rep('t && (t.textContent = "v177");', 't && (t.textContent = "v178");')
open(P, "w").write(s); print("v178 ok")
