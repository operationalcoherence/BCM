# v280: Loops Between Groups, item 6 in his order of the second generation of insight types
# (queue 11-20; his go-ahead 25 Nov 2026 16:22). A LOOP BETWEEN GROUPS, a card under WHY IT BEHAVES THIS WAY
# on Pattern Analysis, after WHO STANDS WHERE. Where one group holds an emotion aimed at a second group, and the
# second holds one aimed back at the first, the two are in a loop. Holder and target come from the words only:
# a group holds an emotion when it opens the note, owns it ("supporters' aggression"), or the emotion sits
# "among", "from", "by" or "within" it; the target is v279's reader. People named by an emotion ("those who are
# defiant, aggressive, or distrustful") count as a group. When the note aimed back doesn't say whose emotion it
# is, the card asks one tap (C.asks "loop|<note id>|<group>") and states the loop only on a Yes.
# WHO STANDS WHERE leaves out a group the new card covers (its readings of that group were the loop, half seen).
p = 'gsm-readable.js'
s = open(p, encoding='utf-8').read()

def rep(old, new, n=1):
    global s
    c = s.count(old)
    assert c == n, (c, old[:100])
    s = s.replace(old, new)

# 1. the card, after WHO STANDS WHERE; the loops are read first so WHO STANDS WHERE can leave them to it
rep('''    /* v276: WHO STANDS WHERE (groups across ground) */
    try {
      var GR = gsmGroups(src);''',
'''    /* v280: loops between groups, read first so WHO STANDS WHERE leaves them to their own card */
    var LP = [],
      LPskip = {};
    try {
      LP = gsmLoops(src);
      SS.loops = LP;
      LP.forEach(function (l) {
        [l.a, l.b].forEach(function (g) {
          null != g.gi && (LPskip[GSMGRP[g.gi][0]] = 1);
        });
      });
      (LP.no || []).forEach(function (g) {
        null != g.gi && (LPskip[GSMGRP[g.gi][0]] = 1);
      });
    } catch (e) {}
    /* v276: WHO STANDS WHERE (groups across ground) */
    try {
      var GR = gsmGroups(src, LPskip);''')

rep('''    /* v277: RISK AFTER THE GOAL */
    try {
      var AG = gsmAfterGoal();''',
'''    /* v280: A LOOP BETWEEN GROUPS */
    try {
      LP.length &&
        card(
          LP.length > 1 ? "LOOPS BETWEEN GROUPS" : "A LOOP BETWEEN GROUPS",
          LP.map(function (l) {
            return "<p>" + l.say + "</p>";
          }).join(""),
          LP.map(function (l) {
            return [l.x, l.y]
              .map(function (n) {
                return "<div><i>" + E[n.em] + (n.side > 0 ? ", helps" : n.side < 0 ? ", hinders" : "") + "</i>: " + gsmStQ(n) + "</div>";
              })
              .join("");
          }).join(""),
        );
    } catch (e) {}
    /* v277: RISK AFTER THE GOAL */
    try {
      var AG = gsmAfterGoal();''')

# 2. WHO STANDS WHERE leaves a covered group's "both ways" reading to the loop card
rep('''  function gsmGroups(src) {''', '''  function gsmGroups(src, skip) {''')
rep('''      say && out.push({ w: w, stem: w.slice(0, 4).toLowerCase(), say: say, rank: rank, n: hit.length, ev: ev.slice(0, 6), ob: 4 === rank ? ob : null });''',
    '''      /* v280: a group in a loop has its own card; only "the plan relies on the people it distrusts" stays here */
      say && !(skip && skip[G[0]] && rank < 4) && out.push({ w: w, stem: w.slice(0, 4).toLowerCase(), say: say, rank: rank, n: hit.length, ev: ev.slice(0, 6), ob: 4 === rank ? ob : null });''')

# 3. the reader
rep('''  function gsmStructBuild() {''', r'''  /* v280: who holds a note's emotion, and at which people it is aimed. General words only. */
  var GSMPPL = /\b(?:those|people|anyone|others)\s+who\s+(?:are|were|is)\s+((?:[a-z-]+(?:\s*,\s*(?:or\s+|and\s+)?|\s+or\s+|\s+and\s+)?){1,5})/i;
  function gsmEmoPeople(t) {
    /* "those who are defiant, aggressive, or distrustful": people named by their emotions */
    var m = GSMPPL.exec(t);
    if (!m) return null;
    var ws = m[1].split(/\s*,\s*|\s+/).filter(Boolean),
      set = [],
      keep = [];
    for (var i = 0; i < ws.length; i++) {
      var w = ws[i].toLowerCase();
      if (/^(or|and)$/.test(w)) continue;
      var e = -1;
      GSMEMW.forEach(function (rx, k) {
        new RegExp("^(?:" + rx + ")$", "i").test(w) && (e = k);
      });
      if (e < 0) break;
      set.indexOf(e) < 0 && set.push(e);
      keep.push(ws[i]);
    }
    if (!set.length) return null;
    var show = keep.length > 2 ? keep.slice(0, -1).join(", ") + ", or " + keep[keep.length - 1] : keep.join(" or ");
    return { id: "e" + set.slice().sort().join(""), set: set, show: "those who are " + show, pl: 1 };
  }
  function gsmGrpOf(w) {
    for (var i = 0; i < GSMGRP.length; i++) if (new RegExp("^(?:" + GSMGRP[i][0] + ")$", "i").test(w)) return i;
    return -1;
  }
  function gsmLoopHolder(n, tg) {
    var t = String(n.txt || "").replace(/\s+/g, " "),
      tw = {};
    tg &&
      tg.key.forEach(function (k) {
        tw[k] = 1;
      });
    var op = /^\W*(?:(?:the|its|their|our|many|some|most|all)\s+)?(?:([a-z-]+)\s+)?([a-z-]+)\b/i.exec(t),
      W = GSMEMW.join("|");
    for (var i = 0; i < GSMGRP.length; i++) {
      var G = GSMGRP[i][0],
        am = new RegExp("\\b(?:among|amongst|from|by|within)\\s+(?:the\\s+|its\\s+|their\\s+|our\\s+)?(?:[a-z-]+\\s+)?(" + G + ")\\b", "i").exec(t),
        own = new RegExp("\\b(" + G + ")(?:'s|s'|'|’s|’)\\s+(?:[a-z-]+\\s+)?(?:" + W + ")\\b", "i").exec(t),
        gx = new RegExp("^(?:" + G + ")$", "i"),
        lead = op && op[1] && gx.test(op[1]) ? op[1] : op && gx.test(op[2]) && !(op[1] && (/^(toward|towards|against|in|of|at|over|about|to|for|with)$/i.test(op[1]) || new RegExp("^(?:" + W + ")$", "i").test(op[1]))) ? op[2] : "",
        m = am || own || (lead ? [lead, lead] : null);
      if (m && !tw[m[1].toLowerCase()]) return { id: "g" + i, gi: i, show: m[1].toLowerCase(), pl: "them" === GSMGRP[i][1] || /s$/i.test(m[1]) };
    }
    var ep = /^\W*(?:those|people|anyone|others)\s+who\b/i.test(t) && gsmEmoPeople(t);
    return ep || null;
  }
  function gsmLoopTarget(n, tg) {
    if (!tg) return null;
    if (/^(those|people|anyone|others) who/.test(tg.show)) {
      var ep = gsmEmoPeople(String(n.txt || "").replace(/\s+/g, " "));
      if (ep) return ep;
    }
    for (var j = tg.key.length - 1; j >= 0; j--) {
      var gi = gsmGrpOf(tg.key[j]);
      if (gi >= 0) return { id: "g" + gi, gi: gi, show: tg.show.replace(/^(?:the|a|an)\s+/i, ""), art: tg.art, pl: "them" === GSMGRP[gi][1] || /s$/i.test(tg.key[j]) };
    }
    return null;
  }
  function gsmLoopSame(a, b) {
    return !!a && !!b && (a.id === b.id || (!!a.set && !!b.set && a.set.some(function (e) { return b.set.indexOf(e) >= 0; })));
  }
  function gsmLoopNid(n) {
    var m = /^note (\d+)$/.exec(n.ref || ""),
      p = /^P(\d+)$/.exec(n.ref || ""),
      r = m ? (C.m || [])[+m[1] - 1] : p ? ((C.p && C.p.m) || [])[+p[1] - 1] : null;
    return String((r && r[8]) || n.ref || "").replace(/[^A-Za-z0-9_-]/g, "");
  }
  window.gsmAskLoop = function (k, v) {
    (C.asks && "object" == typeof C.asks) || (C.asks = {});
    C.asks["loop|" + k] = v;
    P();
  };
  function gsmLoops(src) {
    var E = GSMEMO,
      AK = C.asks || {},
      LOW = function (e) {
        return 0 === e || 2 === e || 4 === e;
      },
      ED = [],
      UN = [],
      NO = [];
    src.forEach(function (n) {
      if (!n.note || null == n.em) return;
      var tg = gsmTarget(n),
        t = gsmLoopTarget(n, tg);
      if (!t) return;
      var h = gsmLoopHolder(n, tg);
      h ? h.id !== t.id && !gsmLoopSame(h, t) && ED.push({ n: n, h: h, t: t }) : UN.push({ n: n, t: t });
    });
    var nm = function (g, cap) {
        var w = Gt(g.show),
          th = !g.set && (g.art || /^(board|council|government|department|community|workforce|constituency|agency|staff)$/i.test(g.show));
        return (th ? (cap ? "The " : "the ") : "") + "<b>" + (cap && !th ? gsmCap(w) : w) + "</b>";
      },
      hv = function (g) {
        return g.pl ? "hold" : "holds";
      },
      out = [],
      seen = {};
    function say(a, b, x, y, ask, yes) {
      var ex = E[x.em],
        ey = E[y.em],
        sx = gsmStNB([x]),
        sy = gsmStNB([y]);
      if (ask)
        return (
          nm(a, 1) + " " + hv(a) + " " + ex + " toward " + nm(b) + sx + ". " + gsmCap(ey) + " is also aimed at " + nm(a) + sy +
          ", but that note doesn't say whose it is. If it comes from " + nm(b) + ", the two are in a loop: each side's " + (ex === ey ? ex : "emotion") +
          " is the other side's evidence, so it grows on its own. Does the " + ey + " in " + gsmStRef(y) + " come from " + nm(b) + "?" +
          '<div class="emo"><button type="button" class="ech" onclick="gsmAskLoop(\'' + ask + '\',\'y\')">Yes</button><button type="button" class="ech" onclick="gsmAskLoop(\'' + ask + "','n')\">No</button></div>"
        );
      var h =
        (ex === ey
          ? nm(a, 1) + " and " + nm(b) + " hold " + ex + " toward each other" + gsmStNB([x, y])
          : nm(a, 1) + " " + hv(a) + " " + ex + " toward " + nm(b) + sx + ", and " + nm(b) + " " + hv(b) + " " + ey + " toward " + nm(a) + sy) +
        (yes ? ' <span class="srnb">(you said the ' + ey + " in " + gsmStRef(y) + " comes from them)</span>" : "") +
        ".";
      if (LOW(x.em) && LOW(y.em))
        h += " Each side's " + (ex === ey ? ex : "emotion") + " is the other side's evidence, so each turn of it makes the next more likely, and the two harden together. It weakens only when one side stops answering in kind, or when something the two share comes to matter more than what divides them.";
      else if (1 === x.em && 1 === y.em) h += " Each side's acceptance confirms the other's, so the tie strengthens itself. A tie this close can also shut out everyone outside it.";
      else h += " The tie runs differently in each direction, so what one side means as an opening, the other may not take as one.";
      return h;
    }
    function add(a, b, x, y, ask, yes) {
      var k = [a.id, b.id].sort().join("~");
      if (seen[k]) return;
      seen[k] = 1;
      out.push({ a: a, b: b, x: x, y: y, firm: !ask, ask: !!ask, say: say(a, b, x, y, ask, yes), rank: ask ? 1 : 2 });
    }
    /* both holders named */
    ED.forEach(function (X) {
      ED.forEach(function (Y) {
        X !== Y && X.n !== Y.n && gsmLoopSame(X.h, Y.t) && gsmLoopSame(X.t, Y.h) && add(X.h, X.t, X.n, Y.n);
      });
    });
    /* the note aimed back names no holder: ask */
    ED.forEach(function (X) {
      UN.forEach(function (Y) {
        if (X.n === Y.n || !gsmLoopSame(Y.t, X.h) || (X.t.set && X.t.set.indexOf(Y.n.em) < 0)) return;
        var key = gsmLoopNid(Y.n) + "|" + X.t.id,
          v = AK["loop|" + key];
        "n" === v ? NO.push(X.h, X.t) : add(X.h, X.t, X.n, Y.n, "y" === v ? null : key, "y" === v);
      });
    });
    out = out
      .sort(function (a, b) {
        return b.rank - a.rank;
      })
      .slice(0, 2);
    out.no = NO; /* groups in a loop the person said is not one: WHO STANDS WHERE says nothing more of them */
    return out;
  }
  function gsmStructBuild() {''')

rep('t && (t.textContent = "v279")', 't && (t.textContent = "v280")')
open(p, 'w', encoding='utf-8').write(s)
print('ok')
