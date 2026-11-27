"""v248: prints what gsmSystems finds and the stories block on Pattern Analysis."""
import json, sys
from playwright.sync_api import sync_playwright
SRC=open(__import__('os').environ.get('GSMJS','../gsm-preview.js'),'rb').read()
HTML=b'<!doctype html><html><head><meta charset="utf-8"></head><body><div id="gsm-mount">L</div><script>window.GSM_ESRI_KEY="";var t=document.createElement("script");t.src="http://t.local/gsm-preview.js";document.body.appendChild(t);</script></body></html>'
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome',args=['--no-sandbox'])
    for f in sys.argv[1:]:
        wb=json.load(open(f))['data']
        pg=b.new_page(viewport={'width':1400,'height':900}); errs=[]
        pg.on('pageerror',lambda e:errs.append(str(e)))
        def route(r):
            u=r.request.url
            if u=='http://t.local/': r.fulfill(status=200,content_type='text/html',body=HTML)
            elif u.startswith('http://t.local/gsm-preview.js'): r.fulfill(status=200,content_type='application/javascript',body=SRC)
            else: r.abort()
        pg.route('**/*',route)
        pg.add_init_script("localStorage.setItem('groundsmith-web-v1',%s);localStorage.setItem('groundsmith-web-welcomed','1');localStorage.setItem('groundsmith-web-privacy',JSON.stringify({solo:{v:'9999'},join:{v:'9999'},lead:{v:'9999'}}));"%json.dumps(json.dumps(wb)))
        pg.goto('http://t.local/'); pg.wait_for_selector('#gsm',timeout=20000); pg.wait_for_timeout(1000)
        pg.evaluate("window.gsmTab(2)"); pg.wait_for_timeout(3500)
        r=pg.evaluate("""()=>{var Y=window.gsmSystems&&window.gsmSystems();if(!Y)return 'none';
          var f=g=>g.n.map(p=>p.lab+':'+(p.e==null?'-':'AcDIF'[p.e]||p.e)).join(' ')+' @'+Math.round(g.x)+','+Math.round(g.y)+' d'+g.depth.toFixed(2);
          var s=document.querySelector('.stories');
          return 'several='+Y.several+'\\nLOW '+Y.low.map(f).join('\\n    ')+'\\nHIGH '+Y.high.map(f).join('\\n    ')+'\\n---\\n'+(s?s.innerText:'(no stories block)')}""")
        print('=====',f); print(r); print('ERR',errs)
        pg.close()
    b.close()
