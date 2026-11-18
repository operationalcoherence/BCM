"""The program/strategy switch on Taking Action cards (v202). Clicks "Make it a strategy" on the first program card,
checks it turns into a strategy and stays on the page with the choice saved in the workbook, then clicks
"Let the engine decide" and checks it goes back.
Usage: python3 -I switch.py WORKBOOK.json"""
import json, sys
from playwright.sync_api import sync_playwright
SRC = open('../gsm-preview.js', 'rb').read()
HTML = b'<!doctype html><html><head><meta charset="utf-8"></head><body><div id="gsm-mount">L</div><script>window.GSM_ESRI_KEY="";var t=document.createElement("script");t.src="http://t.local/gsm-preview.js";document.body.appendChild(t);</script></body></html>'
CARDS = "()=>[...document.querySelectorAll('#gsm .coa')].map(c=>[c.querySelector('.hd b').textContent,c.querySelector('.mode').textContent])"
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome', args=['--no-sandbox'])
    wb = json.load(open(sys.argv[1]))['data']; pg = b.new_page(); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
    def route(r):
        u = r.request.url
        if u == 'http://t.local/': r.fulfill(status=200, content_type='text/html', body=HTML)
        elif u.startswith('http://t.local/gsm-preview.js'): r.fulfill(status=200, content_type='application/javascript', body=SRC)
        else: r.abort()
    pg.route('**/*', route)
    pg.add_init_script("localStorage.setItem('groundsmith-web-v1',%s);localStorage.setItem('groundsmith-web-welcomed','1');" % json.dumps(json.dumps(wb)))
    pg.goto('http://t.local/'); pg.wait_for_selector('#gsm'); pg.wait_for_timeout(1500)
    pg.evaluate("window.gsmTab(4)"); pg.wait_for_timeout(500)
    before = pg.evaluate(CARDS)
    i = [k for k, c in enumerate(before) if c[1] == 'PROGRAM'][0]
    name = before[i][0]
    print('switching:', name)
    pg.evaluate("i=>document.querySelectorAll('#gsm .coa')[i].querySelector('.gsmmode').click()", i)
    pg.wait_for_timeout(1200)
    after = dict(pg.evaluate(CARDS))
    print('after:', after.get(name), '| saved:', pg.evaluate("()=>Object.keys(JSON.parse(localStorage.getItem('groundsmith-web-v1')).asks||{}).filter(k=>/^mode\\|/.test(k))"))
    j = [k for k, c in enumerate(pg.evaluate(CARDS)) if c[0] == name][0]
    pg.evaluate("j=>[...document.querySelectorAll('#gsm .coa')[j].querySelectorAll('.gsmmode')].filter(b=>!b.dataset.mv)[0].click()", j)
    pg.wait_for_timeout(1200)
    print('undone:', dict(pg.evaluate(CARDS)).get(name), '| cards same as before:', pg.evaluate(CARDS) == before)
    for e in errs: print('  !!', e[:160])
    b.close()
