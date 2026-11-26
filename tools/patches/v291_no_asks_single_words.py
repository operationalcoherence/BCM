# v291: third tidy pass on Pattern Analysis (his go-ahead 25 Nov 2026 21:22).
#  1. His rule (19:28): no one-tap questions just to cover what the engine can't tell. Removed:
#     "Is it a theme?" (both kinds), "Does it serve the goal?", the A LOOP BETWEEN GROUPS question,
#     and the TWO WAYS OF RUNNING question. Each finding now says what it can without asking.
#     Kept: THE SAME THING? (his rule: never merge words unless he says) and DOES THIS ANSWER THE GOAL?
#     (he renamed it today; flagged to him).
#  2. His single-word rule, enforced where it still leaked: the word lists in WHAT STANDS OUT
#     (uo), the "For <word>:" line in CROSSES THE GROUND LINE, and WHAT YOU WOULD DO
#     ("deals yet with yet (N3), strong (N7)…").
#  3. gsmThing: "that/this/these/those" after a noun is a relative word, not a determiner
#     ("constraints that permit" no longer makes "permit" a thing).
#  4. ONE EMOTION, SEVERAL TARGETS: the people-versus-ideas sentence is said once, not per emotion.
#  5. POSSIBLE PATTERNS: the generic "“x” sits behind two findings at once" lines are dropped.
p = 'gsm-readable.js'
s = open(p, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, old[:90]); s = s.replace(old, new)

# 3 + helper
rep('''              (GSM_DET.test(cl(w[i - 1])) ||''', '''              (((GSM_DET.test(cl(w[i - 1])) && !(/^(that|this|these|those)$/i.test(cl(w[i - 1])) && i > 1 && !/^(of|in|on|to|for|with|about|at|by|from|into|is|was|are|were|be|and|or|but|all)$/i.test(cl(w[i - 2]))))) ||''')
rep('''  function gsmThingSay(stem, word) {''', '''  /* v291: a word may be stated alone only as a phrase, an emotion, or a thing (his rule, 25 Nov) */
  function gsmOkW(t) {
    t = String(t || "").trim();
    return t.indexOf(" ") > 0 || GSM_EMOW.test(t.toLowerCase()) || !!gsmThing(t);
  }
  function gsmThingSay(stem, word) {''')

# 2a uo
rep('''    function uo(t, e) {
      return (
        (e = e || 3),
        t
          .slice(0, e)''', '''    function uo(t, e) {
      /* v291: single words that are not things are not stated */
      var ok = t.filter(gsmOkW);
      if (!ok.length) return t.length > 1 ? "The words they share" : "The wording";
      t = ok;
      return (
        (e = e || 3),
        t
          .slice(0, e)''')
# 2b CROSSES "For <word>:"
rep('''                  var t = j(w[0]);
                  return t[0] && t[1]
                    ? " For " +''', '''                  var t = j(w[0]);
                  return t[0] && t[1] && gsmOkW(w[0])
                    ? " For " +''')
# 2c WHAT YOU WOULD DO
rep('''                un = FR.unanswered || [],
                an = FR.answered || [];''', '''                un = (FR.unanswered || []).filter(function (k) {
                  return gsmOkW(gsmPhName(k, 1).ph || k);
                }),
                an = FR.answered || [];''')

# 1a loop question
rep('''          " is the other side's evidence, so it grows on its own. Does the " + ey + " in " + gsmStRef(y) + " come from " + nm(b) + "?" +
          '<div class="emo"><button type="button" class="ech" onclick="gsmAskLoop(\\'' + ask + '\\',\\'y\\')">Yes</button><button type="button" class="ech" onclick="gsmAskLoop(\\'' + ask + "','n')\\">No</button></div>"''',
    '''          " is the other side's evidence, so it grows on its own. Whose it is decides whether this is a loop: worth finding out before acting on either side."''')
# 1b two ways
rep('''        "</p><p>If both are meant to stay, the goal is not to replace one way with the other. It is to move between the two as conditions change.</p>" +
        "<p>Is the goal two ways of running, each for its own conditions?</p>" +
        '<div class="emo"><button type="button" class="ech" onclick="gsmAskMode(\\'' +
        key +
        "','y')\\">Yes</button><button type=\\"button\\" class=\\"ech\\" onclick=\\"gsmAskMode('" +
        key +
        "','n')\\">No</button></div>";''', '''        "</p><p>If both are meant to stay, the goal is not to replace one way with the other. It is to move between the two as conditions change.</p>";''')
# 1c theme questions (two blocks)
rep('''" in one note at most. A phrase can be a theme or just wording, and Patterns cannot tell which, so it asks.</p>" +''',
    '''" in one note at most, so the map has not caught up with it yet.</p>" +''', 2)
rep('''                    Gt(jt(c.key)) +
                    '” Is it a theme?<div class="emo"><button type="button" class="ech" onclick="gsmAskT(' +
                    i +
                    ',\\'y\\')">Yes</button><button type="button" class="ech" onclick="gsmAskT(' +
                    i +
                    ",'n')\\">No</button></div></div>"''', '''                    Gt(jt(c.key)) +
                    "”</div>"''')
rep('''                    Gt(gsmPhName(c.key).ph) +
                    '” Is it a theme?<div class="emo"><button type="button" class="ech" onclick="gsmAskW(' +
                    i +
                    ',\\'y\\')">Yes</button><button type="button" class="ech" onclick="gsmAskW(' +
                    i +
                    ",'n')\\">No</button></div></div>"''', '''                    Gt(gsmPhName(c.key).ph) +
                    "”</div>"''')
# 1d serve the goal
rep('''" off the goal or only worded differently, and Patterns cannot tell which, so it asks.</p>" +''',
    '''" off the goal, or the goal may only be worded differently.</p>" +''')
rep('''                    "” Does it serve the goal?" +
                    '<div class="emo"><button type="button" class="ech" onclick="gsmAskG(\\'' +
                    id +
                    '\\',\\'y\\')">Yes</button><button type="button" class="ech" onclick="gsmAskG(\\'' +
                    id +
                    "','n')\\">No</button></div></div>"''', '''                    "”</div>"''')

# 4 ONE EMOTION: say the people/ideas sentence once
rep('''      out.push({ em: +em, say: say, groups: G, n: L.length });
    });
    return out
      .sort(function (a, b) {
        return b.groups.length - a.groups.length || b.n - a.n;
      })
      .slice(0, 2);''', '''      out.push({ em: +em, say: say, groups: G, n: L.length, mv: P.length && O.length ? " " + gsmCap(e) + " aimed at people moves with what those people are seen to do; aimed at an idea or a thing, it moves with what people see of it at work." : "" });
    });
    out = out
      .sort(function (a, b) {
        return b.groups.length - a.groups.length || b.n - a.n;
      })
      .slice(0, 2);
    /* v291: the people-versus-ideas sentence once */
    out[1] && out[0].mv && out[1].mv && (out[1].say = out[1].say.replace(out[1].mv, ""));
    return out;''')

# 5 POSSIBLE PATTERNS: drop the generic meta lines
rep('''                      var c = a.length ? "<b>“" + Gt(a[0]) + "”</b>" : s[0],''', '''                      if (!l) return; /* v291: the generic "sits behind two findings" line adds little */
                      var c = a.length ? "<b>“" + Gt(a[0]) + "”</b>" : s[0],''')

# 6. follow-ups found in testing
# 6a. the serve-the-goal notes carry a class so gsmGoalQ still moves them to Taking Action
rep("""                  return (
                    '<div style="margin:6px 0 10px">' +
                    x[0] +
                    " “" +""", """                  return (
                    '<div class="gq" style="margin:6px 0 10px">' +
                    x[0] +
                    " “" +""")
rep("""    [].slice.call(Rt.querySelectorAll('[onclick^="gsmAskG"]')).forEach(function (b) {
      var d = b.closest(".emo");
      d = d && d.parentElement;
      if (!d || gl.indexOf(d) >= 0) return;
      var pv = d.previousElementSibling;
      while (pv && "P" !== pv.tagName && pv.querySelector && pv.querySelector('[onclick^="gsmAskG"]')) pv = pv.previousElementSibling;""", """    [].slice.call(Rt.querySelectorAll(".gq")).forEach(function (d) {
      if (gl.indexOf(d) >= 0) return;
      var pv = d.previousElementSibling;
      while (pv && pv.classList && pv.classList.contains("gq")) pv = pv.previousElementSibling;""")
# 6b. a finding whose words were all single non-things has nothing left to say: drop it
rep("""      var w = gsmMeanWords(body),
        d = w.length ? gsmMeanData(w) : { q: "", notes: [], em: -1, help: -1, hind: -1 },""", """      var w = gsmMeanWords(body);
      if (!w.length && /^(The words they share|The wording)\\b/.test(body.textContent.trim())) {
        r.parentNode && r.parentNode.removeChild(r);
        return;
      }
      var d = w.length ? gsmMeanData(w) : { q: "", notes: [], em: -1, help: -1, hind: -1 },""")
# 6c. the "For <word>," clause in CONDITION IN THE WAY follows the same rule
rep("""                  var t = j(w[0]);
                  return t[1]
                    ? " For " +
                        "<b>" + Gt(jt(w[0])) + "</b>" +""", """                  var t = j(w[0]);
                  return t[1] && gsmOkW(w[0])
                    ? " For " +
                        "<b>" + Gt(jt(w[0])) + "</b>" +""")

# 7. One first move. THE CHEAPEST FIRST MOVE names the cards to start with; the old "Decide <word> first"
#    note under it named a second, vaguer first and is dropped when the first move is shown. WHERE TO
#    START on Pattern Analysis now names the same cards.
rep("""                Qn +""", """                (TAT && TAT.indexOf("tafirst") >= 0 ? "" : Qn) +""")
rep("""              var W = window.gsmWS;
              out += P0(
                "WHERE TO START",
                W
                  ? "Taking Action puts " +""", """              var W = window.gsmWS;
              out += P0(
                "WHERE TO START",
                W
                  ? '<span class="gsmws2"></span>' + "Taking Action puts " +""")
rep("""          a && o && (fm.innerHTML = fm.innerHTML.split("\\u201c" + Gt(o) + "\\u201d").join("\\u201c" + Gt(a.textContent) + "\\u201d"));
        });
    }""", """          a && o && (fm.innerHTML = fm.innerHTML.split("\\u201c" + Gt(o) + "\\u201d").join("\\u201c" + Gt(a.textContent) + "\\u201d"));
        });
      /* v291: WHERE TO START on Pattern Analysis says the same first move */
      var w2 = Rt.querySelector(".gsmws2");
      fm && w2 && w2.parentNode && (w2.parentNode.innerHTML = "On Taking Action: " + fm.innerHTML.charAt(0).toLowerCase() + fm.innerHTML.slice(1));
    }""")


rep('t.textContent = "v290"', 't.textContent = "v291"')
open(p, 'w', encoding='utf-8').write(s)
print('v291 applied')
