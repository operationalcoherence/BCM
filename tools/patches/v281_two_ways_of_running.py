# v281: Mode switching, item 7 in his order of the second generation of insight types (queue 11-20;
# mockup approved and "build it", 25 Nov 2026 16:46). TWO WAYS OF RUNNING, a card under WHY IT BEHAVES THIS WAY
# on Pattern Analysis, after A LOOP BETWEEN GROUPS. Where one sentence of an answer sets two different conditions
# ("when the environment is conducive to it" ... but ... "during emergent situations"), the answers may describe
# two ways of running rather than one replacing the other. Words alone can't tell a condition from a time
# ("when it has been adopted"), so the card always asks first (C.asks "mode|<answer>") and explains only on a Yes.
# General words only: condition markers, a contrast word, and the rarest words of each condition.
p = 'gsm-readable.js'
s = open(p, encoding='utf-8').read()

def rep(old, new, n=1):
    global s
    c = s.count(old)
    assert c == n, (c, old[:100])
    s = s.replace(old, new)

# 1. the card, right after A LOOP BETWEEN GROUPS
rep('''    /* v277: RISK AFTER THE GOAL */
    try {
      var AG = gsmAfterGoal();''',
'''    /* v281: TWO WAYS OF RUNNING */
    try {
      var MD = gsmModes(src);
      SS.modes = MD;
      MD && card("TWO WAYS OF RUNNING", MD.say, MD.ev);
    } catch (e) {}
    /* v277: RISK AFTER THE GOAL */
    try {
      var AG = gsmAfterGoal();''')

# 2. the reader
rep('''  function gsmStructBuild() {''', r'''  /* v281: two ways of running. An answer sentence that sets two different conditions, with a contrast word,
     may describe two ways of running. Always asked before it is stated. */
  window.gsmAskMode = function (k, v) {
    (C.asks && "object" == typeof C.asks) || (C.asks = {});
    C.asks["mode|" + k] = v;
    P();
  };
  var GSMCOND = /\b(?:when(?:ever)?|during|in times of|(?:in|on) (?:an? |the )?(?:[a-z-]+\s+){0,2}?(?:situations?|conditions?|times|periods|emergenc(?:y|ies)|crises|crisis|contexts?|environments?|events?|days|weeks|months|seasons?|shifts?|hours))\b/gi,
    GSMCONTRA = /\b(but|while|whereas|yet|otherwise|instead|still|rather|at other times)\b/i,
    GSMTIME = /\b(?:has|have|had) been\b|\b(?:once|after|before|until)\b|\b(?:starts?|begins?|began|started)\b/i,
    GSMMSTOP = /^(all|any|one|two|new|old|not|but|who|how|why|may|has|had|was|its|our|day|days|week|weeks|month|months|season|seasons|shift|shifts|hour|hours|the|a|an|is|are|was|were|be|been|it|its|to|of|and|in|on|at|for|with|this|that|these|those|their|our|there|more|less|very|so|as|by|from|they|them|when|whenever|during|times|time|situation|situations|condition|conditions|environment|environments|context|contexts|event|events|period|periods|things|thing|which|what|where|will|would|can|could|should)$/,
    GSMSWITCH = /\b(switch\w*|shift\w* between|mov\w* between|toggl\w*|trigger\w*|threshold\w*|who decides|decid\w* when|escalat\w*|activat\w*|stand(?:s|ing)? (?:up|down)|declar\w* an? (?:emergenc|incident))\b/i,
    GSMUNEVEN = /\b(unstable|instabilit\w*|conflict[- ]prone|confus\w*|mixed (?:signals|messages)|at odds|out of step)\b/i;
  function gsmModeWords(ph) {
    return ph
      .toLowerCase()
      .replace(/[^a-z\s-]/g, " ")
      .split(/\s+/)
      .filter(function (w) {
        return w.length >= 3 && !GSMMSTOP.test(w);
      });
  }
  function gsmModeConds(sent) {
    var out = [],
      m;
    GSMCOND.lastIndex = 0;
    while ((m = GSMCOND.exec(sent))) {
      var mk = m[0],
        ph,
        show;
      if (/^(?:in|on)\b/i.test(mk) && !/^in times of$/i.test(mk)) {
        ph = mk.replace(/^(?:in|on)\s+/i, "");
        show = mk;
      } else {
        var rest = sent.slice(m.index + mk.length).replace(/^\s+/, ""),
          ws = rest.split(/\s+/),
          keep = [];
        var np = !/^when/i.test(mk); /* "during …" names a time, not a clause: stop before the next verb's subject */
        for (var i = 0; i < ws.length && keep.length < 7; i++) {
          var w = ws[i];
          if (/^(but|while|whereas|yet|then|or|and|so|which|that)$/i.test(w.replace(/\W/g, "")) && keep.length) break;
          if (np && keep.length && /^(is|are|was|were|will|would|can|could|get|gets|go|goes|run|runs|take|takes|come|comes)$/i.test(w.replace(/\W/g, ""))) {
            keep.length > 1 && keep.pop();
            break;
          }
          keep.push(w.replace(/[,;:.!?)]+$/, ""));
          if (/[,;:.!?)]$/.test(w)) break;
        }
        ph = keep.join(" ");
        show = mk + " " + ph;
      }
      if (!ph || GSMTIME.test(ph)) continue;
      var kw = gsmModeWords(ph);
      kw.length && out.push({ at: m.index, show: show.trim().replace(/^./, function (c) { return c.toLowerCase(); }), kw: kw });
    }
    return out;
  }
  function gsmModes(src) {
    var ans = src.filter(function (n) {
        return n.q;
      }),
      all = src.filter(function (n) {
        return "GOAL" !== n.ref;
      }),
      found = null;
    for (var a = 0; a < ans.length && !found; a++) {
      var ss = gsmStSent(ans[a].txt);
      for (var j = 0; j < ss.length && !found; j++) {
        if (!GSMCONTRA.test(ss[j])) continue;
        var cs = gsmModeConds(ss[j]);
        for (var x = 0; x < cs.length && !found; x++)
          for (var y = x + 1; y < cs.length && !found; y++) {
            var shared = cs[x].kw.some(function (w) {
                return cs[y].kw.indexOf(w) >= 0;
              }),
              between = ss[j].slice(cs[x].at, cs[y].at);
            !shared && GSMCONTRA.test(between) && (found = { n: ans[a], sent: ss[j], c: [cs[x], cs[y]] });
          }
      }
    }
    if (!found) return null;
    var key = found.n.ref.replace(/\W/g, ""),
      v = (C.asks || {})["mode|" + key];
    if ("n" === v) return null;
    /* the rarest words of each condition, and where else they come up */
    var lim = Math.max(2, Math.floor(0.4 * all.length));
    function has(n, w) {
      return new RegExp("\\b" + w.slice(0, Math.max(4, Math.min(6, w.length - 1))), "i").test(n.txt);
    }
    var design = function (n) {
      return (n.q && n.q >= 5) || (n.note && n.k >= 5);
    };
    found.c.forEach(function (c) {
      c.w = c.kw.filter(function (w) {
        return (
          all.filter(function (n) {
            return has(n, w);
          }).length <= lim
        );
      });
      c.ties = all.filter(function (n) {
        return (
          n !== found.n &&
          c.w.some(function (w) {
            return has(n, w);
          })
        );
      });
      c.sup = c.ties.filter(function (n) {
        return !design(n) && (3 === n.q || (n.note && n.side > 0));
      });
      c.opp = c.ties.filter(function (n) {
        return !design(n) && (2 === n.q || 1 === n.q || (n.note && n.side < 0));
      });
      c.reach = c.ties.filter(design);
    });
    var c1 = found.c[0],
      c2 = found.c[1],
      ord = ["the first", "the second"],
      B = function (c) {
        return "<b>" + Gt(c.show) + "</b>";
      },
      ev = [gsmStQ(found.n, found.sent, c2.w[0] || c2.kw[0])],
      evSeen = {};
    evSeen[found.n.ref] = 1;
    function addEv(list, c) {
      list.forEach(function (n) {
        var k = c && c.rx ? (n.txt.match(c.rx) || [""])[0].toLowerCase().split(/\s+/)[0] : (c && c.w[0]) || null;
        !evSeen[n.ref] && ev.length < 8 && ((evSeen[n.ref] = 1), ev.push(gsmStQ(n, null, k)));
      });
    }
    var say = "";
    if ("y" !== v) {
      say =
        "<p>Your answers describe two ways of running, not one. " +
        gsmStRef(found.n) +
        " sets one way " +
        B(c1) +
        " and another " +
        B(c2) +
        ".";
      found.c.forEach(function (c, i) {
        c.sup.length
          ? (say += " Support is tied to " + ord[i] + gsmStNB(c.sup) + ".")
          : c.opp.length
            ? (say += " Opposition is tied to " + ord[i] + gsmStNB(c.opp) + ".")
            : c.reach.length && (say += " " + ord[i].charAt(0).toUpperCase() + ord[i].slice(1) + " also comes up in what you would design" + gsmStNB(c.reach) + ".");
        addEv(c.sup.length ? c.sup : c.opp.length ? c.opp : c.reach, c);
      });
      say +=
        "</p><p>If both are meant to stay, the goal is not to replace one way with the other. It is to move between the two as conditions change.</p>" +
        "<p>Is the goal two ways of running, each for its own conditions?</p>" +
        '<div class="emo"><button type="button" class="ech" onclick="gsmAskMode(\'' +
        key +
        "','y')\">Yes</button><button type=\"button\" class=\"ech\" onclick=\"gsmAskMode('" +
        key +
        "','n')\">No</button></div>";
      return { say: say, ev: ev.join(""), ask: 1, key: key };
    }
    var tied = [found.n].concat(c1.sup, c1.opp, c2.sup, c2.opp),
      unev = all.filter(function (n) {
        return GSMUNEVEN.test(n.txt);
      }),
      sw = all.filter(function (n) {
        return design(n) && GSMSWITCH.test(n.txt);
      }),
      reach = c1.reach.concat(
        c2.reach.filter(function (n) {
          return c1.reach.indexOf(n) < 0;
        }),
      );
    say =
      "<p>The goal is two ways of running, each for its own conditions: one " +
      B(c1) +
      ", the other " +
      B(c2) +
      gsmStNB(tied) +
      '. <span class="srnb">(you said the goal is two ways of running)</span></p>' +
      "<p>So neither way replaces the other; each is kept for its own conditions. What makes or breaks the goal is the switch: who decides that conditions have changed, and what tells them.</p>";
    var sideOf = function (c) {
      return c.sup.length && !c.opp.length ? "s" : c.opp.length && !c.sup.length ? "o" : "";
    };
    var s1 = sideOf(c1),
      s2 = sideOf(c2);
    s1 && s2 && s1 !== s2 &&
      (say +=
        "<p>Each side already wants one of the two: " +
        ("o" === s1 ? "opposition " + ord[0] + gsmStNB(c1.opp) + ", support " + ord[1] + gsmStNB(c2.sup) : "support " + ord[0] + gsmStNB(c1.sup) + ", opposition " + ord[1] + gsmStNB(c2.opp)) +
        ".</p>");
    say += "<p>The risk is an uneven switch: some people working one way while others work the other." + (unev.length ? " Your answers point to it" + gsmStNB(unev) + "." : "") + "</p>";
    say += sw.length
      ? "<p>What you would design says how the switch is made" + gsmStNB(sw) + ".</p>"
      : reach.length
        ? "<p>What you would design reaches part of this" + gsmStNB(reach) + ", but nothing yet says who decides when to switch, or how.</p>"
        : "<p>Nothing you would design yet says who decides when to switch, or how.</p>";
    addEv(c1.sup.concat(c1.opp, c2.sup, c2.opp), c2);
    addEv(unev, { rx: GSMUNEVEN });
    sw.length ? addEv(sw, { rx: GSMSWITCH }) : addEv(reach, c2);
    return { say: say, ev: ev.join(""), ask: 0, key: key, conds: [c1.show, c2.show], refs: tied.map(function (n) { return n.ref; }) };
  }
  function gsmStructBuild() {''')

# 3. version label
rep('t && (t.textContent = "v280");', 't && (t.textContent = "v281");')

open(p, 'w', encoding='utf-8').write(s)
print('ok')
