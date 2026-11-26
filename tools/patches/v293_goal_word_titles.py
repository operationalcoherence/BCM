# v293a: a Taking Action title must not name only the goal's own words (his "vague 11-13 title":
# 'Redesign "aggressive suppression" with those who oppose it'). When the card's phrase is all goal
# words, the title names the clause of the note the card rests on instead, hindering notes first,
# with its id. Applies to every workbook.
p = 'gsm-readable.js'
s = open(p, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, old[:90]); s = s.replace(old, new)
rep('''    var ph = q(p0),
      fm = (function () {''',
'''    /* v293: a phrase made only of the goal's own words says nothing the goal doesn't; name the note the card
       rests on instead (hindering notes first: aggression, distrust, defiance), with its id */
    var nid = "",
      fromHinder = 0;
    (function () {
      var D = window.gsmData ? window.gsmData() : { goal: "", m: [] },
        G = " " + String(D.goal || "").toLowerCase().replace(/[^a-z0-9 -]/g, " ").replace(/\\s+/g, " ") + " ";
      if (p0.indexOf(" ") < 0 || G.indexOf(" " + p0.toLowerCase().replace(/\\s+/g, " ") + " ") < 0) return;
      var ns = Object.keys(gsmTAIds(c))
          .concat((why.match(/\\bN\\d+\\b/g) || []).map(gsmTANorm))
          .map(function (x) {
            return (/^note (\\d+)$/.exec(x) || [])[1];
          })
          .filter(function (x, i, a) {
            return x && a.indexOf(x) === i;
          }),
        rk = function (n) {
          var r = (D.m || [])[+n - 1];
          return r && [0, 2, 4].indexOf(r[5]) >= 0 ? 0 : 1;
        };
      ns.sort(function (x, y) {
        return rk(x) - rk(y);
      });
      for (var i = 0; i < ns.length; i++) {
        var r = (D.m || [])[+ns[i] - 1],
          g = r ? gsmTAClause(r[3]) : "";
        /* one note names one card: a card asked again keeps the note it got the first time */
        if (g && G.indexOf(" " + g.toLowerCase() + " ") < 0 && (c._tanid === ns[i] || (!c._tanid && !GSM_TA_USED["n|" + ns[i]]))) {
          GSM_TA_USED["n|" + ns[i]] = 1;
          c._tanid = ns[i];
          p0 = g;
          nid = "N" + ns[i];
          fromHinder = !rk(ns[i]);
          return;
        }
      }
    })();
    var ph = q(p0) + (nid ? " (" + nid + ")" : ""),
      fm = (function () {''')
rep('''        [/^Redesign it with those who oppose it/, "Redesign " + ph + " with those who oppose it"],''',
    '''        [/^Redesign it with those who oppose it/, "Redesign " + ph + (fromHinder ? " with the people who hold it" : " with those who oppose it")],''')
rep('t.textContent = "v292"', 't.textContent = "v293"')
open(p, 'w', encoding='utf-8').write(s)
print('v293a applied')
