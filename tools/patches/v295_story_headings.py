# v295: headings on YOUR STORY SO FAR (his ask, 25 Nov 2026 22:26): "Your story, summarized" over the
# four paragraphs; the chapters fold is "Your story in greater detail"
p = 'gsm-readable.js'
s = open(p, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, old[:90]); s = s.replace(old, new)
rep('''      "</p>" +
      '<div class="evo">' +''', '''      "</p>" +
      '<div class="csl" style="margin-top:10px">YOUR STORY, SUMMARIZED</div>' +
      '<div class="evo">' +''')
rep('''<details class="more evst"><summary>Each chapter read on its own</summary>''', '''<details class="more evst"><summary>Your story in greater detail</summary>''')
rep('t.textContent = "v294"', 't.textContent = "v295"')
open(p, 'w', encoding='utf-8').write(s)
print('v295 applied')
