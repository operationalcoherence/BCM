const fs=require('fs');
const LT=fs.readFileSync('stop.txt','utf8').split(' ');
const Ot={}; LT.forEach(t=>Ot[t]=1);
const At={family:1,supply:1,apply:1,rely:1,early:1,assembly:1,ally:1,july:1,italy:1,anomaly:1,butterfly:1,firefly:1,monopoly:1};
const Dsc={}; "good bad new old right wrong big small great true real whole full general specific particular different certain first".split(' ').forEach(t=>Dsc[t]=1);
function Nt(t){let e=t;
 if(/ies$/.test(e)&&e.length>5) e=e.slice(0,-3)+'y';
 else if(/ing$/.test(e)&&e.length>5) e=e.slice(0,-3);
 else if((/ed$/.test(e)&&e.length>5)||(/es$/.test(e)&&e.length>6)) e=e.slice(0,-2);
 else if(/s$/.test(e)&&!/(ss|us|is)$/.test(e)&&e.length>3) e=e.slice(0,-1);
 return e.length>6?e.slice(0,6):e;}
const stats={proper:{},stopHit:{},stems:{},kept:0,total:0,shortDrop:{},numDrop:{},lyDrop:{}};
function Ht(text){
 let n=(text||'').replace(/[’']/g,'');
 n=n.replace(/([.!?;:]\s+|^\s*|\n\s*)([A-Z])/g,(m,a,b)=>a+b.toLowerCase());
 n.split(/(\s+|[,.;:!?()"“”\/]+)/).forEach(tok=>{
  if(!tok||/^\s+$/.test(tok))return;
  if(/^[,.;:!?()"“”\/]+$/.test(tok))return;
  let r=tok.replace(/^-+|-+$/g,''); if(!r)return;
  stats.total++;
  if(/^[A-Z]/.test(r)&&r!=='I'){stats.proper[r]=(stats.proper[r]||0)+1;return;}
  const low=r.toLowerCase();
  if(low.length<3){stats.shortDrop[low]=(stats.shortDrop[low]||0)+1;return;}
  if(Ot[low]){if(!Dsc[low])stats.stopHit[low]=(stats.stopHit[low]||0)+1;return;}
  if(/^\d/.test(low)){stats.numDrop[low]=(stats.numDrop[low]||0)+1;return;}
  if(/ly$/.test(low)&&!At[low]){stats.lyDrop[low]=(stats.lyDrop[low]||0)+1;return;}
  if(!/^[a-z-]+$/.test(low))return;
  const st=Nt(low);
  (stats.stems[st]=stats.stems[st]||{})[low]=(stats.stems[st][low]||0)+1;
  stats.kept++;
 });
}
const wb=JSON.parse(fs.readFileSync(process.argv[2],'utf8')).data;
const texts=[wb.goal||''].concat(wb.a||[]).concat((wb.m||[]).map(r=>r[3]||'')).concat(((wb.p&&wb.p.m)||[]).map(r=>r[3]||''));
texts.forEach(Ht);
const name=process.argv[2];
console.log('=== '+name+'  tokens='+stats.total+' kept='+stats.kept+' ('+Math.round(100*stats.kept/stats.total)+'%)');
const coll=Object.entries(stats.stems).filter(([s,m])=>Object.keys(m).length>1);
console.log('--- STEM COLLISIONS ('+coll.length+' stems hold more than one distinct word)');
coll.sort((a,b)=>Object.keys(b[1]).length-Object.keys(a[1]).length).forEach(([s,m])=>{
  console.log('   '+s+'  <-  '+Object.entries(m).map(([w,c])=>w+'×'+c).join(', '));});
const pn=Object.entries(stats.proper).sort((a,b)=>b[1]-a[1]);
console.log('--- PROPER NOUNS DROPPED: '+pn.length+' distinct, '+pn.reduce((a,b)=>a+b[1],0)+' occurrences');
console.log('   '+pn.slice(0,24).map(([w,c])=>w+'×'+c).join(', '));
const sh=Object.entries(stats.stopHit).sort((a,b)=>b[1]-a[1]);
console.log('--- STOPWORDS HIT: top 20 of '+sh.length);
console.log('   '+sh.slice(0,20).map(([w,c])=>w+'×'+c).join(', '));
const nd=Object.entries(stats.numDrop).sort((a,b)=>b[1]-a[1]);
if(nd.length)console.log('--- NUMERIC DROPPED: '+nd.slice(0,12).map(([w,c])=>w+'×'+c).join(', '));
const ld=Object.entries(stats.lyDrop).sort((a,b)=>b[1]-a[1]);
if(ld.length)console.log('--- -LY DROPPED: '+ld.slice(0,14).map(([w,c])=>w+'×'+c).join(', '));
