"""v237: Way A on strategy cards follows the path the data gives (his review note 6a, 11-19:
"Way A should reflect the strategy pathway or trajectory necessary to move towards the goal... An accurate way is a good way").
Before: START, then the card's notes left to right, then GOAL (a zigzag that said nothing about the ground).
Now, the same route THE WAY ACROSS reads in words:
  START -> the card's low-ground notes, emotion nearest the ridge first (distrust, then aggression, defiance last),
  left to right within each -> the ridge of indifference nearest the first of them -> the acceptance on the help side
  nearest that ridge -> GOAL.
With no ridge on the map it climbs straight to acceptance (bare rock); with no low-ground notes it falls back to the old way.
Programs, and ways B and C, are unchanged. Usage: python3 v237_way_a_follows_data.py gsm-readable.js"""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)
rep('''      ROUTES.push({ key: "A", name: "Its way through its notes", pts: own, st: routeStats(own), dash: [] });''',
'''      /* v237: on a strategy, way A is the path the data gives: low ground (nearest the ridge first, defiance last),
         over the nearest ridge of indifference, up to the acceptance above it, then the goal */
      var aName = "Its way through its notes";
      if (cd.mode === "STRATEGY") {
        var STEP = { 2: 1, 0: 2, 4: 3 },
          lowNs = ns.filter(function (n) {
            return null != n.e && null != STEP[n.e];
          });
        if (lowNs.length) {
          lowNs.sort(function (a, b) {
            return STEP[a.e] - STEP[b.e] || a.x - b.x;
          });
          var allN = (terr && terr.notes) || [],
            near = function (list, p) {
              return (
                list.slice().sort(function (a, b) {
                  return Math.hypot(a.x - p.x, a.y - p.y) - Math.hypot(b.x - p.x, b.y - p.y);
                })[0] || null
              );
            },
            rgN = near(
              allN.filter(function (n) {
                return 3 === n.e;
              }),
              lowNs[0],
            ),
            tgN = near(
              allN.filter(function (n) {
                return 1 === n.e && n.y < 118;
              }),
              rgN || lowNs[0],
            ),
            seq = lowNs.concat(rgN ? [rgN] : []).concat(tgN ? [tgN] : []);
          own = viaPts(
            [[START.x, START.y]]
              .concat(
                seq.map(function (n) {
                  return [n.x, n.y];
                }),
              )
              .concat([[GOAL.x, GOAL.y]]),
          );
          aName =
            "The way the ground points: " +
            list(
              lowNs.slice(0, 4).map(function (n) {
                return "N" + n.k;
              }),
            ) +
            (rgN ? ", over the ridge at N" + rgN.k : ", straight up over bare rock") +
            (tgN ? ", up to acceptance at N" + tgN.k : "");
        }
      }
      ROUTES.push({ key: "A", name: aName, pts: own, st: routeStats(own), dash: [] });''')
rep('t && (t.textContent = "v236");', 't && (t.textContent = "v237");')
open(P, "w").write(s)
print("ok")
