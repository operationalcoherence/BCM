"""v244: place-map tours speak about the place, not about made ground (his note 11-19 12:01: "In place-based maps, those
features are preexisting and have nothing to do with notes or maps ... They need to describe something bespoke to each
user's map, but they cannot talk about ridges and hollows that aren't there").
On a place map (PLACE), and only there:
  - the Synthesis tour's stops are placeStops(), not the line-map readings: where each emotion gathers on the land (its
    notes, and what the emotion means), where two distant emotions sit closest with no indifference between them, and
    what the goal sits among; act names and act openers say "where ... gathers", never high ground, ridge, or hollow;
  - the Analysis tour (introStops(true)) is the same reading, opened by how to read the map;
  - "What a move costs" drops "Climbing takes far more than falling" (on real land it reads as walking uphill).
The line map's tours, and every page text, are unchanged. Wording is Claude's, for the review table.
Usage: python3 v244_place_tours.py gsm-readable.js"""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)

rep('''      if (PLACE) {
        out.push({ act: act, title: "How to read this map", cap: "Each color is an emotion your notes carry, painted where you placed them; the ground is the real terrain. Where it has no color, no notes are nearby, so there is no information there.", at: null });
        out.push({ act: act, title: "What a move costs", cap: cost, at: null });
        return out;
      }''',
'''      if (PLACE) {
        /* v244: a place's land is real; its hills and hollows say nothing about the notes */
        var pcost =
          "Every move between emotions takes energy. Moving toward acceptance takes far more than moving away from it, and the farther apart two emotions are, the more a move costs. Most moves go through indifference. From acceptance and indifference, change can start now; from distrust, aggression, and defiance, it is unlikely in the short or medium term.";
        act = "READING THE MAP";
        out.push({ act: act, title: "How to read this map", cap: "The land is the real place. Its hills and valleys are the terrain itself, not your notes. Each color is an emotion your notes carry, painted around where you placed them. Where there is no color, no notes are nearby, so there is no information there.", at: null });
        primer &&
          placeStops().forEach(function (r) {
            out.push({ act: act, title: r.title, cap: r.cap, at: r.at });
          });
        out.push({ act: act, title: "What a move costs", cap: pcost, at: null });
        return out;
      }''')

# the place stops, defined next to introStops
rep('''    function firstSentence(t) {''',
'''    /* v244: a place map's own reading: where each emotion gathers on the land, where distant emotions sit closest,
       and what the goal sits among. Nothing about hills, ridges, or hollows: on a place those are the real land. */
    var PGROUPS = ["WHERE ACCEPTANCE GATHERS", "WHERE DISTRUST, AGGRESSION, AND DEFIANCE GATHER", "WHERE INDIFFERENCE GATHERS", "HOW THEY MEET ON THE LAND"];
    function placeStops() {
      var N = terr.notes.filter(function (n) {
          return null != n.e;
        }),
        RK = { 1: 0, 3: 1, 2: 2, 0: 3, 4: 4 },
        MEAN = {
          1: "Acceptance is where the goal already has people aligned with it. It takes care to keep, and it is the place to start from.",
          3: "Indifference is where people are not yet for or against. Most moves between emotions go through it, and people can stay there, precariously.",
          2: "Distrust is not bad in itself; what matters is what it is attached to. The road from here to acceptance is long.",
          0: "Aggression is not bad in itself; what matters is what it is attached to. The road from here to acceptance is longer than from distrust.",
          4: "Defiance is not bad in itself; what matters is what it is attached to. Its road to acceptance is the longest.",
        },
        GRP = { 1: 0, 2: 1, 0: 1, 4: 1, 3: 2 },
        out = [],
        nm = function (e) {
          return EMO[e][0].toLowerCase();
        };
      [1, 3, 2, 0, 4].forEach(function (e) {
        var ns = N.filter(function (n) {
          return n.e === e;
        });
        if (!ns.length) return;
        var cx = 0,
          cy = 0;
        ns.forEach(function (n) {
          cx += n.x;
          cy += n.y;
        });
        cx /= ns.length;
        cy /= ns.length;
        var mid = ns.slice().sort(function (a, b) {
            return Math.hypot(a.x - cx, a.y - cy) - Math.hypot(b.x - cx, b.y - cy);
          })[0],
          ks = ns
            .map(function (n) {
              return n.k;
            })
            .sort(function (a, b) {
              return a - b;
            }),
          spread = ns.length > 1 && Math.max.apply(null, ns.map(function (n) {
            return Math.hypot(n.x - cx, n.y - cy);
          })) > 90;
        out.push({
          grp: GRP[e],
          title: "Where " + nm(e) + " gathers",
          cap:
            (ns.length > 1 ? nks(ks.slice(0, 6)) + (ks.length > 6 ? " and " + (ks.length - 6) + " more" : "") + " carry " : nks(ks) + " carries ") +
            nm(e) +
            (spread ? ", spread across the place." : ns.length > 1 ? ", close together." : ".") +
            " " +
            MEAN[e],
          at: [mid.x, mid.y],
        });
      });
      var best = null;
      N.forEach(function (a, i) {
        N.slice(i + 1).forEach(function (b) {
          if (3 === a.e || 3 === b.e || Math.abs(RK[a.e] - RK[b.e]) < 2) return;
          var d = Math.hypot(a.x - b.x, a.y - b.y);
          (!best || d < best.d) && (best = { a: a, b: b, d: d });
        });
      });
      if (best) {
        var hi = RK[best.a.e] < RK[best.b.e] ? best.a : best.b,
          lo = hi === best.a ? best.b : best.a,
          between = N.some(function (n) {
            return 3 === n.e && Math.hypot(n.x - (hi.x + lo.x) / 2, n.y - (hi.y + lo.y) / 2) < best.d / 2 + 4;
          });
        out.push({
          grp: 3,
          title: "Where distant emotions sit closest",
          cap:
            NP + hi.k + " (" + nm(hi.e) + ") and " + NP + lo.k + " (" + nm(lo.e) + ") are the nearest pair of distant emotions on this map" +
            (between ? ", with indifference between them. That is the likeliest way across." : ", with no indifference between them. A move between them takes the most energy, in either direction."),
          at: [(hi.x + lo.x) / 2, (hi.y + lo.y) / 2],
        });
      }
      if (N.length) {
        var g = N.slice().sort(function (a, b) {
          return Math.hypot(a.x - GOAL.x, a.y - GOAL.y) - Math.hypot(b.x - GOAL.x, b.y - GOAL.y);
        })[0];
        out.push({
          grp: 3,
          title: "What the goal sits among",
          cap: "The goal is nearest " + NP + g.k + ", which carries " + nm(g.e) + ". " + (1 === g.e ? "It starts among people already with it." : 3 === g.e ? "It starts where people are not yet for or against it." : "It starts where the road to acceptance is long."),
          at: [GOAL.x, GOAL.y],
        });
      }
      var none = terr.notes.length - N.length;
      none > 0 && out.push({ grp: 3, title: "Notes with no emotion yet", cap: none + (1 === none ? " note has" : " notes have") + " no emotion marked yet (the white pins), so they add no color to the map.", at: null });
      return out;
    }
    function firstSentence(t) {''')

# Synthesis tour on a place: the place stops, groups, and act openers
rep('''          try {
            D.intro = introStops(false);
          } catch (e) {}''',
'''          try {
            D.intro = introStops(false);
          } catch (e) {}
          if (PLACE)
            try {
              /* v244: a place's tour reads the place, not made ground */
              var PS = placeStops();
              D.read = PS.filter(function (r) {
                return r.at;
              }).map(function (r) {
                return { at: r.at, title: r.title, text: r.cap, grp: r.grp, cap: r.cap };
              });
              /* a stop with no spot on the map (notes with no emotion) goes in the opening, which allows that */
              D.intro = (D.intro || []).concat(
                PS.filter(function (r) {
                  return !r.at;
                }).map(function (r) {
                  return { act: "READING THE MAP", title: r.title, cap: r.cap, at: null };
                }),
              );
              D.groups = PGROUPS;
              D.actMean = [
                "Acceptance: where the goal already has people aligned with it.",
                "Distrust, aggression, and defiance: not bad in themselves; what matters is what they are attached to.",
                "Indifference: where people are not yet for or against.",
                "How the emotions sit together on the land, and where the goal starts.",
              ];
            } catch (e) {}''')

rep('t.textContent = "v243"', 't.textContent = "v244"')
open(P, 'w').write(s)
print("v244 applied")
