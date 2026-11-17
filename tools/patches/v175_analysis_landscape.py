"""v175: V1, Pattern Analysis gets the new 3D landscape near the top, read one question at a time,
with WHAT THIS SUGGESTS written from it. The old petal figure is kept hidden for In Parallel until V2."""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:80]); s = s.replace(a, b)

# page: the landscape right under LOOKING IN; the old figure hidden when the landscape can be drawn
rep("""          '<div class="part">1 · LOOKING IN<span>Analysis: the pieces, one at a time.</span></div>' +""",
"""          '<div class="part">1 · LOOKING IN<span>Analysis: the pieces, one at a time.</span></div>' +
          (C.m.some(function (t) {
            return (t[3] || "").trim();
          })
            ? '<div class="plab">YOUR LANDSCAPE, ONE QUESTION AT A TIME</div><div class="gterr-host" data-an="1"></div>'
            : "") +""")
rep("""          (fe ? Oe(U) : Oe(U, "goal")) +""", """          (C.m.some(function (t) {
            return (t[3] || "").trim();
          })
            ? '<div class="gtold" style="display:none" aria-hidden="true">' + (fe ? Oe(U) : Oe(U, "goal")) + "</div>"
            : fe
              ? Oe(U)
              : Oe(U, "goal")) +""")
# the module learns analysis mode from the host
rep("""        mount(h, window.gsmData ? window.gsmData() : window.gsmTD || {});
      } catch (e) {
        h.textContent = "";""", """        var dd = window.gsmData ? window.gsmData() : window.gsmTD || {};
        h.getAttribute("data-an") && (dd.an = 1);
        mount(h, dd);
      } catch (e) {
        h.textContent = "";""")
rep("""      if (data && data.card) {
        how.style.display = "none";
        return;
      }""", """      if (data && (data.card || data.an)) {
        how.style.display = "none";
        return;
      }""")
rep("    var CARDH = !!data.card;", "    var CARDH = !!data.card,\n      ANH = !!data.an,\n      AQ = 0;")
# relief: no numbered readings in analysis mode; focus follows the question buttons
rep("""        } else {
          D.read = READ.map(function (r) {
            return { at: r.at, title: r.title, text: r.short + (r.more ? " " + r.more : "") };
          });""", """        } else if (ANH) {
          D.read = [];
        } else {
          D.read = READ.map(function (r) {
            return { at: r.at, title: r.title, text: r.short + (r.more ? " " + r.more : "") };
          });""")
rep("""      if (host._rel) {
        host._rel.hl(HL);""", """      if (host._rel) {
        if (ANH) {
          host._rel.focusQ && host._rel.focusQ(AQ);
          return;
        }
        host._rel.hl(HL);""")

AN_SETUP = r'''
    if (ANH) {
      host.classList.add("gtan");
      host.querySelectorAll(".plab,.sub,.bar,.gfold").forEach(function (e) {
        e.style.display = "none";
      });
      ["crshead", "courses", "coursebox", "rdhead", "readings", "selnote", "msg"].forEach(function (id) {
        var e = $(id);
        if (e) e.style.display = "none";
      });
      LEGON = false;
      showCause = false;
      var RL = ["why it has not taken root", "opposition", "support", "conditions", "design", "redesign", "reinforce"],
        EN = ["aggression", "acceptance", "distrust", "indifference", "defiance"],
        rows = (data.m || [])
          .map(function (r, i) {
            return { r: r, id: "N" + (i + 1) };
          })
          .filter(function (o) {
            return String(o.r[3] || "").trim();
          }),
        has = [0, 0, 0, 0, 0, 0, 0, 0];
      rows.forEach(function (o) {
        has[o.r[0]] = (has[o.r[0]] || 0) + 1;
      });
      var qb = document.createElement("div");
      qb.className = "gtrb";
      qb.innerHTML = "<span>Show</span>";
      function qbtn(q, label) {
        var b = document.createElement("button");
        b.type = "button";
        b.textContent = label;
        b.title = q ? "Q." + q + " · " + RL[q - 1] + " (" + has[q] + " note" + (1 === has[q] ? "" : "s") + ")" : "Every note";
        b.onclick = function () {
          AQ = q;
          [].slice.call(qb.querySelectorAll("button")).forEach(function (x) {
            x.classList.toggle("on", x === b);
          });
          var t = host.querySelector(".gtansay");
          t && (t.innerHTML = say(q));
          render();
        };
        q || b.classList.add("on");
        qb.appendChild(b);
      }
      qbtn(0, "All notes");
      for (var qq = 1; qq <= 7; qq++) has[qq] && qbtn(qq, "Q." + qq);
      $("stage").parentNode.insertBefore(qb, $("stage"));
      function ids(L) {
        var a = L.map(function (o) {
          return o.id;
        });
        return a.length > 5 ? a.slice(0, 5).join(", ") + " and " + (a.length - 5) + " more" : a.length > 1 ? a.slice(0, -1).join(", ") + " and " + a[a.length - 1] : a[0] || "";
      }
      function prof(L) {
        var c = [0, 0, 0, 0, 0],
          n = 0,
          up = 0;
        L.forEach(function (o) {
          null != o.r[5] && (c[o.r[5]]++, n++);
          o.r[2] < 118 && up++;
        });
        var top = 0;
        c.forEach(function (x, k) {
          x > c[top] && (top = k);
        });
        return { c: c, n: n, up: up, dn: L.length - up, top: top, hard: c[0] + c[4] + c[2] };
      }
      function say(q) {
        if (q) {
          var L = rows.filter(function (o) {
              return o.r[0] === q;
            }),
            p = prof(L),
            t =
              "<b>Q." +
              q +
              " (" +
              RL[q - 1] +
              ")</b> has " +
              L.length +
              " note" +
              (1 === L.length ? "" : "s") +
              " on the map (" +
              ids(L) +
              "), " +
              (p.up && p.dn ? p.up + " above the line and " + p.dn + " below" : p.up ? "all above the line, where things help" : "all below the line, where things hinder") +
              ".";
          p.n &&
            (t +=
              (p.c[p.top] === p.n ? " All of them carry " : 2 * p.c[p.top] > p.n ? " Most of them carry " : " More of them carry ") +
              EN[p.top] +
              " (" +
              p.c[p.top] +
              " of " +
              p.n +
              "), so " +
              (1 === p.top
                ? "this part of your thinking stands on high ground."
                : 3 === p.top
                  ? "it rides the ridge: people here are not yet for or against, and can tip either way."
                  : "this part of your thinking sits in low ground, where the emotions there will meet anything placed in it first."));
          q >= 5 &&
            p.hard &&
            (t +=
              " " +
              p.hard +
              " of these actions sit in distrust, aggression or defiance. An action placed in hard ground has to work with the emotion it lands in, not only toward the goal.");
          2 === q &&
            p.up &&
            (t += " " + p.up + " of the opposition notes sit above the line: something you count as opposition is also placed where it helps. Worth a second look.");
          return t;
        }
        var by = [];
        for (var k = 1; k <= 7; k++) {
          var Lk = rows.filter(function (o) {
            return o.r[0] === k;
          });
          Lk.length && by.push({ q: k, L: Lk, p: prof(Lk) });
        }
        if (!by.length) return "";
        var hi = by.slice().sort(function (a, b) {
            return b.p.c[1] / (b.p.n || 1) - a.p.c[1] / (a.p.n || 1);
          })[0],
          lo = by.slice().sort(function (a, b) {
            return (b.p.c[0] + b.p.c[4]) / (b.p.n || 1) - (a.p.c[0] + a.p.c[4]) / (a.p.n || 1);
          })[0],
          miss = [];
        for (var m = 1; m <= 7; m++) has[m] || miss.push("Q." + m);
        var act = rows.filter(function (o) {
            return o.r[0] >= 5 && null != o.r[5] && 1 !== o.r[5] && 3 !== o.r[5];
          }),
          ind = rows.filter(function (o) {
            return 3 === o.r[5];
          }),
          t = "Each question's notes sit somewhere on this ground, and where they sit says how that part of your thinking feels.";
        hi.p.c[1] &&
          (t += " The high ground belongs mostly to <b>Q." + hi.q + " (" + RL[hi.q - 1] + ")</b>: " + hi.p.c[1] + " of its " + hi.p.n + " notes carry acceptance.");
        lo !== hi &&
          lo.p.c[0] + lo.p.c[4] &&
          (t +=
            " The lowest ground belongs to <b>Q." +
            lo.q +
            " (" +
            RL[lo.q - 1] +
            ")</b>: " +
            (lo.p.c[0] + lo.p.c[4]) +
            " of its " +
            lo.p.n +
            " notes carry aggression or defiance.");
        act.length &&
          (t +=
            " " +
            ids(act) +
            (act.length > 1 ? " are" : " is") +
            " something you would do, placed in hard ground. Those actions will meet the emotion there before they reach the goal.");
        ind.length &&
          (t +=
            " " +
            ids(ind) +
            (ind.length > 1 ? " carry" : " carries") +
            " indifference: the ridge, where most moves between emotions cross.");
        miss.length &&
          (t +=
            " " +
            miss.join(", ") +
            (miss.length > 1 ? " have" : " has") +
            " no note on the ground yet, so " +
            (miss.length > 1 ? "those answers are" : "that answer is") +
            " not yet part of the landscape.");
        return t + " Tap a question above the map to see only its notes.";
      }
      var sy = document.createElement("div");
      sy.className = "gtansay";
      sy.style.cssText = "font-size:15px;line-height:1.55;margin:10px 0 4px;border-left:3px solid #222;padding:2px 0 2px 12px";
      sy.innerHTML = say(0);
      var stg0 = $("stage"),
        after = stg0.nextSibling;
      stg0.parentNode.insertBefore(sy, after);
      var hd = document.createElement("div");
      hd.className = "sec";
      hd.style.marginTop = "12px";
      hd.textContent = "WHAT THIS SUGGESTS";
      stg0.parentNode.insertBefore(hd, sy);
    }
'''
rep("""    if (CARDH) {
      host.classList.add("gtcard");""", AN_SETUP + """    if (CARDH) {
      host.classList.add("gtcard");""")
rep('t && (t.textContent = "v174");', 't && (t.textContent = "v175");')
open(P, "w").write(s); print("v175 ok")
