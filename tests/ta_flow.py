"""v226: the constraint loop on Taking Action, end to end.
Constraint -> card -> Q.4 -> WHAT YOU DID -> re-map (SINCE YOU ACTED), plus the program/strategy switch on a
seeded card moving it between the groups.
Usage (from tests/): python3 ta_flow.py WORKBOOK.json"""
import json, sys
from playwright.sync_api import sync_playwright
SRC = open('../gsm-preview.js', 'rb').read()
HTML = b'<!doctype html><html><head><meta charset="utf-8"></head><body><div id="gsm-mount">L</div><script>window.GSM_ESRI_KEY="";var t=document.createElement("script");t.src="http://t.local/gsm-preview.js";document.body.appendChild(t);</script></body></html>'
wb = json.load(open(sys.argv[1]))['data']
ok = True
def check(c, m):
    global ok
    print(('PASS ' if c else 'FAIL ') + m); ok = ok and bool(c)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome', args=['--no-sandbox'])
    pg = b.new_page(viewport={'width': 1300, 'height': 900}); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
    def route(r):
        u = r.request.url
        if u == 'http://t.local/': r.fulfill(status=200, content_type='text/html', body=HTML)
        elif u.startswith('http://t.local/gsm-preview.js'): r.fulfill(status=200, content_type='application/javascript', body=SRC)
        else: r.abort()
    pg.route('**/*', route)
    pg.add_init_script("if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.setItem('groundsmith-web-v1',%s);localStorage.setItem('groundsmith-web-welcomed','1');localStorage.setItem('groundsmith-web-privacy',JSON.stringify({solo:{v:'9999'},join:{v:'9999'},lead:{v:'9999'}}));}" % json.dumps(json.dumps(wb)))
    pg.goto('http://t.local/'); pg.wait_for_selector('#gsm', timeout=20000); pg.wait_for_timeout(1200)
    pg.evaluate("window.gsmTab(4)"); pg.wait_for_timeout(1200)
    st = pg.evaluate("""()=>({grp:[...document.querySelectorAll('#gsm-pat .tagrp .tagh')].map(e=>e.textContent),
      seeded:[...document.querySelectorAll('#gsm-pat .coa[data-seed]')].map(c=>c.getAttribute('data-seed')+':'+c.querySelector('.hd .mode').textContent),
      test:!!document.querySelector('#gsm-pat .tatst'), split:document.querySelectorAll('#gsm-pat .coa .tasplit').length,
      chart:document.querySelectorAll('#gsm-pat details.gtchart').length})""")
    print(st)
    check(st['test'], 'THE TEST panel shows')
    check(st['grp'][:1] == ['STRATEGIES'], 'strategies grouped first')
    check(any(s.startswith('sys:') for s in st['seeded']) or any(s.startswith('opp:') for s in st['seeded']), 'cards seeded from the structure')
    # constraint on the first seeded card that has a field
    tid = pg.evaluate("""()=>{var t=document.querySelector('#gsm-pat .coa[data-seed] textarea[data-cons]');return t?t.getAttribute('data-cons'):null}""")
    tid or print('SKIP this workbook has no seeded card with a constraint field')
    if tid:
        pg.evaluate("""(id)=>{var t=document.querySelector('#gsm-pat .coa[data-seed] textarea[data-cons="'+id+'"]');var w=t.closest('details');w&&(w.open=true);var b=t.closest('.ccons').querySelector('.tanb');b&&b.click()}""", tid)
        pg.wait_for_timeout(300)
        ta = pg.locator('#gsm-pat .coa[data-seed] textarea[data-cons="%s"]' % tid).first
        ta.scroll_into_view_if_needed()
        pre = pg.evaluate("""(id)=>[...document.querySelectorAll('.consq[data-cqfor="'+id+'"] button')].every(b=>b.disabled)""", tid)
        check(pre, 'add-to-Q buttons show grayed out before anything is written')
        ta.fill('A hundred-year suppression rule still sets the default; write a local exception for managed fire'); pg.wait_for_timeout(300)
        vis = pg.evaluate("""(id)=>[...document.querySelectorAll('.consq[data-cqfor="'+id+'"] button')].every(b=>!b.disabled)""", tid)
        check(vis, 'add-to-Q buttons turn on once a constraint is written (on every card with that note)')
        nc = pg.evaluate("""(id)=>{var q=document.querySelector('.ncons[data-ncid="'+id+'"]');return q?q.textContent:''}""", tid)
        check('local exception' in nc, 'the note on Mapping Landscape shows the constraint as it is typed')
        pg.evaluate("""(id)=>document.querySelector('#gsm-pat .consq[data-cqfor="'+id+'"] button[data-cq="3"]').click()""", tid); pg.wait_for_timeout(1500)
        C = pg.evaluate("()=>JSON.parse(localStorage.getItem('groundsmith-web-v1'))")
        check('local exception for managed fire' in (C['a'][3] or ''), 'constraint added to Q.4 in the workbook')
        mc = pg.evaluate("()=>document.querySelector('.qa[data-i=\"3\"] textarea').value")
        check('local exception for managed fire' in mc, 'Mapping Context shows the new Q.4 text')
        pg.evaluate("window.gsmTab(4)"); pg.wait_for_timeout(1200)
        on = pg.evaluate("""(id)=>{var b=document.querySelector('.consq[data-cqfor="'+id+'"] button[data-cq="3"]');return b?b.textContent:''}""", tid)
        check(on.startswith('In Q.4'), 'button now reads In Q.4: ' + on)
        tst = pg.evaluate("()=>document.querySelector('#gsm-pat .tatst').textContent")
        check('IN Q.4' in tst, 'THE TEST lists the named constraint as in Q.4')
        card = pg.locator('#gsm-pat .coa[data-seed]:has(textarea[data-cons="%s"])' % tid).first
        ac = card.locator('.actcons').text_content() if card.locator('.actcons').count() else ''
        kept = pg.evaluate("""(id)=>{var t=document.querySelector('#gsm-pat textarea[data-cons="'+id+'"]');return !t.closest('.ccons').classList.contains('cempty')}""", tid)
        check(kept, 'a written constraint stays open after the page re-reads')
        check('local exception' in ac, 'WHAT YOU DID lists the constraint named on the card')
        card.locator('.actx').fill('Met the district FMO about a managed-fire exception'); card.locator('.actgo').click(); pg.wait_for_timeout(800)
        C = pg.evaluate("()=>JSON.parse(localStorage.getItem('groundsmith-web-v1'))")
        a = C['acts'][-1] if C.get('acts') else {}
        check(a.get('c') and a['c'][0]['id'] == tid, 'the log entry carries the constraint')
        check(tid in (C.get('remap') or {}), 'the constraint note is flagged to re-map')
        pg.evaluate("window.gsmTab(1)"); pg.wait_for_timeout(600)
        since = pg.evaluate("()=>{var b=document.getElementById('gsm-since');return b?b.innerText:''}")
        check('local exception' in since, 'SINCE YOU ACTED shows the constraint next to its note')
        nc = pg.evaluate("""(id)=>{var q=document.querySelector('.ncons[data-ncid="'+id+'"]');return q?q.textContent:''}""", tid)
        check('(in Q.4)' in nc, 'the note says the constraint is in Q.4')
    # switch a seeded strategy to a program: it moves groups
    pg.evaluate("window.gsmTab(4)"); pg.wait_for_timeout(800)
    btn = pg.locator('#gsm-pat .coa[data-seed] .gsmmode[data-mv="p"]').first
    if btn.count():
        sd = btn.evaluate("b=>b.closest('.coa').getAttribute('data-seed')")
        btn.evaluate('b=>b.click()'); pg.wait_for_timeout(1500); pg.evaluate("window.gsmTab(4)"); pg.wait_for_timeout(900)
        where = pg.evaluate("""(sd)=>{var c=document.querySelector('#gsm-pat .coa[data-seed="'+sd+'"]');var g=null,e=c;while(e&&(e=e.previousElementSibling)){if(e.classList.contains('tagrp')){g=e.querySelector('.tagh').textContent;break}}return [c.querySelector('.hd .mode').textContent,g]}""", sd)
        check(where == ['PROGRAM', 'PROGRAMS'], 'switched seeded card sits under PROGRAMS: %s' % where)
    lay = pg.evaluate("""()=>{var c=[...document.querySelectorAll('#gsm-pat .coa')];return [c.every(x=>x.querySelector('.tawhy')), c.filter(x=>x.querySelector('.tawhy[open]')).length, !!document.querySelector('#gsm-pat .tafirst'), c.filter(x=>x.querySelector('.tastrip')).length]}""")
    check(lay[0] and lay[2] and lay[3] > 0, 'every card layered; first move leads: %s' % lay)
    check(not errs, 'no page errors %s' % errs[:3])
    b.close()
print('ALL PASS' if ok else 'SOME FAILED')
