"""v198: the first pass on Gregory's 11-18 review of v196 (claude/v196_review_plan.md, Phase 1, decided items).
1. What each emotion means: direct quotes from Vigneaux (2026), approved by him 11-18. A tooltip on every emotion
   button in a note, and a fold under the emotion key on the map.
2. Mapping Context: the page title sits at the top; the goal carries his instruction; WORKING WITH A FRIEND sits
   under the goal.
3. Instruction 10 rewritten: the emotional landscape switch only exists on a place map.
4. Pattern Synthesis, the ground's one-tap question: "Supports" / "Does Not Support" (was "Stands for it" /
   "Turns away"), and the question asks the same thing in the same words.
5. "See the two pictures together" leaves Pattern Analysis; it closes Pattern Synthesis, where it is the next step.
6. Taking Action: the Sources list leaves the page (its works are in REFERENCES, Axelrod & Cohen added), and the
   program and strategy explanation ends with (Morin & Kern, 1999; Morin, 2008). NO RESPONSE YET is renamed.
Usage: python3 v198_review_first_pass.py gsm-readable.js"""
import sys

P = sys.argv[1]
s = open(P).read()


def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, (c, a[:90])
    s = s.replace(a, b)


# 1. what each emotion means (index order of the engine's emotion list: aggression, acceptance, distrust,
#    indifference, defiance); quotes are Vigneaux (2026), pages as printed in the journal
EDQ = [
    "“Red denotes the critical emotion of aggression toward the initiative.” “Spatially, aggression is arranged in a manner conducive to transitioning to the most severe emotion, defiance, while the opposite is also true.” (Vigneaux, 2026, p. 27)",
    "“Acceptance is the ideal emotional reaction that provides outreach practitioners with fertile ground to plant an idea of resilience that blooms into the use and propagation of social networks.” (Vigneaux, 2026, p. 27) “Care and concern should continuously be exercised to maintain and grow the emotion of acceptance in the town.” (p. 28)",
    "“It may be possible to gain the trust of those who are distrusting and inspire them to transition to indifference and perhaps partially engage with social networks. It is predicted that, like with any other emotion, distrust can transition to a more severe emotion instead of a more benevolent one.” (Vigneaux, 2026, p. 27)",
    "“Indifference is the emotion of transition, but it is also one that individuals can reside in who are unconcerned about the idea and what it calls for, as minimal as it may be. Being indifferent to an idea is precarious, as there is no engagement with an idea either for or against.” (Vigneaux, 2026, p. 27)",
    "“Defiance is more than aggressive or distrusting of the outreach practitioner and their communication, as those who are in this emotion actively rebel against their presence and message.” (Vigneaux, 2026, p. 27) “Defiance will be the most resistant emotion to this or any strategy.” (p. 29)",
]
ENERGY = "“Some transitions, such as distrust to acceptance or vice versa, require more energy than indifference to acceptance, even with external help.” (Vigneaux, 2026, p. 27)"
js = lambda t: t.replace("\\", "\\\\").replace('"', '\\"')
rep(
    "  function r(t) {\n    return (\n      '<div class=\"emo\"><span class=\"eml\">EMOTION</span>' +",
    "  var EDQ = [" + ", ".join('"' + js(q) + '"' for q in EDQ) + "];\n"
    "  function r(t) {\n    return (\n      '<div class=\"emo\"><span class=\"eml\">EMOTION</span>' +",
)
rep(
    "            '\" data-e=\"' +\n            n +\n            '\"><span class=\"sw\" style=\"background:' +",
    "            '\" data-e=\"' +\n            n +\n            '\" title=\"' +\n            EDQ[n] +\n            '\"><span class=\"sw\" style=\"background:' +",
)
ORDER = [1, 3, 2, 0, 4]  # the paper's order, from most to least open to a new idea
NAMES = ["Aggression", "Acceptance", "Distrust", "Indifference", "Defiance"]
fold = (
    '<details class="fold" style="margin:6px 0 0"><summary>WHAT EACH EMOTION MEANS</summary><div class="mtext">'
    + "".join("<p><b>" + NAMES[k] + ".</b> " + EDQ[k] + "</p>" for k in ORDER)
    + "<p>" + ENERGY + "</p></div></details>"
)
rep(
    "        '</div><div class=\"ekh\">Pick an emotion on any note to color the map.</div><div class=\"ekc\">' +\n        a +\n        \"</div>\"",
    "        '</div><div class=\"ekh\">Pick an emotion on any note to color the map.</div>" + js(fold).replace("'", "\\'") + "<div class=\"ekc\">' +\n        a +\n        \"</div>\"",
)

# 2. Mapping Context: title at the top, the goal's instruction, WORKING WITH A FRIEND under the goal
H1 = '<h1 id="gsm-a-ctx">Mapping Context</h1>\\n  '
rep(H1, "")
rep('  <div class="chain cxq" id="gsm-chain">', "  " + H1 + '<div class="chain cxq" id="gsm-chain">')
i = s.index('  <details class="fold" id="gsm-friend"')
j = s.index("</details>\\n", i) + len("</details>\\n")
FRIEND = s[i:j]
s = s[:i] + s[j:]
rep(
    '<div class="lab">GOAL</div>\\n  <textarea class="goal" data-k="goal" placeholder="Write the goal\\u2026" rows="2"></textarea>\\n',
    '<div class="lab">START HERE \\u00b7 THE GOAL</div>\\n  <div class="whohelp" style="margin:0 0 6px">Provide the goal in as much detail as possible that you are working to accomplish.</div>\\n  <textarea class="goal" data-k="goal" placeholder="Write the goal\\u2026" rows="2"></textarea>\\n' + FRIEND,
)

# 3. instruction 10: the switch exists only on a place map
rep(
    "<li><span>10</span>In Mapping Landscape, turn on the emotional landscape to see how far each emotion toward the change reaches.</li>",
    "<li><span>10</span>On a place map, Show emotional landscape paints how far each emotion reaches toward the change. On the line map, Pattern Synthesis shows it as ground.</li>",
)

# 4. the ground's one-tap question
rep(
    'a.id + " says “" + a.q + "”. Does " + a.id + " stand for “" + th.w + "” or turn away from it? ",',
    'a.id + " says “" + a.q + "”. Does " + a.id + " support “" + th.w + "”? ",',
)
rep('        ["Stands for it", "for"],\n        ["Turns away", "away"],', '        ["Supports", "for"],\n        ["Does Not Support", "away"],')

# 5. the two pictures: from the end of Pattern Analysis to the end of Pattern Synthesis
rep("                      Rt.insertBefore(ht, s));", "                      Rt.insertBefore(ht, ct));")
rep("t && (t.style.display = (2 !== r && 3 !== r) || !window.gsmHasInt ? \"none\" : \"\");",
    "t && (t.style.display = 3 !== r || !window.gsmHasInt ? \"none\" : \"\");")

# 6. Taking Action: sources into REFERENCES, the citation, NO RESPONSE YET
i = s.index('<div class="msub">Sources:</div>')
j = s.index("</div>' +", s.index("Waldrop, M. M. (1992)", i))
s = s[:i] + s[j + len("</div>"):]
rep(
    "start small, and change course as people respond.</div>' +",
    "start small, and change course as people respond (Morin &amp; Kern, 1999; Morin, 2008).</div>' +",
)
rep(
    "<p>Ackoff, R. L. (1999). <i>Ackoff&#39;s best: His classic writings on management.</i> New York, NY: Wiley.</p>",
    "<p>Ackoff, R. L. (1999). <i>Ackoff&#39;s best: His classic writings on management.</i> New York, NY: Wiley.</p><p>Axelrod, R., &amp; Cohen, M. D. (2000). <i>Harnessing complexity: Organizational implications of a scientific frontier.</i> New York, NY: Basic Books.</p>",
)
rep('<div class="rule"><div class="rl">NO RESPONSE YET</div>', '<div class="rule"><div class="rl">NOTHING YOU WOULD DO ANSWERS THESE YET</div>')

s = s.replace('t.textContent = "v197"', 't.textContent = "v198"')
assert 't.textContent = "v198"' in s
open(P, "w").write(s)
