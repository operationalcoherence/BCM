"""v249: Pattern Analysis no longer reads as gibberish (queue 11-20, his screenshot).

The phrase layer never names a note by clipped first words any more:
- gsmStName: a note is named by its whole first sentence when that is short (2-9 words, not
  opening on a pronoun, preposition, or connective); else by its opening words only when they
  stop at a natural break and make sense alone (2+ words, not ending on a pronoun, article,
  or connective, not cut off by the word limit); otherwise it has no name and callers show
  its number once (N23, never "N23 (N23)" or "note 36 N36").
- gsmStThemes: a set of notes is named by the phrases at least two differently worded notes
  in it share (2 to 4 words, joined at most by "and", "of", or "to"; no emotion words, no lone
  words); a phrase another theme contains is dropped, and so is one that only repeats the
  goal's own words. WHAT HOLDS THE SITUATION IN PLACE and
  THE OPPORTUNITY lead with these themes, quoted; the evidence under them quotes the notes.
- AT A GLANCE names a gap only by a repeated phrase carried by two differently worded notes,
  never by one word or a stem.
- The phrase finder (phBest) counts a sentence written twice, as in repeated notes, once
  (same first 60 letters, as THE SAME THING? already does), so copies no longer make a
  fragment look like a repeated phrase.
- WHAT YOUR USE OF THE BEAR CANYON METHOD PRODUCED: a phrase that another phrase contains is
  one theme, under the longer name; the same finding is never named twice in a sentence.
"""
import sys
F = "gsm-readable.js"
s = open(F).read()


def rep(old, new, n=1):
    global s
    c = s.count(old)
    if c != n:
        sys.exit("expected %d, found %d: %r" % (n, c, old[:90]))
    s = s.replace(old, new)


HELPERS = r'''  /* v249: never name a note by clipped first words. */
  var StEmo = /^(accept|aggres|distru|defian|indiff|emotio|feel|concer|oppos|suppor)/i;
  var StStop = /^(the|a|an|of|and|to|in|on|for|with|by|as|at|from|or|toward|towards|within|over|about|around|against|through|across|among|without|while|because|if|every|each|no|your|our|my|his|her|them|us|we|you|i|he|she|is|are|was|were|be|been|being|has|have|had|that|this|it|its|their|there|they|not|but|which|who|what|when|how|all|any|some|more|most|such|into|also|than|then|so|very|just|can|could|will|would|may|might|do|does|did)$/i;
  function gsmStLow(r) {
    return r && !/^[A-Z]{2,}/.test(r) && !/^[A-Z]\w*\s+[A-Z]/.test(r) ? r.charAt(0).toLowerCase() + r.slice(1) : r;
  }
  function gsmStKey(t) {
    return String(t || "").toLowerCase().replace(/[^a-z0-9]+/g, " ").trim().slice(0, 60);
  }
  // is phrase a inside phrase b, word for word?
  function gsmStIn(a, b) {
    var f = function (x) {
      return " " + String(x).toLowerCase().replace(/[^a-z0-9]+/g, " ").trim() + " ";
    };
    return f(b).indexOf(f(a)) >= 0;
  }
  function gsmStName(n) {
    var t = String(n.txt || "")
        .replace(/\([^)]*\)/g, " ")
        .replace(/\s+/g, " ")
        .trim(),
      BAD0 = /^(there|here|it|this|that|they|these|those|them|among|for|to|and|but|or|as|so|if|when|while|of|in|on|by|with|from|at|not|no|its|their|his|her|our|your|my)$/i,
      BADZ = /^(they|them|those|these|it|this|that|their|its|his|her|our|your|my|we|you|i|he|she|a|an|the|and|or|of|to|in|on|for|with|by|as|if|so|but|even|very|more|most|than|then|who|which|what)$/i,
      sen = (t.split(/(?<=[.!?;])\s+/)[0] || "").replace(/[.!?;:,\s]+$/, "").replace(/^(the|a|an)\s+/i, ""),
      w = sen.split(" ").filter(Boolean);
    /* a short first sentence is the note's own name */
    if (w.length >= 2 && w.length <= 9 && !BAD0.test(w[0])) return gsmStLow(sen);
    /* else its opening words, only when they stop at a natural break and make sense alone */
    var c = t.split(/[.,;:!?\n]/)[0].replace(/\s+/g, " ").trim(),
      v = c.split(" "),
      out = [],
      brk = !1,
      VERB = /^(that|which|who|whose|contributes?|presents?|promotes?|enables?|leads?|forces?|turns?|drives?|supports?|freezes?|haunts?|may|could|will|would|has|have|had|is|are|was|were|engage|engages|like|such|including|put|continues?|remains?|solves?|takes?|makes?)$/i,
      PREP = /^(to|within|over|as|where|when|in|by|for|from|on|at|into|among|across|through)$/i;
    while (v.length && /^(the|a|an|as|so|and)$/i.test(v[0])) v.shift();
    for (var i = 0; i < v.length; i++) {
      if (out.length >= 6) {
        /* at the word limit, keep it only if the next word is a natural break */
        brk = VERB.test(v[i]) || PREP.test(v[i]);
        break;
      }
      if ((VERB.test(v[i]) && out.length >= 1) || (PREP.test(v[i]) && out.length >= 2)) {
        brk = !0;
        break;
      }
      out.push(v[i]);
    }
    var whole = !brk && out.length === v.length;
    while (out.length > 1 && /^(and|or|of|the|a|an|to|in|its|their|with)$/i.test(out[out.length - 1])) out.pop();
    if (out.length >= 2 && (brk || whole) && !BAD0.test(out[0]) && !BADZ.test(out[out.length - 1]))
      return gsmStLow(out.join(" ").replace(/[^\w)’'/-]+$/, ""));
    return "";
  }
  // how many differently worded notes these note numbers (N1, N2, …) are
  function gsmStDistinct(ids) {
    var u = {};
    (ids || []).forEach(function (id) {
      var r = /^N\d+$/.test(id) ? (C.m || [])[+id.slice(1) - 1] : null;
      r && (u[gsmStKey(r[3])] = 1);
    });
    return Object.keys(u).length;
  }
  function gsmStQL(a) {
    return phList(
      a.map(function (x) {
        return "“" + Gt(x) + "”";
      }),
    );
  }
  // the phrases at least two differently worded notes in this set share; none contained in another
  function gsmStThemes(list, k) {
    k = k || 3;
    var goal = String(C.goal || ""),
      cnt = {},
      shown = {},
      out = [],
      same = {};
    list.forEach(function (n) {
      var seen = {},
        tk = gsmStKey(n.txt);
      if (same[tk]) return;
      same[tk] = 1;
      String(n.txt || "")
        .replace(/\([^)]*\)/g, " ")
        .split(/[.,;:!?()\[\]"“”—–\n]+/)
        .forEach(function (part) {
          var w = part.match(/[A-Za-z][A-Za-z'’-]*/g) || [];
          for (var len = 2; len <= 4; len++)
            for (var i = 0; i + len <= w.length; i++) {
              var g = w.slice(i, i + len);
              if (StStop.test(g[0]) || StStop.test(g[len - 1])) continue;
              if (
                g.some(function (x) {
                  return (StStop.test(x) && !/^(and|of|to)$/i.test(x)) || StEmo.test(x);
                })
              )
                continue;
              var key = g.join(" ").toLowerCase();
              if (seen[key] || /\b(\w+) \1\b/.test(key)) continue;
              seen[key] = 1;
              cnt[key] = (cnt[key] || 0) + 1;
              shown[key] || (shown[key] = g.join(" "));
            }
        });
    });
    Object.keys(cnt)
      .filter(function (x) {
        return cnt[x] >= 2;
      })
      .sort(function (a, b) {
        return cnt[b] - cnt[a] || b.split(" ").length - a.split(" ").length;
      })
      .forEach(function (x) {
        /* the goal's own words say nothing new about what holds it or what helps */
        if (gsmStIn(x, goal)) return;
        if (
          out.some(function (o) {
            return gsmStIn(x, o.p);
          })
        )
          return;
        out = out.filter(function (o) {
          return !gsmStIn(o.p, x);
        });
        out.push({ p: gsmStLow(shown[x]), c: cnt[x] });
      });
    return out
      .sort(function (a, b) {
        return b.c - a.c;
      })
      .slice(0, k)
      .map(function (o) {
        return o.p;
      });
  }
'''

# 1. gsmStName replaced, helpers added
a = s.index("  function gsmStName(n) {")
b = s.index("  function gsmStRef(n) {")
s = s[:a] + HELPERS + s[b:]

# 2. WHAT HOLDS THE SITUATION IN PLACE
rep('''        n.name && !nm[k] && ((nm[k] = 1), sysNames.push(n.name));
      });
    }
    if (sysNames.length >= 3) {
      SS.sys = sysNames.slice(0, 3);''', '''        n.name && !nm[k] && ((nm[k] = 1), sysNames.push(n.name));
      });
    }
    var sysTh = comp.length >= 3 ? gsmStThemes(comp, 3) : [];
    if (comp.length >= 3) {
      SS.sys = sysTh.length
        ? sysTh
        : sysNames.length >= 2
          ? sysNames.slice(0, 3)
          : comp.slice(0, 3).map(function (n) {
              return n.lab;
            });''')
rep('''        "WHAT HOLDS THE SITUATION IN PLACE",
        Gt(gsmStList(sysNames, 8)).replace(/^./, function (c) {
          return c.toUpperCase();
        }) +
          (self
            ? " reinforce one another into a self-supporting system against the goal. "
            : " hang together against the goal, each sharing ground with the others. ") +
          g,''', '''        "WHAT HOLDS THE SITUATION IN PLACE",
        "What stands against the goal is one connected body" +
          (sysTh.length
            ? ", gathered around " + gsmStQL(sysTh) + ": " + comp.length + " notes"
            : sysNames.length >= 2
              ? " of " +
                comp.length +
                " notes, among them " +
                gsmStQL(
                  sysNames.slice(0, 3).map(function (x) {
                    return x.charAt(0).toUpperCase() + x.slice(1);
                  }),
                )
              : ": " + comp.length + " notes") +
          ", each sharing ground with the others" +
          (self ? ", whose parts reinforce one another into a self-supporting system. " : ". ") +
          g,''')
rep('''            return "<div>" + gsmStRef(n) + " <i>" + (null != n.em ? E[n.em] : "no emotion marked") + "</i>: " + Gt(n.name) + "</div>";''',
    '''            return "<div><i>" + (null != n.em ? E[n.em] : "no emotion marked") + "</i>: " + gsmStQ(n) + "</div>";''')

# 3. THE OPPORTUNITY
rep('''    if (exNames.length >= 2) {
      var oe = gsmStEm(ex).o[0];
      SS.opp = ex.length >= nw.length ? "Most" : "Part";
      SS.D.opp = ex;
      SS.D.oppN = exNames;
      card(
        "THE OPPORTUNITY",
        (ex.length >= nw.length ? "Most" : "Part") +
          " of the alternative already exists: " +
          Gt(gsmStList(exNames, 6)) +
          ". The work is scaling and reinforcing it more than inventing it." +''', '''    var exTh = ex.length >= 2 ? gsmStThemes(ex, 3) : [];
    if (ex.length >= 2 && (exTh.length || exNames.length >= 2)) {
      var oe = gsmStEm(ex).o[0];
      SS.opp = ex.length >= nw.length ? "Most" : "Part";
      SS.D.opp = ex;
      SS.D.oppN = exTh.length ? exTh : exNames;
      card(
        "THE OPPORTUNITY",
        (ex.length >= nw.length ? "Most" : "Part") +
          " of the alternative already exists" +
          (exTh.length
            ? ", around " + gsmStQL(exTh)
            : ", in " +
              gsmStQL(
                exNames.slice(0, 3).map(function (x) {
                  return x.charAt(0).toUpperCase() + x.slice(1);
                }),
              )) +
          ". The work is scaling and reinforcing it more than inventing it." +''')

# 4. AT A GLANCE, BIGGEST GAP
rep('''                      var U = ((window.gsmFR && window.gsmFR.it) || {}).unanswered || [];
                      return U.length
                        ? U.length +
                            " words and phrases you use for what stands in the way have nothing designed, redesigned, or reinforced for them yet. The first is “" +
                            jt(U[0]) +
                            "”" +
                            (U[1] ? ", then “" + jt(U[1]) + "”" : "") +
                            ". Tap to see them all."
                        : d.textContent;''', '''                      var U = ((window.gsmFR && window.gsmFR.it) || {}).unanswered || [],
                        UP = [];
                      /* v249: name a gap only by a phrase two differently worded notes repeat, never one word or a stem */
                      U.forEach(function (k) {
                        var m = gsmPhName(k, !0);
                        m &&
                          m.multi &&
                          gsmStDistinct(m.ids) >= 2 &&
                          UP.length < 2 &&
                          !UP.some(function (p) {
                            return gsmStIn(p, m.ph) || gsmStIn(m.ph, p);
                          }) &&
                          UP.push(m.ph);
                      });
                      return U.length
                        ? U.length +
                            (1 === U.length ? " thing you name as standing in the way has" : " things you name as standing in the way have") +
                            " nothing designed, redesigned, or reinforced for " +
                            (1 === U.length ? "it" : "them") +
                            " yet" +
                            (UP.length ? (1 === U.length ? ": “" : ", among them “") + UP.map(jt).join("” and “") + "”" : "") +
                            ". Tap to see " +
                            (1 === U.length ? "it." : "them all.")
                        : d.textContent;''')

# 5. WHAT YOUR USE OF THE BEAR CANYON METHOD PRODUCED
rep('''            if (ns.length < 2 || /^“/.test(nm)) return;
            seenPh[nm.toLowerCase()] = 1;
            TH.push({ t: t, nm: nm, s: sr, n: ns, g: ge[t] });''', '''            if (ns.length < 2 || /^“/.test(nm)) return;
            seenPh[nm.toLowerCase()] = 1;
            /* v249: a phrase another phrase contains is one theme, under the longer name */
            var inn = TH.filter(function (y) {
              return gsmStIn(nm, y.nm) || gsmStIn(y.nm, nm);
            })[0];
            if (inn) {
              gsmStIn(inn.nm, nm) && ((inn.nm = nm), (inn.t = t), (inn.g = ge[t]));
              sr.forEach(function (id) {
                inn.s.indexOf(id) < 0 && inn.s.push(id);
              });
              ns.forEach(function (id) {
                inn.n.indexOf(id) < 0 && inn.n.push(id);
              });
              return;
            }
            TH.push({ t: t, nm: nm, s: sr, n: ns, g: ge[t] });''')
rep('''            LnN = Ln.map(NM).filter(Boolean);''', '''            LnN = Ln.map(NM).filter(function (x, i, a) {
              return x && a.indexOf(x) === i;
            });''')

# 6. the phrase finder: the same sentence written twice (repeated notes) counts once
rep('''      cnt = {},
      ex = {};
    items.forEach(function (it) {
      phSents(it.t).forEach(function (sen) {
        var T = phToks(sen),''', '''      cnt = {},
      ex = {},
      sameS = {};
    items.forEach(function (it) {
      phSents(it.t).forEach(function (sen) {
        var sk = gsmStKey(sen);
        if (sameS[sk]) return;
        sameS[sk] = 1;
        var T = phToks(sen),''')

# 7. Taking Action: a note with no name shows its number once
rep('''              return gsmStName({ txt: String(x.txt).replace(/^\\s*(reinforce|continue to|support|scale|grow|keep)\\s+/i, "").replace(/^\\s*(for|to|in|on|with|by)\\s+/i, "") }) || x.id;
            }
            function NL(x) {
              var n = String(x.id).replace(/\\D/g, "");
              return Gt(NM(x)) + ' <span class="stn">' + (/^P/.test(x.id) ? "P" : "N") + n + "</span>";
            }''', '''              return NM0(x) || NB(x);
            }
            function NM0(x) {
              return gsmStName({ txt: String(x.txt).replace(/^\\s*(reinforce|continue to|support|scale|grow|keep)\\s+/i, "").replace(/^\\s*(for|to|in|on|with|by)\\s+/i, "") });
            }
            function NB(x) {
              return (/^P|^place/i.test(String(x.id)) ? "P" : "N") + String(x.id).replace(/\\D/g, "");
            }
            function NL(x) {
              var nm = NM0(x);
              return nm ? Gt(nm) + ' <span class="stn">' + NB(x) + "</span>" : NB(x);
            }''')
rep('''"Don’t argue with it; change a condition that keeps it in place. Start with " + sys[0].id + " (" + Gt(NM(sys[0])) + "), the part most tied to the others.",''',
    '''"Don’t argue with it; change a condition that keeps it in place. Start with " + (NM0(sys[0]) ? Gt(NM0(sys[0])) + " (" + NB(sys[0]) + ")" : NB(sys[0])) + ", the part most tied to the others.",''')

# 8. a note number at the start of a list is never lowercased (N14, not n14)
import re
s, k = re.subn(r"(NAMES\([^()]*\))\.replace\(/\^\./,", r"\1.replace(/^(?![NP]\\d)./,", s)
if k != 4:
    sys.exit("expected 4 NAMES lowercasings, found %d" % k)

rep('t && (t.textContent = "v248");', 't && (t.textContent = "v249");')
open(F, "w").write(s)
print("v249 applied")
