# Rebuild gsm-preview.js: clean v150 engine + terrain module. Usage: python3 -I tools/terrain/build_preview.py v164
import os, subprocess, sys
R=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ver=sys.argv[1]
subprocess.run([sys.executable,'-I',os.path.join(R,'tools/terrain/make_module.py')],check=True,stdout=subprocess.DEVNULL)
s=subprocess.run(['git','-C',R,'show','63a6819:gsm-preview.js'],check=True,capture_output=True,text=True).stdout
old='ye+=ee(de.slice(0,qe),ge,Eo,de),'
new=('ye+=(C.m.some(function(t){return(t[3]||"").trim()})?(window.gsmTD={m:C.m,a:Q(),goal:C.goal},'
     '\'<div class="gterr-host"></div><details class="fold gtold"><summary>THE EARLIER FIGURE</summary>\'+ee(de.slice(0,qe),ge,Eo,de)+"</details>"):ee(de.slice(0,qe),ge,Eo,de)),')
assert old in s and 't.textContent="v150"' in s
s=s.replace(old,new).replace('t.textContent="v150"','t.textContent="%s"'%ver)
# Taking Action: each card's way through it is drawn as trails on the same ground (the old graph stays as fallback)
R1=[('function Q(){return C.a.map(function(t,e){return q(e)})}','window.gsmData=function(){return{m:C.m,a:Q(),goal:C.goal}};function Q(){return C.a.map(function(t,e){return q(e)})}'),
    ('"</div>"+function(t,e){var n=e.filter(function(t){return t.line}).map(','"</div>"+function(t,e,stp){var n=e.filter(function(t){return t.line}).map('),
    ('}(t,s||[]),c=t?Wn(','}(t,s||[],e),c=t?Wn('),
    ('return\'<div class="csec"><div class="csl">THE WAY THROUGH IT</div><svg class="cpath"',
     'return\'<div class="csec"><div class="csl">THE WAY THROUGH IT</div><div class="gterr-card" data-mode="\'+(t?"STRATEGY":"PROGRAM")+\'" data-ids="\'+Gt(e.filter(function(x){return x.line}).map(function(x){return x.id}).join(","))+\'" data-steps="\'+Gt(JSON.stringify((stp||[]).map(function(x){return String(x).replace(/<[^>]*>/g,"")})))+\'"><svg class="cpath"'),
    ('\'</svg><div class="csn">\'+f+g+"</div></div>"}','\'</svg><div class="csn">\'+f+g+"</div></div></div>"}')]
for a,b in R1:
    assert s.count(a)==1,a[:60]
    s=s.replace(a,b)

s=s.rstrip()+"\n"+open(os.path.join(R,'tools/terrain/module.js')).read()
open(os.path.join(R,'gsm-preview.js'),'w').write(s)
print('built',ver)
