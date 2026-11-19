"""v236: his answers to the pre-F8 review table (11-19 09:20), applied as one build.
Usage: python3 v236_review_answers.py gsm-readable.js"""
import sys
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)

# 1b, 1e: Start here (his text)
rep("Keep the workbook and return to it as things change while working in the context.</li>",
    "Keep the workbook and return to it as things change while working in the context, especially as acting brings new information to light.</li>")
rep("<li><span>03</span>One and four are the leading questions. The remainder are guidance for their answer.",
    "<li><span>03</span>One through four are questions about grasping context. The remainder are questions about how to design for the context just grasped.")
# 1g: emotion, never feeling
rep("How a note feels, how you know it, and whose view it carries.", "The emotion a note carries, how you know it, and whose view it carries.", 2)
# 2i
rep("part of the larger pattern your answers and notes form, shown in Mapping Synthesis.", "part of the larger pattern your answers and notes form, shown in Pattern Synthesis.")
# 2k
rep("Specify the location of the goal\\'s context to activate the mapping layer. This will be populated below. Leave blank to use the method without a place.",
    "Add the place the goal is about, if it has one, and the place map opens below. Leave it blank for a goal with no place, such as a policy or a practice; the line map is built for those.")
# 3g: strip heading (his wording)
rep("<div class=\"owgl\">WHAT YOU WOULD DESIGN</div>", "<div class=\"owgl\">WHAT YOU WOULD DESIGN FOR THAT CONTEXT</div>")
# 3s, 6t: define THE LOOP and WHERE IT CAN CROSS where they are read
rep('''    function card(lab, html, ev) {
      R.push(
        '<div class="sread"><div class="srl">' +
          lab +
          '</div><div class="srm">' +''', '''    var SDEF = {
      "THE LOOP": "A loop, in this method, is a reinforcing cycle: each turn of it makes the next turn more likely. Systems thinking calls this positive feedback, where positive means self-amplifying, not good. It is not a balancing loop that settles back on its own.",
      "WHERE IT CAN CROSS": "Crossing is a move from one emotion\\u2019s ground to another\\u2019s, such as from distrust toward acceptance. Distant emotions take the most energy to cross between, in either direction.",
    };
    function card(lab, html, ev) {
      R.push(
        '<div class="sread"><div class="srl">' +
          lab +
          "</div>" +
          (SDEF[lab] ? '<div class="srdef">' + SDEF[lab] + "</div>" : "") +
          '<div class="srm">' +''')
rep('''purp: "Each round of it makes the next round harder. Break it at a step you can change, and the ground stops sinking.",''',
    '''purp: "A reinforcing loop: each round of it makes the next round harder. Break it at a step you can change, and the ground stops sinking.",''')
# 4c: tour act openers (his wording)
rep('"Acceptance: where the goal already has people with it. It takes care to keep, and it is the place to start from. "',
    '"Acceptance: where the goal already has people aligned with it. It takes care to keep, and it is the place to start from. "')
rep("They are not bad in themselves; what matters is what they are attached to. The deeper",
    "They are not bad in themselves; what matters is what they are attached to and the present and future they create. The deeper")
# 34: rename
rep("THE EMOTION CHANGES", "THE HIDDEN CHANNELS", 7)
# 5f: In Parallel figure, a lone word is shown as the shortest note that carries it
rep('''        return { k: o.k, ok: o.ok, kind: o.kind, nm: nm, ns: hit };''', '''        if (!/\\s/.test(String(nm).trim()) && hit.length) {
          var sh = hit.slice().sort(function (a, b) {
              return String(a.t).length - String(b.t).length;
            })[0],
            sw = String(sh.t).replace(/\\s+/g, " ").trim().split(" ");
          nm = "\\u201c" + sw.slice(0, 4).join(" ").replace(/[.,;:]+$/, "") + (sw.length > 4 ? "\\u2026" : "") + "\\u201d";
          nm = nm.replace(/[.,;:]+(\\u2026)/, "$1");
        }
        if (!/\\s/.test(String(nm).trim()) && !hit.length) return null;
        return { k: o.k, ok: o.ok, kind: o.kind, nm: nm, ns: hit };''')
rep('''        return { k: o.k, ok: o.ok, kind: o.kind, nm: nm, ns: hit };
      }),
      SVGN = "http://www.w3.org/2000/svg",''', '''        return { k: o.k, ok: o.ok, kind: o.kind, nm: nm, ns: hit };
      }).filter(Boolean),
      SVGN = "http://www.w3.org/2000/svg",''')
# 6f: Carries furthest, in situation language
rep('''                    n(a.c) +
                    " shares notes with " +
                    a.n +
                    " of the other cards, more than any other, so what you decide about it carries furthest.</div>"));''',
    '''                    "Decide " +
                    n(a.c) +
                    " first. It touches more of the situation than anything else here, so what you decide about it reaches furthest.</div>"));''')
rep('''        b && (b.textContent = "Carries furthest:");''', '''        b && b.parentNode.removeChild(b);''')
# 6l, 6s
rep('loop: "The proposed actions address the reinforcing cycle identified in Pattern Analysis.",', 'loop: "What you would design breaks into the cycle that keeps the situation going.",')
rep('" Most shifts happen where people are for nothing yet, the ridge of indifference: " +', '" Most shifts happen on the ridge of indifference, where people are not yet for or against: " +')
rep("People there are for nothing yet, so they can be moved either way", "People there are not yet for or against, so they can be moved either way")
rep("First look for people who are for nothing yet, and add them", "First look for people who are not yet for or against, and add them")
rep("No one is mapped as for nothing yet, so there is no ridge of indifference: every shift is a climb over bare rock. Ask who is for nothing yet.",
    "No one is mapped as not yet for or against, so there is no ridge of indifference: every shift is a climb over bare rock. Ask who is not yet for or against.")
# 6g: ground card titles, note numbers behind
rep('''Gt(em.charAt(0).toUpperCase() + em.slice(1) + " among acceptance, where things help (" + phList(ids) + ")") +
                      \'</b>''', '''Gt(em.charAt(0).toUpperCase() + em.slice(1) + " among acceptance, where things help") +
                      \'</b><span class="gids">\' + Gt(phList(ids)) + "</span>" +
                      \'''')
# W1, W2
rep('<div class="pnote"><b>Prompts, not findings.</b> Each card grows from what Pattern Analysis, Pattern Synthesis, and In Parallel found, or from the words you used. Talk them through with the people involved, and change or drop any that do not fit.</div>',
    '<div class="pnote"><b>Prompts, not findings:</b> talk them through with the people involved, and change or drop any that do not fit.</div>')
rep('<div class="tatsub">Read against the situation you have mapped. The cards below take up each line.</div>', '')
# W3: the two help lines once, under STRATEGIES
rep('''<div class="fhelp">Listed in WHAT YOU DECIDED AND WHY, at the end of the page.</div>''', '')
rep('''<div class="fhelp">Saved with the date. This card’s notes are flagged on Mapping Landscape to map again.</div>''', '')
rep('''    grp("STRATEGIES", "For what holds the goal back and where it has to cross: ground that is not settled.", mS, st);''',
    '''    grp("STRATEGIES", "For what holds the goal back and where it has to cross: ground that is not settled.", mS, st);
    (function () {
      var h = ph.parentNode.querySelector(".tagrp");
      if (!h || ph.parentNode.querySelector(".tacardhelp")) return;
      var d = document.createElement("div");
      d.className = "fhelp tacardhelp";
      d.textContent = "On every card: YOUR DECISION is listed in WHAT YOU DECIDED AND WHY, at the end of the page. WHAT YOU DID is saved with the date, and the card\\u2019s notes are flagged on Mapping Landscape to map again.";
      h.appendChild(d);
    })();''')
rep('''"#gsm .owstrip{''', '''"#gsm .srdef{font-size:12.5px;line-height:1.45;color:#777;margin:2px 0 6px}#gsm .gids{font-size:11.5px;color:#999;font-weight:400;margin-left:6px}#gsm .tacardhelp{margin:4px 0 8px}#gsm .owstrip{''')
rep('t && (t.textContent = "v235");', 't && (t.textContent = "v236");')
open(P, "w").write(s)
print("ok")
