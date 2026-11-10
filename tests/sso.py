import json, sys
from playwright.sync_api import sync_playwright
JS, WB, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
SRC = open(JS, 'rb').read()
HTML = b'<!doctype html><html><head><meta charset="utf-8"></head><body><div id="gsm-mount">L</div><script>window.GSM_ESRI_KEY="";var t=document.createElement("script");t.src="http://t.local/gsm-preview.js";document.body.appendChild(t);</script></body></html>'
wb = json.load(open(WB))['data']

# Collect the WHAT STANDS OUT block: every .rule between the WHAT STANDS OUT
# label and the next .plab label. Click "Show all" first so nothing is capped.
EXTRACT = """
() => {
  const labs = [...document.querySelectorAll('#gsm .plab')];
  const lab = labs.find(l => l.textContent.trim().indexOf('WHAT STANDS OUT') === 0);
  if (!lab) return {error: 'no WHAT STANDS OUT label'};
  const box = lab.nextElementSibling;
  if (!box || !box.classList.contains('secb')) return {error: 'no secb after label'};
  const out = [];
  [...box.querySelectorAll('.rule')].forEach(n => {
    {
      const rl = n.querySelector('.rl');
      const body = rl ? rl.nextElementSibling : null;
      out.push({
        head: rl ? rl.textContent.trim() : '',
        text: body ? body.textContent.trim() : '',
        bold: [...(body ? body.querySelectorAll('b') : [])].map(b => b.textContent.trim()),
        refs: [...(body ? body.querySelectorAll('a.ref') : [])].map(a => a.getAttribute('data-ref'))
      });
    }
  });
  return {findings: out};
}
"""

with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome', args=['--no-sandbox'])
    pg = b.new_page(viewport={'width': 1400, 'height': 900}); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
    def route(r):
        u = r.request.url
        if u == 'http://t.local/': r.fulfill(status=200, content_type='text/html', body=HTML)
        elif u.startswith('http://t.local/gsm-preview.js'): r.fulfill(status=200, content_type='application/javascript', body=SRC)
        else: r.abort()
    pg.route('**/*', route)
    pg.add_init_script("localStorage.setItem('groundsmith-web-v1',%s);localStorage.setItem('groundsmith-web-welcomed','1');" % json.dumps(json.dumps(wb)))
    pg.goto('http://t.local/'); pg.wait_for_selector('#gsm', timeout=20000); pg.wait_for_timeout(1200)
    pg.evaluate("window.gsmTab&&window.gsmTab(2)"); pg.wait_for_timeout(1000)
    capped = pg.evaluate(EXTRACT)
    # expand the cap
    pg.evaluate("()=>{const m=document.querySelector('#gsm-more'); if(m) m.click();}"); pg.wait_for_timeout(700)
    for _ in range(3):
        pg.evaluate("document.querySelectorAll('.closed').forEach(e=>e.classList.remove('closed'))"); pg.wait_for_timeout(200)
    full = pg.evaluate(EXTRACT)
    json.dump({'capped': capped, 'full': full, 'errors': errs}, open(OUT, 'w'), indent=1)
    print(OUT, 'capped:', len(capped.get('findings', [])), 'full:', len(full.get('findings', [])), 'errors:', errs[:3])
    b.close()
