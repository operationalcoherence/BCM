"""v223: In Parallel as a disagreement detector, bridge finder, and hidden-structure finder (his 11-18 19:14 note).
1. The strongest sections leave the closed MORE FROM BOTH PICTURES fold and stand open under the figure, in a new
   section WHAT THE TWO PICTURES REVEAL: Patterns worth a second look, Emotion, Closest and farthest from the goal,
   and Voices. Read together and What might relate to what stay folded.
2. Patterns worth a second look shows every PLACED ONE WAY, TIED THE OTHER and every THE EMOTION CHANGES finding
   first, open; the rest keep "More patterns".
3. PLACED ONE WAY, TIED THE OTHER reads the terrain: the note's own emotion against the emotion of what it is tied
   to. Low ground tied to the high ground = a likely bridge; help placed among ties to low ground = a borrowed
   foothold; otherwise the earlier reading. No counts.
4. THE EMOTION CHANGES says how the word moves on the ground as it goes from the context you have grasped into what
   you would design (climbs or drops, from what to what), and what that move costs: a big move with no indifference
   between takes energy either way; through indifference, it is the usual way across.
5. Emotion leads with where change is likely (acceptance and indifference: it can start now) and where it is not
   (distrust, aggression, and defiance: unlikely in the short or medium term), then what the leading emotion means.
   No "(12 of 34)".
Wording is Claude's, for his redlines.
Usage: python3 v223_in_parallel_reveals.py gsm-readable.js"""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:90]); s = s.replace(a, b)

# 1. lift the strongest sections out of the fold
rep('''  function gsmIntOrder(E, f) {
    var top = [],
      dup = [],
      rest = [];
    E.forEach(function (t) {
      "Where to start" === t[0]
        ? top.push(f(t))
        : "Where both pictures agree" === t[0] || "Where they differ" === t[0]
          ? dup.push(f(t).replace('<div class="intl">', '<div class="intl" data-dup="1">'))
          : rest.push(f(t));
    });
    return (
      top.join("") +
      dup.join("") +''', '''  function gsmIntOrder(E, f) {
    var top = [],
      dup = [],
      lift = [],
      rest = [],
      LIFT = ["Patterns worth a second look", "Emotion", "Closest and farthest from the goal", "Voices"];
    E.forEach(function (t) {
      "Where to start" === t[0]
        ? top.push(f(t))
        : "Where both pictures agree" === t[0] || "Where they differ" === t[0]
          ? dup.push(f(t).replace('<div class="intl">', '<div class="intl" data-dup="1">'))
          : LIFT.indexOf(t[0]) >= 0
            ? lift.push([LIFT.indexOf(t[0]), f(t)])
            : rest.push(f(t));
    });
    lift.sort(function (a, b) {
      return a[0] - b[0];
    });
    return (
      top.join("") +
      dup.join("") +
      (lift.length
        ? '<div class="intrev"><div class="intrevh">WHAT THE TWO PICTURES REVEAL</div>' +
          lift
            .map(function (x) {
              return x[1];
            })
            .join("") +
          "</div>"
        : "") +''')

# 2. bridges and hidden channels first, open
rep('''                      ot = R.slice(0, 3),
                      rt = R.slice(3);''', '''                      PRI = function (t) {
                        return "PLACED ONE WAY, TIED THE OTHER" === t.lab || "THE EMOTION CHANGES" === t.lab;
                      },
                      ot = R.filter(PRI).concat(
                        R.filter(function (t) {
                          return !PRI(t);
                        }).slice(0, 2),
                      ),
                      rt = R.filter(function (t) {
                        return ot.indexOf(t) < 0;
                      });''')

# 3. placed one way, tied the other: terrain reading
rep('''                          o >= Math.ceil((2 * n.length) / 3) &&
                            B(
                              "PLACED ONE WAY, TIED THE OTHER",
                              "a dot placed against its own threads",
                              String(t).replace(/^(?:place )?note (\\d+)/, "N$1") +
                                " sits " +
                                (e.up ? "above" : "below") +
                                " the line, but " +
                                o +
                                " of the " +
                                n.length +
                                " answers and notes it shares words with sit on the other side. Either it " +
                                (e.up ? "helps" : "hinders") +
                                " in a way the rest of your workbook does not show yet, or it was placed " +
                                (e.up ? "more hopefully" : "more darkly") +
                                " than its words. Open it and ask which: if the placement is right, it may be a bridge worth building on; if not, move it, and the patterns will follow.",''',
    '''                          var PEN = ["aggression", "acceptance", "distrust", "indifference", "defiance"],
                            pc = [0, 0, 0, 0, 0];
                          n.forEach(function (k) {
                            C[k].up !== e.up && null != C[k].em && C[k].em >= 0 && C[k].em < 5 && pc[C[k].em]++;
                          });
                          var pm = Math.max.apply(null, pc),
                            pt = pm > 0 ? pc.indexOf(pm) : -1,
                            pe = null != e.em && e.em >= 0 && e.em < 5 ? e.em : -1,
                            plow = [0, 2, 4].indexOf(pe) >= 0,
                            nid = String(t).replace(/^(?:place )?note (\\d+)/, "N$1"),
                            pread =
                              !e.up && plow && (1 === pt || 3 === pt)
                                ? " That makes it a likely bridge: the language of the high ground already reaches into the low ground here, so a move from " +
                                  PEN[pe] +
                                  " toward " +
                                  PEN[pt] +
                                  " has something to hold on to. If the placement is wrong instead, move it, and the patterns will follow."
                                : pe >= 0 && pe === pt
                                  ? " Its emotion matches what it is tied to; only the side differs. The same " +
                                    PEN[pe] +
                                    " may be pointed two ways, against the goal here and for it there, which makes it something to redirect rather than overcome."
                                  : e.up && [0, 2, 4].indexOf(pt) >= 0
                                  ? " That makes it a borrowed foothold: what looks like help speaks the language of the " +
                                    PEN[pt] +
                                    " it is tied to, so it may give way under pressure. Check it before you build on it."
                                  : " Either it " +
                                    (e.up ? "helps" : "hinders") +
                                    " in a way the rest of your workbook does not show yet, or it was placed " +
                                    (e.up ? "more hopefully" : "more darkly") +
                                    " than its words. Open it and ask which: if the placement is right, it may be a bridge worth building on; if not, move it, and the patterns will follow.";
                          o >= Math.ceil((2 * n.length) / 3) &&
                            B(
                              "PLACED ONE WAY, TIED THE OTHER",
                              "a dot placed against its own threads",
                              nid +
                                " sits " +
                                (e.up ? "above" : "below") +
                                " the line" +
                                (pe >= 0 ? ", on " + PEN[pe] : "") +
                                ", but most of what it shares words with sits " +
                                (e.up ? "below" : "above") +
                                " it" +
                                (pt >= 0 ? ", mostly on " + PEN[pt] : "") +
                                ". Its place says it " +
                                (e.up ? "helps" : "hinders") +
                                "; its ties say it belongs with what " +
                                (e.up ? "hinders" : "helps") +
                                "." +
                                pread,''')

# 4. the emotion changes: how it moves on the ground
rep('''                            j(t) +
                              " carries mostly " +
                              b[i] +
                              " in Q.1–Q.4 and mostly " +
                              b[a] +
                              " in Q.5–Q.7. " +''', '''                            j(t) +
                              ([3, 0, 2, 1, 4][a] < [3, 0, 2, 1, 4][i] ? " climbs from " : " drops from ") +
                              b[i] +
                              " to " +
                              b[a] +
                              " as it moves from the context you have grasped into what you would design. " +
                              (3 !== i && 3 !== a && Math.abs([3, 0, 2, 1, 4][a] - [3, 0, 2, 1, 4][i]) >= 2
                                ? "On the ground that is a big move with no ridge of indifference between, so it takes energy either way. "
                                : 3 === i || 3 === a
                                  ? "It passes through indifference, the usual way across. "
                                  : "") +''')

# 5. emotion: where change is likely
rep('''                      es =
                        "Across your notes, " +
                        b[A] +
                        " leads (" +
                        O +
                        " of " +
                        ET +
                        ")" +
                        (1 === A && EH ? ", but aggression and defiance together hold " + EH + "." : ".");''', '''                      es =
                        (EA + EI
                          ? "Change is likely to start where your notes carry acceptance or indifference: from there, it can begin now."
                          : "No note yet carries acceptance or indifference, so nowhere on this ground is change likely to start soon.") +
                        (EH + EC[2]
                          ? " Where they carry distrust, aggression, or defiance, which hold " +
                            (EH + EC[2] > 1.4 * (EA + EI) ? "most" : EH + EC[2] > 0.7 * (EA + EI) ? "much" : "part") +
                            " of this workbook, change is unlikely in the short or medium term."
                          : "") +
                        (0 === A
                          ? " Aggression leads, and it can harden into defiance: what is resisted now can turn to rebellion if it is pushed."
                          : 4 === A
                            ? " Defiance leads: the ground most resistant to any strategy."
                            : 2 === A
                              ? " Distrust leads: trust has to come before anything moves."
                              : 3 === A
                                ? " Indifference leads: most of this ground could still tip either way."
                                : "");''')
rep('''(EI ? EI + " note" + (1 === EI ? "" : "s") + " in indifference, the emotion of transition (Vigneaux, 2026)." : ''',
    '''(EI ? "the indifference you have mapped, the emotion of transition (Vigneaux, 2026)." : ''')

# css for the lifted section
rep('''#gsm .stn{color:#888;font-size:13px}";''',
    '''#gsm .stn{color:#888;font-size:13px}";
    var st2 = document.createElement("style");
    st2.textContent = "#gsm .intrev{margin:18px 0 10px}#gsm .intrevh{font-size:13px;font-weight:700;letter-spacing:.16em;color:#222;border-top:1px solid #222;padding-top:10px;margin-bottom:10px}#gsm .intrev .intl{margin-bottom:12px}";
    document.head.appendChild(st2);''')
for _a, _b in [("carries Q.1–Q.4 into Q.5–Q.7", "carries the context you have grasped into what you would design"),
               ("runs from Q.1–Q.4 into Q.5–Q.7", "runs from the context you have grasped into what you would design")]:
    assert s.count(_a) >= 1, _a
    s = s.replace(_a, _b)
rep('t && (t.textContent = "v222");', 't && (t.textContent = "v223");')
open(P, "w").write(s)
print("ok")
