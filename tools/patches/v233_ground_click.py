"""v233: plan item 3c, the "no questions" click on YOUR LANDSCAPE (Pattern Analysis).
With All notes shown, a tap on the ground says what gathers there: how many notes, from which questions,
the emotion that holds the ground and what kind of ground it is, whether distant emotions meet with no
ridge between them, and whether what you would design stands on the same ground as the context you have
grasped. It works in the 3D relief (raycast onto the ground) and the flat fallback (nearest grid point).
With a question selected, a tap does what it did before. For every workbook; nothing is tied to his.
Usage: python3 v233_ground_click.py gsm-readable.js tools/relief/relief.js"""
import sys
P, R = sys.argv[1], sys.argv[2]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:90]); s = s.replace(a, b)

# --- the reading, built inside the Analysis block where RL and EN live
rep('''    if (ANH) {
      host.classList.add("gtan");''', '''    var ANGROUND = null, GPIN = null;
    if (ANH) {
      host.classList.add("gtan");''')
rep('''        return t + " Tap a question above the map to see only its notes.";
      }''', '''        return t + " Tap a question above the map to see only its notes. With all notes shown, tap the ground to read what gathers there.";
      }
      /* v233: what gathers at a spot on the ground (plan item 3c) */
      ANGROUND = function (x, y) {
        var ns = (terr && terr.notes) || [],
          sg = (terr && terr.sigma) || 18,
          rad = 2.2 * sg,
          near = ns
            .map(function (n) {
              return { n: n, d: Math.hypot(n.x - x, n.y - y) };
            })
            .filter(function (o) {
              return o.d < rad;
            })
            .sort(function (a, b) {
              return a.d - b.d;
            }),
          and = function (a) {
            return a.length > 1 ? a.slice(0, -1).join(", ") + (a.length > 2 ? ", and " : " and ") + a[a.length - 1] : a[0] || "";
          },
          where =
            (y < 118 ? "on the help side" : "on the hinder side") +
            " " +
            (x < 120 ? "near the present" : x > 230 ? "near the goal" : "midway to the goal");
        if (!near.length)
          return { head: "WHAT GATHERS HERE", body: "No notes sit near this spot, " + where + ", so the ground here carries no information yet." };
        var c = [0, 0, 0, 0, 0],
          cw = [0, 0, 0, 0, 0],
          qs = {},
          n = 0,
          top = 0,
          GR = ["lower ground", "the highest ground", "low ground", "the ridge", "the lowest ground"];
        near.forEach(function (o) {
          null != o.n.e && (c[o.n.e]++, n++, (cw[o.n.e] += Math.exp(-(o.d * o.d) / (2 * sg * sg))));
          qs[o.n.q] = (qs[o.n.q] || 0) + 1;
        });
        /* the emotion that colors the spot: weighted by distance, as the ground's own color is */
        cw.forEach(function (v, k) {
          v > cw[top] && (top = k);
        });
        var W0 = cw[0] + cw[1] + cw[2] + cw[3] + cw[4],
          on = function (k) {
            return cw[k] > 0.2 * cw[top];
          };
        var qk = Object.keys(qs)
            .map(Number)
            .sort(function (a, b) {
              return a - b;
            }),
          grasp = qk.filter(function (q) {
            return q <= 4;
          }),
          act = qk.filter(function (q) {
            return q >= 5;
          }),
          tie = cw.filter(function (v) {
            return n && v >= 0.85 * cw[top];
          }).length > 1,
          hard = n && (tie ? cw[0] + cw[2] + cw[4] >= cw[1] + cw[3] : 1 !== top && 3 !== top),
          t =
            near.length +
            (1 === near.length ? " note shapes the ground here, " : " notes shape the ground here, ") +
            where +
            (near[0].d > 1.3 * sg ? ", though none sits right on this spot" : "") +
            ": " +
            and(
              qk.map(function (q) {
                return "Q." + q + " (" + RL[q - 1] + ")";
              }),
            ) +
            ".";
        n && tie
          ? (t +=
              " " +
              and(
                [1, 3, 2, 0, 4]
                  .filter(function (k) {
                    return cw[k] >= 0.85 * cw[top];
                  })
                  .map(function (k) {
                    return EN[k];
                  }),
              ).replace(/^./, function (m) {
                return m.toUpperCase();
              }) +
              " hold this ground in nearly equal measure.")
          : n &&
          (t +=
            " " +
            (1 === n ? "It carries " : c[top] === n ? "All of them carry " : cw[top] > 0.6 * W0 ? "Mostly " : "More ") +
            EN[top] +
            (1 === n || c[top] === n ? "" : cw[top] > 0.6 * W0 ? " colors it" : " than anything else colors it") +
            ", so this is " +
            GR[top] +
            ".");
        var far = [0, 4, 2].filter(on);
        on(1) && far.length && !on(3)
          ? (t +=
              " Acceptance meets " +
              and(
                far.map(function (k) {
                  return EN[k];
                }),
              ) +
              " here with no indifference between them, so getting across is a climb.")
          : on(3) && 3 !== top && !(tie && cw[3] >= 0.85 * cw[top]) && (t += " The indifference here is a ridge, where most moves between emotions cross.");
        act.length && grasp.length
          ? (t += hard
              ? " What you would design sits in the same ground as the context you have grasped, so it meets these emotions first."
              : 3 === top && !tie
                ? " What you would design stands on the ridge with the context you have grasped, where people can still tip either way."
                : " What you would design stands on the same ground as the context you have grasped: a place where it can be seen to work.")
          : grasp.length
            ? (t += hard
                ? " Nothing you would design is placed here yet, so what holds here is unresolved."
                : 1 === top
                  ? " Nothing you would design is placed here yet, so nothing yet uses this high ground."
                  : " Nothing you would design is placed here yet, and people here can still tip either way.")
            : (t += " Only what you would design sits here. No note of the context you have grasped is placed nearby to test it against.");
        var sm =
          near
            .slice(0, 4)
            .map(function (o) {
              var tx = String(o.n.t).replace(/\\s+/g, " ").trim();
              tx.length > 70 && (tx = tx.slice(0, 70).replace(/\\s+\\S*$/, "") + "\\u2026");
              return "N" + o.n.k + (null != o.n.e ? " (" + EN[o.n.e] + ")" : "") + ": " + tx;
            })
            .join(" \\u00b7 ") + (near.length > 4 ? " \\u00b7 and " + (near.length - 4) + " more" : "");
        return { head: "WHAT GATHERS HERE", body: t, sm: sm, long: 1 };
      };''')

# --- flat fallback: a tap on empty ground, with All notes shown, finds the nearest grid point
rep('''      SEL = id && id !== SEL ? id : null;
      SELTH = null;''', '''      GPIN = null;
      if (!id && ANH && !PAR && !AQ && ANGROUND && SXA) {
        var gk = -1,
          gd = 1e9;
        for (var gq = 0; gq < SXA.length; gq++) {
          var dd = Math.hypot(SXA[gq] - x, SYA[gq] - y);
          dd < gd && ((gd = dd), (gk = gq));
        }
        if (gk >= 0 && gd < 40) {
          var gi = ANGROUND((gk % VX) * CX, Math.floor(gk / VX) * CY);
          tip.innerHTML = "";
          var gb = document.createElement("b");
          gb.textContent = gi.head;
          tip.appendChild(gb);
          tip.appendChild(document.createTextNode(gi.body));
          if (gi.sm) {
            var gs = document.createElement("div");
            gs.className = "small";
            gs.style.marginTop = "4px";
            gs.textContent = gi.sm;
            tip.appendChild(gs);
          }
          tip.style.maxWidth = "420px";
          tip.style.display = "block";
          tip.style.left = Math.min(cssW - 430, Math.max(4, x + 12)) + "px";
          tip.style.top = Math.max(4, y - 8 - tip.offsetHeight) + "px";
          GPIN = [x, y];
        }
      }
      SEL = id && id !== SEL ? id : null;
      SELTH = null;''')
rep('''      if (wasTap) {
        pick(e);
        hover(e);
      }''', '''      if (wasTap) {
        pick(e);
        GPIN || hover(e);
      }''')
rep('''    function hover(e) {
      var r = cv.getBoundingClientRect(),
        x = e.clientX - r.left,
        y = e.clientY - r.top,
        best = null,
        bd = 18;''', '''    function hover(e) {
      var r = cv.getBoundingClientRect(),
        x = e.clientX - r.left,
        y = e.clientY - r.top,
        best = null,
        bd = 18;
      if (GPIN) {
        if (Math.hypot(GPIN[0] - x, GPIN[1] - y) < 30) return;
        GPIN = null;
      }''')

# --- the 3D relief asks the engine through D.onGround
rep('''        PAR && (D.spokes = 1);''', '''        PAR && (D.spokes = 1);
        ANH &&
          !PAR &&
          (D.onGround = function (x, y) {
            return AQ || !ANGROUND ? null : ANGROUND(x, y);
          });''')
rep('t && (t.textContent = "v232");', 't && (t.textContent = "v233");')
open(P, "w").write(s)

r = open(R).read()
a = "} else { pinned = null; hoverWay(null); hideTip(); } });"
assert r.count(a) == 1, r.count(a)
b = "bd.length > 420 ? bd.slice(0, 400)"
assert r.count(b) == 1
r = r.replace(b, "bd.length > (o.info.long ? 900 : 420) ? bd.slice(0, 400)")
r = r.replace(a, "} else { const g = D.onGround && groundAt(ev), gi = g && D.onGround(g[0], g[1]); if (gi) { pinned = { info: gi }; hoverWay(null); showTip(pinned, ev); } else { pinned = null; hoverWay(null); hideTip(); } } });")
a = "  function hoverWay(k) {"
assert r.count(a) == 1
r = r.replace(a, "  /* v233: where a tap lands on the ground, in the engine's own coordinates */\n  function groundAt(ev) { const r = renderer.domElement.getBoundingClientRect(); mv.set((ev.clientX - r.left) / r.width * 2 - 1, -(ev.clientY - r.top) / r.height * 2 + 1); ray.setFromCamera(mv, camera); const hit = ray.intersectObject(terrain, false)[0]; return hit ? [hit.point.x + W / 2, hit.point.z + H / 2] : null; }\n" + a)
open(R, "w").write(r)
print("ok")
