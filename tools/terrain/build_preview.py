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
s=s.rstrip()+"\n"+open(os.path.join(R,'tools/terrain/module.js')).read()
open(os.path.join(R,'gsm-preview.js'),'w').write(s)
print('built',ver)
