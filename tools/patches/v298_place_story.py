# v298: YOUR STORY SO FAR for place maps (his go-ahead, 25 Nov 2026 22:50). Inserts
# tools/patches/v298_place_story.js ahead of gsmDropSec and calls it when the line map holds no stories.
p = 'gsm-readable.js'
s = open(p, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, old[:90]); s = s.replace(old, new)
js = open('tools/patches/v298_place_story.js', encoding='utf-8').read()
rep('    if (!Y.several) return;\n', '    if (!Y.several) return gsmPlaceStory(mt);\n')
rep('  function gsmDropSec(box) {\n', js + '  function gsmDropSec(box) {\n')
rep('t.textContent = "v297"', 't.textContent = "v298"')
open(p, 'w', encoding='utf-8').write(s)
print('v298 applied')
