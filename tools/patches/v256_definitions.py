# v256: the approved emotion definitions (his calls 11-24 11:52-12:00).
# Replaces EDQ (per-note definition) and the WHAT EACH EMOTION MEANS fold; label bump.
import re, sys
p = "gsm-readable.js"
s = open(p, encoding="utf-8").read()

C = "(Vigneaux, 2026, p. %s)"
AGG = "“Red denotes the critical emotion of aggression toward [the idea].” “Spatially, aggression is arranged in a manner conducive to transitioning to the most severe emotion, defiance, while the opposite is also true.” " + C % "28"
ACC = ("“Acceptance is rooted in … seeing those who live alongside them, their existence, their property, their livelihoods, and their safety as legitimately as they see their own.” " + C % "29" +
       " “Acceptance is the ideal emotional reaction that provides … fertile ground to plant an idea … that blooms into … use and propagation.” (p. 28)"
       " “Care and concern should continuously be exercised to maintain and grow the emotion of acceptance[.]” (p. 29)")
DIS = "“Lavender is the emotion of distrust.” “The emotion of distrust is third behind indifference and acceptance in that order of emotions that have the potential for adopting a new idea and practice.” “…distrust can transition to a more severe emotion instead of a more benevolent one.” " + C % "28"
IND = "“Indifference is the emotion of transition, but it is also one that individuals can reside in who are unconcerned about the idea and what it calls for, as minimal as it may be. Being indifferent to an idea is precarious, as there is no engagement with an idea either for or against.” " + C % "28"
DEF = "“Defiance is more than aggressive or distrusting … those who are in this emotion actively rebel against [the idea].” " + C % "28" + " “Defiance will be the most resistant emotion to this or any strategy.” (p. 30)"
ALL = "“Some transitions, such as distrust to acceptance or vice versa, require more energy than indifference to acceptance, even with external help.” " + C % "28"
LEAD = "Each emotion is read toward whatever the note is about: the idea, a person, a practice, or an event, on either side of the line."

def js(x): return '"' + x.replace("\\", "\\\\").replace('"', '\\"') + '"'

# 1. EDQ, order 0 aggression, 1 acceptance, 2 distrust, 3 indifference, 4 defiance
s, n = re.subn(r'  var EDQ = \[.*?\];\n', lambda m: "  var EDQ = [" + ", ".join(js(x) for x in [AGG, ACC, DIS, IND, DEF]) + "];\n", s, count=1, flags=re.S)
assert n == 1, "EDQ"

# 2. the fold
fold = ('<div class=\\"mtext\\"><p>' + LEAD + '</p>' +
        "".join("<p><b>%s.</b> %s</p>" % (k, v) for k, v in [("Acceptance", ACC), ("Indifference", IND), ("Distrust", DIS), ("Aggression", AGG), ("Defiance", DEF)]) +
        "<p>" + ALL + "</p></div>")
fold = fold.replace("'", "\\'")
s, n = re.subn(r'<div class=\\"mtext\\"><p><b>Acceptance\.</b>.*?</p></div>', lambda m: fold, s, count=1, flags=re.S)
assert n == 1, "fold"

# 3. label
s, n = re.subn(r't\.textContent = "v255"', 't.textContent = "v256"', s)
assert n == 1, "label"
open(p, "w", encoding="utf-8").write(s)
print("ok")
