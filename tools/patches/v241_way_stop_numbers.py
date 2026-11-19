"""v241: numbered stops on the selected way (his note 11-19 10:52, with a screenshot of a way that doubles back:
"in instances like this, its still impossible to tell what the order is").
The arrows (v240) give direction on each stretch; they can't say which stretch comes first. Now each way carries its
stops in order (the points it is built through: its notes, and for way A the ridge and acceptance it climbs to), and
the 3D numbers them 1, 2, 3 ... on the selected way (on way A when all ways are shown). START and GOAL keep their flags.
Engine part: viaPts() and legs() keep the stops on the point list; way C joins its two parts' stops; data() passes
them to the 3D as routes[].stops. The 3D part is in tools/relief/relief.js (edited directly).
Usage: python3 v241_way_stop_numbers.py gsm-readable.js"""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)

rep('''          out.push([A0[0] + ((B0[0] - A0[0]) * k) / N, A0[1] + ((B0[1] - A0[1]) * k) / N]);
      }
      out.push(pts[pts.length - 1]);
      return out;''',
'''          out.push([A0[0] + ((B0[0] - A0[0]) * k) / N, A0[1] + ((B0[1] - A0[1]) * k) / N]);
      }
      out.push(pts[pts.length - 1]);
      out.stops = pts.slice(); /* v241: the stops, in order, for the numbers on the 3D */
      return out;''')
rep('''            out = out.concat(j ? seg.slice(1) : seg);
          }
          return out;''',
'''            out = out.concat(j ? seg.slice(1) : seg);
          }
          out.stops = stops.slice(); /* v241 */
          return out;''')
rep('''            r3 = first.concat(rest);''',
'''            r3 = first.concat(rest);
          r3.stops = (first.stops || []).concat([[GOAL.x, GOAL.y]]); /* v241 */''')
rep('''            return { key: R.key, name: R.name, pts: R.pts, text: rd[R.key] || "" };''',
'''            return { key: R.key, name: R.name, pts: R.pts, stops: R.pts.stops || null, text: rd[R.key] || "" };''')
rep('t.textContent = "v240"', 't.textContent = "v241"')
open(P, 'w').write(s)
print("v241 applied")
