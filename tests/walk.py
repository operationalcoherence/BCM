"""v259: walk a way on a Taking Action card. Opens the card with the most stops, goes full screen, presses
"Walk way A, step by step", screenshots steps 1, 3 and the last, checks Next/Back/strip taps/Escape.
Usage: python3 -I walk.py WORKBOOK.json [OUTPREFIX] [GSMJS]"""
import json, sys, os
from playwright.sync_api import sync_playwright
WB = sys.argv[1]; OUT = sys.argv[2] if len(sys.argv) > 2 else '/tmp/walk'
SRC = open(sys.argv[3] if len(sys.argv) > 3 else '../gsm-preview.js', 'rb').read(); REL = open('../gsm-relief.js', 'rb').read()
HTML = b'<!doctype html><html><head><meta charset="utf-8"></head><body><div id="gsm-mount">L</div><script>window.GSM_ESRI_KEY="";var t=document.createElement("script");t.src="http://t.local/gsm-preview.js";document.body.appendChild(t);</script></body></html>'
wb = json.load(open(WB))['data']
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome', args=['--no-sandbox', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'])
    pg = b.new_page(viewport={'width': 1600, 'height': 1000}); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e).split('\n')[0]))
    def route(r):
        u = r.request.url
        if u == 'http://t.local/': r.fulfill(status=200, content_type='text/html', body=HTML)
        elif u.startswith('http://t.local/gsm-preview.js'): r.fulfill(status=200, content_type='application/javascript', body=SRC)
        elif u.startswith('http://t.local/gsm-relief.js'): r.fulfill(status=200, content_type='application/javascript', body=REL)
        else: r.abort()
    pg.route('**/*', route)
    pg.add_init_script("localStorage.setItem('groundsmith-web-v1',%s);localStorage.setItem('groundsmith-web-welcomed','1');localStorage.setItem('groundsmith-web-privacy',JSON.stringify({solo:{v:'9999'},join:{v:'9999'},lead:{v:'9999'}}));" % json.dumps(json.dumps(wb)))
    pg.goto('http://t.local/'); pg.wait_for_selector('#gsm'); pg.wait_for_timeout(1500)
    pg.evaluate("window.gsmTab(4)"); pg.wait_for_timeout(1500)
    n = pg.evaluate("document.querySelectorAll('#gsm .coa').length"); best = (-1, -1)
    for i in range(n):
        pg.evaluate("i=>{var c=document.querySelectorAll('#gsm .coa')[i];c.querySelectorAll('details').forEach(d=>d.open=true);c.scrollIntoView()}", i); pg.wait_for_timeout(1300)
        k = pg.evaluate("i=>document.querySelectorAll('#gsm .coa')[i].querySelectorAll('.grel .wn').length", i)
        if k > best[1]: best = (i, k)
    walkable = pg.evaluate("[...document.querySelectorAll('#gsm .coa .grel .wgo')].filter(b=>b.style.display!=='none').length")
    print('cards', n, 'most stops: card', best, '| cards with a walk button', walkable)
    CI = int(os.environ['CARD']) if os.environ.get('CARD') else best[0]
    if CI < 0: print('no card map'); sys.exit(0)
    pg.evaluate("i=>document.querySelectorAll('#gsm .coa')[i].scrollIntoView()", CI); pg.wait_for_timeout(1200)
    c = pg.query_selector_all('#gsm .coa')[CI]
    fs = [x for x in c.query_selector_all('button') if x.is_visible() and (x.inner_text() or '') == 'Full screen']
    if fs and not os.environ.get('NOFS'): fs[0].click(); pg.wait_for_timeout(2500)
    w = [x for x in c.query_selector_all('.grel .wgo') if x.is_visible()]
    print('walk button:', w[0].inner_text() if w else None)
    w[0].evaluate('e=>e.click()'); pg.wait_for_timeout(2500)
    cap = lambda: pg.evaluate("i=>{var g=document.querySelectorAll('#gsm .coa')[i].querySelector('.grel');var c=g.querySelector('.tourcap');return [g.classList.contains('walking'),(c.querySelector('.ta')||{}).textContent,(c.querySelector('.tt')||{}).textContent,((c.querySelector('.tx')||{}).textContent||'').slice(0,90),[...c.querySelectorAll('.wk span')].map(s=>(s.className?s.className+':':'')+s.textContent).join(' ')]}", CI)
    print('card full screen while walking:', pg.evaluate("i=>document.querySelectorAll('#gsm .coa')[i].classList.contains('gtfs-on')", CI)); print('step 1:', cap()); pg.screenshot(path=OUT + '_1.png')
    t0=pg.evaluate('performance.now()'); fr=pg.evaluate('new Promise(r=>{let n=0,t=performance.now();function f(){n++;if(performance.now()-t<2000)requestAnimationFrame(f);else r(n/2)}requestAnimationFrame(f)})'); print('frames per second while walking:', fr)
    nx = c.query_selector('.tourcap .wnx'); nx.evaluate('e=>e.click()'); pg.wait_for_timeout(600); c.query_selector('.tourcap .wnx').evaluate('e=>e.click()'); pg.wait_for_timeout(1500)
    print('after Next x2:', cap()[1:3]); pg.screenshot(path=OUT + '_3.png')
    c.query_selector('.tourcap .walkbar .bt:not(.wnx)').evaluate('e=>e.click()'); pg.wait_for_timeout(500); print('after Back:', cap()[1:3])
    pg.keyboard.press('ArrowRight'); pg.wait_for_timeout(500); print('after ArrowRight:', cap()[1:3])
    sp = c.query_selector_all('.tourcap .wk span'); sp[-1].evaluate('e=>e.click()'); pg.wait_for_timeout(1500); print('tap last stop:', cap()[1:3], '| Next says', c.query_selector('.tourcap .wnx').inner_text()); pg.screenshot(path=OUT + '_last.png')
    c.query_selector('.tourcap .wnx').evaluate('e=>e.click()'); pg.wait_for_timeout(600); print('Done ends the walk:', not cap()[0])
    w[0].evaluate('e=>e.click()'); pg.wait_for_timeout(800); pg.keyboard.press('Escape'); pg.wait_for_timeout(600); print('Escape ends the walk:', not cap()[0], '| card full screen after:', pg.evaluate("i=>document.querySelectorAll('#gsm .coa')[i].classList.contains('gtfs-on')", CI))
    print('errors:', errs[:3])
    b.close()
