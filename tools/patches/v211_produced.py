"""v211: review 3d, WHAT YOUR USE OF THE METHOD PRODUCED deepened (Pattern Analysis, top of the page).
1. Bigger themes: phrases (never lone words) that turn up in the same notes are read as one bigger theme (they
   share at least 2 notes and half of the smaller one's; answers are left out, because a long answer holds everything). Each says where they meet, which side of the line,
   which emotions the notes there carry, and whether the theme reaches what you would design (Q.5-Q.7) or stays
   in the context you have grasped (Q.1-Q.4).
2. The findings that were lone words ("tradition and measures") are named by their phrase, or else by quoting the shortest
   note (5 to 16 words) that uses the word itself; a finding with neither is left out.
3. It ends by leading into YOUR LANDSCAPE, just below: which of these notes sit in the low ground and which on
   the high ground.
4. Paragraphs instead of one block.
Wording is Claude's. Usage: python3 v211_produced.py gsm-readable.js   (the relief is unchanged; --relief is a no-op)"""
import sys

P = sys.argv[1]
if "--relief" in sys.argv:
    sys.exit(0)
s = open(P).read()

A = "          var Ln = [];\n          if (\n            (de"
Z = '                "</div>"));\n        }\n        var In = "",'
i, j = s.index(A), s.index(Z)
assert s.count(A) == 1 and s.count(Z) == 1 and i < j
NEW = r'''          var PD = window.gsmData ? window.gsmData() : { m: [] },
            EMN = function (id) {
              var r = /^N\d+$/.test(id) ? PD.m[+id.slice(1) - 1] : null;
              return r && null != r[5] ? r[5] : null;
            },
            QOF = function (id) {
              var m = /^Q\.(\d)$/.exec(id);
              if (m) return +m[1];
              var r = /^N\d+$/.test(id) ? PD.m[+id.slice(1) - 1] : null;
              return r ? r[0] : null;
            },
            SRC = function (t) {
              var st = String(t).split(" ");
              return phKeep(function () {
                return phAll()
                  .filter(function (x) {
                    return "goal" !== x.src && phIn(st, x.t);
                  })
                  .map(function (x) {
                    return x.src;
                  });
              });
            },
            NM = function (t) {
              /* never a lone word: the repeated phrase, else the shortest note that uses the word itself, quoted */
              var m = gsmPhName(t);
              if (m.multi) return m.ph;
              var w = jt(t),
                re = new RegExp("\\b" + String(w).replace(/[^\w ]/g, "") + "\\b", "i"),
                c = null;
              phAll()
                .filter(function (x) {
                  var n = String(x.t).trim().split(/\s+/).length;
                  return /^N/.test(x.src) && re.test(x.t) && n >= 5 && n <= 16;
                })
                .sort(function (a, b) {
                  return a.t.length - b.t.length;
                })
                .slice(0, 1)
                .forEach(function (x) {
                  c = "“" + String(x.t).trim().replace(/[.\s]+$/, "") + "” (" + x.src + ")";
                });
              return c;
            },
            B = function (x) {
              return "<b>" + Gt(x) + "</b>";
            },
            NL = function (a) {
              a = a.slice().sort(function (x, y) {
                return (/^Q/.test(x) ? 0 : 1e3) + +x.replace(/\D/g, "") - ((/^Q/.test(y) ? 0 : 1e3) + +y.replace(/\D/g, ""));
              });
              return a.length > 4 ? a.slice(0, 4).join(", ") + ", and " + (a.length - 4) + " more" : phList(a);
            },
            EMS = function (ids) {
              var c = {};
              ids.forEach(function (id) {
                var e = EMN(id);
                null != e && (c[e] = (c[e] || 0) + 1);
              });
              return Object.keys(c)
                .sort(function (a, b) {
                  return c[b] - c[a];
                })
                .slice(0, 2)
                .map(function (e) {
                  return o[e][0].toLowerCase();
                });
            },
            PARA = [],
            KG = kn.length;
          KG && PARA.push(kn[0]);
          /* 1: bigger themes, from phrases that turn up in the same answers and notes */
          var TH = [],
            seenPh = {};
          de.slice(0, 24).forEach(function (t) {
            var nm = NM(t);
            if (!nm || seenPh[nm.toLowerCase()]) return;
            var sr = SRC(t),
              ns = sr.filter(function (id) {
                return /^N/.test(id);
              });
            /* only repeated phrases make bigger themes; notes with the same text count once */
            var tx = {};
            ns = ns.filter(function (id) {
              var r = PD.m[+id.slice(1) - 1],
                k = r ? String(r[3]).trim().toLowerCase().replace(/\W+/g, " ").slice(0, 60) : id;
              return tx[k] ? !1 : (tx[k] = 1);
            });
            if (ns.length < 2 || /^“/.test(nm)) return;
            seenPh[nm.toLowerCase()] = 1;
            TH.push({ t: t, nm: nm, s: sr, n: ns, g: ge[t] });
          });
          var BIG = [];
          TH.forEach(function (x) {
            var hit = null;
            BIG.some(function (G) {
              var ov = x.n.filter(function (id) {
                return G.sh.indexOf(id) >= 0;
              }).length;
              return ov >= 2 && ov / Math.min(x.n.length, G.sh.length) >= 0.5 && (hit = G);
            });
            if (hit && hit.m.length < 3) {
              hit.m.push(x);
              hit.sh = hit.sh.filter(function (id) {
                return x.n.indexOf(id) >= 0;
              });
            } else BIG.push({ m: [x], sh: x.n.slice() });
          });
          var BG = BIG.filter(function (G) {
              return G.m.length > 1;
            }).slice(0, 3),
            seenN = {},
            LOW = [],
            HIGH = [];
          function seeNotes(ids) {
            ids.forEach(function (id) {
              if (!/^N/.test(id) || seenN[id]) return;
              seenN[id] = 1;
              var e = EMN(id);
              1 === e ? HIGH.push(id) : 0 === e || 2 === e || 4 === e ? LOW.push(id) : 0;
            });
          }
          if (BG.length) {
            var bs = BG.map(function (G) {
              var up = G.m.some(function (x) {
                  return x.g.up;
                }),
                dn = G.m.some(function (x) {
                  return x.g.dn;
                }),
                em = EMS(G.sh),
                des =
                  G.sh.some(function (id) {
                    return QOF(id) >= 5;
                  }) ||
                  G.m.every(function (x) {
                    return x.s.some(function (id) {
                      return QOF(id) >= 5;
                    });
                  });
              seeNotes(G.sh);
              return (
                phList(
                  G.m.map(function (x) {
                    return B(x.nm);
                  }),
                ).replace(/^(<b>)?([a-z])/, function (m, a, b) {
                  return (a || "") + b.toUpperCase();
                }) +
                " turn up together, in " +
                NL(G.sh) +
                ": one bigger theme" +
                (up && dn ? ", written both for and against the goal" : dn ? ", holding the goal back" : up ? ", helping it" : "") +
                (em.length ? ", and its notes carry " + phList(em) : "") +
                ". " +
                (des
                  ? "It reaches what you would design."
                  : "It stays in the context you have grasped; nothing you would design takes it up yet.")
              );
            });
            PARA.push(
              "Your answers and notes gather into " +
                (1 === BG.length ? "one bigger theme" : ["", "", "two", "three"][BG.length] + " bigger themes") +
                ". " +
                bs.join(" "),
            );
          }
          /* 2: the findings, named by their phrases */
          var Ln = [],
            LnN = null,
            LnI = -1;
          if (
            (de'''
s = s[:i] + NEW + s[i + len(A):]

rep_pairs = [
    (
        """            kn.push(
              "What hinders moving toward the goal gathers around " +
                Ln.map(Tn).join(" and ") +""",
        """            LnN = Ln.map(NM).filter(Boolean);
            LnN.length &&
            ((LnI = kn.length), 1) &&
            kn.push(
              "What holds the goal back gathers around " +
                phList(LnN.map(B)) +""",
    ),
    (
        """                  ? ", and " + (Ln.length > 1 ? "both carry " : "it carries ") + o[bt][0].toLowerCase()""",
        """                  ? ", and " + (LnN.length > 1 ? "both carry " : "it carries ") + o[bt][0].toLowerCase()""",
    ),
    (
        """          On &&
            kn.push(
              Tn(On) +""",
        """          Ln.forEach(function (t) {
            seeNotes(SRC(t));
          });
          On && NM(On) && seeNotes(SRC(On));
          On &&
            NM(On) &&
            kn.push(
              B(NM(On)) +""",
    ),
    (
        """            An !== On &&
            kn.push(Tn(An) + " is already supported or happening and is in Q.5–Q.7: a strength to build on.");""",
        """            An !== On &&
            NM(An) &&
            (seeNotes(SRC(An)),
            kn.push(B(NM(An)) + " is already supported or happening, and you would build on it: a strength to start from."));""",
    ),
    (
        """          Nn &&
            kn.push(
              Tn(Nn) +
                " keeps coming up" +
                ("condition" === ge[Nn].c ? " as a condition" : "") +
                ", but nothing yet designs it.",
            );""",
        """          Nn && NM(Nn) && LnN && LnN.indexOf(NM(Nn)) >= 0 && LnI >= 0
            ? (kn[LnI] +=
                " " +
                (LnN.length > 1
                  ? B(NM(Nn)).replace(/^<b>([a-z])/, function (m, a) {
                      return "<b>" + a.toUpperCase();
                    })
                  : "It") +
                " keeps coming up" +
                ("condition" === ge[Nn].c ? " as a condition" : "") +
                ", but nothing you would design takes it up yet.")
            : Nn &&
            NM(Nn) &&
            kn.push(
              B(NM(Nn)) +
                " keeps coming up" +
                ("condition" === ge[Nn].c ? " as a condition" : "") +
                ", but nothing you would design takes it up yet.",
            );""",
    ),
    (
        """            kn.length > 1 &&
              (we =
                '<div class="plab">WHAT YOUR USE OF THE BEAR CANYON METHOD PRODUCED</div><div class="story">' +
                kn.join(" ") +
                "</div>"));""",
        """            kn.length > KG && PARA.push(kn.slice(KG).join(" ")),
            /* 3: into the map just below */
            (LOW.length || HIGH.length) &&
              PARA.push(
                "Just below, YOUR LANDSCAPE puts these notes on the ground: " +
                  (LOW.length ? NL(LOW) + (1 === LOW.length ? " sits" : " sit") + " in the low ground" : "") +
                  (LOW.length && HIGH.length ? ", and " : "") +
                  (HIGH.length ? NL(HIGH) + (LOW.length ? "" : 1 === HIGH.length ? " sits" : " sit") + " on the high ground" : "") +
                  ". Pick a question above the map to see one part of your thinking at a time.",
              ),
            PARA.length > 1 &&
              (we =
                '<div class="plab">WHAT YOUR USE OF THE BEAR CANYON METHOD PRODUCED</div><div class="story"><p>' +
                PARA.map(function (t) {
                  return t.replace(/^(<[^>]*>)?([a-z])/, function (m, a, b) {
                    return (a || "") + b.toUpperCase();
                  });
                }).join("</p><p>") +
                "</p></div>"));""",
    ),
]
for a, b in rep_pairs:
    assert s.count(a) == 1, (s.count(a), a[:80])
    s = s.replace(a, b)
s = s.replace('t.textContent = "v210"', 't.textContent = "v211"')
assert 't.textContent = "v211"' in s
open(P, "w").write(s)
