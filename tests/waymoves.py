"""FIRST MOVES follows the selected way (v203). Loads the 3D, mounts every Taking Action card, then on each card
that has a way bar clicks each way and "All ways", and prints the line under FIRST MOVES.
Usage: python3 -I waymoves.py WORKBOOK.json"""
import json, sys
from playwright.sync_api import sync_playwright
SRC = open('../gsm-preview.js', 'rb').read(); REL = open('../gsm-relief.js', 'rb').read()
HTML = b'<!doctype html><html><head><meta charset="utf-8"></head><body><div id="gsm-mount">L</div><script>window.GSM_ESRI_KEY="";var t=document.createElement("script");t.src="http://t.local/gsm-preview.js";document.body.appendChild(t);</script></body></html>'
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome', args=['--no-sandbox', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'])
    wb = json.load(open(sys.argv[1]))['data']; pg = b.new_page(viewport={'width': 1400, 'height': 900}); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
    def route(r):
        u = r.request.url
        if u == 'http://t.local/': r.fulfill(status=200, content_type='text/html', body=HTML)
        elif u.startswith('http://t.local/gsm-preview.js'): r.fulfill(status=200, content_type='application/javascript', body=SRC)
        elif u.startswith('http://t.local/gsm-relief.js'): r.fulfill(status=200, content_type='application/javascript', body=REL)
        else: r.abort()
    pg.route('**/*', route)
    pg.add_init_script("localStorage.setItem('groundsmith-web-v1',%s);localStorage.setItem('groundsmith-web-welcomed','1');localStorage.setItem('groundsmith-web-privacy',JSON.stringify({solo:{v:'9999'},join:{v:'9999'},lead:{v:'9999'}}));" % json.dumps(json.dumps(wb)))
    pg.goto('http://t.local/'); pg.wait_for_selector('#gsm'); pg.wait_for_timeout(1500)
    pg.evaluate("window.gsmTab(4)"); pg.wait_for_timeout(800)
    n = pg.evaluate("()=>document.querySelectorAll('#gsm .coa').length")
    for i in range(n):
        pg.evaluate("i=>document.querySelectorAll('#gsm .coa')[i].scrollIntoView()", i); pg.wait_for_timeout(1500)
        title = pg.evaluate("i=>document.querySelectorAll('#gsm .coa')[i].querySelector('.hd b').textContent", i)
        btns = pg.evaluate("i=>[...document.querySelectorAll('#gsm .coa')[i].querySelectorAll('.gtrb button')].map(b=>b.textContent)", i)
        if not btns: continue
        print('==', title[:60])
        for j, lab in list(enumerate(btns))[1:] + [(0, btns[0])]:
            pg.evaluate("([i,j])=>document.querySelectorAll('#gsm .coa')[i].querySelectorAll('.gtrb button')[j].click()", [i, j]); pg.wait_for_timeout(300)
            print('  ', lab, '->', pg.evaluate("i=>{var f=document.querySelectorAll('#gsm .coa')[i].querySelector('.fmway');return f?f.textContent:'(none)'}", i))
    for e in dict.fromkeys(errs): print('  !!', e[:160])
    b.close()
