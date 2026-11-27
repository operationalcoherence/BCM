"""v232 check (Phase 2 step 9, part 1): Start here keeps the method, the instructions sit on their pages,
each note shows its emotion's definition and it follows a click, and the reading-page drop-downs show on
their own tab only. Usage: python3 step9.py JSFILE WORKBOOK.json [SHOTPREFIX]"""
import json, sys
from playwright.sync_api import sync_playwright
JS, WB = sys.argv[1], sys.argv[2]; SHOT = sys.argv[3] if len(sys.argv) > 3 else None
SRC = open(JS, 'rb').read()
HTML = b'<!doctype html><html><head><meta charset="utf-8"></head><body><div id="gsm-mount">L</div><script>window.GSM_ESRI_KEY="";var t=document.createElement("script");t.src="http://t.local/gsm-preview.js";document.body.appendChild(t);</script></body></html>'
wb = json.load(open(WB))['data']
ok = True
def check(c, msg):
    global ok
    print(('PASS ' if c else 'FAIL ') + msg); ok = ok and c
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome', args=['--no-sandbox'])
    pg = b.new_page(viewport={'width': 760, 'height': 1000}); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
    def route(r):
        u = r.request.url
        if u == 'http://t.local/': r.fulfill(status=200, content_type='text/html', body=HTML)
        elif u.startswith('http://t.local/gsm-preview.js'): r.fulfill(status=200, content_type='application/javascript', body=SRC)
        else: r.abort()
    pg.route('**/*', route)
    pg.add_init_script("localStorage.setItem('groundsmith-web-v1',%s);localStorage.setItem('groundsmith-web-welcomed','1');localStorage.setItem('groundsmith-web-privacy',JSON.stringify({solo:{v:'9999'},join:{v:'9999'},lead:{v:'9999'}}));" % json.dumps(json.dumps(wb)))
    pg.goto('http://t.local/'); pg.wait_for_selector('#gsm', timeout=20000); pg.wait_for_timeout(1200)
    vis = "s=>[...document.querySelectorAll(s)].filter(e=>e.offsetParent!==null).length"
    pg.evaluate("gsmTab(5)"); pg.wait_for_timeout(400)
    st = pg.evaluate("document.getElementById('gsm-start').innerText")
    check('Map the context using' not in st and 'Pattern Analysis reveals' not in st and 'One through four are questions about grasping' in st, 'Start here keeps the method, the workbook steps moved')
    if SHOT: pg.screenshot(path=SHOT + '_start.png', full_page=True)
    pg.evaluate("gsmTab(1)"); pg.wait_for_timeout(500)
    pg.evaluate("window.gsmMStep&&gsmMStep(1)"); pg.wait_for_timeout(300)
    check(pg.evaluate(vis, 'details.fold') >= 1 and 'HOW TO MAP' in pg.evaluate("document.querySelector('#gsm-a-chg+.sprog+.fold, #gsm-a-chg~.fold').textContent"), 'step 1: HOW TO MAP inside the drop-down')
    check(pg.evaluate(vis, '.dnhead') == 0, 'step 1: the describe-notes help is not shown')
    pg.evaluate("window.gsmMStep&&gsmMStep(2)"); pg.wait_for_timeout(400)
    check(pg.evaluate(vis, '.dnhead') == 1, 'step 2: the describe-notes help shows once')
    nd = pg.evaluate(vis, '.note .emodef')
    nmark = pg.evaluate("[...document.querySelectorAll('.note')].filter(e=>e.offsetParent!==null&&e.querySelector('.emo .ech.on:not(.none)')).length")
    check(nd == nmark and nmark > 0 or (nmark == 0 and nd == 0), 'step 2: %d notes with an emotion show %d definitions' % (nmark, nd))
    # pick an emotion on the first visible note and check the definition follows
    r = pg.evaluate("""()=>{var F=()=>[...document.querySelectorAll('.note')].filter(e=>e.offsetParent!==null&&e.querySelector('.emo'))[0];
      var n=F(); if(!n) return null; n.querySelector('.emo .ech[data-e="4"]').click();
      var a=F().querySelector('.emodef').textContent; F().querySelector('.emo .ech.none').click();
      var c=F().querySelector('.emodef'); return [a, c.textContent, getComputedStyle(c).display];}""")
    if r is None: print('SKIP no note to click')
    else:
        check(r[0].startswith('“Defiance is more than'), 'click Defiance: its definition shows')
        check(r[1] == '' and r[2] == 'none', 'click Not marked: the definition goes away')
        pg.evaluate("location.reload()"); pg.wait_for_selector('#gsm'); pg.wait_for_timeout(1200)
    if SHOT:
        pg.evaluate("gsmTab(1)"); pg.evaluate("window.gsmMStep&&gsmMStep(2)"); pg.wait_for_timeout(500)
        pg.screenshot(path=SHOT + '_notes.png')
    pg.evaluate("gsmTab(0)"); pg.wait_for_timeout(400)
    check('Combining fills WHO DID WHAT' in pg.evaluate("document.querySelector('#gsm').innerText"), 'Mapping Context: the WHO DID WHAT line shows')
    for tab, want, other in [(2, '.pian', '.pisy'), (3, '.pisy', '.pian'), (4, None, None), (6, None, None)]:
        pg.evaluate("gsmTab(%d)" % tab); pg.wait_for_timeout(600)
        a, y = pg.evaluate(vis, '.pian'), pg.evaluate(vis, '.pisy')
        if want: check(pg.evaluate(vis, want) == 1 and pg.evaluate(vis, other) == 0, 'tab %d: only its own instruction shows' % tab)
        else: check(a == 0 and y == 0, 'tab %d: no reading-page instruction' % tab)
        if SHOT and tab in (2, 3): pg.screenshot(path=SHOT + '_tab%d.png' % tab)
    check(not errs, 'no page errors %s' % errs[:3])
    b.close()
print('ALL PASS' if ok else 'SOME FAILED')
