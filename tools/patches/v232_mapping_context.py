"""v232: Phase 2 step 9, part 1 (Mapping Context and Mapping Landscape).
- Start here keeps the method (old 01-03, 06-08, renumbered 01-06); the workbook instructions move to their pages.
- Mapping Landscape, step 1 (mark the map): old 04, 05, and 10 open the existing INSTRUCTION drop-down, under HOW TO MAP.
- Mapping Landscape, step 2 (describe your notes): one line on what the step is for, then a closed
  DESCRIBE YOUR NOTES: INSTRUCTION drop-down with old 09, 11, and 12.
- Pattern Analysis gets old 13, and Pattern Synthesis old 14 and 15, each in a closed drop-down under the opening note.
- Every note shows the paper's definition of the emotion it is marked with, in small gray text under the buttons
  (approved quotes, Vigneaux 2026). Tooltips stay; the meaning no longer depends on hover.
- Mapping Context: one line saying combining fills WHO DID WHAT with who added what, and when.
His text is moved word for word; nothing of his is reworded here (the redlines come after).
Usage: python3 v232_mapping_context.py gsm-readable.js"""
import sys, re
P = sys.argv[1]
s = open(P).read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:90]); s = s.replace(a, b)

# --- the numbered items on Start here, taken from the file itself so they move word for word
i0 = s.index('<div id="gsm-start">'); i1 = s.index('<div class="sh">THE FIVE PAGES</div>', i0)
block = s[i0:i1]
items = dict(re.findall(r'<li><span>(\d\d)</span>(.*?)</li>', block))
assert sorted(items) == ['%02d' % k for k in range(1, 16)], sorted(items)
def ol(keys):
    return '<ol class="steps">' + ''.join(
        '<li><span>%d</span><div>%s</div></li>' % (n + 1, items[k]) for n, k in enumerate(keys)) + '</ol>'
start_new = block[:block.index('<ol class="steps">')] + '<ol class="steps">' + ''.join(
    '<li><span>%02d</span>%s</li>' % (n + 1, items[k]) for n, k in enumerate(['01', '02', '03', '06', '07', '08'])) + \
    '</ol><div class="sh">IN THIS WORKBOOK</div><p class="mhelp">Each page has its own instructions, in a drop-down at its top.</p>'
s = s[:i0] + start_new + s[i1:]

# --- Mapping Landscape, step 1: the existing drop-down opens with HOW TO MAP
rep('<details class="fold"><summary>MAPPING LANDSCAPE: INSTRUCTION</summary><div class="mtext">\\n',
    '<details class="fold"><summary>MAPPING LANDSCAPE: INSTRUCTION</summary><div class="mtext">\\n<div class="ml">HOW TO MAP</div>' +
    ol(['04', '05', '10']) + '\\n')

# --- Mapping Landscape, step 2: what the step is for, and its own drop-down
rep('<div class="emokey mc2" id="gsm-pek"></div>',
    '<div class="mc2 dnhead"><div class="whohelp">Every note you placed is here, in one place, to describe and edit.</div>'
    '<details class="fold" style="margin:10px 0 14px"><summary>DESCRIBE YOUR NOTES: INSTRUCTION</summary><div class="mtext">' +
    ol(['09', '11', '12']) + '</div></details></div><div class="emokey mc2" id="gsm-pek"></div>')

# --- Pattern Analysis and Pattern Synthesis: one drop-down each, under the opening note
rep('Patterns suggests; you decide.</div>\\n  <div id="gsm-pat"></div>',
    'Patterns suggests; you decide.</div>\\n'
    '  <details class="fold pinst pian"><summary>PATTERN ANALYSIS: INSTRUCTION</summary><div class="mtext"><p>' + items['13'] + '</p></div></details>'
    '<details class="fold pinst pisy"><summary>PATTERN SYNTHESIS: INSTRUCTION</summary><div class="mtext"><p>' + items['14'] + '</p><p>' + items['15'] + '</p></div></details>\\n'
    '  <div id="gsm-pat"></div>')
rep('N.classList.toggle("onta", 4 === i), gsmSince());',
    'N.classList.toggle("onta", 4 === i), N.classList.toggle("onan", 2 === i), N.classList.toggle("onsy", 3 === i), gsmSince());')

# --- Mapping Context: what combining puts in WHO DID WHAT
rep("Then combine the workbooks to see everyone\\'s answers side by side.</div>",
    "Then combine the workbooks to see everyone\\'s answers side by side. Combining fills WHO DID WHAT, below, with who added what, and when.</div>")

# --- the emotion's meaning, visible on every note
rep("""      '<button type="button" class="ech none' +
      (null == t ? " on" : "") +
      '" data-e="">Not marked</button></div>'
    );""",
"""      '<button type="button" class="ech none' +
      (null == t ? " on" : "") +
      '" data-e="">Not marked</button></div><div class="emodef">' +
      (null != t && EDQ[t] ? EDQ[t] : "") +
      "</div>"
    );""")
rep("""          t.querySelectorAll(".emo .ech").forEach(function (t) {
            t.classList.toggle("on", t === o);
          }),
          P(),""",
"""          t.querySelectorAll(".emo .ech").forEach(function (t) {
            t.classList.toggle("on", t === o);
          }),
          t.querySelectorAll(".emodef").forEach(function (d) {
            d.textContent = null != r && EDQ[r] ? EDQ[r] : "";
          }),
          P(),""")

# --- styles
rep('''"#gsm{font-family:'Questrial',sans-serif;''',
    '''"#gsm .emodef{font-size:12.5px;line-height:1.45;color:#777;margin:5px 0 0;max-width:560px}#gsm .emodef:empty{display:none}#gsm .dnhead{margin:4px 0 0}#gsm:not(.onan) .pian,#gsm:not(.onsy) .pisy{display:none}#gsm .pinst{margin:0 0 14px}#gsm{font-family:'Questrial',sans-serif;''')

rep('t && (t.textContent = "v231");', 't && (t.textContent = "v232");')
open(P, "w").write(s)
print("ok")
