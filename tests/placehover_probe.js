(() => {
  window.__zlog = [];
  const tt = () => document.querySelector('.gsm-tt');
  const obs = new MutationObserver(() => {
    const t = tt();
    if (t) window.__zlog.push(t.style.display + ' | ' + (t.innerText || '').split('\n')[0].slice(0, 60));
  });
  const start = () => { const t = tt(); if (t) { obs.observe(t, {attributes:true, childList:true, subtree:true, characterData:true}); return true; } return false; };
  if (!start()) { const i = setInterval(() => { if (start()) clearInterval(i); }, 50); }
})()
