import json, sys
from playwright.sync_api import sync_playwright
JS, WB, TABS = sys.argv[1], sys.argv[2], [int(x) for x in sys.argv[3].split(',')]
SRC=open(JS,'rb').read()
HTML=b'<!doctype html><html><head><meta charset="utf-8"></head><body><div id="gsm-mount">L</div><script>window.GSM_ESRI_KEY="";var t=document.createElement("script");t.src="http://t.local/gsm-preview.js";document.body.appendChild(t);</script></body></html>'
wb=json.load(open(WB))['data']
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome',args=['--no-sandbox'])
    pg=b.new_page(viewport={'width':1400,'height':900}); errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.on('console',lambda m: errs.append('console:'+m.text) if m.type=='error' else None)
    def route(r):
        u=r.request.url
        if u=='http://t.local/': r.fulfill(status=200,content_type='text/html',body=HTML)
        elif u.startswith('http://t.local/gsm-preview.js'): r.fulfill(status=200,content_type='application/javascript',body=SRC)
        else: r.abort()
    pg.route('**/*',route)
    pg.add_init_script("localStorage.setItem('groundsmith-web-v1',%s);localStorage.setItem('groundsmith-web-welcomed','1');"%json.dumps(json.dumps(wb)))
    pg.goto('http://t.local/'); pg.wait_for_selector('#gsm',timeout=20000); pg.wait_for_timeout(1200)
    for tab in TABS:
        pg.evaluate("window.gsmTab&&window.gsmTab(%d)"%tab); pg.wait_for_timeout(900)
        for _ in range(4):
            pg.evaluate("document.querySelectorAll('.closed').forEach(e=>e.classList.remove('closed'))"); pg.wait_for_timeout(200)
        print("######## TAB %d"%tab)
        print(pg.evaluate("()=>document.querySelector('#gsm').innerText"))
    print("######## ERRORS", errs)
    b.close()
