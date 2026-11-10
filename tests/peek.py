import json, sys
from playwright.sync_api import sync_playwright
JS, WB, TAB = sys.argv[1], sys.argv[2], int(sys.argv[3])
SRC=open(JS,'rb').read()
HTML=b'<!doctype html><html><head><meta charset="utf-8"></head><body><div id="gsm-mount">L</div><script>window.GSM_ESRI_KEY="";var t=document.createElement("script");t.src="http://t.local/gsm-preview.js";document.body.appendChild(t);</script></body></html>'
wb=json.load(open(WB))['data']
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome',args=['--no-sandbox'])
    pg=b.new_page(); 
    def route(r):
        u=r.request.url
        if u=='http://t.local/': r.fulfill(status=200,content_type='text/html',body=HTML)
        elif u.startswith('http://t.local/gsm-preview.js'): r.fulfill(status=200,content_type='application/javascript',body=SRC)
        else: r.abort()
    pg.route('**/*',route)
    pg.add_init_script("localStorage.setItem('groundsmith-web-v1',%s);localStorage.setItem('groundsmith-web-welcomed','1');"%json.dumps(json.dumps(wb)))
    pg.goto('http://t.local/'); pg.wait_for_selector('#gsm'); pg.wait_for_timeout(800)
    pg.evaluate("window.gsmTab(%d)"%TAB); pg.wait_for_timeout(600)
    print(pg.evaluate("""()=>{var o=[];document.querySelectorAll('.plab').forEach(function(l){if(/STILL OPEN/.test(l.textContent)){var n=l.nextElementSibling;o.push(l.textContent+' => '+(n?n.textContent:''));var m=l.parentNode;}});return o.join('\\n')}"""))
    b.close()
