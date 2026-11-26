# v294: the story on Pattern Analysis is built from what each workbook holds, not from stock sentences
# written for one workbook (11-13 was told it protects "who decides, what counts as good work, and who
# is safe", and that "the change looks adopted while the old order goes on inside it"). A detector reads
# the notes on the hindering side and the answers to Q.1 and Q.2 and finds what holds the situation in
# place: tradition, livelihoods, fear of failure and blame, what the public and those in power expect,
# a present that feeds itself, and adoption shown but not lived. A finding needs two places in the
# workbook. Sentences about shown-not-lived adoption now need that finding. Applies to every workbook.
p = 'gsm-readable.js'
s = open(p, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, old[:90]); s = s.replace(old, new)

# 1. the detector
rep('''  function gsmStories(mt) {
    if (!mt || mt.querySelector(".stories")) return;''', '''  /* v294: what holds the situation in place, read from the workbook itself. Each finding needs two
     places (notes on the hindering side, or the answers to Q.1 and Q.2). */
  var GSM_HOLD = [
    ["trad", /\\btradition|\\bcentur(?:y|ies)\\b|hundred years|\\bdecades\\b|\\bhistor(?:y|ic)\\b|always been|\\blegacy\\b|entrench|\\bhabits?\\b|ingrained|cultural norm|not broken/i],
    ["liv", /\\bmoney\\b|financ|\\bprofit|occupation|livelihood|\\bemploy|\\bjobs?\\b|\\bcareers?\\b|\\bincome\\b|\\bwages?\\b|\\bcomplex\\b(?! adaptive)|apparatus|\\bearn\\b/i],
    ["fear", /\\bfears?\\b|\\bfeared\\b|afraid|liabilit|\\bescapes?\\b|danger|deadly|\\bblame|disaster|worried|catastroph/i],
    ["expect", /expectation|\\bpublic\\b|politic|\\bmedia\\b|televis|perception|community reaction/i],
    ["loop", /reinforc\\w* (?:the need|itself)|feedback|feeds? (?:on )?itself|vicious|grows? thicker|accumulat/i],
    ["show", /\\bas if\\b|workaround|circumvent|appearance of|in name only|officially adopted|on paper/i],
  ];
  function gsmHolds(texts) {
    var n = {};
    (texts || []).forEach(function (t) {
      var seen = {};
      GSM_HOLD.forEach(function (h) {
        h[1].test(String(t || "")) && !seen[h[0]] && ((seen[h[0]] = 1), (n[h[0]] = (n[h[0]] || 0) + 1));
      });
    });
    return n;
  }
  function gsmHoldTexts() {
    var a = (C && C.a) || [];
    return ((C && C.m) || [])
      .filter(function (t) {
        return t && t[0] >= 1 && t[0] <= 4 && ([0, 2, 4].indexOf(t[5]) >= 0 || ("number" == typeof t[2] && t[2] > 118));
      })
      .map(function (t) {
        return t[3];
      })
      .concat(
        String(a[0] || "").split(/(?<=[.!?;])\\s+|\\n+/),
        String(a[1] || "").split(/(?<=[.!?;])\\s+|\\n+/),
      );
  }
  function gsmStories(mt) {
    if (!mt || mt.querySelector(".stories")) return;
    var HD = gsmHolds(gsmHoldTexts()),
      HAS = function (k) {
        return (HD[k] || 0) >= 2;
      },
      SHOW = HAS("show");''')

# 2. chapters: the goal-side sentences about shown-not-lived adoption need SHOW; content reasons first
rep('''      var wh = where(g),
        o = lowEm(g),''', '''      var wh = where(g),
        gw = "goal" === wh && SHOW,
        HG = gsmHolds(
          g.n
            .filter(function (p) {
              return [0, 2, 4].indexOf(p.e) >= 0 || p.side < 0;
            })
            .map(function (p) {
              return p.txt;
            }),
        ),
        hg = function (k) {
          return (HG[k] || 0) >= 1 && HAS(k);
        },
        o = lowEm(g),''')
rep('''        "goal" === wh
          ? "Close to the goal, the ground drops again, into " +
              emo +
              ". This is the low ground that waits where the change is close to arriving, where a new arrangement can exist in name while the old one goes on underneath it."
          : "mid" === wh''', '''        gw
          ? "Close to the goal, the ground drops again, into " +
              emo +
              ". This is the low ground that waits where the change is close to arriving, where a new arrangement can exist in name while the old one goes on underneath it."
          : "goal" === wh
            ? "Close to the goal, the ground drops again, into " +
              emo +
              ". This resistance does not meet the change at the start; it waits for the change to arrive."
          : "mid" === wh''')
rep('''          ["goal" === wh, "w-goal", "It emerges because a change can ask for new behavior without changing what people are rewarded, trusted, or protected for, and then the old behavior stays the safer one."],''',
    '''          [gw, "w-goal", "It emerges because a change can ask for new behavior without changing what people are rewarded, trusted, or protected for, and then the old behavior stays the safer one."],
          [hg("trad"), "w-trad", "It emerges where a long tradition has made the present way seem like the only sensible one, so the change has to argue against what people take for granted."],
          [hg("liv"), "w-liv", "It emerges where jobs, money, and standing are built around the present way, so changing it costs real people something."],
          [hg("fear"), "w-fear", "It emerges where fear of what happens when something goes wrong, and of who will be blamed, makes holding back the safer choice."],
          [hg("expect"), "w-exp", "It emerges where what the public and those in power expect to see keeps rewarding the present way."],''')
rep('''          ["goal" === wh, "r-goal", "What keeps recreating it is that adoption can be shown without being lived.''',
    '''          [hg("loop"), "r-loop2", "What keeps recreating it is that the present way feeds itself: each round of it leaves conditions that call for more of the same."],
          [gw, "r-goal", "What keeps recreating it is that adoption can be shown without being lived.''')
rep('''        "goal" === wh
          ? "It reveals that in this system adoption and change may not be the same thing: the structure can move while the behavior stays."''',
    '''        gw
          ? "It reveals that in this system adoption and change may not be the same thing: the structure can move while the behavior stays."''')
rep('''          : "goal" === wh
            ? "It matters because it can undo the work after the work looks finished, and because it is the hardest of these low grounds to see."''',
    '''          : gw
            ? "It matters because it can undo the work after the work looks finished, and because it is the hardest of these low grounds to see."''')
rep('''        ("goal" === wh
          ? "If it continues, the system can look changed while behaving as before, and the gap between the two will be taken as proof that the change never worked. Meanwhile, "
          : "") +''', '''        (gw
          ? "If it continues, the system can look changed while behaving as before, and the gap between the two will be taken as proof that the change never worked. Meanwhile, "
          : "") +''')
for k in ['"f-def", ("goal" === wh ? "d" : "Left as it is, d")', '"f-agg", ("goal" === wh ? "a" : "Left as it is, a")', '"f-dis", ("goal" === wh ? "d" : "Left as it is, d")']:
    rep(k, k.replace('"goal" === wh', 'gw'))
rep('''      "goal" === wh && !(window.gsmStructSum || {}).after && S.push("Near the goal''', '''      gw && !(window.gsmStructSum || {}).after && S.push("Near the goal''')
rep('''      chap.push({ x: g.x, wh: wh, e0: e0, acc: acc });''', '''      chap.push({ x: g.x, wh: wh, e0: e0, acc: acc, hg: hg });''')

# 3. what each chapter protects: shown-not-lived practice needs SHOW; otherwise the chapter's own finding
rep('''      practice: {
        what: "practice: the everyday ways of working''', '''      trad: { what: "", why: "", verb: "", obj: "" },
      liv: { what: "", why: "", verb: "", obj: "" },
      fear: { what: "", why: "", verb: "", obj: "" },
      expect: { what: "", why: "", verb: "", obj: "" },
      practice: {
        what: "practice: the everyday ways of working''')
rep('''      var d =
        "goal" === c.wh
          ? "practice"
          : "mid" === c.wh''', '''      var own = ["trad", "liv", "fear", "expect"].filter(function (k) {
          return c.hg(k) && !usedD[k];
        })[0],
        d =
        "goal" === c.wh && SHOW
          ? "practice"
          : own && !(c.acc && !usedD.legit)
            ? own
          : "mid" === c.wh''')
rep('''        practice: "quiet practice under a new name",
      },''', '''        practice: "quiet practice under a new name",
        trad: "the weight of tradition",
        liv: "a defense of the livelihoods built on it",
        fear: "fear of what happens when it goes wrong",
        expect: "what the public and those in power expect",
      },''')
rep('''      hasGoal = CH.some(function (c) {
        return "goal" === c.wh;
      }),''', '''      hasGoal =
        SHOW &&
        CH.some(function (c) {
          return "goal" === c.wh;
        }),''')
rep('''      K = anyAcc ? "legit" : allDef ? "ident" : "order",''', '''      K = anyAcc
        ? "legit"
        : allDef
          ? "ident"
          : ["trad", "liv", "fear", "expect"].sort(function (a, b) {
              return (HD[b] || 0) - (HD[a] || 0);
            }).filter(HAS)[0] || "order",''')

# 4. the opening paragraph: the movement out of sight needs a chapter about place or practice
rep('''      (CH.length >= 2
        ? "With each step the change takes, the resistance moves closer to each person and further out of sight"''', '''      (CH.length >= 2 &&
      CH.some(function (c) {
        return "place" === c.key || "practice" === c.key;
      })
        ? "With each step the change takes, the resistance moves closer to each person and further out of sight"
        : CH.length >= 2
          ? "The resistance does not sit in one place: it meets the change " +
            gsmMeanList(
              CH.map(function (c) {
                return { start: "at the start", mid: "partway to the goal", goal: "close to the goal" }[c.wh];
              }).filter(function (x, i, L) {
                return L.indexOf(x) === i;
              }),
            ).replace(/, and /, ", and again ").replace(/^(at the start) and /, "$1 and again ") +
            ", and it takes the form of " +
            forms.replace(/^the /, "") +
            (HAS("loop") ? ". The present way also feeds itself, so the longer it runs, the more it is needed" : "")''')

# 5. what keeps it going: the workbook's own findings come after the shape-based ones, four at most
rep('''    M.length < 2 && M.push("nothing in the change yet alters what people are trusted, protected, or rewarded for");''',
    '''    var MC = {
      trad: "a long tradition makes the present way look like the only sensible one",
      liv: "jobs, money, and standing are built around the present way, so changing it costs real people something",
      fear: "fear of what happens when something goes wrong, and of who will be blamed, makes holding back the safer choice",
      expect: "what the public and those in power expect to see keeps rewarding the present way",
      loop: "the present way feeds itself: each round of it leaves conditions that call for more of the same",
    };
    ["trad", "liv", "fear", "expect", "loop"].forEach(function (k) {
      HAS(k) && M.length < 4 && M.push(MC[k]);
    });
    M.length < 2 && M.push("nothing in the change yet alters what people are trusted, protected, or rewarded for");''')
open(p, 'w', encoding='utf-8').write(s)
print('v294 part 1 applied')
