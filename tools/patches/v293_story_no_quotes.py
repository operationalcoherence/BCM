# v293b: "The whole workbook read as one story" (YOUR STORY SO FAR's base text) follows his story rule
# (24 Nov 2026): notes are evidence only, so no quoting, no note ids, and no labelled sections in the
# narrative. The opening reads the map by emotion and place instead of quoting notes; WHAT STANDS IN
# THE WAY, WHAT IS ALREADY HELPING, WHAT HAS TO BE TRUE, WHAT YOU WOULD DO, and WHERE TO START become
# continuous paragraphs with no labels or ids. Applies to every workbook.
p = 'gsm-readable.js'
s = open(p, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, old[:90]); s = s.replace(old, new)
# sections become plain paragraphs
rep('''              function P0(h, body) {
                return body ? '<div class="csl" style="margin-top:14px">' + h + "</div><p>" + body + "</p>" : "";
              }''', '''              /* v293: no labelled sections in the story: each part is a paragraph */
              function P0(h, body) {
                return body ? "<p>" + body + "</p>" : "";
              }''')
# opening: no Q.1 quote
rep('''                Q1 && S.push("It starts with why the goal has not taken root: “" + Gt(Q1.replace(/[\\s.;:,]+$/, "")) + "” (Q.1).");''',
    '''                /* v293: the story does not quote the notes or answers; it reads them by emotion and place */
                function feel(L) {
                  var E = emo(L);
                  return E.n ? and(E.ord.slice(0, 2).map(function (k) {
                    return EN[k];
                  })) : "";
                }
                function are(x) {
                  return / and /.test(x) ? "are" : "is";
                }''')
rep('''                  hn.length &&
                    S.push(
                      "In the present, close at hand, " +
                        (hn.length > 1 ? "these hold it back: " : "this holds it back: ") +
                        list(pick(hn, 2, HARD, far)) +
                        ".",
                    );
                  pn.length &&
                    S.push(
                      (hn.length ? "On the same ground, where things help, you placed " : "In the present, where things help, you placed ") +
                        list(pick(pn, pn.length > 1 ? 2 : 1, SOFT, far)) +
                        ".",
                    );
                  (hl.length || pl.length) &&
                    S.push(
                      "Further on, toward the goal, " +
                        (hl.length ? list(pick(hl, 1, HARD, far)) + " waits on the side that hinders" : "") +
                        (hl.length && pl.length ? ", and " : "") +
                        (pl.length ? list(pick(pl, 1, SOFT, far)) + " on the side that helps" : "") +
                        ".",
                    );''',
'''                  var fhn = feel(hn),
                    fpn = feel(pn),
                    fhl = feel(hl),
                    fpl = feel(pl);
                  fhn && S.push("In the present, close at hand, what holds the goal back carries " + fhn + ".");
                  fpn &&
                    S.push(
                      (fhn ? "On the same ground, where things help, " : "In the present, where things help, ") + fpn + " " + are(fpn) + " already at work.",
                    );
                  (fhl || fpl) &&
                    S.push(
                      "Further on, toward the goal, " +
                        (fhl ? fhl + " " + (are(fhl) === "is" ? "waits" : "wait") + " on the side that hinders" : "") +
                        (fhl && fpl ? ", and " : "") +
                        (fpl ? fpl + " on the side that helps" : "") +
                        ".",
                    );''')
rep('''                  q2.length &&
                    S.push((q2.length > 1 ? "Today, these hold it back: " : "Today, this holds it back: ") + list(pick(q2, 2, HARD)) + ".");
                  q3.length && S.push("On the side that helps, you name " + list(pick(q3, 1, SOFT)) + ".");
                  q4.length && S.push("For the goal to take root, " + list(pick(q4, 1, SOFT)) + " has to come true.");''',
'''                  feel(q2) && S.push("Today, what holds the goal back carries " + feel(q2) + ".");
                  feel(q3) && S.push("On the side that helps, " + feel(q3) + " " + are(feel(q3)) + " already at work.");''')
# what stands in the way: no ids
rep('''                  " in the way (" +
                  ids(OP) +
                  ").";''', '''                  " in the way.";''')
rep('''              s1 && OP.length && s1.indexOf("You name") && (s1 += ' <span class="stn">(' + ids(OP) + ")</span>");''', '')
rep('''                s2 += ' <span class="stn">(' + ids(SU) + ")</span>";''', '')
# what has to be true: the sentence that only restates the question goes; the gap stays
rep('''                ? (s3 =
                    "What has to be true for the goal to take root sets the tests that what you would design will have to pass." +
                    ' <span class="stn">(' +
                    ids(CO) +
                    ")</span>")''', '''                ? (s3 = "")''')
# what you would do: no word fragments, no ids
rep('''                    " Nothing you would design, redesign, or reinforce deals yet with " +
                    phList(
                      un.slice(0, 3).map(function (k) {
                        return gsmPhNameH(k, 1);
                      }),
                    ) +
                    (un.length > 3 ? ", among other things" : "") +
                    " that stand in the way in the context you’ve grasped." +''',
    '''                    " Nothing you would design, redesign, or reinforce deals yet with " +
                    (un.length > an.length ? "most" : "some") +
                    " of what stands in the way in the context you’ve grasped." +''')
rep('''              s4 && AC.length && (s4 += ' <span class="stn">(' + ids(AC) + ")</span>");''', '')
open(p, 'w', encoding='utf-8').write(s)
print('v293b applied')
