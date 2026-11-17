"""v180: N4, In Parallel findings told as meaning: Emotion, Two people two sides, The emotion changes,
Placed one way tied the other."""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:80]); s = s.replace(a, b)

rep('''                    E.push([
                      "Emotion",
                      A !== e.brLead.k
                        ? "Across all your notes, " +
                          b[A] +
                          " leads. On “" +
                          e.brLead.name +
                          "”, the thread that carries Q.1–Q.4 into Q.5–Q.7, " +
                          b[e.brLead.k] +
                          " leads. The idea that connects cause to action is where the emotion changes, so expect friction there."
                        : "Across all your notes, " +
                          b[A] +
                          " leads, and it leads on “" +
                          e.brLead.name +
                          "” too, the thread that carries Q.1–Q.4 into Q.5–Q.7. The connection does not add resistance.",
                    ]);''', '''                    var EC = n.emo,
                      ET = EC.reduce(function (a, v) {
                        return a + v;
                      }, 0),
                      EH = EC[0] + EC[4],
                      EA = EC[1],
                      EI = EC[3],
                      es =
                        "Across your notes, " +
                        b[A] +
                        " leads (" +
                        O +
                        " of " +
                        ET +
                        ")" +
                        (1 === A && EH ? ", but aggression and defiance together hold " + EH + "." : ".");
                    EA && EH >= 0.7 * EA && EH <= 1.4 * EA
                      ? (es +=
                          " The weight is close to even between the emotions that could carry the goal and those that resist it. Neither side is likely to give way on its own. If change comes, it will come mostly through the ground in between: " +
                          (EI ? EI + " note" + (1 === EI ? "" : "s") + " in indifference, the emotion of transition (Vigneaux, 2026)." : "indifference, the emotion of transition, and you have no note there yet (Vigneaux, 2026)."))
                      : EA > 1.4 * EH
                        ? (es +=
                            " Most of the ground already accepts the goal. The risk is less resistance than drift: no emotion is stable, acceptance included, so it has to be kept up as things move (Vigneaux, 2026).")
                        : EH > 1.4 * EA &&
                          (es +=
                            " Resistance outweighs acceptance. Argument is unlikely to move it soon; behaviors that fit the emotions already there are more likely to (Vigneaux, 2026).");
                    es +=
                      A !== e.brLead.k
                        ? " On “" +
                          e.brLead.name +
                          "”, the thread that carries Q.1–Q.4 into Q.5–Q.7, " +
                          b[e.brLead.k] +
                          " leads instead. The idea that links cause to action feels different from the workbook as a whole, so expect friction exactly where understanding turns into doing."
                        : " “" +
                          e.brLead.name +
                          "”, the thread that carries Q.1–Q.4 into Q.5–Q.7, carries the same emotion, so turning understanding into doing should not add resistance of its own.";
                    E.push(["Emotion", es]);''')

rep('''                              ". The disagreement about it may be between people rather than inside one person's thinking.",''',
    '''              ". So the split is not one person's mixed feelings; it runs between groups. A course of action about it will be heard differently by each, and what wins over one may lose the other. Before acting on it, ask each group what they mean by the word: they may be naming different things with it." +
                              (window.gsmMED && Object.keys(window.gsmMED).length ? " ONE WORD, SEVERAL MEANINGS on Pattern Analysis shows the phrases each side uses." : ""),''')

rep('''                              " in Q.1–Q.4 and mostly " +
                              b[a] +
                              " in Q.5–Q.7. The same word may change emotion once it becomes something to do.",''',
    '''                              " in Q.1–Q.4 and mostly " +
                              b[a] +
                              " in Q.5–Q.7. Thinking of it as something to do changes how it feels. That can be read two ways: the doing may be what brings people from " +
                              b[i] +
                              " to " +
                              b[a] +
                              ", which makes it a place to start; or your plans may be more hopeful than the ground they will land on. The notes in Q.1–Q.4 that carry it tell you which ground that is.",''')

rep('''                                " places it shares words with sit on the other side. Where you put it and what it ties to may not agree.",''',
    '''                                " answers and notes it shares words with sit on the other side. Either it " +
                                (e.up ? "helps" : "hinders") +
                                " in a way the rest of your workbook does not show yet, or it was placed " +
                                (e.up ? "more hopefully" : "more darkly") +
                                " than its words. Open it and ask which: if the placement is right, it may be a bridge worth building on; if not, move it, and the patterns will follow.",''')
rep('''                              t +
                                " sits " +
                                (e.up ? "above" : "below") +''', '''                              String(t).replace(/^(?:place )?note (\\d+)/, "N$1") +
                                " sits " +
                                (e.up ? "above" : "below") +''')
a='''" in Q.5–Q.7. Thinking of it as something to do changes how it feels. That can be read two ways: the doing may be what brings people from " +
                              b[i] +
                              " to " +
                              b[a] +
                              ", which makes it a place to start; or your plans may be more hopeful than the ground they will land on. The notes in Q.1–Q.4 that carry it tell you which ground that is.",'''
b='''" in Q.5–Q.7. " +
                              ([3, 0, 2, 1, 4][a] < [3, 0, 2, 1, 4][i]
                                ? "Thinking of it as something to do makes it feel easier. That can be read two ways: the doing may be what brings people from " +
                                  b[i] +
                                  " toward " +
                                  b[a] +
                                  ", which makes it a place to start; or your plans may be more hopeful than the ground they will land on. The notes in Q.1–Q.4 that carry it tell you which ground that is."
                                : "Turning it into something to do makes it harder: the plans carry " +
                                  b[a] +
                                  " where the situation carries " +
                                  b[i] +
                                  ". The actions may be stirring resistance the situation does not hold. Look at how those Q.5–Q.7 notes are worded and what they ask of people; a gentler way in may keep the " +
                                  b[i] +
                                  " that is already there."),'''
rep(a, b)
rep('t && (t.textContent = "v179");', 't && (t.textContent = "v180");')
open(P, "w").write(s); print("v180 ok")
