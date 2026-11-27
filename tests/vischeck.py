"""Pattern Analysis (2) and Taking Action (4), every fold open, 3D loaded.
python3 -I vischeck.py JS RELIEF WORKBOOK.json WIDTH OUTPREFIX
Writes OUTPREFIX_tabN.txt and OUTPREFIX_tabN.png; prints errors and overflow."""
import json, sys
from playwright.sync_api import sync_playwright
JS, RELF, WB, W, OUT = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]), sys.argv[5]
SRC = open(JS, 'rb').read(); REL = open(RELF, 'rb').read()
HTML = b'<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body style="margin:0"><div id="gsm-mount">L</div><script>window.GSM_ESRI_KEY="";var t=document.createElement("script");t.src="http://t.local/gsm-preview.js";document.body.appendChild(t);</script></body></html>'
wb = json.load(open(WB))['data']
OPEN = "document.querySelectorAll('.closed').forEach(e=>e.classList.remove('closed'));document.querySelectorAll('details').forEach(d=>d.open=true)"
WIDE = """()=>{const W=document.documentElement.clientWidth,o=[];document.querySelectorAll('#gsm *').forEach(e=>{const r=e.getBoundingClientRect();if(r.width>0&&r.right>W+2){let p=e.parentElement,clip=false;while(p&&p.id!=='gsm'){const s=getComputedStyle(p);if(/(auto|scroll|hidden)/.test(s.overflowX)){clip=true;break}p=p.parentElement}if(!clip)o.push(e.tagName+'.'+(e.className&&e.className.baseVal!==undefined?e.className.baseVal:e.className)+' '+Math.round(r.right)+' '+(e.innerText||'').slice(0,40).replace(/\\n/g,' '))}});return {W, scroll:document.documentElement.scrollWidth, o:o.slice(0,15)}}"""
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome', args=['--no-sandbox', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'])
    ctx = b.new_context(viewport={'width': W, 'height': 900}, device_scale_factor=1, is_mobile=W < 600, has_touch=W < 600)
    pg = ctx.new_page(); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e).split('\n')[0]))
    pg.on('console', lambda m: m.type == 'error' and errs.append('console: ' + m.text[:150]))
    def route(r):
        u = r.request.url
        if u == 'http://t.local/': r.fulfill(status=200, content_type='text/html', body=HTML)
        elif u.startswith('http://t.local/gsm-preview.js'): r.fulfill(status=200, content_type='application/javascript', body=SRC)
        elif u.startswith('http://t.local/gsm-relief.js'): r.fulfill(status=200, content_type='application/javascript', body=REL)
        else: r.abort()
    pg.route('**/*', route)
    pg.add_init_script("localStorage.setItem('groundsmith-web-v1',%s);localStorage.setItem('groundsmith-web-welcomed','1');localStorage.setItem('groundsmith-web-privacy',JSON.stringify({solo:{v:'9999'},join:{v:'9999'},lead:{v:'9999'}}));" % json.dumps(json.dumps(wb)))
    pg.goto('http://t.local/'); pg.wait_for_selector('#gsm', timeout=25000)
    for tab in (2, 4):
        pg.evaluate("window.gsmTab(%d)" % tab); pg.wait_for_timeout(1500)
        for _ in range(40): pg.mouse.wheel(0, 700); pg.wait_for_timeout(250)
        pg.wait_for_timeout(4000)
        for _ in range(5): pg.evaluate(OPEN); pg.wait_for_timeout(300)
        pg.wait_for_timeout(1500)
        open('%s_tab%d.txt' % (OUT, tab), 'w').write(pg.evaluate("()=>document.querySelector('#gsm').innerText"))
        print('tab', tab, 'wide:', json.dumps(pg.evaluate(WIDE)))
        pg.evaluate("window.scrollTo(0,0)"); pg.wait_for_timeout(300)
        pg.screenshot(path='%s_tab%d.png' % (OUT, tab), full_page=True)
    print('ERRORS', errs)
    b.close()
