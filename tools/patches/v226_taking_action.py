"""v226: Phase 2 step 8, Taking Action rebuilt around the central test (BCM_ARCHITECTURE.md §0.3):
"Does what you would design change the conditions and invite the transitions the goal needs?"

1. THE TEST panel at the top of the page reads the workbook against the test: what holds it, what already
   moves, where it can shift, where the reading splits, the cheapest first move, and the constraints named.
2. Cards seeded from Pattern Analysis's structure (gsmStruct, now keeping its notes in gsmStructSum.D):
   strategies from THE SYSTEM THAT HOLDS, THE KEY TENSION, and THE LOOP; programs from THE OPPORTUNITY,
   WHAT IS ALREADY HELPING, and SUPPORT NOT YET REINFORCED. Each seeded card carries the test on its own
   notes (DOES WHAT YOU WOULD DESIGN MEET IT?), THE WAY ACROSS (ridge before bare rock, the cost of each
   move, behaviors first below the ridge and emotions first above it, entrenched notes), FIRST MOVES or
   THE SEQUENCE, the 3D ways, and the constraint fields.
3. Split readings carried into action: In Parallel keeps its double readings in window.gsmSplit; each card
   whose notes they touch gets WHERE THE READING SPLITS with what it means for acting (TWO PEOPLE, TWO SIDES;
   THE EMOTION CHANGES; ONE IDEA UNDER TWO NAMES; PLACED ONE WAY, TIED THE OTHER). Splits no card takes up
   are listed in THE TEST.
4. Constraint -> card -> WHAT YOU DID -> re-map: a named constraint gets one-tap buttons to add it to Q.4,
   Q.6, or Q.7 (the answer is updated on Mapping Context too); WHAT YOU DID lists the constraints named on the
   card, saves them with the log entry (acts[].c), and flags those notes on Mapping Landscape; SINCE YOU ACTED
   shows each flagged note's constraint.
5. Strategies and programs grouped, each under its own heading with its explanation; seeded cards first.
6. The chart comparing the ways is open by default.
7. Each field says in one line what it does and where it goes; WHAT EACH PART OF A CARD DOES explains them all.
All wording is Claude's, for his redlines.
Usage: python3 v226_taking_action.py gsm-readable.js"""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)

# ---------------------------------------------------------------- 1. structure keeps its notes
rep('''    var SS = (window.gsmStructSum = {});''', '''    var SS = (window.gsmStructSum = {});
    SS.D = {};''')
rep('''      SS.sys = sysNames.slice(0, 3);''', '''      SS.sys = sysNames.slice(0, 3);
      SS.D.sys = comp;''')
rep('''        SS.tension = 1;''', '''        SS.tension = 1;
        SS.D.ten = {
          gc: gc.replace(/^(to|and|whereas)\\s+/i, ""),
          f: fears.map(function (x) {
            return x.n;
          }),
          h: notes.filter(function (n) {
            if (n.side <= 0) return !1;
            for (var k in gk) if (n.keys[k]) return !0;
            return !1;
          }),
        };''')
rep('''      card(
        "THE LOOP",''', '''      SS.D.loop = { s: best.s, t: best.t, k: lk, n: lsk.map(function (l) { return l.s; }).filter(function (n) { return n.note; }) };
      card(
        "THE LOOP",''')
rep('''      SS.opp = ex.length >= nw.length ? "Most" : "Part";''', '''      SS.opp = ex.length >= nw.length ? "Most" : "Part";
      SS.D.opp = ex;
      SS.D.oppN = exNames;''')
rep('''    var ind = notes.filter(function (n) {
      return 3 === n.em;
    });''', '''    var ind = notes.filter(function (n) {
      return 3 === n.em;
    });
    SS.D.ind = ind;''')

# ---------------------------------------------------------------- 2. what Q.5-Q.7 reaches, kept for Taking Action
rep('''          window.gsmNR = { u: U, t: T, rs: RS };''', '''          window.gsmNR = { u: U, t: T, rs: RS, rw: RW, cm: CM, ri: RI };''')

# ---------------------------------------------------------------- 3. In Parallel keeps its double readings
rep('''                      { words: [t.w], voices: i.concat(a) },''', '''                      { words: [t.w], voices: i.concat(a), vi: i, va: a, eu: eu, ed: ed },''')
rep('''                              7 + o / 100,
                              { notes: [t] },''', '''                              7 + o / 100,
                              { notes: [t], pe: pe, pt: pt, up: e.up },''')
rep('''                  R.sort(function (t, e) {
                    return e.rare - t.rare;
                  });''', '''                  try {
                    window.gsmSplit = R.filter(function (r) {
                      return /^(TWO PEOPLE, TWO SIDES|THE EMOTION CHANGES|ONE IDEA UNDER TWO NAMES|PLACED ONE WAY, TIED THE OTHER)$/.test(r.lab);
                    }).map(function (r) {
                      var ids = (r.k.notes || []).slice();
                      (r.k.words || []).forEach(function (w) {
                        N.forEach(function (t) {
                          t.w === w &&
                            t.ids.forEach(function (i) {
                              ids.indexOf(i) < 0 && ids.push(i);
                            });
                        });
                      });
                      var su = 0,
                        sd = 0;
                      ids.forEach(function (i) {
                        var o = C[i];
                        o && (!0 === o.up ? su++ : !1 === o.up && sd++);
                      });
                      return {
                        lab: r.lab,
                        k: r.k,
                        su: su,
                        sd: sd,
                        names: (r.k.words || []).map(function (w) {
                          return jt(w);
                        }),
                        ids: ids.map(function (i) {
                          return String(i).replace(/^place note (\\d+)/, "P$1");
                        }),
                      };
                    });
                  } catch (e0) {
                    window.gsmSplit = [];
                  }
                  R.sort(function (t, e) {
                    return e.rare - t.rare;
                  });''')

# ---------------------------------------------------------------- 4. seeded cards and THE TEST
rep('''        var In = "",
          Qn = "",
          qn = "";''', '''        var In = "",
          Qn = "",
          qn = "",
          TAT = "";''')

SEED = r'''          (function () {
            try {
              window.gsmStruct && window.gsmStruct();
            } catch (e) {}
            var SS = window.gsmStructSum || {},
              D = SS.D || {},
              NR = window.gsmNR || {},
              RW = NR.rw || {},
              CM = NR.cm || {},
              RI = NR.ri || {},
              BY = {},
              RK = [4, 1, 3, 2, 5],
              E = EMN;
            a.forEach(function (x) {
              BY[x.id] = x;
            });
            var UNU = {};
            de.forEach(function (t) {
              ge[t] &&
                "unused" === ge[t].c &&
                xo(t).forEach(function (x) {
                  var r = x.line || x.place,
                    e = r ? r[5] : null;
                  (x.line ? x.line[2] < 118 : 3 === x.k || 7 === x.k) && 0 !== e && 2 !== e && 4 !== e && (UNU[x.id] = 1);
                });
            });
            function IT(ns) {
              var o = [],
                sn = {};
              (ns || []).forEach(function (n) {
                var x = BY[n && n.ref ? n.ref : n];
                x && x.txt.trim() && !sn[x.id] && ((sn[x.id] = 1), o.push(x));
              });
              return o;
            }
            function EO(x) {
              var r = x.line || x.place;
              return r && null != r[5] && r[5] >= 0 && r[5] < 5 ? +r[5] : null;
            }
            function LOW(x) {
              var e = EO(x);
              return 0 === e || 2 === e || 4 === e;
            }
            function UP(x) {
              return x.line ? x.line[2] < 118 : 3 === x.k || 7 === x.k;
            }
            function LS(xs, k) {
              k = k || 4;
              var b = xs.slice(0, k).map(function (x) {
                return x.id;
              });
              xs.length > k && b.push(xs.length - k + " more");
              return phList(b);
            }
            function NM(x) {
              return gsmStName({ txt: String(x.txt).replace(/^\s*(reinforce|continue to|support|scale|grow|keep)\s+/i, "") }) || x.id;
            }
            function ME(x) {
              var n = String(x.id).replace(/\D/g, "");
              return /^P/.test(x.id) ? "N" + n + " (place)" : "N" + n;
            }
            function REACH(x) {
              var r = x.line || x.place,
                me = ME(x),
                by = [];
              Object.keys(x.t.k).forEach(function (k) {
                !CM[k] &&
                  RW[k] &&
                  RW[k].forEach(function (l) {
                    l !== me && by.indexOf(l) < 0 && by.push(l);
                  });
              });
              r &&
                (C.links || []).some(function (l) {
                  return (l.f === r[8] && RI[l.t]) || (l.t === r[8] && RI[l.f]);
                }) &&
                by.push("a link you drew");
              var ak = r && (C.asks || {})["resp|" + r[8]];
              return "n" === ak ? [] : by.length ? by : "y" === ak ? ["your yes"] : [];
            }
            function TEST(xs, help) {
              if (!xs.length) return null;
              var met = [],
                not = [],
                by = [];
              xs.forEach(function (x) {
                if (help && UNU[x.id]) return void not.push(x);
                if (help && x.k >= 5) return void met.push(x);
                var b = REACH(x);
                b.length
                  ? (met.push(x),
                    b.slice(0, 2).forEach(function (l) {
                      by.indexOf(l) < 0 && by.push(l);
                    }))
                  : not.push(x);
              });
              var h = "";
              met.length && (h += "What you would design reaches " + LS(met) + (by.length ? " (through " + phList(by.slice(0, 3)) + ")" : "") + ". ");
              not.length
                ? (h += "Nothing you would design " + (help ? "builds on " : "answers ") + LS(not) + " yet, so " + (help ? (1 === not.length ? "it" : "they") + " can slip." : (1 === not.length ? "it keeps" : "they keep") + " holding."))
                : (h += help ? "All of it is built on." : "All of it is answered somewhere.");
              return { h: h, met: met, not: not, v: not.length ? (met.length ? "partly" : "not yet") : "yes" };
            }
            var RIDGE = IT(D.ind),
              ACC = a.filter(function (x) {
                return x.txt.trim() && 1 === EO(x) && UP(x);
              });
            function DST(p, q) {
              return p.line && q.line ? Math.hypot(p.line[1] - q.line[1], p.line[2] - q.line[2]) : 999;
            }
            function NEAR(list, x) {
              return (
                list.slice().sort(function (p, q) {
                  return DST(x, p) - DST(x, q);
                })[0] || null
              );
            }
            function COST(n) {
              return n <= 1 ? "low" : n <= 3 ? "moderate" : "high";
            }
            function WAY(xs) {
              var lows = xs.filter(LOW);
              if (!lows.length) return null;
              var G = {};
              lows.forEach(function (x) {
                var e = EO(x);
                (G[e] = G[e] || []).push(x);
              });
              var ems = Object.keys(G)
                  .map(Number)
                  .sort(function (p, q) {
                    return RK[p] - RK[q];
                  }),
                s0 = G[ems[0]][0],
                rg = NEAR(RIDGE, s0),
                tg = rg ? NEAR(ACC, rg) : NEAR(ACC, s0),
                out = [],
                ids = [];
              ems.forEach(function (e, i) {
                var st = Math.abs(RK[e] - 2),
                  xe = G[e];
                xe.slice(0, 2).forEach(function (x) {
                  ids.push(x);
                });
                if (4 === e && ems.length > 1 && i === ems.length - 1)
                  return void out.push("Leave the defiance (" + LS(xe, 3) + ") for last: it is the longest road to acceptance.");
                out.push(
                  (0 === i ? "Start with the " : "Then the ") +
                    E[e] +
                    " (" +
                    LS(xe, 3) +
                    "): " +
                    (rg
                      ? (1 === st ? "one step" : st + " steps") + " to the ridge of indifference" + (0 === i ? " at " + rg.id : "") + ", then one more up to acceptance" + (0 === i && tg ? " at " + tg.id : "")
                      : st + 1 + " steps straight up to acceptance") +
                    " (cost: " +
                    COST(st + 1 + (rg ? 0 : 2)) +
                    ").",
                );
              });
              out.push(
                rg
                  ? "Straight across from " + E[ems[0]] + " to acceptance would be a climb over bare rock, which costs more."
                  : "There is no ridge of indifference here yet, so every crossing is a climb over bare rock. First look for people who are for nothing yet, and add them to the map: a ridge can form there.",
              );
              var held = lows.filter(function (x) {
                var r = x.line || x.place,
                  h = r && window.gsmHy ? window.gsmHy(r[8]) : null;
                return h && h.hy > 1.05;
              });
              held.length && out.push(LS(held, 3) + (1 === held.length ? " has" : " have") + " been held where " + (1 === held.length ? "it is" : "they are") + " for a while, so " + (1 === held.length ? "it costs" : "they cost") + " more to move.");
              out.push("Below the ridge, behaviors first; from the ridge up, emotions first (Vigneaux, 2026).");
              rg && ids.push(rg);
              tg && ids.push(tg);
              return { h: out.join(" "), ids: ids, e0: ems[0], s0: s0, rg: rg };
            }
            function PWAY(xs) {
              if (!xs.length) return null;
              var edge = a.filter(function (y) {
                  return (
                    y.txt.trim() &&
                    xs.indexOf(y) < 0 &&
                    (LOW(y) || 3 === EO(y)) &&
                    xs.some(function (x) {
                      return DST(x, y) <= 60;
                    })
                  );
                }),
                le = edge.filter(LOW),
                ie = edge.filter(function (y) {
                  return 3 === EO(y);
                }),
                h = "Already on the high ground: no crossing, so the cost is low.";
              ie.length && (h += " " + LS(ie, 2) + ", at its edge on the ridge, could tip either way: bring " + (1 === ie.length ? "it" : "them") + " in early.");
              le.length && (h += " " + LS(le, 2) + ", close by in " + E[EO(le[0])] + ", could pull it down.");
              h += " Emotions first, and keep it up: acceptance doesn’t hold on its own (Vigneaux, 2026).";
              return { h: h, ids: xs.slice(0, 6).concat(ie.slice(0, 1)) };
            }
            function MIX(xs) {
              return (
                xs.some(function (x) {
                  return 1 === EO(x);
                }) && xs.some(LOW)
              );
            }
            function DOM(xs) {
              var c = [0, 0, 0, 0, 0];
              xs.forEach(function (x) {
                var e = EO(x);
                null != e && LOW(x) && c[e]++;
              });
              var m = Math.max.apply(null, c);
              return m > 0 ? c.indexOf(m) : null;
            }
            var CARDS = [],
              ROWS = { hold: [], move: [] },
              HTML = [];
            function CARD(o) {
              var OV = gsmModeOv(o.key),
                S = null == OV ? !!o.isS : !!OV,
                its = [],
                sn = {};
              (o.way ? o.way.ids : []).concat(o.items).forEach(function (x) {
                x && !sn[x.id] && ((sn[x.id] = 1), its.push(x));
              });
              CARDS.push({ S: S, title: o.title, seed: o.seed, ids: its });
              HTML.push(
                '<div class="coa" data-seed="' +
                  o.seed +
                  '" data-seedids="' +
                  Gt(
                    its
                      .map(function (x) {
                        return x.id;
                      })
                      .join(","),
                  ) +
                  '"><div class="hd"><div class="hdt"><b>' +
                  Gt(o.title) +
                  '</b><span class="phctx"> · grown from ' +
                  o.from +
                  '</span></div><span class="mode' +
                  (S ? " s" : "") +
                  '">' +
                  (S ? "STRATEGY" : "PROGRAM") +
                  '</span></div><div class="bd"><div class="purp"><b>IN SERVICE OF THE GOAL</b> ' +
                  o.purp +
                  "</div>" +
                  (o.test
                    ? '<div class="csec tatest"><div class="csl">DOES WHAT YOU WOULD DESIGN MEET IT? <span class="tav tav-' +
                      o.test.v.replace(" ", "") +
                      '">' +
                      o.test.v.toUpperCase() +
                      '</span></div><div class="csn">' +
                      o.test.h +
                      "</div></div>"
                    : "") +
                  '<div class="coacall">A <b>' +
                  (S ? "strategy" : "program") +
                  "</b>, because " +
                  (null != OV ? "you set it as one." : o.why) +
                  gsmModeBtn(o.key, S) +
                  "</div>" +
                  (o.way ? '<div class="csec taway"><div class="csl">THE WAY ACROSS</div><div class="csn">' + o.way.h + "</div></div>" : "") +
                  Un(S, o.moves, o.have || [], o.stand || [], [], [], [], its) +
                  '<div class="q">' +
                  (S ? Mn : jn) +
                  "</div></div></div>",
              );
            }
            // strategies: what holds it
            var sys = IT(D.sys);
            if (sys.length >= 3 && SS.sys) {
              var tS = TEST(sys, 0),
                wS = WAY(tS.not.concat(tS.met)),
                dS = DOM(sys),
                mS = [
                  "Don’t argue with it; change a condition that keeps it in place. Start with " + sys[0].id + " (" + Gt(NM(sys[0])) + "), the part most tied to the others.",
                ];
              wS && mS.push("Cross where it is cheapest first: " + Gt(E[wS.e0]) + (wS.rg ? ", through the ridge at " + wS.rg.id : "") + ". THE WAY ACROSS gives the order.");
              null != dS && mS.push("In the low ground, bring the behavior before its label: something people can do that fits the " + E[dS] + " already there.");
              tS.not.length && mS.push("Name what holds " + LS(tS.not, 3) + " below, and add it to Q.4 or Q.6, so what you would design answers it.");
              mS.push("Watch whether the parts start to come apart from each other: that is the system giving.");
              CARD({
                key: "seed|sys",
                seed: "sys",
                title: "What holds it: " + gsmMeanList(SS.sys.slice(0, 3)),
                from: "THE SYSTEM THAT HOLDS (Pattern Analysis)",
                isS: 1,
                purp: "These parts hold each other up against the goal. Changing one condition under them moves more than arguing with any one of them.",
                test: tS,
                why: "it works in the low ground" + (null != dS ? ", mostly " + E[dS] : "") + ", where every crossing is uncertain and the course has to change as people respond.",
                way: wS,
                moves: mS,
                stand: sys,
                items: tS.not.concat(tS.met),
              });
              ROWS.hold.push({ lab: "The system that holds", t: tS, title: "What holds it: " + gsmMeanList(SS.sys.slice(0, 3)) });
            }
            // strategies: the key tension
            if (D.ten && D.ten.f && D.ten.f.length) {
              var fT = IT(D.ten.f),
                hT = IT(D.ten.h).slice(0, 3),
                tT = TEST(fT, 0),
                wT = WAY(fT),
                gc = String(D.ten.gc || "").replace(/\s+/g, " ").trim(),
                gw = gc.split(" "),
                gs = gw.slice(0, 9).join(" ") + (gw.length > 9 ? "…" : "");
              if (fT.length) {
                var mT = [
                  "Change what people expect “" + Gt(gs) + "” to do before you ask for more of it.",
                  "Start with " + fT[0].id + " and the people behind it: show the practice done small and safely before you ask them to support it.",
                ];
                hT.length && mT.push("Lean on " + LS(hT, 2) + ", where the same idea already helps the goal.");
                mT.push("Watch the fear in " + fT[0].id + ": does it soften or harden as the work grows?");
                CARD({
                  key: "seed|ten",
                  seed: "ten",
                  title: "The key tension: " + gs,
                  from: "THE KEY TENSION (Pattern Analysis)",
                  isS: 1,
                  purp: "The goal asks for more of what people fear. The work is to change what people expect it to do, so that asking for more of it stops raising the fear.",
                  test: tT,
                  why: "it is pulled two ways: what one side asks for, the other side fears.",
                  way: wT,
                  moves: mT,
                  have: hT,
                  stand: fT,
                  items: fT.concat(hT),
                });
                ROWS.hold.push({ lab: "The key tension", t: tT, title: "The key tension: " + gs });
              }
            }
            // strategies: the loop
            if (D.loop && D.loop.n && D.loop.n.length) {
              var lI = IT(D.loop.n),
                tL = TEST(lI, 0),
                wL = WAY(lI),
                lsrc = D.loop.s && D.loop.s.note ? BY[D.loop.s.ref] : null,
                lt = lsrc ? NM(lsrc) : lI[0] ? NM(lI[0]) : "";
              if (lI.length && lt) {
                var mL = [
                  "Find the step in the loop you can change, not its result: " + gsmStQ(D.loop.s, D.loop.t, D.loop.k) + ".",
                  "Act early: each round makes the next one harder.",
                  "Name that step below as what holds it, and add it to Q.4: a condition to establish, so the loop stops feeding itself.",
                  "Watch the next round: if it calls for more of the same, the loop still runs.",
                ];
                CARD({
                  key: "seed|loop",
                  seed: "loop",
                  title: "The loop: " + lt,
                  from: "THE LOOP (Pattern Analysis)",
                  isS: 1,
                  purp: "Each round of it makes the next round harder. Break it at a step you can change, and the ground stops sinking.",
                  test: tL,
                  why: "a loop changes as you act on it, so the course has to change with it.",
                  way: wL,
                  moves: mL,
                  stand: lI,
                  items: lI,
                });
                ROWS.hold.push({ lab: "The loop", t: tL, title: "The loop: " + lt });
              }
            }
            // programs: what already moves
            var opp = IT(D.opp),
              oSet = {},
              PCARDS = [];
            opp.forEach(function (x) {
              oSet[x.id] = 1;
            });
            var help = a.filter(function (x) {
                var e = EO(x);
                return x.txt.trim() && x.k <= 4 && UP(x) && (null == e || 1 === e || 3 === e) && !oSet[x.id];
              }),
              snr = opp.concat(help).filter(function (x) {
                return UNU[x.id] || (x.k <= 4 && !REACH(x).length);
              });
            function OVL(xs, ys) {
              var m = {};
              ys.forEach(function (y) {
                m[y.id] = 1;
              });
              return xs.length
                ? xs.filter(function (x) {
                    return m[x.id];
                  }).length / xs.length
                : 1;
            }
            if (opp.length >= 2) {
              var tO = TEST(opp, 1),
                nO = (D.oppN || []).slice(0, 3),
                mO = ["Scale what already exists: " + Gt(gsmMeanList(nO.length ? nO : opp.slice(0, 3).map(NM))) + ".", "Ask the people doing it what they need to keep going, and to grow."];
              mO.push(tO.not.length ? "Add " + LS(tO.not, 3) + " to Q.7, so what you would reinforce builds on " + (1 === tO.not.length ? "it" : "them") + "." : "Set who does what and when, and repeat it.");
              mO.push("Check back that the acceptance holds: it doesn’t keep on its own.");
              var sO = MIX(opp);
              CARD({
                key: "seed|opp",
                seed: "opp",
                title: "The opportunity: " + gsmMeanList(nO.length ? nO : opp.slice(0, 3).map(NM)),
                from: "THE OPPORTUNITY (Pattern Analysis)",
                isS: sO,
                purp: "Much of the alternative already exists. Scaling it moves the goal further, for less energy, than inventing something new.",
                test: tO,
                why: sO ? "its notes reach from acceptance into the low ground, a high-risk move a program cannot plan for." : "it already stands on the high ground and nothing here asks it to cross, so a set sequence can carry it.",
                way: sO ? WAY(opp) : PWAY(opp),
                moves: mO,
                have: opp,
                items: opp,
              });
              PCARDS.push(opp);
              ROWS.move.push({ lab: "The opportunity", t: tO, title: "The opportunity" });
            }
            if (
              help.length >= 2 &&
              PCARDS.every(function (c) {
                return OVL(help, c) < 0.7;
              })
            ) {
              var tH = TEST(help, 1),
                q4 = help.some(function (x) {
                  return 4 === x.k;
                }),
                mH = ["Build on " + LS(help, 3) + " rather than starting over.", "Ask who is behind it, and what would help them do more of it."];
              tH.not.length && mH.push("Add " + LS(tH.not, 3) + " to Q.7, so what you would reinforce takes it up.");
              mH.push("Check back if circumstances change.");
              CARD({
                key: "seed|help",
                seed: "help",
                title: "What is already helping: " + gsmMeanList(help.slice(0, 3).map(NM)),
                from: "WHAT IS ALREADY HELPING (Pattern Analysis)",
                isS: 0,
                purp: "Part of the ground already helps the goal" + (q4 ? ", and part of what has to be true is already true" : "") + ". Building on it takes the least energy.",
                test: tH,
                why: "it already helps the goal and asks for no crossing, so a set sequence can carry it.",
                way: PWAY(help),
                moves: mH,
                have: help,
                items: help,
              });
              PCARDS.push(help);
              ROWS.move.push({ lab: "What is already helping", t: tH, title: "What is already helping" });
            }
            if (
              snr.length >= 2 &&
              PCARDS.every(function (c) {
                return OVL(snr, c) < 0.5;
              })
            ) {
              CARD({
                key: "seed|snr",
                seed: "snr",
                title: "Support not yet reinforced: " + gsmMeanList(snr.slice(0, 3).map(NM)),
                from: "SUPPORT NOT YET REINFORCED (Pattern Analysis)",
                isS: 0,
                purp: "This support already works, and nothing you would design builds on it yet. Left alone, it can slip.",
                test: TEST(snr, 1),
                why: "it already works; a set sequence of support can keep it going.",
                way: PWAY(snr),
                moves: ["Add " + LS(snr, 3) + " to Q.7: what needs to be reinforced.", "Ask the people behind it what would help them keep going.", "Set who does what and when, and repeat it.", "Check back that it holds."],
                have: snr,
                items: snr,
              });
            }
            In = HTML.join("") + In;
            // THE TEST
            if (!CARDS.length) return;
            var VL = function (t) {
                return t ? '<span class="tav tav-' + t.v.replace(" ", "") + '">' + t.v.toUpperCase() + "</span>" : "";
              },
              row = function (lab, body) {
                return '<div class="tatr"><div class="tatl">' + lab + "</div>" + body + "</div>";
              },
              hold = ROWS.hold
                .map(function (r) {
                  return "<div><i>" + r.lab + "</i> " + VL(r.t) + " " + (r.t.not.length ? "Not yet answered: " + LS(r.t.not, 3) + "." : "Answered.") + "</div>";
                })
                .join(""),
              move = ROWS.move
                .map(function (r) {
                  return "<div><i>" + r.lab + "</i> " + VL(r.t) + " " + (r.t.not.length ? "Not yet built on: " + LS(r.t.not, 3) + "." : "Built on.") + "</div>";
                })
                .join(""),
              tR = TEST(RIDGE, 0),
              shift = RIDGE.length
                ? "<div>" +
                  VL(tR) +
                  " The ridge of indifference runs through " +
                  LS(RIDGE, 4) +
                  ": " +
                  (tR.met.length ? "what you would design reaches " + LS(tR.met, 3) + (tR.not.length ? ", not yet " + LS(tR.not, 3) : "") + "." : "nothing you would design reaches it yet, and most crossings go through it.") +
                  "</div>"
                : "<div>" + VL({ v: "not yet" }) + " No note carries indifference, so there is no ridge on this ground yet: every crossing is a climb over bare rock. Ask who is for nothing yet.</div>",
              first = (function () {
                var pr = CARDS.filter(function (c) {
                    return !c.S;
                  })[0],
                  st = CARDS.filter(function (c) {
                    return c.S;
                  })[0];
                return pr && st
                  ? "Start with the program “" + Gt(pr.title) + "”: it stands on high ground and asks for no crossing. Then take up the strategy “" + Gt(st.title) + "”, crossing where it is cheapest, through the ridge."
                  : st
                    ? "Start with the strategy “" + Gt(st.title) + "”, crossing where it is cheapest, through the ridge."
                    : pr
                      ? "Start with the program “" + Gt(pr.title) + "”: it stands on high ground and asks for no crossing."
                      : "";
              })(),
              AK = C.asks || {},
              cons = [];
            C.m.concat((C.p && C.p.m) || []).forEach(function (r, i) {
              var x = r && r[8] ? String(AK["cons|" + r[8]] || "").trim() : "";
              if (!x) return;
              var pl = i >= C.m.length,
                k = pl ? i - C.m.length : i,
                inq = [3, 5, 6]
                  .filter(function (q) {
                    return String(C.a[q] || "").indexOf(x) >= 0;
                  })
                  .map(function (q) {
                    return "Q." + (q + 1);
                  });
              cons.push("<div>" + (pl ? "P" + (k + 1) : "note " + (k + 1)) + ": “" + Gt(x.length > 110 ? x.slice(0, 110) + "…" : x) + "” " + (inq.length ? '<span class="tav tav-yes">IN ' + inq.join(", ") + "</span>" : '<span class="tav tav-notyet">NOT YET IN Q.4, Q.6, OR Q.7</span>') + "</div>");
            });
            TAT =
              '<div class="tatst"><div class="tatq">THE TEST</div><div class="tatqq">Does what you would design change the conditions and invite the transitions the goal needs?</div><div class="tatsub">Read against your workbook. Each line points to the cards below that take it up.</div>' +
              (hold ? row("What holds it", hold) : "") +
              (move ? row("What already moves", move) : "") +
              row("Where it can shift", shift) +
              row("Where the reading splits", '<div class="tasplitrow">In Parallel found nothing that splits the reading of these cards.</div>') +
              (cons.length ? row("What holds it, as you named it", cons.join("")) : "") +
              (first ? row("The cheapest first move", "<div>" + first + "</div>") : "") +
              "</div>" +
              '<details class="fold tafields"><summary>WHAT EACH PART OF A CARD DOES</summary><div class="mtext"><ul class="glos">' +
              [
                ["IN SERVICE OF THE GOAL", "What the card is for, in your own words."],
                ["DOES WHAT YOU WOULD DESIGN MEET IT?", "The test on this card’s notes: which ones Q.5–Q.7 already reach, and which nothing reaches yet."],
                ["WHERE THE READING SPLITS", "What In Parallel found under this card’s notes, and what it means for how you act."],
                ["A strategy or a program", "Why the card is one or the other. The button switches it, and your choice is saved."],
                ["THE WAY ACROSS", "The order of the crossings on the ground of Pattern Synthesis: through the ridge of indifference before bare rock, with the cost of each move."],
                ["FIRST MOVES or THE SEQUENCE", "What to do first. Under the map it follows the way you choose."],
                ["THE WAY THROUGH IT", "The card’s ways drawn on the ground, and a chart comparing their effort, impact, benefit, and return."],
                ["WHAT HOLDS IT IN THE LOW GROUND", "Write the constraint or rule that keeps a note low. It is saved with the note and shows on every card that holds it; one tap adds it to Q.4, Q.6, or Q.7."],
                ["YOUR DECISION", "Keep, change, or drop the card, with a line on why. It is listed in WHAT YOU DECIDED AND WHY."],
                ["WHAT YOU DID", "Log what you did and what happened. The card’s notes, and any note whose constraint you named, are flagged on Mapping Landscape to check again: map, act, map again."],
              ]
                .map(function (f) {
                  return "<li><b>" + f[0] + ".</b> " + f[1] + "</li>";
                })
                .join("") +
              "</ul></div></details>";
          })();
'''
rep('''          var Xn = _n.concat(''', SEED + '''          var Xn = _n.concat(''')

# ro: the test after the opening note; the opening note now names where the cards come from
rep('''<b>Prompts, not findings.</b> Each card is built from a template and the words you used. Talk them through with the people involved, and change or drop any that do not fit.</div><div class="meta">Programs''',
    '''<b>Prompts, not findings.</b> Each card grows from what Pattern Analysis, Pattern Synthesis, and In Parallel found, or from the words you used. Talk them through with the people involved, and change or drop any that do not fit.</div>' + TAT + '<div class="meta">Programs''')

# ---------------------------------------------------------------- 5. constraints: one tap into Q.4, Q.6, or Q.7
rep('''                      '" rows="2" placeholder="The constraint or rule, and how to change it">' +
                      Gt(v) +
                      "</textarea></label></div>"''', '''                      '" rows="2" placeholder="The constraint or rule, and how to change it">' +
                      Gt(v) +
                      "</textarea></label>" +
                      gsmConsQ(key, v) +
                      "</div>"''')
rep('''                '<div class="csn" style="font-size:12.5px;color:#666">A change you name here is a condition (Q.4), a redesign (Q.6) or something to reinforce (Q.7). Add it there too, so the rest of the method sees it. After Juarrero (2023).</div></div>\'''',
    '''                '<div class="fhelp">Saved with the note and shown on every card that holds it. One tap adds it to Q.4, Q.6, or Q.7, so the rest of the method reads it (after Juarrero, 2023).</div></div>\'''')

rep('''    t.value.trim() ? (C.asks[k] = t.value) : delete C.asks[k];
    document.querySelectorAll("textarea[data-cons]").forEach(function (o) {
      o !== t && o.getAttribute("data-cons") === id && (o.value = t.value);
    });''', '''    t.value.trim() ? (C.asks[k] = t.value) : delete C.asks[k];
    document.querySelectorAll("textarea[data-cons]").forEach(function (o) {
      o !== t && o.getAttribute("data-cons") === id && (o.value = t.value);
    });
    document.querySelectorAll(".consq[data-cqfor]").forEach(function (q) {
      q.getAttribute("data-cqfor") === id && (q.outerHTML = gsmConsQ(id, t.value));
    });''')

HELP = r'''  function gsmConsQ(key, v) {
    v = String(v || "").trim();
    return (
      '<div class="consq" data-cqfor="' +
      Gt(key) +
      '"' +
      (v ? "" : ' style="display:none"') +
      ">Add it to " +
      [
        [3, "Q.4", "a condition to establish"],
        [5, "Q.6", "something to redesign"],
        [6, "Q.7", "something to reinforce"],
      ]
        .map(function (b) {
          var inq = v && String(C.a[b[0]] || "").indexOf(v) >= 0;
          return (
            '<button type="button" class="ech' +
            (inq ? " on" : "") +
            '" data-cq="' +
            b[0] +
            '" data-cqid="' +
            Gt(key) +
            '">' +
            (inq ? "In " + b[1] + " \u2713" : b[1] + " \u00b7 " + b[2]) +
            "</button>"
          );
        })
        .join("") +
      "</div>"
    );
  }
  document.addEventListener("click", function (ev) {
    var b = ev.target.closest && ev.target.closest("#gsm button[data-cq]");
    if (!b) return;
    ev.preventDefault();
    var id = b.getAttribute("data-cqid"),
      q = +b.getAttribute("data-cq"),
      tx = String((C.asks || {})["cons|" + id] || "").trim();
    if (!tx || !(q >= 0 && q < 7)) return;
    var cur = String(C.a[q] || "").replace(/\s+$/, "");
    cur.indexOf(tx) < 0 && (C.a[q] = (cur ? cur + "\n\n" : "") + tx);
    var qa = N.querySelector('.qa[data-i="' + q + '"]');
    if (qa) {
      var ta = qa.querySelector("textarea"),
        pa = qa.querySelector(".pa");
      ta && (ta.value = C.a[q]);
      pa && (pa.textContent = C.a[q]);
      qa.classList.add("has");
    }
    P();
  });
  function gsmTANorm(x) {
    x = String(x || "").trim();
    var m = /^(?:note\s*|N)(\d+)$/i.exec(x),
      pm = /^(?:place note\s*|P)(\d+)$/i.exec(x);
    return m ? "note " + m[1] : pm ? "P" + pm[1] : x;
  }
  function gsmTAIds(card) {
    var o = {};
    [].slice.call(card.querySelectorAll("[data-ids]")).concat([card]).forEach(function (el) {
      String(el.getAttribute("data-ids") || "")
        .split(",")
        .concat(String(el.getAttribute("data-seedids") || "").split(","))
        .forEach(function (x) {
          x = gsmTANorm(x);
          x && (o[x] = 1);
        });
    });
    return o;
  }
  function gsmCardCons(card) {
    var out = [],
      AK = C.asks || {};
    Object.keys(gsmTAIds(card)).forEach(function (x) {
      var m = /^note (\d+)$/.exec(x),
        pm = /^P(\d+)$/.exec(x),
        pl = !!pm,
        k = pm ? +pm[1] : m ? +m[1] : 0,
        r = k ? (pl ? C.p.m[k - 1] : C.m[k - 1]) : null;
      if (!r || !r[8]) return;
      var t = String(AK["cons|" + r[8]] || "").trim();
      t &&
        out.push({
          id: String(r[8]),
          lab: p(pl, k - 1),
          x: t,
          q: [3, 5, 6]
            .filter(function (i) {
              return String(C.a[i] || "").indexOf(t) >= 0;
            })
            .map(function (i) {
              return "Q." + (i + 1);
            }),
        });
    });
    return out;
  }
  function gsmTACss() {
    if (document.getElementById("gsm-ta-css")) return;
    var st = document.createElement("style");
    st.id = "gsm-ta-css";
    st.textContent =
      "#gsm .tatst{border:2px solid #111;background:#fff;padding:12px 18px 10px;margin:14px 0 18px}#gsm .tatq{font-size:12px;font-weight:700;letter-spacing:.16em;color:#444}#gsm .tatqq{font-size:19px;line-height:1.4;color:#111;margin:4px 0 4px}#gsm .tatsub{font-size:13px;color:#666;margin-bottom:8px}#gsm .tatr{border-top:1px solid #ddd;padding:8px 0 6px;font-size:15px;line-height:1.5}#gsm .tatr>div{margin:2px 0}#gsm .tatl{font-size:11.5px;font-weight:700;letter-spacing:.14em;color:#222;text-transform:uppercase}#gsm .tatr i{font-style:normal;font-weight:700}#gsm .tav{display:inline-block;font-size:10.5px;font-weight:700;letter-spacing:.1em;padding:1px 6px;border:1px solid #111;margin:0 2px;vertical-align:1px}#gsm .tav-yes{background:#111;color:#fff}#gsm .tav-partly{background:#fff;color:#111}#gsm .tav-notyet{background:#fff;color:#b22;border-color:#b22;border-style:dashed}#gsm .tagrp{margin:26px 0 10px;border-top:3px solid #111;padding-top:10px}#gsm .tagh{font-size:15px;font-weight:700;letter-spacing:.18em;color:#111}#gsm .tags{font-size:14px;color:#555;margin:2px 0 6px}#gsm .tagrp .meta{margin:6px 0 4px}#gsm .coa .tasplit .tspl{margin:0 0 6px}#gsm .tsk{font-size:11px;font-weight:700;letter-spacing:.1em;color:#555;margin-right:6px}#gsm .fhelp{font-size:12.5px;color:#666;line-height:1.4;margin:4px 0 2px}#gsm .consq{margin:4px 0 8px;font-size:13px;color:#444}#gsm .consq .ech{font-size:12.5px;margin:3px 4px 0 0}#gsm .actcons{font-size:13.5px;color:#333;margin:4px 0 6px;padding-left:9px;border-left:2px solid #ddd}#gsm .actcons b{font-size:11px;letter-spacing:.12em;color:#555}#gsm .coa[data-seed] .phctx{color:#888}";
    document.head.appendChild(st);
  }
  function gsmTASay(s) {
    var E = GSMEMO,
      k = s.k || {},
      w = s.names || [],
      q = function (x) {
        return "\u201c" + Gt(x) + "\u201d";
      },
      TR = [3, 0, 2, 1, 4];
    if ("TWO PEOPLE, TWO SIDES" === s.lab)
      return (
        q(w[0]) +
        " is read two ways: in the notes from " +
        Gt(gsmMeanList(k.vi || [])) +
        " it sits where things help, in the notes from " +
        Gt(gsmMeanList(k.va || [])) +
        " where things hinder. Plan a way in for each group, and test the wording with both before you act on it at scale." +
        (null != k.eu && null != k.ed && k.eu >= 0 && k.ed >= 0
          ? k.eu === k.ed
            ? " Both carry " + E[k.eu] + ", so agree on the direction first; neither side has to change how it feels."
            : 3 !== k.eu && 3 !== k.ed && Math.abs(TR[k.eu] - TR[k.ed]) >= 2
              ? " Their emotions sit far apart, with no ridge between them, so no single message will carry both."
              : ""
          : "")
      );
    if ("THE EMOTION CHANGES" === s.lab && k.emo) {
      var i = k.emo[0],
        a = k.emo[1];
      return TR[a] < TR[i]
        ? q(w[0]) + ": your plans carry " + E[a] + " where the situation still carries " + E[i] + ". Try the plan on the ground it will land on, small, before you scale it."
        : q(w[0]) + ": your plans carry " + E[a] + " where the situation carries " + E[i] + ". Reword what the actions ask of people, so the work doesn\u2019t stir resistance the situation doesn\u2019t hold.";
    }
    if ("ONE IDEA UNDER TWO NAMES" === s.lab)
      return (
        q(w[0]) +
        " and " +
        q(w[1] || "") +
        " never part in your workbook: act on them as one, since a move on one moves the other." +
        (s.su && s.sd
          ? " Both sides claim them: lead with them, ground the two sides already share."
          : s.sd
            ? " They sit only where things hinder: answer them directly, or the resistance stays."
            : s.su
              ? " They sit only where things help: build on them together."
              : "")
      );
    if ("PLACED ONE WAY, TIED THE OTHER" === s.lab) {
      var n = String((k.notes || [])[0] || "").replace(/^(?:place )?note (\d+)/, "N$1"),
        pe = null != k.pe ? k.pe : -1,
        pt = null != k.pt ? k.pt : -1,
        low = [0, 2, 4].indexOf(pe) >= 0;
      return !k.up && low && (1 === pt || 3 === pt)
        ? Gt(n) + " sits in the low ground but speaks the language of the high ground: use it as a foothold for the crossing."
        : pe >= 0 && pe === pt
          ? Gt(n) + " carries the same " + E[pe] + " as what it is tied to, pointed the other way: redirect it toward the goal rather than overcome it."
          : k.up && [0, 2, 4].indexOf(pt) >= 0
            ? Gt(n) + " looks like help but is tied to " + E[pt] + ": check it before this card leans on it."
            : Gt(n) + "\u2019s place and ties disagree: check which is right before this card relies on it.";
    }
    return "";
  }
  function gsmTAPass(Rt, tries) {
    if (!Rt) return;
    gsmTACss();
    var kids = [].slice.call(Rt.children),
      pi = -1;
    kids.forEach(function (k, i) {
      k.classList.contains("part") && /COURSES OF ACTION/.test(k.textContent) && (pi = i);
    });
    if (pi < 0) return;
    var region = [];
    for (var i = pi + 1; i < kids.length && !kids[i].classList.contains("part"); i++) region.push(kids[i]);
    var cards = region.filter(function (c) {
      return c.classList.contains("coa");
    });
    if (!cards.length || Rt.querySelector(".tagrp")) return;
    var SP = window.gsmSplit;
    if (!SP && (tries || 0) < 8)
      return void setTimeout(function () {
        try {
          gsmTAPass(Rt, (tries || 0) + 1);
        } catch (e) {}
      }, 150);
    SP = SP || [];
    // split readings onto the cards they touch
    var trip = [],
      tl = function (c) {
        var b = c.querySelector(".hd b");
        return b ? b.textContent : "";
      };
    cards.forEach(function (c, ci) {
      var ids = gsmTAIds(c),
        tt = tl(c).toLowerCase();
      SP.forEach(function (sp, si) {
        var n = sp.ids.filter(function (x) {
            return ids[gsmTANorm(x)];
          }).length,
          tw = (sp.names || []).some(function (w) {
            w = String(w || "").toLowerCase();
            return w.length > 3 && tt.indexOf(w.slice(0, Math.min(6, w.length))) >= 0;
          }),
          need = "PLACED ONE WAY, TIED THE OTHER" === sp.lab ? 1 : 2,
          sc = n + (tw ? 3 : 0);
        sc >= need && trip.push({ c: ci, s: si, sc: sc });
      });
    });
    trip.sort(function (x, y) {
      return y.sc - x.sc;
    });
    var perC = {},
      perS = {};
    trip.forEach(function (t) {
      (perC[t.c] || []).length < 2 && (perS[t.s] || []).length < 2 && ((perC[t.c] = perC[t.c] || []).push(t.s), (perS[t.s] = perS[t.s] || []).push(t.c));
    });
    Object.keys(perC).forEach(function (ci) {
      var c = cards[ci],
        bd = c.querySelector(".bd"),
        h = perC[ci]
          .map(function (si) {
            var t = gsmTASay(SP[si]);
            return t ? '<div class="tspl"><span class="tsk">' + SP[si].lab + "</span> " + t + "</div>" : "";
          })
          .join("");
      if (!bd || !h) return;
      var d = document.createElement("div");
      d.className = "csec tasplit";
      d.innerHTML = '<div class="csl">WHERE THE READING SPLITS</div><div class="csn">' + h + '</div>';
      var at = bd.querySelector(".tatest") || bd.querySelector(".why") || bd.querySelector(".purp");
      at ? at.parentNode.insertBefore(d, at.nextSibling) : bd.insertBefore(d, bd.firstChild);
    });
    var sr = Rt.querySelector(".tasplitrow");
    sr &&
      SP.length &&
      (sr.outerHTML = SP.slice(0, 6)
        .map(function (sp, si) {
          var on = (perS[si] || []).map(function (ci) {
            return "\u201c" + Gt(tl(cards[ci]).replace(/:.*$/, "")) + "\u201d";
          });
          return (
            '<div><span class="tsk">' +
            sp.lab +
            "</span> " +
            (sp.names[0] ? "\u201c" + Gt(sp.names.slice(0, 2).join("\u201d and \u201c")) + "\u201d" : Gt(String((sp.k.notes || [])[0] || "").replace(/^(?:place )?note (\d+)/, "N$1"))) +
            (on.length ? ": carried onto " + gsmMeanList(on) + "." : ": no card takes it up yet. " + gsmTASay(sp)) +
            "</div>"
          );
        })
        .join(""));
    // group strategies and programs
    var isS = function (c) {
        var m = c.querySelector(".hd .mode");
        return !!m && /STRATEGY/.test(m.textContent);
      },
      ord = function (a) {
        return a
          .map(function (c, i) {
            return { c: c, i: i, s: c.hasAttribute("data-seed") ? 0 : 1 };
          })
          .sort(function (x, y) {
            return x.s - y.s || x.i - y.i;
          })
          .map(function (x) {
            return x.c;
          });
      },
      st = ord(cards.filter(isS)),
      pr = ord(
        cards.filter(function (c) {
          return !isS(c);
        }),
      ),
      metas = region.filter(function (c) {
        return c.classList.contains("meta");
      }),
      mS = metas.filter(function (m) {
        return /^Strategies work best/.test(m.textContent.trim());
      })[0],
      mP = metas.filter(function (m) {
        return /^Programs work best/.test(m.textContent.trim());
      })[0],
      ph = document.createElement("div");
    cards[0].parentNode.insertBefore(ph, cards[0]);
    var keep = function (c) {
      if (c.hasAttribute("data-seed") || c.hasAttribute("data-ground") || c.querySelector('.gsmmode[data-mv=""]')) return !0;
      var k = ae(c),
        d = ie()[k];
      if (d && null != d.d) return !0;
      if (
        (C.acts || []).some(function (x) {
          return x && x.k === k;
        })
      )
        return !0;
      var ws = window.gsmWS && String(window.gsmWS.h || "").replace(/<[^>]*>/g, "");
      return !!ws && ws === (c.querySelector(".hd b") || {}).textContent;
    };
    function grp(lab, sub, meta, list) {
      if (!list.length) return;
      var d = document.createElement("div");
      d.className = "tagrp";
      d.innerHTML = '<div class="tagh">' + lab + '</div><div class="tags">' + sub + "</div>";
      meta && d.appendChild(meta);
      ph.parentNode.insertBefore(d, ph);
      var more = list.filter(function (c) {
        return !keep(c);
      });
      list.forEach(function (c) {
        more.indexOf(c) < 0 && ph.parentNode.insertBefore(c, ph);
      });
      if (!more.length) return;
      var f = document.createElement("details");
      f.className = "fold tamore";
      f.innerHTML = "<summary>MORE " + lab + ", FROM THE WORDS YOU USE</summary><div class=\"fhelp\">Built from words and phrases that recur in your workbook. They overlap with the cards above; open them for a word\u2019s own course of action.</div>";
      more.forEach(function (c) {
        f.appendChild(c);
      });
      ph.parentNode.insertBefore(f, ph);
    }
    grp("STRATEGIES", "For what holds the goal back and where it has to cross: ground that is not settled.", mS, st);
    grp("PROGRAMS", "For what already moves toward the goal: ground settled enough to set a sequence.", mP, pr);
    ph.parentNode.removeChild(ph);
    window.gsmTAV = (window.gsmTAV || 0) + 1;
  }
'''
rep('''  function gsmActUI(card, key, bd) {''', HELP + '''  function gsmActUI(card, key, bd) {''')

# ---------------------------------------------------------------- 6. WHAT YOU DID carries the constraints; re-map flags their notes
rep('''    Array.isArray(C.acts) || (C.acts = []);
    var w = document.createElement("div");
    w.className = "acted";''', '''    Array.isArray(C.acts) || (C.acts = []);
    var w = document.createElement("div"),
      cs0 = gsmCardCons(card);
    w.className = "acted";''')
rep('''            Gt(a.x) +
            (a.l && a.l.length ? '<br><span class="ad">Flagged to check on the map: ' + Gt(a.l.join(", ")) + "</span>" : "") +''', '''            Gt(a.x) +
            (a.c && a.c.length
              ? '<br><span class="ad">What holds it, as you named it: ' +
                a.c
                  .map(function (c) {
                    return Gt(c.lab) + " \u201c" + Gt(String(c.x).slice(0, 80)) + "\u201d";
                  })
                  .join("; ") +
                "</span>"
              : "") +
            (a.l && a.l.length ? '<br><span class="ad">Flagged to check on the map: ' + Gt(a.l.join(", ")) + "</span>" : "") +''')
rep('''        .join("") +
      '<textarea class="actx" rows="2" maxlength="600" placeholder="What you did, and what happened" aria-label="What you did, and what happened"></textarea><button type="button" class="ech actgo">Log it</button><div class="actmsg" style="font-size:13px;color:#555;margin-top:6px"></div>';''', '''        .join("") +
      (cs0.length
        ? '<div class="actcons"><b>WHAT HOLDS IT, AS YOU NAMED IT</b>' +
          cs0
            .map(function (c) {
              return "<div>" + Gt(c.lab) + ": \u201c" + Gt(c.x.length > 140 ? c.x.slice(0, 140) + "\u2026" : c.x) + "\u201d" + (c.q.length ? ' <span class="ad">(in ' + c.q.join(", ") + ")</span>" : "") + "</div>";
            })
            .join("") +
          "</div>"
        : "") +
      '<textarea class="actx" rows="2" maxlength="600" placeholder="What you did, and what happened" aria-label="What you did, and what happened"></textarea><button type="button" class="ech actgo">Log it</button><div class="actmsg" style="font-size:13px;color:#555;margin-top:6px"></div><div class="fhelp">Saved with the date. This card\u2019s notes are flagged on Mapping Landscape to map again.</div>';''')
rep('''      var now = new Date().toISOString(),
        fl = gsmCardQ14(card);
      C.acts.push({ k: key, t: now, w: (C.who || "").trim(), x: tx, n: fl.map(function (f) { return f.id; }), l: fl.map(function (f) { return f.lab; }) });''', '''      var now = new Date().toISOString(),
        fl = gsmCardQ14(card),
        cs = gsmCardCons(card);
      cs.forEach(function (c) {
        fl.some(function (f) {
          return f.id === c.id;
        }) || fl.push({ id: c.id, lab: c.lab });
      });
      C.acts.push({
        k: key,
        t: now,
        w: (C.who || "").trim(),
        x: tx,
        n: fl.map(function (f) { return f.id; }),
        l: fl.map(function (f) { return f.lab; }),
        c: cs.map(function (c) {
          return { id: c.id, lab: c.lab, x: c.x };
        }),
      });''')
rep('''        ? "Logged. " + fl.map(function (f) { return f.lab; }).join(", ") + " (Q.1\\u2013Q.4) are flagged on Mapping Landscape: check whether their emotion or place has changed, then read Pattern Synthesis again."''',
    '''        ? "Logged. " + fl.map(function (f) { return f.lab; }).join(", ") + " are flagged on Mapping Landscape: check whether their emotion or place has changed, then read Pattern Synthesis again."''')
rep('''            Gt(t.length > 70 ? t.slice(0, 70) + "\\u2026" : t) +
            '<button type="button" class="lnk sm" data-sd="' +''', '''            Gt(t.length > 70 ? t.slice(0, 70) + "\\u2026" : t) +
            (function (cx) {
              cx = String(cx || "").trim();
              return cx ? '<br><span style="color:#666;font-size:13px">What holds it, as you named it: \\u201c' + Gt(cx.length > 90 ? cx.slice(0, 90) + "\\u2026" : cx) + "\\u201d</span>" : "";
            })((C.asks || {})["cons|" + id]) +
            '<button type="button" class="lnk sm" data-sd="' +''')

# ---------------------------------------------------------------- 7. decision field help; run the pass after the cards are wired
rep(''''<input type="text" class="dwhy" maxlength="160" placeholder="Why, in a line" aria-label="Why">'));''', ''''<input type="text" class="dwhy" maxlength="160" placeholder="Why, in a line" aria-label="Why"><div class="fhelp">Listed in WHAT YOU DECIDED AND WHY, at the end of the page.</div>'));''')
rep('''                    n.appendChild(i),
                    gsmActUI(e, o, n));
                }
              }),
              se());''', '''                    n.appendChild(i),
                    gsmActUI(e, o, n));
                }
              }),
              se(),
              setTimeout(function () {
                try {
                  gsmTAPass(Rt);
                } catch (e) {}
              }, 0));''')

# ---------------------------------------------------------------- 8. the chart, shown openly
rep('''      d.className = "gtchart";''', '''      d.className = "gtchart";
      d.open = !0;''')
rep('''      sm.textContent = "COMPARE THE WAYS IN A CHART";''', '''      sm.textContent = "THE WAYS COMPARED";''')

rep('''                      '<div class="coa"><div class="hd"><b>' +
                      Gt(em.charAt(0)''', '''                      '<div class="coa" data-ground="1"><div class="hd"><b>' +
                      Gt(em.charAt(0)''')
rep('''t.textContent = "v225"''', '''t.textContent = "v226"''')
open(P, "w").write(s)
print("ok")
