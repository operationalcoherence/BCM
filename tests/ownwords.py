"""v235: YOUR OWN WORDS strip on Pattern Analysis. Prints the strip and screenshots it.
Usage: python3 -I ownwords.py WORKBOOK.json [OUT.png] [WIDTH]"""
import json, sys
from playwright.sync_api import sync_playwright
SRC=open('../gsm-preview.js','rb').read()
HTML=b'<!doctype html><html><head><meta charset="utf-8"></head><body><div id="gsm-mount">L</div><script>window.GSM_ESRI_KEY="";var t=document.createElement("script");t.src="http://t.local/gsm-preview.js";document.body.appendChild(t);</script></body></html>'
wb=json.load(open(sys.argv[1]))['data']; W=int(sys.argv[3]) if len(sys.argv)>3 else 760
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome',args=['--no-sandbox'])
    pg=b.new_page(viewport={'width':W,'height':900}); errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e)))
    def route(r):
        u=r.request.url
        if u=='http://t.local/': r.fulfill(status=200,content_type='text/html',body=HTML)
        elif u.startswith('http://t.local/gsm-preview.js'): r.fulfill(status=200,content_type='application/javascript',body=SRC)
        else: r.abort()
    pg.route('**/*',route)
    pg.add_init_script("localStorage.setItem('groundsmith-web-v1',%s);localStorage.setItem('groundsmith-web-welcomed','1');localStorage.setItem('groundsmith-web-privacy',JSON.stringify({solo:{v:'9999'},join:{v:'9999'},lead:{v:'9999'}}));"%json.dumps(json.dumps(wb)))
    pg.goto('http://t.local/'); pg.wait_for_selector('#gsm',timeout=20000); pg.wait_for_timeout(1200)
    pg.evaluate("gsmTab(2)"); pg.wait_for_timeout(3500)
    n=pg.evaluate("document.querySelectorAll('.owstrip').length")
    print('strips:',n)
    if n:
        pg.evaluate("var s=document.querySelector('.owstrip');var d=s.closest('details');d.open=true;var p=d.parentElement.closest('details');p&&(p.open=true);s.scrollIntoView({block:'center'})"); pg.wait_for_timeout(500)
        print(pg.evaluate("document.querySelector('.owstrip').innerText.replace(/\\n+/g,' | ')"))
        el=pg.query_selector('.owstrip'); bb=el.bounding_box()
        if len(sys.argv)>2: pg.screenshot(path=sys.argv[2],clip={'x':0,'y':bb['y']-40,'width':W,'height':bb['height']+80})
    print('errors',errs)
    b.close()
