# v270: the top tab bar ran its labels together ("Mapping Context Mapping Landscape").
# Each tab gets its own padded space and a thin divider; names stay on one line on wide
# screens and stack onto two lines on narrow ones.
p = 'gsm-readable.js'
s = open(p, encoding='utf-8').read()
old = '#gsm .jump .jrow:first-child button{flex:1 1 auto;padding:8px 2px 7px;border-bottom-width:3px;color:#888;font-size:clamp(11px,3vw,15px);letter-spacing:.01em;line-height:1.2}'
new = ('#gsm .jump .jrow:first-child button{flex:1 1 auto;position:relative;padding:8px 9px 7px;border-bottom-width:3px;color:#888;font-size:clamp(11px,3vw,14px);letter-spacing:.01em;line-height:1.2;text-align:center;white-space:nowrap}'
       '@media(max-width:660px){#gsm .jump .jrow:first-child button{white-space:normal;padding:8px 4px 7px}}'
       '#gsm .jump .jrow:first-child button+button:before{content:\\"\\";position:absolute;left:0;top:22%;bottom:22%;border-left:1px solid #d4d4d4}')
assert s.count(old) == 1
s = s.replace(old, new).replace('t.textContent = "v269"', 't.textContent = "v270"')
open(p, 'w', encoding='utf-8').write(s)
