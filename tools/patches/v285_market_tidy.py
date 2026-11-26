# v285: tidy for market (his call, 25 Nov 2026 18:31: "delete repeats, consolidate where possible,
# tidy up, make engine fixes, focus on UI"). Engine fixes only; no wording of his changed.
# 1. IN YOUR ANSWERS, NOT ON THE MAP: the same phrase is never asked twice ("emergent situations" x2).
# 2. The Q.5-Q.7 lists (Not in Q.5-Q.7 yet, For and against, Unused support, Q.5-Q.7 only):
#    each phrase once; a phrase that is a piece of a longer one in the same list goes;
#    a single word is not stated (his rule), except the five emotion names.
# 3. RUNS TOGETHER never quotes the goal back to the user when a note or answer says it too.
# 4. Card maps: "doubles back 1 times" / "1 time" read "once".
# 5. EMERGING and MORE INFORMATION NEEDED: no fragments of contractions ("dont fix").
# 6. DOES THIS ANSWER THE GOAL?: a preposition ("among") never pairs a hindrance with a response.
p = 'gsm-readable.js'
s = open(p, encoding='utf-8').read()

def rep(old, new, n=1):
    global s
    c = s.count(old)
    assert c == n, (c, old[:100])
    s = s.replace(old, new)

# shared helpers, defined once near gsmPhNameH
rep('''  function gsmPhNameH(key, ctx) {''', '''  /* v285: one phrase, said once */
  var GSM_EMOW = /^(accept|indiff|distru|aggres|defian)/;
  var GSM_CONTR = /\\b(dont|doesnt|didnt|isnt|arent|wasnt|werent|cant|couldnt|wont|wouldnt|shouldnt|havent|hasnt|hadnt|aint)\\b/;
  function gsmPhOnce(keys, name) {
    var nm = keys.map(function (k) {
        return { k: k, n: String(name(k) || "").toLowerCase().replace(/[^a-z0-9]+/g, " ").trim() };
      }),
      seen = {};
    return nm
      .filter(function (o) {
        if (!o.n || GSM_CONTR.test(o.n)) return !1;
        if (o.n.indexOf(" ") < 0 && !GSM_EMOW.test(o.n)) return !1;
        if (seen[o.n]) return !1;
        if (
          nm.some(function (x) {
            return x.n !== o.n && x.n.length > o.n.length && (" " + x.n + " ").indexOf(" " + o.n + " ") >= 0;
          })
        )
          return !1;
        return (seen[o.n] = 1);
      })
      .map(function (o) {
        return o.k;
      });
  }
  function gsmPhNameH(key, ctx) {''')

# 1. theme asks: once per phrase, and not again when WQ already asks it
rep('''          WD = WD.filter(function (c) {
            return !one(c);
          });''', '''          WD = WD.filter(function (c) {
            return !one(c);
          });
          /* v285: never ask the same phrase twice */
          var asked = {};
          WQ.concat(SH).forEach(function (c) {
            asked[String(jt(c.key)).toLowerCase()] = 1;
          });
          WD = WD.filter(function (c) {
            var n = String(gsmPhName(c.key).ph || "").toLowerCase();
            return !asked[n] && (asked[n] = 1);
          });''')

# 2. the lists
rep('''              var e = st[t];
              e &&
                ((e = e.sort(function (t, e) {
                  var n = t.indexOf(" ") > 0 ? p[t] : g[t];
                  return (e.indexOf(" ") > 0 ? p[e] : g[e]) - n;
                })),''', '''              var e = st[t];
              e &&
                (e = gsmPhOnce(e, function (k) {
                  return gsmPhName(k, "unanswered" === t || "condition" === t).ph || jt(k);
                })).length &&
                ((e = e.sort(function (t, e) {
                  var n = t.indexOf(" ") > 0 ? p[t] : g[t];
                  return (e.indexOf(" ") > 0 ? p[e] : g[e]) - n;
                })),''')

# 3. RUNS TOGETHER: quote a note or answer, not the goal, when one carries the words
rep('''    var q = gsmMeanQuote(all.slice(), rx),''', '''    var ng = all.filter(function (o) {
        return "GOAL" !== o.s.ref;
      }),
      q = gsmMeanQuote((ng.length ? ng : all).slice(), rx),''')

# 4. once, not "1 times"
rep('''                      : "Crosses the help and hinder line " +
                      l +
                      (1 === l ? " time" : " times") +''', '''                      : "Crosses the help and hinder line " +
                      (1 === l ? "once" : l + " times") +''')
rep('''                        ? " It is marked a program, but the way through it doubles back " +
                          l +
                          " times across the line. It may not run straight through as a program needs to."''', '''                        ? " It is marked a program, but the way through it doubles back " +
                          (1 === l ? "once" : l + " times") +
                          " across the line. It may not run straight through as a program needs to."''')
# the reader of that line on cards (v284) parses the old form; keep it matching both
rep('''/^Crosses the help and hinder line .*?goal\\./''', '''/^Crosses the help and hinder line .*?goal\\./''')

# 5. EMERGING: no contraction fragments
rep('''                1 === (p[e] || 0) &&
                  nn.length < 2 &&''', '''                1 === (p[e] || 0) &&
                  nn.length < 2 &&
                  !GSM_CONTR.test(e) &&''')

# 6. prepositions never pair a hindrance with a response
rep('''                  !CM[k] &&
                  !/^(aggres|hostil|anger|angry|accept|distru|mistru|suspic|indiff|apath|defian|defiant|rebel)/.test(k) &&''', '''                  !CM[k] &&
                  !/^(aggres|hostil|anger|angry|accept|distru|mistru|suspic|indiff|apath|defian|defiant|rebel)/.test(k) &&
                  !/^(among|amongst|within|without|toward|towards|across|between|upon|via|per|despite|beyond|throughout|onto|into|unto)$/.test(k) &&''')

rep('t.textContent = "v284"', 't.textContent = "v285"')
open(p, 'w', encoding='utf-8').write(s)
print('ok')

# 4b. the card reader (v284) parses the count; read "once" too
s = open(p, encoding='utf-8').read()
rep('''var mn = mm && /line (\\d+) times?; ([\\d.]+)\\u00d7/.exec(mm[0]);''',
    '''var mn = mm && /line (?:(\\d+) times?|(once)); ([\\d.]+)\\u00d7/.exec(mm[0]);
      mn && (mn = [mn[0], mn[1] || "1", mn[3]]);''')
# 6b. generic verbs never pair either
rep('''!/^(among|amongst|within|without|toward|towards|across|between|upon|via|per|despite|beyond|throughout|onto|into|unto)$/.test(k) &&''',
    '''!/^(among|amongst|within|without|toward|towards|across|between|upon|via|per|despite|beyond|throughout|onto|into|unto)$/.test(k) &&
                  !/^(contin\\w*|begin\\w*|began|start\\w*|becom\\w*|make|made|take|took|get|got|go|went|come|came|use|used|need\\w*|want\\w*|seem\\w*|keep|kept|give|gave)$/.test(k) &&''')
open(p, 'w', encoding='utf-8').write(s)
print('ok2')
