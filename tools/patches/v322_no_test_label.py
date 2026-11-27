"""v322: no TEST label on Lead a project (Gregory, 26 Nov 20:57: "lets remove the "test" label from "lead a project"").
The card's TEST badge and the "(TEST ONLY: use test data)" note in the lead's box are gone. Lead a project still shows only
with ?f8test=1; nothing else changes.
Run from the repository root:  python3 tools/patches/v322_no_test_label.py"""
P = 'gsm-readable.js'
s = open(P, encoding='utf-8').read()
def rep(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (c, old[:90]); s = s.replace(old, new)
rep('t && (t.textContent = "v321");', 't && (t.textContent = "v322");')
rep('bd && (bd.textContent = "TEST");', 'bd && bd.parentNode.removeChild(bd);')
rep("""'<div class="lt">LEAD A PROJECT <span style="color:#a33">(TEST ONLY: use test data)</span></div>' +""", """'<div class="lt">LEAD A PROJECT</div>' +""")
open(P, 'w', encoding='utf-8').write(s)
print('v322 patched')
