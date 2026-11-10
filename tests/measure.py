import json, sys
from playwright.sync_api import sync_playwright
JS, WB = sys.argv[1], sys.argv[2]
SRC=open(JS,'rb').read()
HTML=b'<!doctype html><html><head><meta charset="utf-8"></head><body><div id="gsm-mount">L</div><script>window.GSM_ESRI_KEY="";var t=document.createElement("script");t.src="http://t.local/gsm-preview.js";document.body.appendChild(t);</script></body></html>'
wb=json.load(open(WB))['data']
JSM="""()=>{var out=[];document.querySelectorAll('svg[viewBox]').forEach(function(s){var vb=s.getAttribute('viewBox');if(vb.indexOf('388')<0&&s.parentNode.getAttribute('data-fig')!=='hang'&&!s.closest('[data-fig=hang]'))return;
var u=null;Array.prototype.forEach.call(s.children,function(c,i){if(c.tagName==='rect'&&i==0)return;try{var b=c.getBBox();if(!b.width&&!b.height)return;var r=[b.x,b.y,b.x+b.width,b.y+b.height];u=u?[Math.min(u[0],r[0]),Math.min(u[1],r[1]),Math.max(u[2],r[2]),Math.max(u[3],r[3])]:r}catch(e){}});
out.push({vb:vb,draw:u&&u.map(function(x){return Math.round(x*10)/10})})});return out}"""
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome',args=['--no-sandbox'])
    pg=b.new_page(viewport={'width':1400,'height':900}); errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e)))
    def route(r):
        u=r.request.url
        if u=='http://t.local/': r.fulfill(status=200,content_type='text/html',body=HTML)
        elif u.startswith('http://t.local/gsm-preview.js'): r.fulfill(status=200,content_type='application/javascript',body=SRC)
        else: r.abort()
    pg.route('**/*',route)
    pg.add_init_script("localStorage.setItem('groundsmith-web-v1',%s);localStorage.setItem('groundsmith-web-welcomed','1');"%json.dumps(json.dumps(wb)))
    pg.goto('http://t.local/'); pg.wait_for_selector('#gsm',timeout=20000); pg.wait_for_timeout(1200)
    for tab in (3,6):
        pg.evaluate("window.gsmTab(%d)"%tab); pg.wait_for_timeout(900)
        print('tab',tab,pg.evaluate(JSM))
    print('errors',errs)
    b.close()
