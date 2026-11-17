"""v173 batch 3: N1 YOUR STORY SO FAR as a story; N2 BIGGEST GAP as a sentence; story paragraph cleanup."""
import sys
P = sys.argv[1]
s = open(P).read()


def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, (c, n, a[:90])
    s = s.replace(a, b)


STORY = r'''
            function SY() {
              var EN = ["aggression", "acceptance", "distrust", "indifference", "defiance"],
                FR = (window.gsmFR && window.gsmFR.it) || {},
                MED = window.gsmMED || {},
                live = notes.filter(function (o) {
                  return String(o.r[3] || "").trim();
                });
              function ids(L, k) {
                var a = L.map(function (o) {
                  return o.lab;
                });
                k = k || 6;
                return a.length > k ? a.slice(0, k).join(", ") + " and " + (a.length - k) + " more" : and(a);
              }
              function and(a) {
                return a.length > 1 ? a.slice(0, -1).join(", ") + " and " + a[a.length - 1] : a[0] || "";
              }
              function q(L) {
                return and(
                  L.map(function (t) {
                    return "“" + Gt(jt(t)) + "”";
                  }),
                );
              }
              function emo(L) {
                var c = [0, 0, 0, 0, 0],
                  n = 0;
                L.forEach(function (o) {
                  null != o.r[5] && (c[o.r[5]]++, n++);
                });
                var ord = [0, 1, 2, 3, 4]
                  .filter(function (k) {
                    return c[k];
                  })
                  .sort(function (a, b) {
                    return c[b] - c[a];
                  });
                return { c: c, n: n, ord: ord };
              }
              function byQ(k) {
                return live.filter(function (o) {
                  return k.indexOf(o.r[0]) >= 0;
                });
              }
              function P0(h, body) {
                return body ? '<div class="csl" style="margin-top:14px">' + h + "</div><p>" + body + "</p>" : "";
              }
              var out = "",
                mk = Object.keys(MED).sort(function (a, b) {
                  return MED[b].n - MED[a].n;
                })[0];
              /* opening: what the workbook turns on */
              if (mk) {
                var M = MED[mk],
                  sides = { 1: [], "-1": [], 0: [] };
                M.subs
                  .slice()
                  .sort(function (a, b) {
                    return M.cnt[b] - M.cnt[a];
                  })
                  .forEach(function (b) {
                    var up = 0,
                      dn = 0;
                    live.forEach(function (o) {
                      var t = (o.tk = o.tk || Ht(o.r[3])).b;
                      t[b] && (o.r[2] < 118 ? up++ : dn++);
                    });
                    sides[up > dn ? 1 : dn > up ? -1 : 0].push(b);
                  });
                out +=
                  "<p>Your workbook turns on <b>“" +
                  Gt(jt(mk)) +
                  "”</b>. It runs through " +
                  M.n +
                  " of your " +
                  M.of +
                  " answers and notes, so the word alone tells you little. What tells you something is the company it keeps." +
                  (sides[1].length ? " Where your notes help the goal, it is " + q(sides[1].slice(0, 3)) + "." : "") +
                  (sides[-1].length
                    ? " Where they hinder it, it is " + q(sides[-1].slice(0, 3)) + "."
                    : "") +
                  (sides[1].length && sides[-1].length
                    ? " The same word is doing two jobs, and the line between them is the line your work has to draw for other people."
                    : "") +
                  "</p>";
              }
              /* what stands in the way */
              var OP = byQ([2]),
                E = emo(OP),
                hard = E.c[0] + E.c[4],
                s1 = "";
              if (OP.length) {
                s1 =
                  "You name " +
                  OP.length +
                  " thing" +
                  (OP.length > 1 ? "s" : "") +
                  " that stand" +
                  (OP.length > 1 ? "" : "s") +
                  " in the way (" +
                  ids(OP) +
                  ").";
                if (E.n && hard * 2 >= E.n)
                  s1 +=
                    " Most of them carry aggression or defiance (" +
                    hard +
                    " of " +
                    E.n +
                    "), the two emotions Vigneaux (2026) places furthest from taking up a new idea. Opposition held in these emotions is rarely argued out of its position; it moves, if at all, when people see something done that fits what they already value. That is the case for starting with behaviors rather than with persuasion.";
                else if (E.n && E.ord[0] === 2)
                  s1 +=
                    " Most of them carry distrust (" +
                    E.c[2] +
                    " of " +
                    E.n +
                    "). Distrust is about who is speaking more than what is said, so small commitments kept in plain view are likely to do more than a better argument.";
                else if (E.n && E.ord[0] === 3)
                  s1 +=
                    " Most of them carry indifference (" +
                    E.c[3] +
                    " of " +
                    E.n +
                    "): people not yet for or against. That is the most movable ground there is, and the least stable, because it can tip either way.";
                var VO = {};
                OP.forEach(function (o) {
                  var v = o.r[7];
                  v && null != o.r[5] && ((VO[v] = VO[v] || [0, 0, 0, 0, 0])[o.r[5]]++);
                });
                var vk = Object.keys(VO);
                if (vk.length > 1) {
                  var lean = vk.map(function (v) {
                    var c = VO[v],
                      m = 0;
                    c.forEach(function (x, k) {
                      x > c[m] && (m = k);
                    });
                    return [v, m];
                  });
                  lean[0][1] !== lean[1][1] &&
                    (s1 +=
                      " The resistance does not look the same from every side: in the notes from " +
                      Gt(lean[0][0]) +
                      " it leans " +
                      EN[lean[0][1]] +
                      ", in the notes from " +
                      Gt(lean[1][0]) +
                      " it leans " +
                      EN[lean[1][1]] +
                      ". What answers one may not reach the other.");
                }
              }
              out += P0("WHAT STANDS IN THE WAY", s1);
              /* what is already helping */
              var SU = byQ([3]),
                s2 = "";
              if (SU.length) {
                s2 =
                  SU.length +
                  " note" +
                  (SU.length > 1 ? "s name" : " names") +
                  " support already there (" +
                  ids(SU) +
                  ").";
                OP.length >= 2 * SU.length &&
                  (s2 +=
                    " That is " +
                    OP.length +
                    " things against the goal to " +
                    SU.length +
                    " for it. The map may be weighted toward what is wrong because that is how things are, or because that is where you have looked; it is worth asking who else could name what is working.");
                (FR.unused || []).length &&
                  (s2 +=
                    " " +
                    q(FR.unused.slice(0, 3)) +
                    " " +
                    (FR.unused.length > 1 ? "are" : "is") +
                    " support already at work that nothing you would design, redesign or reinforce draws on yet. Support that nothing opposes and nothing yet builds on is the least costly place to begin.");
              } else if (OP.length)
                s2 =
                  "No note yet names what is already working for the goal. Without it, every move has to start from nothing.";
              out += P0("WHAT IS ALREADY HELPING", s2);
              /* what has to be true */
              var CO = byQ([4]),
                s3 = "";
              CO.length
                ? (s3 =
                    CO.length +
                    " note" +
                    (CO.length > 1 ? "s say" : " says") +
                    " what has to be true for the goal to take root (" +
                    ids(CO) +
                    "). Each one is a test the actions in Q.5–Q.7 will have to pass.")
                : (s3 =
                    "No note yet says what has to be true for the goal to take root. Q.4 is one of the two leading questions: without it, there is nothing to hold the actions up against.");
              out += P0("WHAT HAS TO BE TRUE", s3);
              /* what you would do */
              var D5 = byQ([5]),
                D6 = byQ([6]),
                D7 = byQ([7]),
                AC = D5.concat(D6, D7),
                s4 = "",
                un = FR.unanswered || [],
                an = FR.answered || [];
              if (AC.length) {
                var big = [
                  [D5.length, "design something new (Q.5)"],
                  [D6.length, "change what already exists (Q.6)"],
                  [D7.length, "strengthen what already works (Q.7)"],
                ].sort(function (a, b) {
                  return b[0] - a[0];
                });
                s4 =
                  AC.length +
                  " note" +
                  (AC.length > 1 ? "s say" : " says") +
                  " what you would do (" +
                  ids(AC) +
                  "). Most of it would " +
                  big[0][1] +
                  ".";
                un.length + an.length &&
                  (s4 +=
                    " Of the words and phrases you use for causes, opposition and conditions, " +
                    an.length +
                    " also turn up in what you would do and " +
                    un.length +
                    " do not" +
                    (un.length ? ", among them " + q(un.slice(0, 3)) : "") +
                    "." +
                    (un.length > an.length
                      ? " So far, your plan reaches less of the problem than the problem holds."
                      : ""));
              }
              out += P0("WHAT YOU WOULD DO", s4);
              var W = window.gsmWS;
              out += P0(
                "WHERE TO START",
                W
                  ? "Taking Action puts " +
                      W.h +
                      " first, as " +
                      (W.st ? "a strategy" : "a program") +
                      ": it shares notes with more of the other courses of action than any other, so what you decide about it carries furthest."
                  : "",
              );
              var U = NR.u;
              out += P0(
                "NOT YET ANSWERED",
                U.length
                  ? and(
                      U.map(function (u) {
                        return u.lab;
                      }),
                    ) +
                      (U.length > 1 ? " hinder" : " hinders") +
                      " the goal, and nothing in Q.5–Q.7 or in your design, redesign and reinforce notes responds to " +
                      (U.length > 1 ? "them" : "it") +
                      " yet. Left as they are, these are where things push back first."
                  : "",
              );
              return out;
            }
'''

rep('''            function sec(l, h) {
              return h ? '<div class="csl" style="margin-top:14px">' + l + "</div>" + h : "";
            }
            return (
              '<details class="fold" open><summary>YOUR STORY SO FAR</summary><div class="mtext"><p>Your answers and notes in the order the method asks them, each in your own words. This only puts them in order; it does not say what they mean. A note is shown as answered only where you said so or drew the link.</p>' +
              sec("THE GOAL", '<div style="margin:4px 0">“' + Gt(g1) + "”</div>") +''',
    '''            function sec(l, h) {
              return h ? '<div class="csl" style="margin-top:14px">' + l + "</div>" + h : "";
            }''' + STORY + '''
            return (
              '<details class="fold" open><summary>YOUR STORY SO FAR</summary><div class="mtext">' +
              SY() +
              '<details class="more"><summary>Your own words, in the order the method asks for them</summary><p>This only puts them in order; it does not say what they mean. A note is shown as answered only where you said so or drew the link.</p>' +
              sec("THE GOAL", '<div style="margin:4px 0">“' + Gt(g1) + "”</div>") +''')
rep('''              sec("NOT YET ANSWERED", h7) +
              "</div></details>"''', '''              sec("NOT YET ANSWERED", h7) +
              "</details></div></details>"''')

# WHAT YOUR USE OF THE BEAR CANYON METHOD PRODUCED: no recurrence count; sentences start with a capital
rep('''          (de.length && kn.push(Cn + " of the " + de.length + " recurring words and phrases are in Q.5–Q.7."),
            kn.length > 1 &&''', '''          ((kn = kn.map(function (t) {
            return t.replace(/^(<[^>]*>)?([a-z])/, function (m, a, b) {
              return (a || "") + b.toUpperCase();
            });
          })),
            kn.length > 1 &&''')

# N2: BIGGEST GAP at a glance reads as one sentence about the gap, not a word list
rep('''                d && o.push(["BIGGEST GAP", d.textContent, d]),''', '''                d &&
                  o.push([
                    "BIGGEST GAP",
                    (function () {
                      var U = ((window.gsmFR && window.gsmFR.it) || {}).unanswered || [];
                      return U.length
                        ? U.length +
                            " words and phrases you use for what stands in the way have nothing designed, redesigned or reinforced for them yet. The first is “" +
                            jt(U[0]) +
                            "”" +
                            (U[1] ? ", then “" + jt(U[1]) + "”" : "") +
                            ". Tap to see them all."
                        : d.textContent;
                    })(),
                    d,
                  ]),''')
open(P, "w").write(s)
print("batch3 ok")
