"""v315: READING THEM TOGETHER says when nobody has written a note yet: Pattern Analysis then has no ground to
build and shows the answers only (the old figure). Same rule as the solo workbook.
Run from the repository root:  python3 tools/patches/v315_no_ground_yet.py"""
P = 'gsm-readable.js'
s = open(P, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, old[:80]); s = s.replace(old, new)
rep('t && (t.textContent = "v314");', 't && (t.textContent = "v315");')
rep('''      (nq < 7 ? " Pattern Analysis opens once each of the seven questions has an answer from someone; so far " + nq + " of 7 do." : "") + "</div>";''',
'''      (nq < 7 ? " Pattern Analysis opens once each of the seven questions has an answer from someone; so far " + nq + " of 7 do." : "") +
      (rows.some(function (r) { return r.notes; })
        ? ""
        : " <b>There is no ground yet:</b> nobody has written a note. Symbols placed without words don’t count. Until someone writes one, Pattern Analysis shows the answers only.") +
      "</div>";''')
open(P, 'w', encoding='utf-8').write(s)
print('ok')
