"""v200: the phrase-and-meaning layer, first half (review plan, Phase 1 step 4; P1): Taking Action cards.
1. Card titles are phrases from the user's own writing, never a lone word. A thread card takes the phrase around its
   word that the workbook uses most (two to five words, names kept whole and never split); a card built from Q.3,
   Q.5, Q.6, or Q.7 takes the clause it came from, starting at the phrase ("instead places significant
   responsibility" becomes "places significant responsibility for fire outcomes on the shoulders of home and
   property owners"). Hovering a title shows the whole sentence it came from.
2. Every card says what it serves: IN SERVICE OF THE GOAL, three short sentences built from the workbook. What the
   goal names about it; what you would design, redesign, or reinforce about it (Q.5–Q.7 and their notes), quoted,
   with the whole sentence on hover; and where the context you've grasped (Q.1–Q.4 notes) has it helping or holding
   the goal back.
Engine only, for every workbook. The helpers leave the word tallies as they found them (as v199's pass does).
Usage: python3 v200_phrases_cards.py gsm-readable.js"""
import sys

P = sys.argv[1]
s = open(P).read()


def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, (c, a[:90])
    s = s.replace(a, b)


HELP = r'''  var PhC = {};
  function phKeep(f) {
    var SV = [Mt, NmK, NmD].map(function (o) {
      return JSON.stringify(o);
    });
    try {
      return f();
    } finally {
      [Mt, NmK, NmD].forEach(function (o, i) {
        for (var k in o) delete o[k];
        var v = JSON.parse(SV[i]);
        for (k in v) o[k] = v[k];
      });
    }
  }
  var PhBrk = { including: 1, like: 1, such: 1, especially: 1, particularly: 1, among: 1, via: 1, using: 1, per: 1, versus: 1, etc: 1, throughout: 1, toward: 1, towards: 1, across: 1, within: 1, without: 1, around: 1, through: 1, into: 1, onto: 1, upon: 1, beyond: 1, despite: 1, during: 1, along: 1, between: 1, against: 1 },
    PhUsed = {},
    PhDF = null;
  function phStem(w) {
    var lw = w.toLowerCase().replace(/[’']s$/, "");
    return PhBrk[lw] ? [] : lw in PhC ? PhC[lw] : (PhC[lw] = Ht(lw).seq.filter(Boolean));
  }
  // in how many texts each stem appears (once per pass)
  function phDF() {
    if (PhDF) return PhDF;
    PhDF = {};
    phAll().forEach(function (it) {
      var o = {};
      phSents(it.t).forEach(function (sen) {
        phToks(sen).forEach(function (t) {
          t.st.forEach(function (k) {
            o[k] = 1;
          });
        });
      });
      for (var k in o) PhDF[k] = (PhDF[k] || 0) + 1;
    });
    return PhDF;
  }
  function phSents(t) {
    return (String(t || "").match(/[^.!?\n]+[.!?]*/g) || [])
      .map(function (x) {
        return x.trim();
      })
      .filter(Boolean);
  }
  function phToks(sen) {
    var re = /[A-Za-z][A-Za-z’'\-]*[A-Za-z]|[A-Za-z]/g,
      m,
      T = [];
    while ((m = re.exec(sen))) T.push({ w: m[0], i: m.index, e: m.index + m[0].length });
    T.forEach(function (o, j) {
      o.st = phStem(o.w);
      o.raw = o.w.toLowerCase().replace(/[’']s$/, "");
      o.c = o.st.length > 0 || !!Dsc[o.raw];
      o.cap = j > 0 && /^[A-Z][a-z]/.test(o.w) && !/[.!?:"“(]\s*$/.test(sen.slice(T[j - 1].e, o.i));
    });
    return T;
  }
  function phGap(sen, T, a, b) {
    return sen.slice(T[a].e, T[b].i);
  }
  function phHas(o, k) {
    return o.st.indexOf(k) >= 0 || o.raw === k;
  }
  function phHit(o, S) {
    return (
      !o.cap &&
      (!!S[o.raw] ||
        o.st.some(function (k) {
          return S[k];
        }))
    );
  }
  function phSet(stems) {
    var S = {};
    stems.forEach(function (k) {
      S[k] = 1;
    });
    return S;
  }
  function phLow(x, T0) {
    return T0 && !T0.cap && /^[A-Z][a-z]/.test(x) ? x.charAt(0).toLowerCase() + x.slice(1) : x;
  }
  function phList(a) {
    return a.length < 3 ? a.join(" and ") : a.slice(0, -1).join(", ") + ", and " + a[a.length - 1];
  }
  // the phrase around the stems that the given texts use most: [{t, src}] -> {ph, sent, src} or null
  function phBest(stems, items) {
    var S = phSet(stems),
      DF = phDF(),
      cnt = {},
      ex = {};
    items.forEach(function (it) {
      phSents(it.t).forEach(function (sen) {
        var T = phToks(sen),
          seen = {};
        T.forEach(function (o, j) {
          if (!phHit(o, S)) return;
          var a = j,
            b = j,
            ok = function (x, y) {
              return /^[\s\-–]*$/.test(phGap(sen, T, x, y));
            };
          while (a > 0 && j - a < 3 && ok(a - 1, a) && T[a - 1].c && !T[a - 1].cap) a--;
          while (b < T.length - 1 && b - j < 3 && ok(b, b + 1) && T[b + 1].c && !T[b + 1].cap) b++;
          for (var x = a; x <= j; x++)
            for (var y = Math.max(j, x + 1); y <= b && y - x < 5; y++) {
              var ws = T.slice(x, y + 1);
              if (
                !stems.every(function (k) {
                  return ws.some(function (o) {
                    return phHas(o, k);
                  });
                })
              )
                continue;
              var key = ws
                .map(function (o) {
                  return o.w.toLowerCase();
                })
                .join(" ");
              if (seen[key]) continue;
              seen[key] = 1;
              cnt[key] = (cnt[key] || 0) + 1;
              ex[key] ||
                (ex[key] = {
                  ph: phLow(sen.slice(ws[0].i, ws[ws.length - 1].e), ws[0]),
                  sent: sen,
                  src: it.src,
                  n: ws.length,
                  g: 0,
                  df: ws.reduce(function (z, o) {
                    return z + (o.st.some(function (k) {
                      return S[k];
                    })
                      ? 0
                      : Math.min.apply(null, o.st.map(function (k) {
                          return DF[k] || 0;
                        }).concat([99])));
                  }, 0) / ws.length,
                });
              "goal" === it.src && (ex[key].g = 1);
            }
        });
      });
    });
    var K = Object.keys(cnt).sort(function (p, q) {
      return cnt[q] - cnt[p] || ex[q].g - ex[p].g || ex[q].df - ex[p].df || ex[p].n - ex[q].n;
    });
    return K.length
      ? ((ex[K[0]].alt = K.slice(1).map(function (k) {
          return ex[k];
        })),
        ex[K[0]])
      : null;
  }
  // the clause of a text that starts at the stems: -> {cl, sent} or null
  var PhLead = { instead: 1, also: 1, then: 1, still: 1, just: 1, and: 1, but: 1, or: 1, so: 1 };
  function phClause(stems, text, cap) {
    cap = cap || 16;
    var S = phSet(stems),
      best = null;
    phSents(text).some(function (sen) {
      var T = phToks(sen),
        hits = [];
      T.forEach(function (o, j) {
        phHit(o, S) && hits.push(j);
      });
      var covers = function (from) {
        return stems.every(function (k) {
          return hits.some(function (j) {
            return j >= from && phHas(T[j], k);
          });
        });
      };
      if (!hits.length || !covers(0)) return !1;
      var a = hits.filter(covers).pop(),
        last = hits[hits.length - 1],
        tight = function (x, y) {
          return /^[\s\-–]*$/.test(phGap(sen, T, x, y));
        };
      if (PhLead[T[a].w.toLowerCase()]) while (a < last && PhLead[T[a].w.toLowerCase()]) a++;
      else for (var z = 0; z < 2 && a > 0 && tight(a - 1, a) && T[a - 1].c && !T[a - 1].cap && !PhLead[T[a - 1].w.toLowerCase()]; z++) a--;
      var stop = function (x) {
          return /[,;:()\[\]"“”—–/]/.test(phGap(sen, T, x, x + 1));
        },
        b = a,
        cut = !1;
      while (b < T.length - 1 && (b < last || !stop(b)) && b - a < cap - 1) b++;
      b < T.length - 1 && !stop(b) && (cut = !0);
      if (cut) while (b > a + 2 && !T[b].c) b--;
      if (b - a < 3)
        while (a > 0 && b - a < 5 && (/^\s*,\s*$/.test(phGap(sen, T, a - 1, a)) || /^(and|or)$/i.test(T[a - 1].w))) a--;
      var o = { cl: phLow(sen.slice(T[a].i, T[b].e), T[a]) + (cut ? "…" : ""), sent: sen, n: b - a + 1 };
      (!best || o.n > best.n) && (best = o);
      return o.n >= 4;
    });
    return best;
  }
  function phAll() {
    var D = window.gsmData ? window.gsmData() : { m: [], a: [] },
      it = [{ t: C.goal || "", src: "goal" }];
    (D.a || []).forEach(function (x, i) {
      it.push({ t: x || "", src: "Q." + (i + 1), q: i + 1 });
    });
    (D.m || []).forEach(function (r, i) {
      it.push({ t: r[3] || "", src: "N" + (i + 1), q: r[0] });
    });
    return it;
  }
  function phAttr(x) {
    return Gt(x).replace(/"/g, "&quot;");
  }
  // a card's title from its thread key
  var PhTi = {};
  function gsmPhTitle(key) {
    if (key in PhTi) return PhTi[key];
    return (PhTi[key] = phKeep(function () {
      var stems = String(key).split(" "),
        b = phBest(stems, phAll());
      if (!b) return null;
      var L = [b].concat(b.alt).filter(function (x) {
        return x.n >= 2 && !PhUsed[x.ph.toLowerCase()];
      });
      return L[0] ? ((PhUsed[L[0].ph.toLowerCase()] = 1), L[0]) : null;
    }));
  }
  // a card's title from the clause it came from
  function gsmPhClauseTitle(stems, text) {
    return phKeep(function () {
      return phClause(stems, text);
    });
  }
  // IN SERVICE OF THE GOAL for a card: stems, the notes behind it that help and that hold the goal back (or null:
  // find the Q.1–Q.4 notes that share its words), its own source, and the clause it came from
  function gsmPurpose(stems, help, hold, own, cl) {
    return phKeep(function () {
      var all = phAll(),
        out = [],
        g = phBest(stems, [all[0]]),
        me = all.filter(function (x) {
          return x.src === own;
        })[0];
      g && out.push("The goal names “" + Gt(g.ph) + ".”");
      if (me && me.q >= 5 && me.q <= 7) out.push("It is what you would " + ["design", "redesign", "reinforce"][me.q - 5] + " (" + own + ").");
      else if (me && (3 === me.q || 7 === me.q || 1 === me.q)) out.push("It is already working (" + own + ").");
      else {
        var d = null;
        all.some(function (it) {
          if (!(it.q >= 5 && it.q <= 7) || it.src === own) return !1;
          var c = phClause(stems, it.t);
          return c && c.n >= 3 && (d = { c: c, it: it });
        });
        out.push(
          d
            ? "What you would " +
                ["design", "redesign", "reinforce"][d.it.q - 5] +
                ' says <span class="purq" title="' +
                phAttr(d.c.sent) +
                '">“' +
                Gt(d.c.cl) +
                "”</span> (" +
                d.it.src +
                ")."
            : "Nothing you would design, redesign, or reinforce names it yet.",
        );
      }
      var M = (window.gsmData ? window.gsmData().m : []) || [],
        H = [],
        B = [];
      if (help || hold) {
        var ids = function (L) {
          return L.filter(function (t) {
            return t.k <= 4 && t.id;
          }).map(function (t) {
            return t.id;
          });
        };
        H = ids(help || []);
        B = ids(hold || []);
      } else if (cl) {
        var MED = window.gsmMED || {},
          mine = {};
        phToks(cl).forEach(function (t) {
          t.st.forEach(function (k) {
            MED[k] || (mine[k] = 1);
          });
        });
        M.forEach(function (r, i) {
          if (!(r[0] >= 1 && r[0] <= 4)) return;
          var sh = {};
          phToks(r[3] || "").forEach(function (t) {
            t.st.forEach(function (k) {
              mine[k] && (sh[k] = 1);
            });
          });
          Object.keys(sh).length >= 2 && (r[2] >= 118 ? B : H).push("N" + (i + 1));
        });
      }
      ((H = H.slice(0, 3)), (B = B.slice(0, 3)));
      (H.length || B.length) &&
        out.push(
          "In the context you’ve grasped, it " +
            (cl && !(help || hold)
              ? (B.length ? "answers what holds the goal back in " + phList(B) : "") + (B.length && H.length ? " and " : "") + (H.length ? "builds on what helps in " + phList(H) : "")
              : (H.length ? "helps in " + phList(H) : "") + (H.length && B.length ? " and " : "") + (B.length ? "holds the goal back in " + phList(B) : "")) +
            ".",
        );
      return '<div class="purp"><b>IN SERVICE OF THE GOAL</b> ' + out.join(" ") + "</div>";
    });
  }
'''
rep("  var Mt = {};\n  function jt(t) {\n", "  var Mt = {};\n" + HELP + "  function jt(t) {\n")

# a fresh stem cache every pass (merges on THE SAME THING? change stems)
rep("  window.gsmDerive = function () {\n", "  window.gsmDerive = function () {\n    PhC = {};\n    PhDF = null;\n    PhUsed = {};\n    PhTi = {};\n")

# style
rep(
    "#gsm .coa .why{color:#555;font-size:13px;margin-bottom:6px}",
    "#gsm .coa .why{color:#555;font-size:13px;margin-bottom:6px}#gsm .coa .purp{font-size:14px;line-height:1.5;color:#222;margin:0 0 8px}#gsm .coa .purp b{display:block;font-size:11px;letter-spacing:.14em;margin-bottom:2px}#gsm .coa .purq{border-bottom:1px dotted #8a8a8a;cursor:help}#gsm .coa .hd b[title]{cursor:help}",
)

# 1. thread cards
rep(
    "                  return (\n                    '<div class=\"coa\"><div class=\"hd\"><b>' +\n                    Gt(jt(t)) +\n                    '</b><span class=\"mode' +\n                    (a ? \" s\" : \"\") +\n                    '\">' +\n                    (a ? \"STRATEGY\" : \"PROGRAM\") +\n                    '</span></div><div class=\"bd\"><div class=\"why\">Why: ' +",
    "                  var PT = gsmPhTitle(t);\n"
    "                  return (\n                    '<div class=\"coa\"><div class=\"hd\"><b' +\n"
    "                    (PT ? ' title=\"' + phAttr(PT.sent) + '\"' : \"\") +\n"
    "                    \">\" +\n"
    "                    Gt(PT ? PT.ph : jt(t)) +\n                    '</b><span class=\"mode' +\n                    (a ? \" s\" : \"\") +\n                    '\">' +\n                    (a ? \"STRATEGY\" : \"PROGRAM\") +\n                    '</span></div><div class=\"bd\">' +\n"
    "                    gsmPurpose(String(t).split(\" \"), f, g, null) +\n"
    "                    '<div class=\"why\">Why: ' +",
)

# 2. cards from what Q.3 and Q.7 say is already working
rep(
    "              Jn.map(function (t) {\n                var e = t.key.split(\" \").map(jt).join(\" \"),\n                  n = t.src,",
    "              Jn.map(function (t) {\n"
    "                var SRC = phAll().filter(function (x) {\n"
    "                    return x.src === t.src;\n"
    "                  })[0],\n"
    "                  CT = SRC ? gsmPhClauseTitle(t.key.split(\" \"), SRC.t) : null,\n"
    "                  e = CT ? CT.cl : t.key.split(\" \").map(jt).join(\" \"),\n                  n = t.src,",
)
rep(
    "                return (\n                  '<div class=\"coa\"><div class=\"hd\"><b>' +\n                  Gt(e) +\n                  '</b><span class=\"mode\">PROGRAM</span></div><div class=\"bd\"><div class=\"why\">Why: ' +\n                  r +",
    "                return (\n                  '<div class=\"coa\"><div class=\"hd\"><b' +\n"
    "                  (CT ? ' title=\"' + phAttr(CT.sent) + '\"' : \"\") +\n"
    "                  \">\" +\n"
    "                  Gt(e) +\n                  '</b><span class=\"mode\">PROGRAM</span></div><div class=\"bd\">' +\n"
    "                  gsmPurpose(t.key.split(\" \"), null, null, t.src, CT ? CT.cl : null) +\n"
    "                  '<div class=\"why\">Why: ' +\n                  r +",
)

# 3. cards from what Q.5, Q.6, and Q.7 name
rep(
    "                var r = e[0].join(\" \"),\n                  l = e[0].map(jt).join(\" \"),",
    "                var r = e[0].join(\" \"),\n"
    "                  CT = gsmPhClauseTitle(e[0], Q()[t] || \"\"),\n"
    "                  l = CT ? CT.cl : e[0].map(jt).join(\" \"),",
)
rep(
    "                  (In +=\n                    '<div class=\"coa\"><div class=\"hd\"><b>' +\n                    Gt(l) +",
    "                  (In +=\n                    '<div class=\"coa\"><div class=\"hd\"><b' +\n"
    "                    (CT ? ' title=\"' + phAttr(CT.sent) + '\"' : \"\") +\n"
    "                    \">\" +\n"
    "                    Gt(l) +",
)
rep(
    "                    (h ? \"STRATEGY\" : \"PROGRAM\") +\n                    '</span></div><div class=\"bd\"><div class=\"why\">Why: ' +\n                    f.join(\", \") +",
    "                    (h ? \"STRATEGY\" : \"PROGRAM\") +\n                    '</span></div><div class=\"bd\">' +\n"
    "                    gsmPurpose(e[0], null, null, \"Q.\" + (t + 1), CT ? CT.cl : null) +\n"
    "                    '<div class=\"why\">Why: ' +\n                    f.join(\", \") +",
)

# WHERE THE CARDS MEET and Where to start name thread cards the same way
rep(
    "                    return {\n                      w: t,\n                      name: jt(t),\n                      st: Fn(t),",
    "                    return {\n                      w: t,\n                      name: (gsmPhTitle(t) || { ph: jt(t) }).ph,\n                      st: Fn(t),",
)

s = s.replace('t.textContent = "v199"', 't.textContent = "v200"')
assert 't.textContent = "v200"' in s
open(P, "w").write(s)
