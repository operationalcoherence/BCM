# v257: WHAT THE SYSTEM IS DOING trimmed to match the approved definitions and tied to the
# user's own levers (his go-ahead 11-24 12:10; review: claude/pattern_analysis_reader_review_2026-11-24.md).
# Six paragraphs become four: no repeated sequence, no textbook close, the Q.1 reasons
# acknowledged instead of contradicted, "who belongs" dropped, and an ending that names what
# the user's own design already reaches and what nothing yet answers. Engine-wide; no 3D change.
import sys
p = "gsm-readable.js"
s = open(p, encoding="utf-8").read()

a = s.index("    /* 1. pattern */\n    EP.push(")
b = s.index("    /* v251: AT A GLANCE opens with what the system is doing")
NEW = r'''    /* v257: four paragraphs (his go-ahead 11-24 12:10). 1 the pattern and how it moves; 2 what keeps
       it going, after the user's own Q.1 reasons; 3 what it protects and why that is reasonable;
       4 what the user's own design already reaches, and what nothing yet answers. */
    var Q1 = ((C && C.a && C.a[0]) || "").toLowerCase(),
      saidInfo = /knowledge|information|understand|aware|educat|learn|familiar/.test(Q1),
      DS = []
        .concat(
          ((C && C.a) || []).slice(4, 7),
          ((C && C.m) || [])
            .filter(function (t) {
              return t[0] >= 5;
            })
            .map(function (t) {
              return t[3] || "";
            }),
        )
        .join(" \n ")
        .toLowerCase(),
      Q2 = ((C && C.a && C.a[1]) || "").toLowerCase();
    EP.push(
      "The change meets resistance again and again, and each time the resistance takes the shape the change has reached: " +
        forms.replace(/, and /, ", and finally ").replace(/^([^,]*) and /, CH.length === 2 ? "$1, and then " : "$1 and ") +
        ". With each step it moves closer to each person and further out of sight" +
        (hasGoal ? ", until the change looks adopted while the old order goes on inside it." : ".") +
        (helpAgg ? " Around it, support answers resistance in kind, and each side hardens the other." : "") +
        (wideMid ? " Between them lies a wide middle, neither for nor against, waiting to see which way things go." : ""),
    );
    var M = [];
    anyAcc && M.push("the present arrangement is still accepted as the right one, so any alternative has to argue against common sense");
    helpAgg && M.push("each side reads the other's response as proof of its own fears");
    hasMid && M.push("the rewards people can count on are tied to the places they hold now");
    hasGoal && M.push("the change is judged by what is declared rather than by what is done");
    M.length < 2 && M.push("nothing in the change yet alters what people are trusted, protected, or rewarded for");
    EP.push(
      (saidInfo
        ? "A lack of knowledge is among the reasons you gave, but the notes point more strongly elsewhere: "
        : "What keeps it going is that ") +
        (M.length > 2 ? M.slice(0, -1).join("; ") + "; and " + M[M.length - 1] : M.join(" and ")) +
        ". Each of these keeps recreating the same response, because the response keeps the system able to act in the way it already knows.",
    );
    var INV = {
      legit: "the standing of the present arrangement as the legitimate one: a shared sense of what is right" + (hasMid ? ", and of each person's place in it" : ""),
      ident: "its present identity: people remaining recognizable to themselves and to one another",
      order: "the present order of control: knowing who decides, what counts as good work, and who is safe",
    }[K];
    EP.push(
      "Underneath, one thing stays the same. From beginning to end the system protects " +
        INV +
        ". That is not unreasonable. " +
        (K === "legit"
          ? "Without that shared sense, every decision would have to be fought for again."
          : K === "ident"
            ? "Without that continuity, people lose the pride and competence their work carries."
            : "Without it, the system cannot coordinate under pressure.") +
        (hasMid ? " For the people inside it the stakes are also material: their places, skills, and livelihoods rest on the arrangement as it stands." : ""),
    );
    /* the levers: each mechanism, and whether the user's own design (Q.5 to Q.7 and their notes;
       for the protected order, Q.2's reassurance too) already reaches it */
    var LV = [],
      NO = [];
    function lever(on, re, txt, gap, also) {
      if (!on) return;
      re.test(DS) || (also && re.test(also)) ? LV.push(txt) : NO.push(gap);
    }
    lever(
      anyAcc || K !== "legit",
      /orderl|predictab|repeatab|stabil|reassur|continuit|familiar|retain|keep the/,
      "keeping the order people rely on available when conditions call for it",
      "how the order people rely on is kept while the change goes in",
      Q2,
    );
    lever(hasMid, /expectation|incentive|reward|role|career|employ|job|position|performance|train/, "changing what people are expected and rewarded for", "what the change offers people in place of the positions they hold now");
    lever(hasGoal, /measur|pattern|monitor|observ|evaluat|assess|indicator|metric/, "measuring what people do rather than what is declared", "how the change will be judged by what is done");
    lever(helpAgg, /oppos|across|bridge|dialog|discussion|conversation|engag|participat|includ|listen|perspective/, "engaging those who resist rather than only those who already agree", "how support reaches across the line instead of answering resistance in kind");
    EP.push(
      "Change succeeds here not when the resistance is overcome but when what it protects is provided another way: " +
        (K === "legit"
          ? "a new arrangement people can hold as legitimately as the old one."
          : K === "ident"
            ? "a new way of working people can recognize themselves in."
            : "a new order as predictable as the old one.") +
        (LV.length ? " Your own answers already reach part of this: " + gsmMeanList(LV) + "." : "") +
        (NO.length ? " Nothing you would design yet answers " + gsmMeanList(NO) + "." : "") +
        " Pressing or outlasting the resistance only teaches it new forms.",
    );
'''
s = s[:a] + NEW + s[b:]

old = 'legit: "what the present arrangement gives it: a shared sense of what is right and of who belongs",'
assert s.count(old) == 1, "GI"
s = s.replace(old, 'legit: "what the present arrangement gives it: a shared sense of what is right" + (hasMid ? ", and each person\\u2019s place" : ""),')

old = 't && (t.textContent = "v256");'
assert s.count(old) == 1, "label"
s = s.replace(old, 't && (t.textContent = "v257");')
open(p, "w", encoding="utf-8").write(s)
print("ok")
