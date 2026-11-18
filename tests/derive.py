"""Derived state without In Parallel (v199). Boots a workbook, never opens In Parallel, and reports:
the action points (window.gsmGridPts) at boot; the same after an edit (one note's emotion changed, saved
through the page's own save); and whether Taking Action's MOVES, IN ORDER follows the edit.
Usage: python3 -I derive.py WORKBOOK.json [NOTE_INDEX NEW_EMOTION]"""
import json, sys
from playwright.sync_api import sync_playwright

SRC = open('../gsm-preview.js', 'rb').read()
REL = open('../gsm-relief.js', 'rb').read()
HTML = b'<!doctype html><html><head><meta charset="utf-8"></head><body><div id="gsm-mount">L</div><script>window.GSM_ESRI_KEY="";var t=document.createElement("script");t.src="http://t.local/gsm-preview.js";document.body.appendChild(t);</script></body></html>'
f = sys.argv[1]
ni = int(sys.argv[2]) if len(sys.argv) > 2 else 3
ne = int(sys.argv[3]) if len(sys.argv) > 3 else 0
PTS = "()=>(window.gsmGridPts||null)&&window.gsmGridPts.map(p=>p.id+':'+p.d.toFixed(1)+'/'+p.any.toFixed(2)).join(' ')"
MOVES = "()=>(document.body.textContent.match(/1\\. Start with.{0,150}/g)||[])"
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome',
                          args=['--no-sandbox', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'])
    wb = json.load(open(f))['data']
    pg = b.new_page(viewport={'width': 1400, 'height': 900}); errs = []
    pg.on('pageerror', lambda e: errs.append('PAGEERROR: ' + str(e).split('\n')[0]))
    def route(r):
        u = r.request.url
        if u == 'http://t.local/': r.fulfill(status=200, content_type='text/html', body=HTML)
        elif u.startswith('http://t.local/gsm-preview.js'): r.fulfill(status=200, content_type='application/javascript', body=SRC)
        elif u.startswith('http://t.local/gsm-relief.js'): r.fulfill(status=200, content_type='application/javascript', body=REL)
        else: r.abort()
    pg.route('**/*', route)
    pg.add_init_script("localStorage.setItem('groundsmith-web-v1',%s);localStorage.setItem('groundsmith-web-welcomed','1');" % json.dumps(json.dumps(wb)))
    pg.goto('http://t.local/'); pg.wait_for_selector('#gsm', timeout=25000); pg.wait_for_timeout(1500)
    print('derived version at boot:', pg.evaluate("()=>window.gsmDV||null"))
    print('points at boot (no In Parallel):', pg.evaluate(PTS))
    print('nothing-answers list at boot:', pg.evaluate("()=>window.gsmNR?window.gsmNR.u.map(u=>u.lab).join(' '):null"))

    def moves():
        pg.evaluate("window.gsmTab&&window.gsmTab(4)"); pg.wait_for_timeout(1200)
        h = pg.evaluate("()=>document.body.scrollHeight")
        for y in range(0, h + 900, 600):
            pg.evaluate("y=>window.scrollTo(0,y)", y); pg.wait_for_timeout(200)
        pg.wait_for_timeout(1200)
        for y in range(0, h + 900, 600):
            pg.evaluate("y=>window.scrollTo(0,y)", y); pg.wait_for_timeout(200)
        pg.wait_for_timeout(800)
        return pg.evaluate(MOVES)
    m0 = moves()
    print('moves before:'); [print('   ', x) for x in m0]
    pg.evaluate("([i,e])=>{var m=window.gsmData().m;m[i][5]=e;window.gsmAskG('__probe','y');}", [ni, ne])
    pg.wait_for_timeout(1500)
    print('derived version after edit:', pg.evaluate("()=>window.gsmDV||null"))
    print('points after edit (N%d emotion -> %d):' % (ni + 1, ne), pg.evaluate(PTS))
    m1 = moves()
    print('moves after:'); [print('   ', x) for x in m1]
    print('moves changed:', m0 != m1)
    for e in dict.fromkeys(errs): print('   !!', e[:170])
    b.close()
