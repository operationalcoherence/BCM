# v278: Designer Is the Obstacle on Taking Action, item 4 in his order (queue 11-20; his "#4", 25 Nov 2026 15:57).
# v276's WHO STANDS WHERE already finds it on Pattern Analysis ("the plan relies on the people it distrusts").
# Here it reaches the cards: a card whose notes are the ones that make that reading (the design that turns on
# the group, or the distrust aimed at it) gets a first move that says who designs it, before what gets designed.
# Inactive unless WHO STANDS WHERE makes that reading.
p = 'gsm-readable.js'
s = open(p, encoding='utf-8').read()

def rep(old, new, n=1):
    global s
    c = s.count(old)
    assert c == n, (c, old[:100])
    s = s.replace(old, new)

# 1. keep what made the reading, for Taking Action
rep('''        rank = 4;
        ev = TD.concat(D.filter(function (n) { return n.note; }));''',
'''        rank = 4;
        ev = TD.concat(D.filter(function (n) { return n.note; }));
        var ob = {
          d: D.map(function (n) {
            return n.ref;
          }),
          td: TD.map(function (n) {
            return n.ref;
          }),
          it: it,
          W: art + Gt(w),
        };''')
rep('''      say && out.push({ w: w, stem: w.slice(0, 4).toLowerCase(), say: say, rank: rank, n: hit.length, ev: ev.slice(0, 6) });''',
'''      say && out.push({ w: w, stem: w.slice(0, 4).toLowerCase(), say: say, rank: rank, n: hit.length, ev: ev.slice(0, 6), ob: 4 === rank ? ob : null });''')

# 2. the first move on the cards it lands on
rep('''            function CARD(o) {
              var OV = gsmModeOv(o.key),''',
'''            /* v278: designer is the obstacle */
            var OBS = (SS.groups || []).filter(function (g) {
              return g.ob;
            });
            function OBMOVE(its) {
              var has = {};
              its.forEach(function (x) {
                x && (has[x.id] = 1);
              });
              for (var i = 0; i < OBS.length; i++) {
                var g = OBS[i].ob,
                  hit = g.d.concat(g.td).some(function (r) {
                    return has[r];
                  });
                if (!hit) continue;
                var one = "it" === g.it,
                  tdN = g.td.map(function (r) {
                    return "N" + String(r).replace(/\\D/g, "");
                  });
                return (
                  "Settle who designs it first: the plan turns on " +
                  g.W +
                  ", and your notes distrust " +
                  (one ? "it" : "them") +
                  " (" +
                  phList(tdN) +
                  "). Design it with people who doubt the change, and let " +
                  g.W +
                  " go first in doing what " +
                  (one ? "it asks" : "they ask") +
                  " of others."
                );
              }
              return "";
            }
            function CARD(o) {
              var OV = gsmModeOv(o.key),''')
rep('''              CARDS.push({ S: S, title: o.title, seed: o.seed, ids: its });''',
'''              var obm = OBMOVE(its);
              obm && (o.moves = [obm].concat(o.moves || []));
              CARDS.push({ S: S, title: o.title, seed: o.seed, ids: its, ob: !!obm });''')

rep('t && (t.textContent = "v277")', 't && (t.textContent = "v278")')
open(p, 'w', encoding='utf-8').write(s)
print('ok')
