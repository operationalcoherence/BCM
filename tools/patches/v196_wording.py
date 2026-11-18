"""v196: Gregory's wording review of v171-v195 (review sheet, 2026-11-17), plus the serial comma everywhere.
Rows changed: 5 (an emotions-first method), 15 (Winograd & Flores page), 26 (behaviors first), 27 (program),
39 (Morin quote in full), 40 and 47 (commas). Serial comma (his call, 11-17): every list of three or more the engine
writes, and the fixed lists in its own sentences. Two-item lists ("A and B") are unchanged. His instruction text in
the page template (line 7) is not touched.
Usage: python3 v196_wording.py gsm-readable.js  (and: python3 v196_wording.py tools/relief/relief.js --relief)"""
import re
import sys

P = sys.argv[1]
RELIEF = "--relief" in sys.argv
s = open(P).read()


def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, (c, a[:80])
    s = s.replace(a, b)


def sub(pat, b, n, flags=0):
    global s
    s, c = re.subn(pat, b, s, flags=flags)
    assert c == n, (c, pat[:80])


if RELIEF:
    rep("a note, question, the goal, a number or a way", "a note, question, the goal, a number, or a way")
    open(P, "w").write(s)
    sys.exit(0)

head, body = s.split("\n", 7)[:7], s.split("\n", 7)[7]
s = body  # everything after the page template (line 7 holds his instruction text)

# --- his wording ---
rep(
    "calls this ground ready for <b>emotions first</b>:",
    "calls this ground ready for an <b>emotions-first</b> method:",
)
rep("/\\bemotions first\\b/i", "/\\bemotions[- ]first\\b/i")
rep("(Winograd &amp; Flores, 1986)", "(Winograd &amp; Flores, 1986, p. 174)")
rep(
    "let a small shift in emotion follow over time (Vigneaux, 2026).",
    "let a small shift in emotion follow over time. The result is more important than the dominant emotion that produces it (Vigneaux, 2026).",
)
rep('"A program runs to completion."', '"A program runs linearly and possibly repetitively to completion."')
rep("A program runs to completion. Decide now", "A program runs linearly and possibly repetitively to completion. Decide now")
rep(
    "As soon as an action is taken it begins to escape your intentions, and the setting can turn it into its opposite (Morin, 2008, p. 55).",
    "“This is where the notion of the ecology of action intervenes. As soon as an individual takes an action, whatever that action may be, it begins to escape from his intentions. The action enters into the universe of interactions and, in the end, it is the environment that seizes it in the sense that it can become the opposite of the initial intention. Often the action will fly back at our heads like a boomerang. This obliges us to follow the action, to attempt to correct it – if there is still time – and sometimes to torpedo it like NASA engineers who, if a missile leaves its trajectory, send another missile to blow it up.” (Morin, 2008, p. 55).",
)
rep("Edit a note and it leaves this list.", "Edit a note, and it leaves this list.")

# --- serial comma: fixed lists in the engine's own sentences ---
for a, b in [
    ("design, redesign or reinforce", "design, redesign, or reinforce"),
    ("designed, redesigned or reinforced", "designed, redesigned, or reinforced"),
    ("design, redesign and reinforce", "design, redesign, and reinforce"),
    ("aggression, distrust and defiance", "aggression, distrust, and defiance"),
    ("aggression, distrust or defiance", "aggression, distrust, or defiance"),
    ("distrust, aggression or defiance", "distrust, aggression, or defiance"),
    ("town, county, state or province", "town, county, state, or province"),
    ("N1, N2 and so on", "N1, N2, and so on"),
    ("answer, note or the goal", "answer, note, or the goal"),
    ("goal, answers and notes", "goal, answers, and notes"),
    ("as opposition (Q.2) or as", "as opposition (Q.2), or as"),
    ("cause, opposition or condition", "cause, opposition, or condition"),
    ("notes, answers and the goal", "notes, answers, and the goal"),
    ("an answer, another note or the goal", "an answer, another note, or the goal"),
    ("support, contradict or reinforce", "support, contradict, or reinforce"),
    ("causes, opposition and conditions", "causes, opposition, and conditions"),
    ("climbing, friction and rock faces", "climbing, friction, and rock faces"),
    ("grass, soil or rock", "grass, soil, or rock"),
]:
    c = s.count(a)
    assert c >= 1, a
    s = s.replace(a, b)

# --- serial comma: lists the engine builds ---
# a.slice(0, -1).join(", ") + " and " + a[a.length - 1]   (one line or across lines)
sub(
    r'(\w+)\.slice\(0, -1\)\.join\(", "\) \+(\s+)" and " \+(\s+)\1\[\1\.length - 1\]',
    r'\1.slice(0, -1).join(", ") +\2(\1.length > 2 ? ", and " : " and ") +\3\1[\1.length - 1]',
    15,
)
# "A, B, C and 4 more": the shown part is always 3 or more items here
sub(r'\.join\(", "\) \+ " and " \+ \((\w+)\.length - (\w+)\) \+ " more"', r'.join(", ") + ", and " + (\1.length - \2) + " more"', 4)
skip = {"U.length > 4 ? \" and \" + (U.length - 4)": 0}
lines = s.split("\n")
n = 0
for i, l in enumerate(lines):
    m = re.search(r'\? " and " \+ \((\w+(?:\.\w+)?)\.length - (\d+)\) \+ " more"', l)
    if not m:
        continue
    prev = " ".join(lines[max(0, i - 3) : i])
    if "L5.length" in prev or "lst(bare" in prev or '.join("; ")' in prev:
        continue  # already ends in a joined list, or a "; " list
    lines[i] = l.replace('? " and " + (', '? ", and " + (', 1)
    n += 1
assert n == 16, n
s = "\n".join(lines)
rep(
    '.replace(/, ([^,]*)$/, " and $1")',
    '.replace(/, ([^,]*)$/, function (m, p, o, w) { return (w.split(", ").length > 2 ? ", and " : " and ") + p; })',
)

s = "\n".join(head) + "\n" + s
s = s.replace('t.textContent = "v195"', 't.textContent = "v196"')
assert 't.textContent = "v196"' in s
open(P, "w").write(s)
