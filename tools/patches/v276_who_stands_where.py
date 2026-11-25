# v276: Groups Across Ground, the next insight type in his order (queue 11-20; layers tracker, row 36).
# WHO STANDS WHERE, a card under WHY IT BEHAVES THIS WAY on Pattern Analysis. It finds the groups of people the
# notes name (leadership, supporters, residents, homeowners, the board, staff...) and reads where each stands:
# on which side of the line, with which emotions, and whether an emotion is aimed at it or rises among it.
# Inactive unless a group is named in two or more differently worded notes and stands in more than one place.
# Words are never merged: "leaders" and "leadership" are two groups unless the person says otherwise.
p = 'gsm-readable.js'
s = open(p, encoding='utf-8').read()

def rep(old, new, n=1):
    global s
    c = s.count(old)
    assert c == n, (c, old[:100])
    s = s.replace(old, new)

rep('''    return R.length >= 1 ? '<div class="plab">WHY IT BEHAVES THIS WAY</div><div class="sreads">' + R.join("") + "</div>" : "";''',
'''    /* v276: WHO STANDS WHERE (groups across ground) */
    try {
      var GR = gsmGroups(src);
      SS.groups = GR;
      GR.length &&
        card(
          "WHO STANDS WHERE",
          GR.map(function (g) {
            return "<p>" + g.say + "</p>";
          }).join(""),
          GR.map(function (g) {
            return g.ev
              .map(function (n) {
                return "<div><i>" + (null != n.em ? E[n.em] : "no emotion marked") + (n.side > 0 ? ", helps" : n.side < 0 ? ", hinders" : "") + "</i>: " + gsmStQ(n, null, g.stem) + "</div>";
              })
              .join("");
          }).join(""),
        );
    } catch (e) {}
    return R.length >= 1 ? '<div class="plab">WHY IT BEHAVES THIS WAY</div><div class="sreads">' + R.join("") + "</div>" : "";''')

rep('''  function gsmStructBuild() {''', r'''  /* v276: groups of people named in the notes, and where each stands. A general list of words for groups of
     people, not a list for one subject. Target: an emotion aimed at the group ("distrust in leadership",
     "aggression toward supporters"). Among: the emotion rises inside it ("aggression amongst supporters"). */
  var GSMGRP = [
    ["leadership", "it"], ["leaders?", "them"], ["managers?", "them"], ["supervisors?", "them"], ["executives?", "them"],
    ["administrators?", "them"], ["staff", "them"], ["employees?", "them"], ["workers?", "them"], ["workforce", "it"],
    ["subordinates?", "them"], ["colleagues?", "them"], ["members?", "them"], ["teams?", "them"], ["crews?", "them"],
    ["unions?", "them"], ["supporters?", "them"], ["opponents?", "them"], ["critics?", "them"], ["stakeholders?", "them"],
    ["partners?", "them"], ["volunteers?", "them"], ["residents?", "them"], ["homeowners?", "them"], ["landowners?", "them"],
    ["owners?", "them"], ["neighbou?rs?", "them"], ["communit(?:y|ies)", "it"], ["citizens?", "them"], ["voters?", "them"],
    ["constituency", "it"], ["constituents?", "them"], ["board", "it"], ["council", "it"], ["officials?", "them"],
    ["agenc(?:y|ies)", "it"], ["government", "it"], ["department", "it"], ["customers?", "them"], ["clients?", "them"],
    ["users?", "them"], ["patients?", "them"], ["students?", "them"], ["teachers?", "them"], ["parents?", "them"],
    ["families", "them"], ["nurses?", "them"], ["doctors?", "them"], ["physicians?", "them"], ["firefighters?", "them"],
    ["donors?", "them"], ["investors?", "them"], ["youth", "them"], ["elders?", "them"],
  ];
  function gsmGroups(src) {
    var E = GSMEMO,
      LOW = function (e) {
        return 0 === e || 2 === e || 4 === e;
      },
      notes = src.filter(function (n) {
        return n.note;
      }),
      acts = src.filter(function (n) {
        return (n.note && n.k >= 5) || (!n.note && n.q >= 5);
      }),
      out = [];
    GSMGRP.forEach(function (G) {
      var rx = new RegExp("\\b(" + G[0] + ")\\b", "i"),
        tg = new RegExp("\\b(toward|towards|against|in|of|at|on|over)\\s+(?:the\\s+|its\\s+|their\\s+|our\\s+|his\\s+|her\\s+)?(?:[a-z-]+\\s+)?(" + G[0] + ")\\b", "i"),
        am = new RegExp("\\b(among|amongst|from|by|within)\\s+(?:the\\s+|its\\s+|their\\s+|our\\s+)?(?:[a-z-]+\\s+)?(" + G[0] + ")\\b", "i"),
        hit = notes.filter(function (n) {
          return rx.test(n.txt.replace(/\bcommunit(?:y|ies) of practice\b/gi, ""));
        });
      var txts = {};
      hit = hit.filter(function (n) {
        var k = n.txt.toLowerCase().replace(/[^a-z0-9]+/g, " ").trim();
        return !txts[k] && (txts[k] = 1);
      });
      if (hit.length < 2) return;
      /* the word as the person writes it most */
      var form = {};
      hit.forEach(function (n) {
        var m = n.txt.match(rx);
        m && (form[m[1].toLowerCase()] = (form[m[1].toLowerCase()] || 0) + 1);
      });
      var w = Object.keys(form).sort(function (a, b) {
          return form[b] - form[a];
        })[0],
        it = "it" === G[1] && !/s$/.test(w) ? "it" : "them",
        T = hit.filter(function (n) {
          return tg.test(n.txt) && null != n.em;
        }),
        A = hit.filter(function (n) {
          return T.indexOf(n) < 0 && null != n.em && (am.test(n.txt) || new RegExp("^\\W*(?:\\w+\\s+){0,2}(" + G[0] + ")\\b", "i").test(n.txt));
        }),
        H = hit.filter(function (n) {
          return n.side > 0;
        }),
        N = hit.filter(function (n) {
          return n.side < 0;
        }),
        D = acts.filter(function (n) {
          return rx.test(n.txt) && !tg.test(n.txt);
        }),
        TL = T.filter(function (n) {
          return LOW(n.em) && n.side < 0;
        }),
        AL = A.filter(function (n) {
          return LOW(n.em);
        }),
        fam = {};
      hit.forEach(function (n) {
        null != n.em && (fam[LOW(n.em) ? "low" : "high"] = 1);
      });
      var em = function (L) {
          var u = [];
          L.forEach(function (n) {
            u.indexOf(E[n.em]) < 0 && u.push(E[n.em]);
          });
          return gsmMeanList(u);
        },
        art = /^(board|council|government|department|community|workforce|constituency|agency|staff)$/.test(w) ? "the " : "",
        W = art + "<b>" + Gt(w) + "</b>",
        Wc = art ? "The <b>" + Gt(w) + "</b>" : "<b>" + Gt(w.charAt(0).toUpperCase() + w.slice(1)) + "</b>",
        say = "",
        rank = 0,
        ev = hit;
      var TD = TL.filter(function (n) {
        return 2 === n.em;
      });
      if (TD.length && D.length) {
        /* the designer is the obstacle: those the plan relies on are the ones distrusted */
        say =
          "What you would do turns on " + W + gsmStNB(D) + ", yet distrust is aimed at " + it + " where things hinder" + gsmStNB(TD) +
          ". The change rests on the people it is least trusted with: until that trust moves, whatever they design will be read through it.";
        rank = 4;
        ev = TD.concat(D.filter(function (n) { return n.note; }));
      } else if (T.some(function (n) { return LOW(n.em); }) && AL.length) {
        var TT = T.filter(function (n) {
          return LOW(n.em);
        });
        say =
          gsmCap(em(TT.concat(AL))) + " runs both ways around " + W + ": it is aimed at " + it + gsmStNB(TT) + " and rises among " + it + gsmStNB(AL) +
          ". Each side's emotion becomes the other side's evidence, so the loop feeds itself.";
        rank = 3;
        ev = TT.concat(AL);
      } else if (H.length && N.length) {
        say =
          Wc + " is not one block: " + ("it" === it ? "it helps" : "they help") + " in some notes" + gsmStNB(H) + " and " + ("it" === it ? "hinders" : "hinder") + " in others" + gsmStNB(N) +
          ". Reach the part that hinders through the part that helps, rather than treating " + W + " as one.";
        rank = 2;
      } else if (
        A.some(function (n) {
          return LOW(n.em);
        }) &&
        A.some(function (n) {
          return !LOW(n.em);
        })
      ) {
        /* only where the group itself holds the emotion, not where it is only mentioned */
        var lo = A.filter(function (n) {
            return LOW(n.em);
          }),
          hi = A.filter(function (n) {
            return !LOW(n.em);
          });
        say = Wc + " carries both " + em(hi) + gsmStNB(hi) + " and " + em(lo) + gsmStNB(lo) + ": one name may cover different people, or people partway between.";
        rank = 1;
      }
      say && out.push({ w: w, stem: w.slice(0, 4).toLowerCase(), say: say, rank: rank, n: hit.length, ev: ev.slice(0, 6) });
    });
    return out
      .sort(function (a, b) {
        return b.rank - a.rank || b.n - a.n;
      })
      .slice(0, 3);
  }
  function gsmCap(t) {
    return String(t).replace(/^./, function (c) {
      return c.toUpperCase();
    });
  }
  function gsmStructBuild() {''')

rep('t && (t.textContent = "v275")', 't && (t.textContent = "v276")')
open(p, 'w', encoding='utf-8').write(s)
print('ok')
