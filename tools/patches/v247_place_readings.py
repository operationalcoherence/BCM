"""v247: a place map's written reading (WHAT THE GROUND SAYS, under the Synthesis map) drops the line map's language
(his yes 11-19 14:50: "yes to losing the line map language in place maps").
On a place map the reading list is now the same place reading the tours use since v244 (placeStops): where each emotion
gathers, where distant emotions sit closest, and what the goal sits among, under the place act names. This also mends a
mismatch from v244: the numbered markers on the 3D followed the place stops while the list under it still showed the
line-map readings. The line map's readings are unchanged. Usage: python3 v247_place_readings.py gsm-readable.js"""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)
rep('''      READ = R.slice(0, 13);
    }''',
'''      READ = R.slice(0, 13);
      /* v247: a place reads as a place (the same reading as its tour), never ridges, hollows, or wells */
      if (PLACE)
        try {
          READ = placeStops()
            .filter(function (r) {
              return r.at;
            })
            .map(function (r) {
              return { grp: r.grp, title: r.title, short: r.cap, more: "", at: r.at, kind: "place" };
            });
        } catch (e) {}
    }''')
rep('''          g.textContent = GROUPS[r.grp];
          el.appendChild(g);''',
'''          g.textContent = (PLACE ? placeGroupNames() : GROUPS)[r.grp];
          el.appendChild(g);''')
rep('''    function placeStops() {''',
'''    function placeGroupNames() {
      return ["WHERE ACCEPTANCE GATHERS", "WHERE DISTRUST, AGGRESSION, AND DEFIANCE GATHER", "WHERE INDIFFERENCE GATHERS", "HOW THEY MEET ON THE LAND"];
    }
    function placeStops() {''')
# pattern meanings on a place: by the notes' own emotions, never raised or sunk ground; no "line between present and goal"
rep('''      ns.forEach(function (n) {
        g[ground(hAt(n.x, n.y))].push(NP + n.k);
      });''',
'''      ns.forEach(function (n) {
        /* v247: on a place, by the note's own emotion (acceptance or indifference / distrust, aggression, or defiance) */
        g[PLACE ? (null == n.e ? "level" : 1 === n.e || 3 === n.e ? "raised" : "sunk") : ground(hAt(n.x, n.y))].push(NP + n.k);
      });''')
rep('''            " on raised ground, where things hold up. The idea already has footing: a place to build from.",''',
'''            (PLACE ? " where acceptance or indifference gathers." : " on raised ground, where things hold up.") +
              " The idea already has footing: a place to build from.",''')
rep('''            " in sunk ground." +
            (Object.keys(pi).length''',
'''            (PLACE ? " where distrust, aggression, or defiance gathers." : " in sunk ground.") +
            (PLACE
              ? " Where this phrase is, change is slow to start."
              : Object.keys(pi).length''')
rep('''          "Its notes sit on both kinds of ground: raised at " +
            list(g.raised) +
            ", sunk at " +
            list(g.sunk) +''',
'''          (PLACE ? "Its notes carry both: acceptance or indifference at " : "Its notes sit on both kinds of ground: raised at ") +
            list(g.raised) +
            (PLACE ? "; distrust, aggression, or defiance at " : ", sunk at ") +
            list(g.sunk) +''')
rep('''      else out.push("Its notes sit on level ground, so no emotion pulls it either way yet.");
      var near = ns.filter(function (n) {
        return Math.abs(n.y - trailY(n.x)) < 28;
      }).length;
      if (near)''',
'''      else out.push(PLACE ? "None of its notes has an emotion marked yet, so no emotion pulls it either way." : "Its notes sit on level ground, so no emotion pulls it either way yet.");
      var near = ns.filter(function (n) {
        return Math.abs(n.y - trailY(n.x)) < 28;
      }).length;
      if (PLACE);
      else if (near)''')
# HOW THIS MAP IS MADE on a place
rep('''        " on the line map; " +
        withE +
        " have an emotion marked and shape the ground" +''',
'''        (PLACE ? " on the place map; " : " on the line map; ") +
        withE +
        (PLACE ? " have an emotion marked and color the map" : " have an emotion marked and shape the ground") +''')
rep('''            " none yet and sit" +
            (none === 1 ? "s" : "") +
            " on level ground."
          : ".");
    }
    function fillSel() {''',
'''            (PLACE ? " none yet and add" + (none === 1 ? "s" : "") + " no color." : " none yet and sit" + (none === 1 ? "s" : "") + " on level ground.")
          : ".");
      if (PLACE) {
        /* v247: a place's land is real; say so, and drop the made-ground lines */
        var hn = $("count").parentNode.querySelectorAll(".note");
        hn[1] && (hn[1].textContent = "Each note with an emotion colors the map around where you placed it. More notes in one place make the color stronger.");
        hn[3] && (hn[3].textContent = "The land is the real place: its hills, valleys, and rock are the terrain itself and say nothing about your notes. Heights are exaggerated so the slopes show; the legend gives how much.");
        hn[4] && (hn[4].textContent = "Colors soften toward each other where emotions meet. Plain ground with no color means no notes nearby, so no information there.");
      }
    }
    function fillSel() {''')
rep('t.textContent = "v246"', 't.textContent = "v247"')
open(P, 'w').write(s)
print("v247 applied")
