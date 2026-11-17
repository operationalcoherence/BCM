"""v183: N3, POSSIBLE PATTERNS names the emotion it means, from the notes that carry the word."""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:80]); s = s.replace(a, b)
rep('''                    "A WORD THAT CROSSES QUESTIONS",
                    "ONE EMOTION THROUGHOUT",
                    function (t) {
                      return (
                        t +
                        " appears in several answers, with the same emotion each time. That emotion may be coloring more of your workbook than you meant."
                      );
                    },''', '''                    "A WORD THAT CROSSES QUESTIONS",
                    "ONE EMOTION THROUGHOUT",
                    function (t, stem) {
                      var EN = ["aggression", "acceptance", "distrust", "indifference", "defiance"],
                        c = [0, 0, 0, 0, 0],
                        k = 0,
                        ids = [];
                      stem &&
                        (window.gsmData ? window.gsmData().m || [] : []).forEach(function (r, i) {
                          null != r[5] && (r[3] || "").trim() && Ht(r[3]).k[stem] && (c[r[5]]++, k++, ids.push("N" + (i + 1)));
                        });
                      var m = 0;
                      c.forEach(function (x, j) {
                        x > c[m] && (m = j);
                      });
                      return k
                        ? t +
                            " runs through several answers, and the notes that carry it " +
                            (c[m] === k ? "all hold " : "mostly hold ") +
                            EN[m] +
                            " (" +
                            c[m] +
                            " of " +
                            k +
                            ": " +
                            ids.slice(0, 4).join(", ") +
                            (ids.length > 4 ? " and more" : "") +
                            "). Everything you write about it arrives already " +
                            ({ 0: "aggressive", 1: "accepting", 2: "distrustful", 3: "indifferent", 4: "defiant" })[m] +
                            ". That emotion may be coloring more of your workbook than you meant" +
                            (1 === m
                              ? ", and a hopeful color is easy to mistake for how things are."
                              : 3 === m
                                ? ": indifference here may mean no one has yet made it matter."
                                : ": it may be how you see it, or how others do; the voices on those notes say which.")
                        : t +
                            " appears in several answers, with the same emotion each time. That emotion may be coloring more of your workbook than you meant.";
                    },''')
rep('''                        d = l
                          ? l(c)''', '''                        d = l
                          ? l(c, a.length ? a[0] : null)''')
# V5: a small voice is not flattened by a large one: each voiced note weighs sqrt(mean voice size / its voice's size), 0.6-1.8
rep("""          t: String(n[3]),
          e: e,
        });
      });
      return notes;""", """          t: String(n[3]),
          e: e,
          v: n[7] ? String(n[7]) : "",
        });
      });
      return notes;""")
rep("""      var pts = notes.filter(function (n) {
        return n.e != null;
      });
      var sigma = 22;""", """      var pts = notes.filter(function (n) {
        return n.e != null;
      });
      (function () {
        var vc = {},
          vk;
        pts.forEach(function (p) {
          p.v && (vc[p.v] = (vc[p.v] || 0) + 1);
        });
        vk = Object.keys(vc);
        var mean =
          vk.reduce(function (a, k) {
            return a + vc[k];
          }, 0) / (vk.length || 1);
        pts.forEach(function (p) {
          p.w = vk.length > 1 && p.v ? Math.max(0.6, Math.min(1.8, Math.sqrt(mean / vc[p.v]))) : 1;
        });
      })();
      var sigma = 22;""")
rep("""            sw[pts[p].e] += Math.exp(-d2 / s2);""", """            sw[pts[p].e] += (pts[p].w || 1) * Math.exp(-d2 / s2);""")
a='<div class="note">Each note with an emotion assigned to it shapes the ground around it. More notes accumulating in one place shape it to a greater extent.</div>'
assert s.count(a)==1
s=s.replace(a, a+'\\n  <div class="note">Where notes carry voices, each voice counts about evenly: a voice with few notes is weighted up and one with many is weighted down (between 0.6 and 1.8 times), so a small voice is not flattened by a large one.</div>')
rep('t && (t.textContent = "v182");', 't && (t.textContent = "v183");')
open(P, "w").write(s); print("v183 ok")
