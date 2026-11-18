"""v204: ground cards read his 11-18 workbook rightly.
1. The card no longer says the emotion "stands in the goal's way". He places aggression on the help side on purpose
   (N32: aggression toward full suppression where it isn't warranted; N34: the push for good fire). The card now says
   where he placed it and what the risk is, without deciding what the emotion is aimed at.
2. The line under FIRST MOVES for a way names the emotions it meets instead of calling them resistance.
3. Up to three ground cards (was two), so a third patch (N35 on his 11-18 workbook) gets its card.
Usage: python3 v204_ground_wording.py gsm-readable.js"""
import sys

P = sys.argv[1]
s = open(P).read()


def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, (c, a[:90])
    s = s.replace(a, b)


rep(
    """". It stands in the goal’s way inside ground that otherwise helps it. Turning it keeps the acceptance around it (" +
                      phList(nbi) +
                      ") working for the goal.</div><div class=\\"why\\">Why: " +""",
    """". You placed " +
                      (ids.length > 1 ? "them" : "it") +
                      " where things help the goal. Keep " +
                      (ids.length > 1 ? "them" : "it") +
                      " working for the goal without letting the " +
                      em +
                      " spread into the acceptance around it (" +
                      phList(nbi) +
                      ").</div><div class=\\"why\\">Why: " +""",
)
rep(
    """                        "Find out what the " + em + " in " + phList(ids) + " answers before you act on it.",""",
    """                        "Find out what the " + em + " in " + phList(ids) + " is aimed at, and whom it reaches, before you act on it.",""",
)
rep(
    """                        : "going from acceptance into " + em + " is a high-risk move: " + WHY[e0] + " (Vigneaux, 2026).") +""",
    """                        : "acceptance and " + em + " side by side is a high-risk mix, whatever the " + em + " is aimed at: " + WHY[e0] + " (Vigneaux, 2026).") +""",
)
rep("                return G.slice(0, 2)\n", "                return G.slice(0, 3)\n")
# FIRST MOVES per way: name the emotions, not what they are aimed at
rep(
    '        ? t.push("and meets what resists the goal at " + N(st.hard) + " (bring something to do, not an argument)")\n        : t.push("and goes around what resists the goal, which stays as it is");',
    '        ? t.push("and meets aggression, distrust, or defiance at " + N(st.hard) + " (bring something to do, not an argument)")\n        : t.push("and goes around the aggression, distrust, and defiance, which stay as they are");',
)

s = s.replace('t.textContent = "v203"', 't.textContent = "v204"')
assert 't.textContent = "v204"' in s
open(P, "w").write(s)
