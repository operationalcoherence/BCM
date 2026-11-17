"""v171 batch 1: renames, removals, bug fixes, wording, IP footer, references.
Run on the readable source: python3 batch1.py src.js"""
import sys
P = sys.argv[1]
s = open(P).read()


def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, (c, n, a[:90])
    s = s.replace(a, b)


# ---- U1: Mapping Change -> Mapping Landscape (page name, tab, instructions, back links)
assert s.count("Mapping Change") == 16, s.count("Mapping Change")
s = s.replace("Mapping Change", "Mapping Landscape").replace("MAPPING CHANGE", "MAPPING LANDSCAPE")
rep("the change map", "the landscape map", 4)

# ---- At a glance: drop PRESSING NOW ("fire in 22 places"), TOP STRATEGY, TOP PROGRAM, WHAT IT RESTS ON, WHAT YOU LINKED
rep('r && o.push(["PRESSING NOW", r.textContent, f("WHAT TO PAY ATTENTION TO")]);', "")
rep("""                s &&
                  o.push([
                    "TOP STRATEGY",""", """                0 && s &&
                  o.push([
                    "TOP STRATEGY",""")
rep("""                l &&
                  o.push([
                    "TOP PROGRAM",""", """                0 && l &&
                  o.push([
                    "TOP PROGRAM",""")
rep('c && window.gsmGround && o.push(["WHAT IT RESTS ON", window.gsmGround, c]);', "")
rep('u && window.gsmLinkG && o.push(["WHAT YOU LINKED", window.gsmLinkG, u]);', "")

# ---- IN THE WORDS: a recurring name is not a finding
rep("""                      "ANSWERED, WITH NOTHING ON THE MAP": 1,
                    }[t[0]];""", """                      "ANSWERED, WITH NOTHING ON THE MAP": 1,
                      "A NAME THAT RECURS": 1,
                    }[t[0]];""")

# ---- B6: "Q.1 not already is answered but has no symbol on the map yet"
rep("""            t && !D[e + 1] && W.push("Q." + (e + 1) + " " + n[e]);""",
    """            t &&
              !D[e + 1] &&
              W.push(
                "Q." +
                  (e + 1) +
                  " (" +
                  ["why the goal has not taken root", "opposition", "support", "conditions", "design", "redesign", "reinforce"][e] +
                  ")",
              );""")
rep("""              W.join(", ") +
                (W.length > 1 ? " are" : " is") +
                " answered but " +
                (W.length > 1 ? "have" : "has") +
                " no symbol on the map yet.",""",
    """              W.join(", ") +
                (W.length > 1 ? " are" : " is") +
                " answered, but no note on the map carries " +
                (W.length > 1 ? "their symbols" : "its symbol") +
                " yet. What you wrote there is still only in the answer. On Mapping Landscape, add a note with " +
                (W.length > 1 ? "each symbol" : "that symbol") +
                " where it belongs, so the map can show it.",""")

# ---- WHAT IT MIGHT MEAN (Pattern Synthesis): no recurrence counts; keep what has meaning, say what to do
rep('''              "They are part of why the goal has not taken root or of the opposition, with nothing planned for them yet. These may be gaps in Q.5–Q.7.",
              "It is part of why the goal has not taken root or of the opposition, with nothing planned for it yet. This may be a gap in Q.5–Q.7.",''',
    '''              "You name them as part of why the goal has not taken root (Q.1), as opposition (Q.2) or as conditions (Q.4), but nothing you would design, redesign or reinforce (Q.5–Q.7) deals with them yet. Left alone, they keep holding the goal back as they do now. For each one, ask what would have to be designed, redesigned or reinforced so it no longer stands in the way, and add that to Q.5–Q.7 or as a note.",
              "You name it as part of why the goal has not taken root (Q.1), as opposition (Q.2) or as a condition (Q.4), but nothing you would design, redesign or reinforce (Q.5–Q.7) deals with it yet. Left alone, it keeps holding the goal back as it does now. Ask what would have to be designed, redesigned or reinforced so it no longer stands in the way, and add that to Q.5–Q.7 or as a note.",''')
rep('''              "They repeat across Q.5–Q.7 without a cause or objection behind them. Worth asking what they answer.",
              "It repeats across Q.5–Q.7 without a cause or objection behind it. Worth asking what it answers.",''',
    '''              "They appear only in what you would design, redesign or reinforce (Q.5–Q.7). Nothing in Q.1–Q.4 says what problem they solve or what condition they meet. An action with no reason written behind it is hard to defend and easy to drop: for each, write down the cause, opposition or condition it answers, in Q.1–Q.4 or as a note.",
              "It appears only in what you would design, redesign or reinforce (Q.5–Q.7). Nothing in Q.1–Q.4 says what problem it solves or what condition it meets. An action with no reason written behind it is hard to defend and easy to drop: write down the cause, opposition or condition it answers, in Q.1–Q.4 or as a note.",''')
rep('''              "They support the goal already, and there is something to reinforce.",
              "It supports the goal already, and there is something to reinforce.",''',
    '''              "They already support the goal. To reinforce one, add a note with the Q.7 (reinforce) symbol on Mapping Landscape that says who keeps it going, with what, and for how long.",
              "It already supports the goal. To reinforce it, add a note with the Q.7 (reinforce) symbol on Mapping Landscape that says who keeps it going, with what, and for how long.",''')
rep('''          ((lt +=
            "<p><b>" +
            it.length +
            " words and phrases recur</b> across your goal, answers and notes. Read by where they appear:</p>"),
            [
              "unanswered",
              "contested",
              "answered",
              "unused",
              "condition",
              "plan",
              "strength",
              "goal",
            ].forEach(''', '''          ([
              "unanswered",
              "contested",
              "unused",
              "plan",
              "strength",
            ].forEach(''')
rep('''          ut > dt
            ? (lt +=
                "<p>More of what recurs is missing from Q.5–Q.7 than appears in them, so they may not yet reach the causes and objections you named.</p>")
            : 0;''', "")
rep('''          lt +=
            "<p>" +
            (ht.length
              ? ht.length +''', '''          0 &&
            (lt +=
            "<p>" +
            (ht.length
              ? ht.length +''')
rep('''              : "None of them are in the goal, so the answers may be drifting from it.") +
            "</p>";''', '''              : "None of them are in the goal, so the answers may be drifting from it.") +
            "</p>");''')

# ---- C3: say what "behaviors first" and "emotions first" are, in place (Vigneaux, 2026); no domain words
rep('''"<p>Aggression and defiance are as strong as acceptance, or stronger. The article’s “behaviors first” strategy may fit: start with actions that work alongside the emotions already there.</p>")''',
    '''"<p>Aggression and defiance are as strong as acceptance, or stronger. Vigneaux (2026) describes two ways of working with emotion. <b>Emotions first</b> suits acceptance and indifference: connect people to acceptance, or something close to it, then tie that acceptance to what needs doing. <b>Behaviors first</b> suits aggression, distrust and defiance: introduce the behavior itself, without its label, in a form that fits the emotions already there, and let a small shift in emotion follow over time. Here, behaviors first may fit.</p>")''')
rep('''"<p>Acceptance is the strongest emotion in your notes. The article’s “emotions first” strategy may fit: start where people already accept, and build toward the mitigation work.</p>")''',
    '''"<p>Acceptance is the strongest emotion in your notes. Vigneaux (2026) calls this ground ready for <b>emotions first</b>: connect people to the acceptance already there, then tie it to what needs doing to reach the goal. (The other way, <b>behaviors first</b>, suits aggression, distrust and defiance: introduce the behavior itself, without its label, and let the emotion shift after it.)</p>")''')

# ---- WHAT IT RESTS ON: keep Source, Voices and how a word reads by voice; drop per-question voice lines
rep("""            (dn.length && on.push("No note yet speaks for " + dn.map(Gt).join(", ") + "."),
              [2, 3, 4, 7, 1, 5, 6].forEach(""", """            (dn.length && on.push("No note yet speaks for " + dn.map(Gt).join(", ") + "."),
              [].forEach(""")
rep("""                Ie.length &&
                  on.push(
                    "<b>" +
                      Ie.slice(0, 4).join(", ") +""", """                Ie.length &&
                  0 &&
                  on.push(
                    "<b>" +
                      Ie.slice(0, 4).join(", ") +""")

# ---- WHAT YOU LINKED: about linking notes, not about dots moved in the old figure
rep("""            wn.moved.length &&
              gn.push(
                "<b>You moved " +""", """            0 &&
              wn.moved.length &&
              gn.push(
                "<b>You moved " +""")
rep('<div class="plab">WHAT YOU LINKED</div><div class="msub">Links you drew between notes, answers and the goal, including the ones you added in the figures, and what you moved or hid there. They sit beside the links the words make, and they can join things the words never would.</div>',
    '<div class="plab">WHAT YOU LINKED</div><div class="msub">Links you drew between notes, answers and the goal on Mapping Landscape (open a note and use + Link). They sit beside the threads the words make, and they can join things the words never would.</div>')

# ---- C5: define "thread" where it is used; say what "grounded" means
rep('''                  "<b>Spread out.</b> The threads run through " +
                    Ue.length +
                    " pieces fairly evenly, so no single answer or note holds the picture together.",''',
    '''                  "<b>Spread out.</b> A thread is a word or phrase that two or more answers or notes share. Here the threads run through " +
                    Ue.length +
                    " answers and notes fairly evenly, so no single one holds the picture together.",''')
rep('''                  "<b>Leans on a few pieces.</b> " +''', '''                  "<b>Leans on a few pieces.</b> A thread is a word or phrase that two or more answers or notes share. " +''')
rep('''            Fe.push(
              "<b>Grounded " +
                (Je.length ? "unevenly" : "across the board") +
                ".</b> On the map: " +
                Ke.join(", ") +
                "." +''', '''            Fe.push(
              "<b>Grounded " +
                (Je.length ? "unevenly" : "across the board") +
                ".</b> " +
                (Je.length ? "The map has notes for: " : "Every kind of answer has notes on the map (") +
                Ke.join(", ") +
                (Je.length ? "." : "), so each part of your thinking has something on the ground to check it against.") +''')

# ---- Pattern Synthesis: the old figure goes; it stays only where the 3D map cannot be drawn (no notes)
rep("""'<div class="gterr-host"></div><details class="fold gtold"><summary>THE EARLIER FIGURE</summary>' +
                  ee(de.slice(0, qe), ge, Eo, de) +
                  "</details>")""", """'<div class="gterr-host"></div><div class="gtold" style="display:none" aria-hidden="true">' +
                  ee(de.slice(0, qe), ge, Eo, de) +
                  "</div>")""")

# ---- Pattern Synthesis layout: what the ground says above the map, phrases right under it (open), how it is made at the top
old_tpl_head = '''<div class="plab">THE LAY OF THE LAND</div><div class="sub">The ground your notes describe, read before Taking Action leads you across it. The numbers on the ground are explained below the map. Drag to turn it; scroll or pinch to zoom.</div>
  <div class="bar">
  </div>'''
new_tpl_head = '''<div class="plab">THE LAY OF THE LAND</div><div class="sub">The ground your notes describe, read before Taking Action leads you across it. Each number on the ground is explained here first; hover or tap a number on the map to read it there. Drag to turn the map; scroll or pinch to zoom.</div>
  <div class="sec" data-gt="rdhead" style="margin-top:12px">WHAT THE GROUND SAYS</div>
  <div data-gt="readings"></div>
  <div class="bar">
  </div>'''
rep(old_tpl_head.replace('\n','\\n'), new_tpl_head.replace('\n','\\n'))
T2=('''  <div class="sec" data-gt="crshead" style="margin-top:12px">MODEL A COURSE OF ACTION</div>
  <div data-gt="courses"></div>
  <div data-gt="coursebox"></div>
  <div class="sec" data-gt="rdhead" style="margin-top:12px">WHAT THE GROUND SAYS</div>
  <div data-gt="readings"></div>
  <div data-gt="selnote" class="row"></div>
  <details class="gfold"><summary><span class="sec" data-gt="phhead">PHRASES THAT RUN THROUGH</span></summary>
  <div class="small" style="margin:4px 0">Two words used together in more than one note or answer, with what each means. Tick one to draw its loop on the map.</div>
  <div data-gt="threads"></div></details>
  <details class="gfold"><summary><span class="sec">HOW THIS MAP IS MADE</span></summary>''',
    '''  <div data-gt="selnote" class="row"></div>
  <details class="gfold" open><summary><span class="sec" data-gt="phhead">PATTERNS THAT RUN THROUGH IT</span></summary>
  <div class="small" style="margin:4px 0">Two words used together in more than one note or answer, with what each means. Tick one to draw its loop on the map above.</div>
  <div data-gt="threads"></div></details>
  <div class="sec" data-gt="crshead" style="margin-top:12px">MODEL A COURSE OF ACTION</div>
  <div data-gt="courses"></div>
  <div data-gt="coursebox"></div>
  <details class="gfold gthow"><summary><span class="sec">HOW THIS MAP IS MADE</span></summary>''')
rep(T2[0].replace('\n','\\n'), T2[1].replace('\n','\\n'))
# move HOW THIS MAP IS MADE to the top of the page, under LOOKING OUT (Pattern Synthesis only, not on cards)
rep('''  function mount(host, data) {
    "use strict";
    host.className += " gterr";
    host.innerHTML = TPL;''', '''  function mount(host, data) {
    "use strict";
    host.className += " gterr";
    host.innerHTML = TPL;
    (function () {
      var how = host.querySelector(".gthow"),
        sec = host.closest(".secb") || host.parentNode,
        root = document.getElementById("gsm"),
        part = null;
      if (!how) return;
      if (data && data.card) {
        how.remove();
        return;
      }
      if (root)
        root.querySelectorAll(".part").forEach(function (p) {
          if (!part && /LOOKING OUT/.test(p.textContent) && p.offsetParent !== undefined) part = p;
        });
      var old = root && root.querySelector(".gthow-top");
      if (old) old.remove();
      if (part && part.parentNode) {
        how.className = "fold gthow-top";
        how.style.margin = "14px 0 4px";
        host._how = how;
        part.parentNode.insertBefore(how, part.nextSibling);
      }
    })();''')

# ---- C4: cite Thompson (2007) where the cell image is used
rep('''                " Like a cell turning toward what feeds it, this is the direction the ground already favors: the least costly way up leads toward N" +
                u.dest.k +
                ".",''', '''                " Like a cell turning toward what feeds it (Thompson, 2007), this is the direction the ground already favors: the least costly way up leads toward N" +
                u.dest.k +
                ".",''')

# ---- R1: references on Taking Action (Kurtz & Snowden) and a full reference list at the end of the workbook
rep('''<div class="msub">Morin, E. (2008). <i>On complexity</i>. (R. Postel, Trans.). Cresskill, NJ: Hampton Press.</div>''',
    '''<div class="msub">Kurtz, C. F., &amp; Snowden, D. J. (2003). The new dynamics of strategy: Sense-making in a complex and complicated world. <i>IBM Systems Journal, 42</i>(3), 462-483.</div><div class="msub">Morin, E. (2008). <i>On complexity</i>. (R. Postel, Trans.). Cresskill, NJ: Hampton Press.</div>''')

REFS = ('<details class="fold gsmrefs"><summary>REFERENCES</summary><div class="mtext">'
        '<p>Ackoff, R. L. (1999). <i>Ackoff&#39;s best: His classic writings on management.</i> New York, NY: Wiley.</p>'
        '<p>Juarrero, A. (2023). <i>Context changes everything: How constraints create change.</i> Cambridge, MA: The MIT Press.</p>'
        '<p>Kurtz, C. F., &amp; Snowden, D. J. (2003). The new dynamics of strategy: Sense-making in a complex and complicated world. <i>IBM Systems Journal, 42</i>(3), 462-483.</p>'
        '<p>Morin, E. (2008). <i>On complexity.</i> (R. Postel, Trans.). Cresskill, NJ: Hampton Press.</p>'
        '<p>Morin, E., &amp; Kern, A. B. (1999). <i>Homeland earth: A manifesto for the new millennium.</i> (S. M. Kelly, &amp; R. LaPointe, Trans.) Cresskill, NJ: Hampton Press.</p>'
        '<p>Paci-Green, R., Vigneaux, G., Jensen, S., &amp; Petal, M. (2016). Developing and Implementing Comprehensive School Safety Policy: GADRRRES Research-into-Practice Brief.</p>'
        '<p>Thompson, E. (2007). <i>Mind in life: Biology, phenomenology, and the sciences of mind.</i> Cambridge, MA: The Belknap Press of Harvard University Press.</p>'
        '<p>Vigneaux, G. J. (2026). Transitioning From Biological Networks To Participation In Social Networks. <i>Journal of Emergency Management, 24</i>(7), 23-32. doi:10.5055/jem.0952</p>'
        '<p>Waldrop, M. M. (1992). <i>The emerging science at the edge of order and chaos.</i> New York, NY: Touchstone.</p>'
        '</div></details>')

# ---- I1: footer statement, the formal statement one tap away, and the statement on exported files
FOOT_OLD = '''<div class="copy">\\u00a9 2026 Operational Coherence. Copyrighted: attribution required.<span class="fbsep"> \\u00b7 </span><a href="mailto:greg@operationalcoherence.com?subject=Bear%20Canyon%20Method%20feedback">Send feedback</a></div>'''
FOOT_NEW = ('<div class="gsmrefwrap"></div>'
            '<div class="copy">The Bear Canyon Method (BCM) is provided free of charge for personal and professional use. Attribution to Operational Coherence is required. The Bear Canyon Method remains the intellectual property of Operational Coherence. All rights reserved.'
            '<span class="fbsep"> \\u00b7 </span><a href="mailto:greg@operationalcoherence.com?subject=Bear%20Canyon%20Method%20feedback">Send feedback</a>'
            '<details class="ipd"><summary>Intellectual property statement</summary><div class="ipt">The Bear Canyon Method (BCM) is free to use and developed by Operational Coherence. BCM is founded on original research and draws from insights derived from adjacent literature, their interpretations and experiences, and acknowledges the contributions of the broader communities from which those insights originate. The architecture, methodology, framework design, system structure, and implementation of BCM were conceived, developed, and are owned by Operational Coherence. Use of BCM is permitted without fee; attribution to Operational Coherence is required. All intellectual property rights remain with Operational Coherence.</div></details></div>')
rep(FOOT_OLD, FOOT_NEW)
# reference list sits above the footer, shown on Taking Action (the end of the workbook)
rep('''#gsm .copy a{color:#555}''', '''#gsm .copy a{color:#555}#gsm .copy{line-height:1.5}#gsm .ipd{margin:6px auto 0;max-width:560px}#gsm .ipd summary{cursor:pointer;text-decoration:underline;color:#555;list-style:none}#gsm .ipd summary::-webkit-details-marker{display:none}#gsm .ipt{text-align:left;color:#555;margin-top:6px}#gsm .gsmrefs .mtext p{font-size:13.5px;padding-left:22px;text-indent:-22px}''')
EXPORT = ("This document was generated using The Bear Canyon Method, a method developed by Operational Coherence. "
          "The Bear Canyon Method is provided free of charge; however, attribution to Operational Coherence is required. "
          "The Bear Canyon Method, including its architecture, framework design, and implementation, remains the intellectual property of Operational Coherence.")
rep('''"© 2026 Operational Coherence. Copyrighted: attribution required.",
                                  E,
                                  762,''', '''"© 2026 Operational Coherence. The Bear Canyon Method: free to use; attribution required.",
                                  E,
                                  762,''')
rep('''"© 2026 Operational Coherence. Copyrighted: attribution required.",
                                  40,
                                  600,''', '''"© 2026 Operational Coherence. The Bear Canyon Method: free to use; attribution required.",
                                  40,
                                  600,''')
rep('''                                P(xt(a), 8, "normal", 4, 110)),
                              F(),
                              b.save("bear-canyon-method.pdf"),''', '''                                P(xt(a), 8, "normal", 4, 110)),
                              (x += 10),
                              P(%r, 8, "italic", 4, 110),
                              F(),
                              b.save("bear-canyon-method.pdf"),''' % EXPORT)
rep('''JSON.stringify({ app: "groundsmith", v: 1, saved: o.toISOString(), data: C }, null, 1)''',
    '''JSON.stringify({ app: "groundsmith", v: 1, saved: o.toISOString(), notice: %r, data: C }, null, 1)''' % EXPORT)

rep('((r = i), N.classList.toggle("onstart", 5 === i));', '((r = i), N.classList.toggle("onstart", 5 === i), N.classList.toggle("onta", 4 === i));')
rep("<div class=\"gsmrefwrap\"></div>", "<div class=\"gsmrefwrap\">" + REFS.replace("'", "\\'") + "</div>")
rep("#gsm .copy{line-height:1.5}", "#gsm .copy{line-height:1.5}#gsm .gsmrefwrap{display:none;margin:18px 0 0}#gsm.onta .gsmrefwrap{display:block}")
rep("""    function $(id) {
      return host.querySelector('[data-gt="' + id + '"]');
    }""", """    function $(id) {
      return (
        host.querySelector('[data-gt="' + id + '"]') ||
        (host._how ? host._how.querySelector('[data-gt="' + id + '"]') : null)
      );
    }""")
rep('a = e.querySelector(".pnet") ? "figure" :', 'a = e.querySelector(".pnet,.gterr-host") ? "figure" :')
rep('$("phhead").textContent = "PHRASES THAT RUN THROUGH (" + T.threads.length + ")";', '$("phhead").textContent = "PATTERNS THAT RUN THROUGH IT (" + T.threads.length + ")";')
rep("""      if (host._rel) {
        host._rel.hl(HL);
        if (CARDH) host._rel.setWay(ROUTESEL);
        return;
      }""", """      if (host._rel) {
        host._rel.hl(HL);
        if (CARDH) host._rel.setWay(ROUTESEL);
        if (host._rel.loops && terr && terr.threads)
          host._rel.loops(
            terr.threads
              .filter(function (th) {
                return thOn[th.w] || (SEL && SELTH === th.w) || (HL != null && READ[HL] && READ[HL].w === th.w);
              })
              .map(function (th) {
                return { w: th.w, lines: [].concat.apply([], th.rings || []) };
              }),
          );
        return;
      }""")
rep('["Defiance", "#1d3557"]', '["Defiance", "#1b2a8f"]')
rep('["Defiance", [29, 53, 87]],', '["Defiance", [27, 42, 143]],')
rep("""                          "THE TWO PICTURES TOGETHER" === r ||
                          e.querySelector(".pnet")
                        );""", """                          "THE TWO PICTURES TOGETHER" === r ||
                          e.querySelector(".pnet,.gterr-host")
                        );""")
rep("""    function resize() {
      var w = $("stage").clientWidth;""", """    function resize() {
      var sg = $("stage"),
        w = sg ? sg.clientWidth : 0;""")
open(P, "w").write(s)
print("batch1 ok")
