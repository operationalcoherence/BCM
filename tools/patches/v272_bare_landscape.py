# v272: THE BARE LANDSCAPE (his call, 25 Nov 2026), and YOUR WORDS ON THE GROUND removed.
# A new section on Pattern Analysis, after AT A GLANCE and before WHY IT BEHAVES THIS WAY: the line
# map's 3D ground with the notes and questions off (their emotion colors stay in the ground), read in
# BCM terms: where the force sits, which way it leans, what holds the situation in place, what can move
# now, what is less likely, and what is presently out of reach. Tapping the ground, a color in the bar,
# or a row of the table says what that ground is doing. Wording from his redline (doc "Redline: The Bare
# Ground", 25 Nov 2026). The section from In Parallel (v271) is gone from the page; Taking Action is
# unchanged.
p = 'gsm-readable.js'
s = open(p, encoding='utf-8').read()

def rep(old, new, n=1):
    global s
    c = s.count(old)
    assert c == n, (c, old[:90])
    s = s.replace(old, new)

# 1. YOUR WORDS ON THE GROUND no longer goes on the page; its button elsewhere stays hidden
rep('gsmWGPlace(Rt, ut, lt, a),', 'void a,')
rep('((window.gsmHasInt = !0), window.gsmJsub && window.gsmJsub());', '((window.gsmHasInt = !1), window.gsmJsub && window.gsmJsub());')

# 2. the section's place: before WHY IT BEHAVES THIS WAY (AT A GLANCE goes in above everything later)
rep('''          (window.gsmStruct ? window.gsmStruct() : "") +
          we +''', '''          (window.gsmData().m.some(function (t) {
            return (t[3] || "").trim() && null != t[5];
          })
            ? '<div class="plab">THE BARE LANDSCAPE</div><div class="gterr-host" data-an="1" data-bare="1"></div>'
            : "") +
          (window.gsmStruct ? window.gsmStruct() : "") +
          we +''')
rep('h.getAttribute("data-par") && (dd.par = 1);', 'h.getAttribute("data-par") && (dd.par = 1);\n        h.getAttribute("data-bare") && (dd.bare = 1);')

# 3. the flag
rep('''      ANH = !!data.an,
      PAR = !!data.par,''', '''      ANH = !!data.an,
      BARE = !!data.bare,
      PAR = !!data.par,''')

# 4. the 3D: notes and questions off, no tour, the ground reads itself when tapped
rep('host._rel.focusQ && host._rel.focusQ(AQ);', 'host._rel.focusQ && host._rel.focusQ(BARE ? -1 : AQ);')
rep('''            D.intro = introStops(true);''', '''            BARE || (D.intro = introStops(true));''')
rep('''            return AQ || !ANGROUND ? null : ANGROUND(x, y);
          });
        return D;''', '''            return AQ || !ANGROUND ? null : ANGROUND(x, y);
          });
        BARE && ((D.qpos = []), (D.read = []), (D.intro = []), (D.onGround = function (x, y) {
          return BAREGROUND ? BAREGROUND(x, y) : null;
        }));
        return D;''')
rep('''              host._rel = window.gsmRelief.mount(box, data());''', '''              host._rel = window.gsmRelief.mount(box, data());
              BARE && BAREAFTER && BAREAFTER(box);''')

# 5. the reading itself
rep('''    if (CARDH) {
      host.classList.add("gtcard");''', r'''    var BAREGROUND = null, BAREAFTER = null;
    if (BARE) {
      /* v272: THE BARE LANDSCAPE. The question buttons, the question text and WHAT THIS SUGGESTS are for the
         notes; this map has none showing. */
      host.querySelectorAll(".gtrb,.gtqpop,.gtansay").forEach(function (e) {
        e.parentNode && e.parentNode.removeChild(e);
      });
      [].slice.call(host.querySelectorAll(".sec")).forEach(function (e) {
        /^WHAT THIS SUGGESTS$/.test(e.textContent.trim()) && e.parentNode.removeChild(e);
      });
      host.classList.add("gtbare");
      if (!document.getElementById("gsm-barecss")) {
        var bcss = document.createElement("style");
        bcss.id = "gsm-barecss";
        bcss.textContent =
          ".gtbare .bri{font-size:15px;line-height:1.55;margin:0 0 10px}.gtbare .brh{border:1px solid #222;padding:12px 14px;margin:12px 0 0;min-height:70px;font-size:15px;line-height:1.5}" +
          ".gtbare .brh .hd{font-size:12.5px;letter-spacing:.12em;font-weight:bold;margin-bottom:4px}.gtbare .brh .k{display:inline-block;font-size:11.5px;letter-spacing:.08em;padding:1px 7px;margin:0 6px 6px 0;border:1px solid #222}" +
          ".gtbare .brh p{margin:4px 0}.gtbare .brh .em{color:#888}.gtbare .brb{display:flex;height:22px;margin:12px 0 4px;border:1px solid #222}.gtbare .brb i{display:block;height:100%;cursor:pointer}" +
          ".gtbare .brb i:hover{outline:2px solid #111;outline-offset:-2px}.gtbare .brl{display:flex;flex-wrap:wrap;gap:4px 14px;font-size:12.5px;color:#555}.gtbare .brl em{display:inline-block;width:10px;height:10px;margin-right:5px;vertical-align:-1px}" +
          ".gtbare .brr p{margin:10px 0;font-size:15px;line-height:1.55}.gtbare .brr .ld{font-size:16.5px}.gtbare .brr .nt{color:#777;font-size:13.5px}" +
          ".gtbare table.brt{border-collapse:collapse;width:100%;font-size:14px;margin:8px 0 6px}.gtbare table.brt th{text-align:left;font-size:11.5px;letter-spacing:.1em;color:#555;border-bottom:1px solid #222;padding:6px 8px 4px 0}" +
          ".gtbare table.brt td{border-bottom:1px solid #e4e4e4;padding:7px 8px 7px 0;vertical-align:top}.gtbare table.brt td.n{text-align:right;white-space:nowrap}.gtbare table.brt tr[data-k]{cursor:pointer}" +
          ".gtbare details.brm{margin:6px 0 0}.gtbare details.brm summary{cursor:pointer;font-size:14px;color:#555}";
        document.head.appendChild(bcss);
      }
      (function () {
        /* emotion index (EMO order) by height of ground, highest first */
        var bA = 1, bI = 3, bT = 2, bG = 0, bF = 4,
          ORD = [bA, bI, bT, bG, bF],
          RK = {},
          NM = EMO.map(function (e) {
            return e[0];
          }),
          CL = EMO.map(function (e) {
            return "rgb(" + e[1].join(",") + ")";
          }),
          esc = function (t) {
            return String(t).replace(/[&<>"]/g, function (c) {
              return "&#" + c.charCodeAt(0) + ";";
            });
          },
          pc = function (a, b) {
            return b ? Math.round((100 * a) / b) : 0;
          },
          and = function (a) {
            return a.length > 1 ? a.slice(0, -1).join(", ") + (a.length > 2 ? ", and " : " and ") + a[a.length - 1] : a[0] || "";
          };
        ORD.forEach(function (k, r) {
          RK[k] = r;
        });
        var rows = (data.m || []).filter(function (r) {
            return String(r[3] || "").trim();
          }),
          EN = rows.filter(function (r) {
            return null != r[5];
          }),
          TOT = EN.length,
          NONE = rows.length - TOT,
          up = function (r) {
            return null != r.hd ? !r.hd : r[2] < 118;
          },
          grasp = function (r) {
            return (r[0] || 0) <= 4;
          },
          by = {};
        if (!TOT) return;
        ORD.forEach(function (k) {
          var L = EN.filter(function (r) {
            return r[5] === k;
          });
          by[k] = { n: L.length, help: L.filter(up).length, cause: L.filter(grasp).length };
          by[k].hinder = by[k].n - by[k].help;
          by[k].act = by[k].n - by[k].cause;
        });
        var CAN = {};
        CAN[bA] = "Possible now";
        CAN[bI] = "Possible, as a crossing";
        CAN[bT] = "Unlikely in the short or medium term";
        CAN[bG] = "Unlikely soon; can be redirected";
        CAN[bF] = "Presently out of reach";
        function does(k, h) {
          if (k === bA)
            return h
              ? "It permits. Here people are already aligned with what serves the goal, so change can start now and be seen. It takes care to keep."
              : "It holds. This is acceptance of what hinders the goal: the present way feels right here, so it keeps itself in place without anyone pushing.";
          if (k === bI)
            return (
              "It neither helps nor hinders yet. It is the ridge most moves between emotions have to cross, and people can stay on it, precariously. This stretch tilts " +
              (h ? "toward" : "against") +
              " the goal; it could still be used to engage with others as they stay indifferent or in the interest of transitioning to acceptance."
            );
          if (k === bT)
            return h
              ? "It prohibits for now, though here it is distrust of what hinders the goal. It will not move quickly in either direction."
              : "It prohibits for now. This is part of what keeps the situation in its current and historic state, and it will not move quickly.";
          if (k === bG)
            return h
              ? "Energy already moving, pointed at what hinders the goal. It carries the goal, but it can harden into defiance."
              : "Energy already moving, pointed against the goal. It is something to redirect rather than overcome.";
          return "The lowest ground and the longest road back to acceptance. Pushed, resistance here turns to rebellion." + (h ? " Here it is defiance of what hinders the goal." : "");
        }
        /* the reading */
        var srt = ORD.filter(function (k) {
            return by[k].n;
          }).sort(function (a, b) {
            return by[b].n - by[a].n;
          }),
          tw = EN.filter(up).length,
          ag = TOT - tw,
          low = pc(by[bT].n + by[bG].n + by[bF].n, TOT),
          hold = by[bA].hinder + by[bT].hinder + by[bF].hinder,
          nowN = by[bA].help + by[bI].n,
          less = by[bT].n + by[bG].n,
          cT = EN.filter(grasp),
          aT = EN.filter(function (r) {
            return !grasp(r);
          }),
          lowOf = function (L) {
            return pc(
              L.filter(function (r) {
                return RK[r[5]] >= 2;
              }).length,
              L.length,
            );
          },
          HP = [
            [bA, "acceptance of what hinders the goal", "the present way feels right to the people holding it, so the situation keeps itself as it is without anyone pushing"],
            [bT, "distrust on the hindering side", "it will not move quickly, and it is much of what keeps the situation in its historic state"],
            [bF, "defiance on the hindering side", "the hardest of it, and the slowest to change"],
          ].sort(function (a, b) {
            return by[b[0]].hinder - by[a[0]].hinder;
          }),
          R = [];
        R.push(
          '<p class="ld">' +
            (TOT < 6 ? "This rests on only " + TOT + (1 === TOT ? " note" : " notes") + " with an emotion, so read it lightly. " : "") +
            (low > 55
              ? "Most of the force on this ground is low (" + low + "% on distrust, aggression, or defiance). "
              : low < 45
                ? "Most of the force on this ground is high (" + (100 - low) + "% on acceptance or indifference). "
                : "") +
            NM[srt[0]] +
            " carries the most (" +
            pc(by[srt[0]].n, TOT) +
            "%)" +
            (srt[1] != null ? ", then " + NM[srt[1]].toLowerCase() + " (" + pc(by[srt[1]].n, TOT) + "%)" : "") +
            ". Of all of it, " +
            pc(tw, TOT) +
            "% leans toward the goal and " +
            pc(ag, TOT) +
            "% against it" +
            (Math.abs(tw - ag) <= TOT * 0.15
              ? ": close to even, so neither side is likely to give way on its own."
              : tw > ag
                ? ": the ground already favors the goal."
                : ": the ground favors the present state.") +
            "</p>",
        );
        hold &&
          R.push(
            "<p><b>What holds it in place.</b> " +
              pc(hold, TOT) +
              "% of the force sits on the hindering side as acceptance, distrust, or defiance. The largest part of that is " +
              HP[0][1] +
              " (" +
              pc(by[HP[0][0]].hinder, TOT) +
              "%): " +
              HP[0][2] +
              ".</p>",
          );
        R.push(
          "<p><b>What can move now.</b> " +
            pc(nowN, TOT) +
            "%: acceptance on the helping side and the ridge of indifference. " +
            (by[bI].n
              ? "The ridge holds " +
                pc(by[bI].n, TOT) +
                "% of the force, and " +
                pc(by[bI].hinder, by[bI].n) +
                "% of that tilts against the goal. That is ground that can still be explored and possibly constructively engaged with, and it is the crossing most other moves have to use."
              : "No note carries indifference, so there is no ridge to cross by.") +
            "</p>",
        );
        less &&
          R.push(
            "<p><b>What is less likely.</b> " +
              pc(less, TOT) +
              "% sits on distrust and aggression, which will not move in the short or medium term." +
              (by[bG].n
                ? by[bG].help
                  ? " " +
                    pc(by[bG].help, by[bG].n) +
                    "% of the aggression is pointed at what hinders the goal, so " +
                    (by[bG].help >= by[bG].hinder ? "much" : "some") +
                    " of that energy is already working for it."
                  : " All of the aggression is pointed against the goal."
                : "") +
              "</p>",
          );
        by[bF].n &&
          R.push(
            "<p><b>What is presently out of reach.</b> Defiance holds " +
              pc(by[bF].n, TOT) +
              "%. It is the longest road back to acceptance, and pushing it turns resistance into rebellion.</p>",
          );
        if (cT.length && aT.length) {
          var lc = lowOf(cT),
            la = lowOf(aT);
          R.push(
            "<p><b>Where understanding turns into doing.</b> In what you have grasped (Q.1–Q.4), " +
              pc(cT.filter(up).length, cT.length) +
              "% of the force leans toward the goal; in what you would design (Q.5–Q.7), " +
              pc(aT.filter(up).length, aT.length) +
              "%. " +
              (Math.abs(lc - la) >= 8
                ? "Your plans sit on " +
                  (la > lc ? "lower" : "higher") +
                  " ground than the situation does (" +
                  la +
                  "% against " +
                  lc +
                  "% on distrust, aggression, or defiance), so expect " +
                  (la > lc ? "friction where the actions begin." : "the actions to meet less resistance than the situation holds.")
                : "Your plans stand on much the same ground as the situation, so they will meet the emotions already there.") +
              "</p>",
          );
        }
        R.push(
          '<p class="nt">Force here means how much of what was written carries each emotion.' +
            (NONE ? " " + NONE + (1 === NONE ? " note carries" : " notes carry") + " no emotion and " + (1 === NONE ? "is" : "are") + " not counted." : "") +
            " A ground that rests on a few notes rests on little.</p>",
        );
        var bar = "",
          lab = "",
          tb = "<tr><th>GROUND</th><th class=\"n\">FORCE</th><th class=\"n\">TOWARD THE GOAL</th><th>WHAT IT ALLOWS</th></tr>";
        ORD.forEach(function (k) {
          if (!by[k].n) return;
          bar += '<i data-k="' + k + '" style="width:' + (100 * by[k].n) / TOT + "%;background:" + CL[k] + '" title="' + NM[k] + ": " + pc(by[k].n, TOT) + '% of the force"></i>';
          lab += '<span><em style="background:' + CL[k] + '"></em>' + NM[k] + " " + pc(by[k].n, TOT) + "%</span>";
          tb +=
            '<tr data-k="' +
            k +
            '"><td><span style="display:inline-block;width:12px;height:12px;margin-right:6px;vertical-align:-1px;background:' +
            CL[k] +
            '"></span>' +
            NM[k] +
            '</td><td class="n">' +
            pc(by[k].n, TOT) +
            '%</td><td class="n">' +
            pc(by[k].help, by[k].n) +
            "%</td><td>" +
            CAN[k] +
            "</td></tr>";
        });
        var intro = document.createElement("div");
        intro.className = "bri";
        intro.textContent =
          "Your landscape with the notes and questions removed: only the emotions from the notes you provided earlier. Before reading what anyone said, read what the ground is doing: where the force sits, which way it leans, and what it allows.";
        host.insertBefore(intro, host.firstChild);
        var out = document.createElement("div");
        out.innerHTML =
          '<div class="brh"><div class="hd">WHAT THIS GROUND IS DOING</div><p class="em">Tap the ground, a color in the bar, or a row in the table to read it.</p></div>' +
          '<div class="brb">' +
          bar +
          '</div><div class="brl">' +
          lab +
          '</div><div class="brr">' +
          R.join("") +
          '</div><details class="brm"><summary>Each ground, side by side</summary><table class="brt">' +
          tb +
          "</table></details>";
        host.appendChild(out);
        var here = out.querySelector(".brh");
        function panel(head, tags, body) {
          here.innerHTML =
            '<div class="hd">' +
            esc(head) +
            "</div>" +
            tags
              .map(function (x) {
                return '<span class="k">' + esc(x) + "</span>";
              })
              .join("") +
            body
              .map(function (x) {
                return "<p>" + esc(x) + "</p>";
              })
              .join("");
        }
        function whole(k) {
          var b = by[k];
          panel(NM[k].toUpperCase() + ", ACROSS THE WHOLE MAP", [pc(b.n, TOT) + "% of the force", pc(b.help, b.n) + "% toward the goal", CAN[k]], [
            does(k, b.help >= b.hinder),
            "Of it, " + pc(b.cause, b.n) + "% is in what you have grasped and " + pc(b.act, b.n) + "% in what you would design.",
          ]);
          try {
            here.scrollIntoView({ behavior: "smooth", block: "nearest" });
          } catch (e) {}
        }
        out.addEventListener("click", function (ev) {
          var t = ev.target.closest && ev.target.closest("[data-k]");
          t && whole(+t.getAttribute("data-k"));
        });
        BAREGROUND = function (x, y) {
          var ns = ((terr && terr.notes) || []).filter(function (n) {
              return null != n.e;
            }),
            sg = (terr && terr.sigma) || 18,
            near = ns
              .map(function (n) {
                return { n: n, d: Math.hypot(n.x - x, n.y - y) };
              })
              .sort(function (a, b) {
                return a.d - b.d;
              });
          if (!near.length || near[0].d > 1.2 * sg) {
            panel("NO NOTES NEARBY", [], ["Plain ground: nothing was written here, so the map has no information about it."]);
            return { head: "No notes nearby", body: "Nothing was written here, so there is no information." };
          }
          var k = near[0].n.e,
            h = y < 118,
            pt = near
              .filter(function (o) {
                return o.d < 2.2 * sg && o.n.e === k;
              })
              .map(function (o) {
                return o.n;
              }),
            ph = pt.filter(function (n) {
              return n.y < 118;
            }).length,
            ar = near
              .filter(function (o) {
                return o.d < 2.5 * sg;
              })
              .map(function (o) {
                return o.n.e;
              }),
            ridge = k !== bI && ar.indexOf(bI) >= 0,
            far = ar.filter(function (e, i) {
              return ar.indexOf(e) === i && Math.abs(RK[e] - RK[k]) >= 2;
            }),
            nb = [];
          ridge && nb.push("A ridge of indifference runs beside it: there is a way across from here.");
          far.length &&
            !ridge &&
            nb.push(
              "It meets " +
                and(
                  far.map(function (e) {
                    return NM[e].toLowerCase();
                  }),
                ) +
                " with no ridge between: bare rock, so getting across is a climb either way.",
            );
          nb.length || k === bI || nb.push("Its neighbors are close emotions, so a move from here is short.");
          var body = [
            "This stretch of ground holds " +
              pc(pt.length, TOT) +
              "% of the force on the map (" +
              NM[k].toLowerCase() +
              " as a whole: " +
              pc(by[k].n, TOT) +
              "%). " +
              (pt.length > 1 ? pc(ph, pt.length) + "% of it leans toward the goal." : "It rests on a single note, so it says little."),
            does(k, h),
          ].concat(nb);
          panel("WHAT THIS GROUND IS DOING", [NM[k].toUpperCase(), h ? "HELP SIDE" : "HINDER SIDE", CAN[k]], body);
          return { head: NM[k] + " · " + (h ? "help side" : "hinder side") + " · " + CAN[k].toLowerCase(), body: body.join(" "), long: 1 };
        };
        BAREAFTER = function (bx) {
          host._rel && host._rel.focusQ && host._rel.focusQ(-1);
          bx.querySelectorAll(".grleg .r span").forEach(function (sp) {
            /^Pins are notes/.test(sp.textContent) &&
              (sp.textContent =
                "Notes and questions are off. The green flag is the present; the checkered flag is the goal. ← PRESENT and FUTURE → run along the front; ↑ HELP and ↓ HINDER run back to front.");
            /^Drag to turn/.test(sp.textContent) && (sp.textContent = "Drag to turn, scroll or pinch to zoom. Tap the ground to read what it is doing.");
          });
        };
      })();
    }
    if (CARDH) {
      host.classList.add("gtcard");''')

open(p, 'w', encoding='utf-8').write(s)
print('v272 patched')
