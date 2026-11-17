"""v177: T1-T3, Taking Action. Each way forward is costed from the ground (effort, impact, benefit, return on effort);
Comparing the ways says why to choose each, why take the harder way, and when to stop and readjust (Morin, 2008);
an expandable chart compares the ways."""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:80]); s = s.replace(a, b)

# --- route stats: climbing energy, and who the way meets
rep("""      var straight = Math.hypot(GOAL.x - START.x, GOAL.y - START.y);
      return {
        L: L,
        ratio: L / straight,
        sunk: sunk / L,
        raised: raised / L,
        pits: Object.keys(pits).map(Number),
        deep: deep,
      };""", """      var straight = Math.hypot(GOAL.x - START.x, GOAL.y - START.y),
        climb = 0,
        rad = 0.8 * ((terr && terr.sigma) || 18),
        met = {};
      for (var i2 = 1; i2 < R.length; i2++) {
        var dh = hAt(R[i2][0], R[i2][1]) - hAt(R[i2 - 1][0], R[i2 - 1][1]);
        dh > 0 && (climb += dh);
      }
      (terr && terr.notes ? terr.notes : []).forEach(function (n) {
        if (null == n.e) return;
        for (var j2 = 0; j2 < R.length; j2 += 2)
          if (Math.hypot(R[j2][0] - n.x, R[j2][1] - n.y) < rad) {
            met[n.k] = n.e;
            return;
          }
      });
      var mk = Object.keys(met),
        hard = mk.filter(function (k) {
          return 0 === met[k] || 2 === met[k] || 4 === met[k];
        }),
        acc = mk.filter(function (k) {
          return 1 === met[k];
        }),
        ind = mk.filter(function (k) {
          return 3 === met[k];
        }),
        emos = {};
      mk.forEach(function (k) {
        emos[met[k]] = 1;
      });
      return {
        L: L,
        ratio: L / straight,
        sunk: sunk / L,
        raised: raised / L,
        pits: Object.keys(pits).map(Number),
        deep: deep,
        climb: climb,
        hard: hard.map(Number),
        acc: acc.map(Number),
        ind: ind.map(Number),
        emoN: Object.keys(emos).length,
        effort: climb + 0.15 * (L / straight),
        impact: hard.length + 0.5 * Object.keys(emos).length,
        benefit: acc.length + 0.5 * ind.length,
      };""")

# --- comparing the ways
OLD_CMP_END = """          out.push({ k: "", title: "Comparing the ways", text: t });
        }
      }
      return out;
    }"""
NEW_CMP_END = r"""          out.push({ k: "", title: "Comparing the ways", text: t });
          var nm = function (a) {
              return list(
                a.slice(0, 4).map(function (k) {
                  return "N" + k;
                }),
              );
            },
            byEff = ROUTES.slice().sort(function (a, b) {
              return a.st.effort - b.st.effort;
            }),
            easy = byEff[0],
            hardW = byEff[byEff.length - 1],
            reach = ROUTES.slice().sort(function (a, b) {
              return b.st.impact - a.st.impact;
            })[0];
          ROUTES.forEach(function (R) {
            var S = R.st,
              why =
                R === reach && R === hardW
                  ? "the harder way. It costs the most energy, but it is the way that meets the most of what resists the goal" +
                    (S.hard.length ? " (" + nm(S.hard) + ")" : "") +
                    ", in " +
                    S.emoN +
                    " different emotions. Choose it when the goal cannot be reached around those people, only with them: it is the way that changes the ground rather than crossing it."
                  : R === easy
                    ? "the way that saves energy. It climbs the least and stays on ground that holds" +
                      (S.acc.length ? ", passing acceptance at " + nm(S.acc) : "") +
                      ". Choose it to build momentum first, small and visible, where people already accept; Vigneaux (2026) puts the start there, and the harder ground after, once something is moving on its own. It leaves the resistance where it is."
                    : R === reach
                      ? "the way that meets the most resistance" +
                        (S.hard.length ? " (" + nm(S.hard) + ")" : "") +
                        " without the steepest climb. Choose it when you need to reach the opposition but have little energy to spend."
                      : "a middle way: more contact than the easiest, less climbing than the hardest. Choose it when you are unsure which matters more.";
            out.push({ k: "", title: R.key + ": why choose it", text: R.key + " is " + why });
          });
          out.push({
            k: "",
            title: "Why take the harder way?",
            text:
              "On paper " +
              easy.key +
              " reaches the goal for less. But a way that goes around the resistance leaves it as it was, and if those people can stop the goal, they still can. " +
              hardW.key +
              " costs more because it goes where the work is: into the emotions that hold the goal back, and among people who see it differently. That contact is how the ground itself changes. A common order is both: " +
              easy.key +
              " first, small, to build momentum, then " +
              hardW.key +
              " once there is something to show.",
          });
          var watch = [];
          ROUTES.forEach(function (R) {
            R.st.ind.forEach(function (k) {
              watch.indexOf("N" + k) < 0 && watch.push("N" + k);
            });
          });
          out.push({
            k: "",
            title: "When to stop and readjust",
            text:
              "As soon as an action is taken it begins to escape your intentions, and the setting can turn it into its opposite (Morin, 2008, p. 55). So follow each way as it goes, and stop to readjust when: people you pass answer with more resistance than you expected" +
              (watch.length ? " (watch " + list(watch.slice(0, 4)) + ": indifference can tip either way)" : "") +
              "; the way stalls in sunk ground" +
              (crossing.length === ROUTES.length ? ", as every way here risks doing" : crossing.length ? " (" + list(crossing.map(function (R) { return R.key; })) + " " + (crossing.length > 1 ? "pass" : "passes") + " a place where it is easy to get stuck)" : "") +
              "; or what you expected to run like a program needs constant attention. Then come back to the map, update the notes, and read the ground again. A strategy is meant to change course; a program is not (Morin, 2008).",
          });
        }
      }
      return out;
    }
    function waysChart(box) {
      if (ROUTES.length < 2) return;
      var M = [
          ["Effort", "effort", "How much climbing the way does: the energy it takes."],
          ["Impact", "impact", "How many notes held in distrust, aggression or defiance it meets, and in how many emotions."],
          ["Benefit", "benefit", "Notes of acceptance it passes, and indifference it can win over."],
          ["Return on effort", "roi", "Impact and benefit for the energy spent."],
        ],
        mx = {};
      ROUTES.forEach(function (R) {
        R.st.roi = (R.st.impact + R.st.benefit) / Math.max(0.05, R.st.effort);
      });
      M.forEach(function (m) {
        mx[m[1]] = Math.max.apply(
          null,
          ROUTES.map(function (R) {
            return R.st[m[1]];
          }).concat([0.0001]),
        );
      });
      var d = document.createElement("details");
      d.className = "gtchart";
      d.style.margin = "8px 0 4px";
      var sm = document.createElement("summary");
      sm.style.cssText = "cursor:pointer;font:12px Questrial,sans-serif;letter-spacing:.08em;text-decoration:underline";
      sm.textContent = "COMPARE THE WAYS IN A CHART";
      d.appendChild(sm);
      M.forEach(function (m) {
        var g = document.createElement("div");
        g.style.margin = "8px 0 2px";
        var h = document.createElement("div");
        h.style.cssText = "font-size:12.5px;color:#222";
        h.innerHTML = "<b>" + m[0] + "</b> <span style=\"color:#777\">" + m[2] + "</span>";
        g.appendChild(h);
        ROUTES.forEach(function (R) {
          var v = R.st[m[1]] / mx[m[1]],
            row = document.createElement("div");
          row.style.cssText = "display:flex;align-items:center;gap:8px;margin:3px 0";
          row.setAttribute("data-way", R.key);
          var k = document.createElement("span");
          k.textContent = R.key;
          k.style.cssText =
            "flex:0 0 20px;height:20px;line-height:16px;text-align:center;border-radius:50%;font:bold 11px Helvetica,Arial,sans-serif;border:2px solid " +
            (R.key === "B" ? "#111" : "#fff") +
            ";background:" +
            (RCOL[R.key] || "#111") +
            ";color:" +
            (R.key === "B" ? "#111" : "#fff");
          var tr = document.createElement("div");
          tr.style.cssText = "flex:1;height:12px;background:#f1f0ea;position:relative";
          var bar = document.createElement("div");
          bar.style.cssText =
            "position:absolute;left:0;top:0;bottom:0;width:" +
            Math.max(2, Math.round(v * 100)) +
            "%;background:" +
            (R.key === "B" ? "#fff" : RCOL[R.key] || "#111") +
            (R.key === "B" ? ";box-shadow:inset 0 0 0 1.5px #111" : "");
          tr.appendChild(bar);
          var lab = document.createElement("span");
          lab.style.cssText = "flex:0 0 42px;font-size:11.5px;color:#555;text-align:right";
          lab.textContent = Math.round(v * 100) + "%";
          row.appendChild(k);
          row.appendChild(tr);
          row.appendChild(lab);
          g.appendChild(row);
        });
        d.appendChild(g);
      });
      var nt = document.createElement("div");
      nt.className = "small";
      nt.style.marginTop = "6px";
      nt.textContent =
        "Each bar is relative to the largest of the ways on this card, read from the ground on your own map, not a standard measure. Patterns suggests; you decide.";
      d.appendChild(nt);
      box.appendChild(d);
    }"""
rep(OLD_CMP_END, NEW_CMP_END)
# chart after the readings, before the footnote
rep("""      var f = document.createElement("div");
      f.className = "small";
      f.style.marginTop = "4px";
      f.textContent =
        "The card itself is on Taking Action. " +""", """      cd.mode === "STRATEGY" && waysChart(box);
      var f = document.createElement("div");
      f.className = "small";
      f.style.marginTop = "4px";
      f.textContent =
        "The card itself is on Taking Action. " +""")
# Taking Action sources: Morin already listed; nothing else needed. Version.
rep('t && (t.textContent = "v176");', 't && (t.textContent = "v177");')
open(P, "w").write(s); print("v177 ok")
