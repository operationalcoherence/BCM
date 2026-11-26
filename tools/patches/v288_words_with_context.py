# v288: the halfway measure on the one-word rule (his yes, 25 Nov 2026 19:19).
# A single word is stated again when it (1) reads as a thing in the user's own words: somewhere it follows
# a/an/the/this/that/these/those/their/our/its/his/her/my/your/each/every/no/any, with at most one word
# between ("a stable lease"); (2) comes up in at least two differently worded places (goal, answers, notes);
# and (3) is always shown with its context: the user's own clause, and where it is ("N5").
# Emotion names still always count. Applies to the v285 and v287 places.
p = 'gsm-readable.js'
s = open(p, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, old[:90]); s = s.replace(old, new)

rep('''  function gsmPhOnce(keys, name) {''', r'''  /* v288: a single word that reads as a thing, said with its context */
  var GSM_DET = /^(a|an|the|this|that|these|those|their|our|its|his|her|my|your|each|every|no|any)$/i;
  function gsmThing(stem) {
    stem = String(stem || "").toLowerCase().replace(/[^a-z]/g, "");
    if (stem.length < 3 || /^(thing|way|part|idea|kind|sort|lot|number|fact|case|point|area|level|form|type|side|time|end)/.test(stem)) return null;
    if (GSM_EMOW.test(stem)) return { ctx: "", lab: "" };
    var src = gsmMeanSrc(),
      where = {},
      det = !1,
      best = null,
      hit = function (w) {
        w = w.toLowerCase().replace(/[^a-z]/g, "");
        return w.length >= 4 && 0 === w.indexOf(stem) && w.length - stem.length <= 3;
      };
    src.forEach(function (o) {
      String(o.txt)
        .replace(/\s+/g, " ")
        .split(/(?<=[.!?;])\s+|\n+/)
        .forEach(function (se) {
          var w = se.split(" "),
            any = !1;
          w.forEach(function (x, i) {
            if (!hit(x)) return;
            any = !0;
            var cl = function (y) {
                return String(y || "").replace(/[^a-z]/gi, "");
              },
              nx = cl(w[i + 1]),
              head = /[,;:.!?)"\u201d]$/.test(x) || !nx || StStop.test(nx) || /^(that|which|who|whom|whose|where|while|so|because)$/i.test(nx);
            head &&
              (GSM_DET.test(cl(w[i - 1])) || (GSM_DET.test(cl(w[i - 2])) && !/[,;:]$/.test(w[i - 1] || ""))) &&
              (det = !0);
          });
          if (!any) return;
          where[o.lab] = 1;
          var n = w.length,
            sc = (o.note ? 0 : 20) + (n > 16 ? n : 0) + ("GOAL" === o.ref ? 40 : 0);
          (!best || sc < best.sc) && (best = { sc: sc, t: se.trim(), lab: o.lab });
        });
    });
    if (!det || Object.keys(where).length < 2 || !best) return null;
    var tw = best.t.replace(/[.;]+$/, "").split(" ");
    if (tw.length > 14) {
      var at = 0;
      tw.forEach(function (x, i) {
        hit(x) && !at && (at = i);
      });
      var a = Math.max(0, Math.min(at - 5, tw.length - 14));
      tw = (a ? ["…"] : []).concat(tw.slice(a, a + 14), a + 14 < tw.length ? ["…"] : []);
    }
    return { ctx: tw.join(" ").replace(/^… /, "…").replace(/ …$/, "…"), lab: best.lab };
  }
  function gsmThingSay(stem, word) {
    var t = gsmThing(stem);
    return t && t.ctx ? "<b>" + Gt(word || stem) + "</b>: “" + Gt(t.ctx) + "” (" + Gt(t.lab) + ")" : "";
  }
  function gsmPhOnce(keys, name) {''')

# v285 lists: a single word passes when it reads as a thing
rep('''        if (o.n.indexOf(" ") < 0 && !GSM_EMOW.test(o.n)) return !1;''',
    '''        if (o.n.indexOf(" ") < 0 && !GSM_EMOW.test(o.n) && !gsmThing(o.k)) return !1;''')
# ...and is shown with its context
rep('''                    .map(function (k) {
                      return gsmPhNameH(k, "unanswered" === t || "condition" === t);
                    })''', '''                    .map(function (k) {
                      var nm1 = gsmPhName(k, "unanswered" === t || "condition" === t).ph || jt(k);
                      return (String(nm1).indexOf(" ") < 0 && gsmThingSay(k, nm1)) || gsmPhNameH(k, "unanswered" === t || "condition" === t);
                    })''')

# v287 word overlaps
rep('''          return i[e].k[t] && (t.indexOf(" ") > 0 || GSM_EMOW.test(t));''',
    '''          return i[e].k[t] && (t.indexOf(" ") > 0 || GSM_EMOW.test(t) || !!gsmThing(t));''')
rep('''    function uo(t, e) {
      return (
        (e = e || 3),
        t
          .slice(0, e)
          .map(function (t) {
            return "<b>" + Gt(jt(t)) + "</b>";
          })
          .join(", ")
      );
    }''', '''    function uo(t, e) {
      return (
        (e = e || 3),
        t
          .slice(0, e)
          .map(function (t) {
            /* v288: a single word comes with its context */
            return (t.indexOf(" ") < 0 && !GSM_EMOW.test(t) && gsmThingSay(t, jt(t))) || "<b>" + Gt(jt(t)) + "</b>";
          })
          .join(t.slice(0, e).some(function (x) {
            return x.indexOf(" ") < 0 && !GSM_EMOW.test(x);
          }) ? "; " : ", ")
      );
    }''')

# WHERE THESE MEET
rep('''            return !o.w || o.k.slice(2).indexOf(" ") > 0 || GSM_EMOW.test(o.k.slice(2));''',
    '''            return !o.w || o.k.slice(2).indexOf(" ") > 0 || GSM_EMOW.test(o.k.slice(2)) || !!gsmThing(o.k.slice(2));''')
rep('''                if (o.w) lab = "The word “" + Gt(nm[o.k] || r) + "”";''',
    '''                if (o.w) {
                  lab = "“" + Gt(nm[o.k] || r) + "”";
                  var th = gsmThing(r);
                  th && th.ctx && (tx = th.ctx, lab += " (" + Gt(th.lab) + ")");
                }''')

# POSSIBLE PATTERNS
rep('''                    if (a.length && String(a[0]).indexOf(" ") < 0 && !GSM_EMOW.test(String(a[0]).toLowerCase())) return;''',
    '''                    if (a.length && String(a[0]).indexOf(" ") < 0 && !GSM_EMOW.test(String(a[0]).toLowerCase()) && !gsmThing(a[0])) return;''')

rep('t.textContent = "v287"', 't.textContent = "v288"')
open(p, 'w', encoding='utf-8').write(s); print('ok')

s = open(p, encoding='utf-8').read()
# the second mention in one finding is the word alone
rep('''                    ? " For " +
                        uo([w[0]]) +
                        ", the notes below the line are " +''', '''                    ? " For " +
                        "<b>" + Gt(jt(w[0])) + "</b>" +
                        ", the notes below the line are " +''')
# WHERE THESE MEET: a word whose context is a note already listed is not listed again
rep('''                if (o.w) {
                  lab = "“" + Gt(nm[o.k] || r) + "”";
                  var th = gsmThing(r);
                  th && th.ctx && (tx = th.ctx, lab += " (" + Gt(th.lab) + ")");
                }''', '''                if (o.w) {
                  lab = "“" + Gt(nm[o.k] || r) + "”";
                  var th = gsmThing(r);
                  if (
                    th &&
                    out.some(function (x) {
                      var mx = /^note (\\d+)$/.exec(x.k.slice(2)) || /^P(\\d+)$/.exec(x.k.slice(2));
                      return !x.w && (mx ? "N" + mx[1] : x.k.slice(2)) === th.lab;
                    })
                  )
                    return "";
                  th && th.ctx && ((tx = th.ctx), (lab += " (" + Gt(th.lab) + ")"));
                }''')
open(p, 'w', encoding='utf-8').write(s); print('ok3')
