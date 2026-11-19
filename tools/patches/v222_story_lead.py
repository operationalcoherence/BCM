"""v222: YOUR STORY SO FAR becomes the lead of Pattern Analysis (his 11-18 19:08 note).
"Consider ways to elevate it as the primary synthesis output produced by Pattern Analysis." "Prefer explanations,
tensions, reinforcing dynamics, opportunities, obstacles, and implications over counts, frequencies, and inventories."
1. YOUR STORY SO FAR moves to the top of Pattern Analysis (under THE SAME THING? prompt, above WHY IT BEHAVES THIS
   WAY), in its own panel with larger type and a line saying what it is.
2. A new paragraph in the story, WHERE THIS LEAVES THE WORK, right after the opening, ties the v221 readings into
   one implication: what holds the work in place, what it fears, what already stands, where people can cross, and
   so what the work is.
3. The story's own sentences lead with meaning, not counts: "You name 14 things…", "5 notes name support…",
   "4 notes say…", "12 notes say…", "(10 of 14)" and the like are gone; the note numbers follow in small gray type.
Wording is Claude's, for his redlines.
Usage: python3 v222_story_lead.py gsm-readable.js"""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:90]); s = s.replace(a, b)

# --- 3. meaning before counts in the story ---
rep('''                        ? "Most of what hinders sits in the present (" + hn.length + " of " + H + "), and most of what helps lies further on (" + pl.length + " of " + U + "): the help is still ahead of the trouble."''',
    '''                        ? "Most of what hinders sits in the present, and most of what helps lies further on: the help is still ahead of the trouble."''')
rep('''                          ? "Most of what helps is already here (" + pn.length + " of " + U + "), and most of what hinders lies further on (" + hl.length + " of " + H + "): the trouble is still ahead, which leaves time to meet it."''',
    '''                          ? "Most of what helps is already here, and most of what hinders lies further on: the trouble is still ahead, which leaves time to meet it."''')
rep('''                            ? "Most of what hinders (" + hn.length + " of " + H + ") and most of what helps (" + pn.length + " of " + U + ") sit in the present, so little of the context you have grasped yet reaches toward the goal."
                            : "What hinders and what helps are spread from the present toward the goal (" + hn.length + " of " + H + " hindering, and " + pn.length + " of " + U + " helping, sit in the present)."),''',
    '''                            ? "Most of what hinders and most of what helps sit in the present, so little of the context you have grasped yet reaches toward the goal."
                            : "What hinders and what helps are spread from the present toward the goal, so the work meets both all the way along."),''')

rep('''                  " in the way (" +
                  ids(OP) +
                  ").";
                if (E.n && hard * 2 >= E.n)''', '''                  " in the way (" +
                  ids(OP) +
                  ").";
                var c1 = s1;
                if (E.n && hard * 2 >= E.n)''')
rep('''                    " Most of them carry aggression or defiance (" +
                    hard +
                    " of " +
                    E.n +
                    "), the two emotions''', '''                    " Most of what stands in the way carries aggression or defiance, the two emotions''')
rep('''                    " Most of them carry distrust (" +
                    E.c[2] +
                    " of " +
                    E.n +
                    "). Distrust''', '''                    " Most of what stands in the way carries distrust. Distrust''')
rep('''                    " Most of them carry indifference (" +
                    E.c[3] +
                    " of " +
                    E.n +
                    "): people not yet''', '''                    " Most of what stands in the way carries indifference: people not yet''')
rep('''                var VO = {};
                OP.forEach(function (o) {''', '''                s1 !== c1 && (s1 = s1.slice(c1.length).trim());
                var VO = {};
                OP.forEach(function (o) {''')
rep('''              out += P0("WHAT STANDS IN THE WAY", s1);''',
    '''              s1 && OP.length && s1.indexOf("You name") && (s1 += ' <span class="stn">(' + ids(OP) + ")</span>");
              out += P0("WHAT STANDS IN THE WAY", s1);''')
rep('''                s2 =
                  SU.length +
                  " note" +
                  (SU.length > 1 ? "s name" : " names") +
                  " support already there (" +
                  ids(SU) +
                  ").";
                OP.length >= 2 * SU.length &&
                  (s2 +=
                    " That is " +
                    OP.length +
                    " things against the goal to " +
                    SU.length +
                    " for it. The map may be weighted toward what is wrong because that is how things are, or because that is where you have looked; it is worth asking who else could name what is working.");''',
    '''                s2 = "Support for the goal is already at work.";
                OP.length >= 2 * SU.length &&
                  (s2 =
                    "Support for the goal is already at work, but the map leans hard toward what is wrong. That may be how things are, or it may be where you have looked; it is worth asking who else could name what is working.");''')
rep('''              } else if (OP.length)
                s2 =
                  "No note yet names what is already working for the goal. Without it, every move has to start from nothing.";''',
    '''                s2 += ' <span class="stn">(' + ids(SU) + ")</span>";
              } else if (OP.length)
                s2 =
                  "No note yet names what is already working for the goal. Without it, every move has to start from nothing.";''')
rep('''                ? (s3 =
                    CO.length +
                    " note" +
                    (CO.length > 1 ? "s say" : " says") +
                    " what has to be true for the goal to take root (" +
                    ids(CO) +
                    "). Each one is a test the actions in Q.5–Q.7 will have to pass.")''',
    '''                ? (s3 =
                    "What has to be true for the goal to take root sets the tests that what you would design will have to pass." +
                    ' <span class="stn">(' +
                    ids(CO) +
                    ")</span>")''')
rep('''                s4 =
                  AC.length +
                  " note" +
                  (AC.length > 1 ? "s say" : " says") +
                  " what you would do (" +
                  ids(AC) +
                  "). Most of it would " +
                  big[0][1] +
                  ".";''', '''                s4 = "Most of what you would do would " + big[0][1].replace(/ \\(Q\\.\\d\\)$/, "") + ".";''')
rep('''              out += P0("WHAT YOU WOULD DO", s4);''',
    '''              s4 && AC.length && (s4 += ' <span class="stn">(' + ids(AC) + ")</span>");
              out += P0("WHAT YOU WOULD DO", s4);''')

# --- 2. the structure summary for the story ---
rep('''  function gsmStructBuild() {
    gsmMeanCss();''', '''  function gsmStructBuild() {
    gsmMeanCss();
    var SS = (window.gsmStructSum = {});''')
rep('''    if (sysNames.length >= 3) {
      var tied''', '''    if (sysNames.length >= 3) {
      SS.sys = sysNames.slice(0, 3);
      SS.low = [0, 2, 4].indexOf(gsmStEm(comp).o[0]) >= 0;
      var tied''')
rep('''      if (fears.length && helpHas) {
        var f0 = fears[0].n,''', '''      if (fears.length && helpHas) {
        SS.tension = 1;
        var f0 = fears[0].n,''')
rep('''    if (lk) {
      var lsk''', '''    if (lk) {
      SS.loop = 1;
      var lsk''')
rep('''    if (exNames.length >= 2) {
      var oe = gsmStEm(ex).o[0];''', '''    if (exNames.length >= 2) {
      var oe = gsmStEm(ex).o[0];
      SS.opp = ex.length >= nw.length ? "Most" : "Part";''')
rep('''    if (ind.length && sysNames.length >= 3) {''', '''    if (ind.length && sysNames.length >= 3) {
      SS.cross = ind.slice(0, 4).map(gsmStRef);''')

# --- 1. the story leads the page ---
JS = r'''
  function gsmStoryLead(root, tries) {
    if (!root || root.querySelector(".storylead")) return;
    var sm = [].slice.call(root.querySelectorAll("details.fold > summary")).filter(function (x) {
      return "YOUR STORY SO FAR" === x.textContent.trim();
    })[0];
    if (!sm) {
      (tries || 0) < 12 &&
        setTimeout(function () {
          try {
            gsmStoryLead(root, (tries || 0) + 1);
          } catch (e) {}
        }, 250);
      return;
    }
    var fd = sm.parentNode,
      anchor =
        [].slice.call(root.querySelectorAll(".plab")).filter(function (p) {
          return /^(WHY IT BEHAVES THIS WAY|WHAT YOUR USE OF THE BEAR CANYON METHOD PRODUCED)/.test(p.textContent.trim());
        })[0] || root.querySelector(".plab");
    if (!anchor) return;
    var box = document.createElement("div");
    box.className = "storylead";
    anchor.parentNode.insertBefore(box, anchor);
    box.appendChild(fd);
    fd.open = !0;
    sm.innerHTML = 'YOUR STORY SO FAR<span class="stsub">What Pattern Analysis makes of your workbook: the story first, the evidence after.</span>';
    var SS = window.gsmStructSum || {},
      P = [];
    SS.sys &&
      P.push(
        Gt(SS.sys.join(", ")).replace(/^./, function (c) {
          return c.toUpperCase();
        }) +
          ", and what stands with them," +
          (SS.low ? " hold the work in place from the low ground" : " hold the work in place for now, though loosely") +
          (SS.loop ? ", and a loop in it makes each round harder than the last." : "."),
      );
    SS.tension && P.push("What the goal needs more of is what that ground has learned to fear.");
    SS.opp && P.push(SS.opp + " of the alternative already stands on higher ground.");
    SS.cross && P.push("The way between them runs through the indifference in " + SS.cross.join(", ").replace(/,([^,]*)$/, ", and$1") + ".");
    SS.opp && SS.cross
      ? P.push("So the work is less about inventing than about reinforcing what already stands and bringing people across that ridge.")
      : SS.opp
        ? P.push("So the work is less about inventing than about reinforcing what already stands.")
        : SS.sys && P.push("So the work starts with what keeps that system in place, not with persuasion.");
    if (P.length >= 3) {
      var mt = fd.querySelector(".mtext"),
        p1 = mt && mt.querySelector(":scope > p");
      if (mt) {
        var h = document.createElement("div");
        h.className = "csl stimp";
        h.textContent = "WHERE THIS LEAVES THE WORK";
        var p = document.createElement("p");
        p.className = "stimpp";
        p.innerHTML = P.join(" ");
        p1 ? (p1.after(h), h.after(p)) : (mt.prepend(p), mt.prepend(h));
      }
    }
  }
'''
rep('''  function gsmMeanPass(sec) {
    setTimeout(function () {
      try {
        if (!sec || !sec.closest || !sec.closest('[data-pv="2"]')) return;
        gsmMeanRun(sec);
      } catch (e) {}
    }, 0);
  }''', JS + '''  function gsmMeanPass(sec) {
    setTimeout(function () {
      try {
        if (!sec || !sec.closest || !sec.closest('[data-pv="2"]')) return;
        gsmMeanRun(sec);
        gsmStoryLead(sec.closest('[data-pv="2"]'));
      } catch (e) {}
    }, 0);
  }''')
rep('''#gsm .sread .srq{margin:8px 0 4px;color:#222}";''',
    '''#gsm .sread .srq{margin:8px 0 4px;color:#222}#gsm .storylead{margin:18px 0 26px}#gsm .storylead>details.fold{border:2px solid #111;background:#faf8f3;padding:2px 20px 8px}#gsm .storylead>details.fold>summary{font-size:16px;letter-spacing:.14em}#gsm .storylead .stsub{display:block;font-weight:400;letter-spacing:0;font-size:13px;color:#666;margin-top:4px}#gsm .storylead .mtext>p:first-of-type,#gsm .storylead .mtext p.stimpp{font-size:17.5px;line-height:1.65;color:#111}#gsm .storylead .mtext p.stimpp{border-left:3px solid #111;padding-left:12px}#gsm .storylead .mtext p{font-size:15.5px;line-height:1.6}#gsm .stn{color:#888;font-size:13px}";''')
rep('t && (t.textContent = "v221");', 't && (t.textContent = "v222");')
open(P, "w").write(s)
print("ok")
