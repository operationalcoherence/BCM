"""v225: In Parallel's patterns explain why one workbook supports more than one reading (his 11-18 19:36 note).
1. Patterns worth a second look opens with one line naming what it found, as kinds of double reading (a note whose
   place and ties disagree, an emotional turn, a disagreement hidden under a shared word, two words that may be one
   idea, a hinge, two big ideas never held together), and says each one below gives the readings it allows.
2. TWO PEOPLE, TWO SIDES: a hidden disagreement. It now gives each group's emotion and reads the gap on the ground:
   the same emotion pointed two ways (a disagreement about direction, not value), far-apart emotions with no ridge
   between (no single message carries both), or through indifference.
3. ONE IDEA UNDER TWO NAMES: no count. Read by side: both sides (a hidden agreement both sides claim), only where
   things help (what the support may really be about), only where things hinder (what the resistance may be about).
4. THE UNCLOSED TRIANGLE: named a hinge; if it goes, the two come apart.
5. NEVER IN THE SAME PLACE: no counts.
Wording is Claude's, for his redlines.
Usage: python3 v225_readings_not_counts.py gsm-readable.js"""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:90]); s = s.replace(a, b)

# 2. two people, two sides
rep('''                        i.length &&
                          a.length &&
                          B(
                            "TWO PEOPLE, TWO SIDES",
                            "two people on two sides",
                            j(t) +
                              " sits above the line in the notes from " +
                              F(i) +
                              ", and below it in the notes from " +
                              F(a) +''', '''                        var TE = ["aggression", "acceptance", "distrust", "indifference", "defiance"],
                          TR = [3, 0, 2, 1, 4],
                          tu = [0, 0, 0, 0, 0],
                          td = [0, 0, 0, 0, 0];
                        t.ids.forEach(function (k) {
                          var o = C[k];
                          o && null != o.up && null != o.em && o.em >= 0 && o.em < 5 && (o.up ? tu : td)[o.em]++;
                        });
                        var tmu = Math.max.apply(null, tu),
                          tmd = Math.max.apply(null, td),
                          eu = tmu > 0 ? tu.indexOf(tmu) : -1,
                          ed = tmd > 0 ? td.indexOf(tmd) : -1,
                          tg =
                            eu < 0 || ed < 0
                              ? ""
                              : " In the notes from " +
                                F(i) +
                                " it carries " +
                                TE[eu] +
                                "; in the notes from " +
                                F(a) +
                                ", " +
                                TE[ed] +
                                "." +
                                (eu === ed
                                  ? " They feel the same way about it and point it in opposite directions: a disagreement about direction, not about what matters."
                                  : 3 !== eu && 3 !== ed && Math.abs(TR[eu] - TR[ed]) >= 2
                                    ? " Those emotions sit far apart, with no ridge of indifference between them, so no single message will carry both groups."
                                    : 3 === eu || 3 === ed
                                      ? " One side is indifference, so that group can still be moved either way; start there."
                                      : "");
                        i.length &&
                          a.length &&
                          B(
                            "TWO PEOPLE, TWO SIDES",
                            "two people on two sides",
                            "A disagreement hidden under a shared word: " +
                              j(t) +
                              " sits above the line in the notes from " +
                              F(i) +
                              ", and below it in the notes from " +
                              F(a) +
                              "." +
                              tg +
                              " So the split is not one person's mixed feelings; it runs between groups" +''')
rep('''              ". So the split is not one person's mixed feelings; it runs between groups.''', '''              ".''')

# 3. one idea under two names
rep('''                        j(W.a) +
                          " and " +
                          j(W.b) +
                          " appear in the same " +
                          W.a.n +
                          " places and never apart. They may be one idea under two names, or two things you cannot separate.",''', '''                        (function () {
                          var su = 0,
                            sd = 0;
                          W.a.ids.forEach(function (k) {
                            var o = C[k];
                            o && (!0 === o.up ? su++ : !1 === o.up && sd++);
                          });
                          return (
                            "Wherever you write " +
                            j(W.a) +
                            ", you also write " +
                            j(W.b) +
                            ": in your workbook they never part. " +
                            (su && sd
                              ? "They turn up on both sides of the line, so the pair is something both sides claim: a hidden agreement the work could stand on. "
                              : su
                                ? "They turn up only where things help, so together they may be what the support is really about. "
                                : sd
                                  ? "They turn up only where things hinder, so together they may be what the resistance is really about. "
                                  : "") +
                            "They may be one idea under two names, or two things you can’t separate; if they are one, THE SAME THING? on Pattern Analysis can join them."
                          );
                        })(),''')

# 4. the unclosed triangle as a hinge
rep('''                          " never meet. " +
                          j(G.b) +
                          " may be the only thing holding those two together.",''', '''                          " never meet. " +
                          j(G.b) +
                          " is a hinge: it may be the only thing holding those two together, and if it goes, they come apart.",''')

# 5. never in the same place: no counts
rep('''                          " are among the words you use most — " +
                          P.a.n +
                          " places and " +
                          P.b.n +
                          " — and they never once appear in the same place.''', '''                          " are among the words you use most, and they never once appear in the same place.''')

# 1. framing line
rep('''                    E.push([
                      "Patterns worth a second look",
                      ot.map(nt).join("") +''', '''                    var KIND = {
                        "PLACED ONE WAY, TIED THE OTHER": "a note whose place and ties disagree",
                        "THE EMOTION CHANGES": "an emotional turn between what you have grasped and what you would design",
                        "TWO PEOPLE, TWO SIDES": "a disagreement hidden under a shared word",
                        "ONE IDEA UNDER TWO NAMES": "two words that may be one idea",
                        "THE UNCLOSED TRIANGLE": "a hinge holding two ideas together",
                        "NEVER IN THE SAME PLACE": "two big ideas never held together",
                      },
                      kinds = [];
                    R.forEach(function (t) {
                      KIND[t.lab] && kinds.indexOf(KIND[t.lab]) < 0 && kinds.push(KIND[t.lab]);
                    });
                    var kl =
                      kinds.length < 2
                        ? kinds.join("")
                        : kinds.length < 3
                          ? kinds.join(" and ")
                          : kinds.slice(0, -1).join(", ") + ", and " + kinds[kinds.length - 1];
                    E.push([
                      "Patterns worth a second look",
                      (kinds.length
                        ? '<div class="intframe">Here the same workbook supports more than one reading: ' +
                          Gt(kl) +
                          ". Each one below says which readings it allows and how to tell them apart.</div>"
                        : "") +
                        ot.map(nt).join("") +''')
rep('''#gsm .intrev .intl{margin-bottom:12px}";''', '''#gsm .intrev .intl{margin-bottom:12px}#gsm .intframe{font-size:15px;line-height:1.5;color:#222;margin:4px 0 10px}";''')
rep('t && (t.textContent = "v224");', 't && (t.textContent = "v225");')
open(P, "w").write(s)
print("ok")
