import json,sys
from playwright.sync_api import sync_playwright
SRC=open('../gsm-preview.js','rb').read()
HTML=b'<!doctype html><html><head><meta charset="utf-8"></head><body><div id="gsm-mount">L</div><script>window.GSM_ESRI_KEY="";var t=document.createElement("script");t.src="http://t.local/gsm-preview.js";document.body.appendChild(t);</script></body></html>'
wb=json.load(open(sys.argv[1]))['data']
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome',args=['--no-sandbox'])
    pg=b.new_page(viewport={'width':1400,'height':900})
    def route(r):
        u=r.request.url
        if u=='http://t.local/': r.fulfill(status=200,content_type='text/html',body=HTML)
        elif u.startswith('http://t.local/gsm-preview.js'): r.fulfill(status=200,content_type='application/javascript',body=SRC)
        else: r.abort()
    pg.route('**/*',route)
    pg.add_init_script("localStorage.setItem('groundsmith-web-v1',%s);localStorage.setItem('groundsmith-web-welcomed','1');"%json.dumps(json.dumps(wb)))
    pg.goto('http://t.local/');pg.wait_for_selector('#gsm',timeout=20000);pg.wait_for_timeout(1200)
    for tab in (2,3,6):
        pg.evaluate("window.gsmTab&&window.gsmTab(%d)"%tab);pg.wait_for_timeout(900)
    out=pg.evaluate("()=>({lo:window.__lo||[],err:window.__loerr||null})")
    json.dump(out,open(sys.argv[2],'w'),indent=1)
    print('lists recorded:',len(out['lo']),'| error:',out['err'])
    b.close()
