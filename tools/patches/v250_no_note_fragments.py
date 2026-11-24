"""v250: no note fragments in the narrative (his note 11-24 08:23 on v249).

"Sending supporters of the transformation" or "Going along with the transition" quoted as
what already exists has no meaning on its own; such fragments devalue the narrative.
A note is never named in a narrative line any more. A line names a theme only when it is a
phrase at least two differently worded notes share; otherwise it says what the notes are
and where they stand, and their numbers go behind as evidence.

- THE OPPORTUNITY: with no shared phrase it says how many notes of support already stand on
  the high ground and where along the way they sit (near the start, partway, close to the
  goal), instead of quoting notes.
- WHAT HOLDS THE SITUATION IN PLACE: with no shared phrase it gives the count, no quotes.
- The one-line story: with no shared phrase, "What stands against the goal holds the work in
  place …" instead of a list of note openings.
- Taking Action: the seeded cards' titles carry a theme only when there is one ("What holds
  the situation in place", "The opportunity", "What is already helping", "Support not yet
  reinforced" stand alone otherwise); FIRST MOVE says "Scale the support already standing";
  the test lines count notes ("Two notes already help the goal …") with the numbers behind.
"""
import re, sys
F = "gsm-readable.js"
s = open(F).read()


def rep(old, new, n=1):
    global s
    c = s.count(old)
    if c != n:
        sys.exit("expected %d, found %d: %r" % (n, c, old[:90]))
    s = s.replace(old, new)


# where along the way a set of notes sits (line map x: start 10, goal 305)
rep('''  function gsmStQL(a) {''', '''  function gsmStWhere(list) {
    var c = [0, 0, 0],
      n = 0;
    list.forEach(function (x) {
      var r = x.ref && /^note (\\d+)$/.exec(x.ref),
        row = r ? (C.m || [])[+r[1] - 1] : null,
        X = row && "number" == typeof row[1] ? row[1] : null;
      null != X && X >= 0 && X <= 340 && (c[X < 108 ? 0 : X < 207 ? 1 : 2]++, n++);
    });
    if (n < 2) return "";
    var i = c.indexOf(Math.max.apply(null, c));
    return c[i] / n > 0.5 ? ["near the start of the change", "partway along", "close to the goal"][i] : "";
  }
  function gsmStCount(n, noun) {
    return (n < 10 ? ["no", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"][n] : String(n)) + " " + noun + (1 === n ? "" : "s");
  }
  function gsmStQL(a) {''')

# THE OPPORTUNITY
rep('''          (exTh.length
            ? ", around " + gsmStQL(exTh)
            : ", in " +
              gsmStQL(
                exNames.slice(0, 3).map(function (x) {
                  return x.charAt(0).toUpperCase() + x.slice(1);
                }),
              )) +''', '''          (exTh.length
            ? ", around " + gsmStQL(exTh)
            : ": " +
              gsmStCount(ex.length, "note") +
              " of support" +
              (gsmStWhere(ex) ? ", most of them " + gsmStWhere(ex) : "")) +''')
rep('''      SS.D.oppN = exTh.length ? exTh : exNames;''', '''      SS.D.oppN = exTh;''')

# WHAT HOLDS THE SITUATION IN PLACE
rep('''            : sysNames.length >= 2
              ? " of " +
                comp.length +
                " notes, among them " +
                gsmStQL(
                  sysNames.slice(0, 3).map(function (x) {
                    return x.charAt(0).toUpperCase() + x.slice(1);
                  }),
                )
              : ": " + comp.length + " notes") +''', '''            : ": " + comp.length + " notes" + (gsmStWhere(comp) ? ", most of them " + gsmStWhere(comp) : "")) +''')
rep('''      SS.sys = sysTh.length
        ? sysTh
        : sysNames.length >= 2
          ? sysNames.slice(0, 3)
          : comp.slice(0, 3).map(function (n) {
              return n.lab;
            });''', '''      SS.sys = sysTh;
      SS.sysOn = 1;''')

# the one-line story
rep('''    SS.sys &&
      P.push(
        Gt(SS.sys.join(", ")).replace(/^./, function (c) {
          return c.toUpperCase();
        }) +
          ", and what stands with them," +''', '''    SS.sysOn &&
      P.push(
        (SS.sys.length
          ? "What gathers around " +
            phList(
              SS.sys.map(function (x) {
                return "“" + Gt(x) + "”";
              }),
            ) +
            ", and what stands with it, holds"
          : "What stands against the goal holds") +''')
rep('''          (SS.low ? " hold the work in place from the low ground" : " hold the work in place for now, though loosely") +''',
    '''          (SS.low ? " the work in place from the low ground" : " the work in place for now, though loosely") +''')
rep('''        : SS.sys && P.push("So the work starts with what keeps that system in place, not with persuasion.");''',
    '''        : SS.sysOn && P.push("So the work starts with what keeps that system in place, not with persuasion.");''')

# Taking Action: seeded card titles and first moves
rep('''            if (sys.length >= 3 && SS.sys) {''', '''            if (sys.length >= 3 && SS.sysOn) {''')
rep('''                title: "What holds the situation in place: " + gsmMeanList(SS.sys.slice(0, 3)),''',
    '''                title: "What holds the situation in place" + (SS.sys.length ? ": " + gsmMeanList(SS.sys.slice(0, 3)) : ""),''')
rep('''                mO = ["Scale what already exists: " + Gt(gsmMeanList(nO.length ? nO : opp.slice(0, 3).map(NM))) + ".", "Ask the people doing it what they need to keep going, and to grow."];''',
    '''                mO = [(nO.length ? "Scale what already exists: " + Gt(gsmMeanList(nO)) + "." : "Scale the support already standing (" + opp.map(NB).join(", ") + ")."), "Ask the people doing it what they need to keep going, and to grow."];''')
rep('''                title: "The opportunity: " + gsmMeanList(nO.length ? nO : opp.slice(0, 3).map(NM)),''',
    '''                title: "The opportunity" + (nO.length ? ": " + gsmMeanList(nO) : ""),''')
rep('''                title: "What is already helping: " + gsmMeanList(help.slice(0, 3).map(NM)),''',
    '''                title: "What is already helping" + (gsmStThemes(help, 3).length ? ": " + gsmMeanList(gsmStThemes(help, 3)) : ""),''')
rep('''                title: "Support not yet reinforced: " + gsmMeanList(snr.slice(0, 3).map(NM)),''',
    '''                title: "Support not yet reinforced" + (gsmStThemes(snr, 3).length ? ": " + gsmMeanList(gsmStThemes(snr, 3)) : ""),''')
rep('''                mH = ["Build on " + LS(help, 3) + " rather than starting over.",''',
    '''                mH = ["Build on what already helps (" + LS(help, 3) + ") rather than starting over.",''')

# Taking Action: test lines count notes; numbers stay behind
rep('''            function NAMES(xs, k) {
              k = k || 3;
              var b = xs.slice(0, k).map(function (x) {
                return Gt(NM(x));
              });
              xs.length > k && b.push(xs.length - k + " more");
              return phList(b).replace(/^./, function (c) {
                return c.toUpperCase();
              });''', '''            function NAMES(xs, k) {
              /* v250: no note fragments; the count, with the numbers behind */
              return gsmStCount(xs.length, "note").replace(/^./, function (c) {
                return c.toUpperCase();
              });''')

rep('''                      ? "The proposed actions reach " + NAMES(tR.met).replace(/^(?![NP]\\d)./, function (c) { return c.toLowerCase(); }) + ", but not yet " + NAMES(tR.not).replace(/^(?![NP]\\d)./, function (c) { return c.toLowerCase(); }) + "."''',
    '''                      ? "The proposed actions reach " + gsmStCount(tR.met.length, "").split(" ")[0] + " of them, but not yet " + (1 === tR.not.length ? (2 === tR.met.length + tR.not.length ? "the other" : "the last one") : "the other " + gsmStCount(tR.not.length, "").split(" ")[0]) + "."''')
rep('t && (t.textContent = "v249");', 't && (t.textContent = "v250");')
open(F, "w").write(s)
print("v250 applied")
