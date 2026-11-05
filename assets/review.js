// Copy review timestamps without pretending to control a cross-origin player.
document.querySelectorAll('[data-time]').forEach(button=>{
  const label=button.querySelector('span').textContent;
  button.setAttribute('aria-label',`Copy timestamp ${label}: ${button.textContent.trim()}`);
  button.addEventListener('click',async()=>{
    const text=`${label} — ${button.textContent.trim().replace(label,'').trim()}`;
    try{await navigator.clipboard.writeText(text);document.getElementById('chapter-note').textContent=`Copied ${text}`;}
    catch{document.getElementById('chapter-note').textContent=text;}
  });
});
