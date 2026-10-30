const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const pg = await b.newPage();
  const errs=[]; pg.on('pageerror',e=>errs.push(e.message));
  await pg.goto('file://'+process.cwd()+'/page.html#test'); await pg.click('#who-TEST');
  const res = await pg.evaluate(()=>{
    const setA=(tag,L)=>{ const it=BYTAG[tag]; const i=it.opts.findIndex(o=>o.charAt(0)===L); document.getElementById(safeId(tag)+"_"+i).checked=true; update(); };
    ITEMS.forEach(it=>{ if(it.notes||it.sec.step||!isShown(it)) return; const i=it.opts.findIndex((o,oi)=>!(it.hideOpts||[]).includes(oi)); document.getElementById(safeId(it.tag)+"_"+i).checked=true; update(); });
    setA("R5.2","C"); setA("R8.1","D"); setA("R8.2","E"); setA("R8.4","D"); setA("R8.5","C"); setA("R8.3-30","A"); setA("R8.3-45","A");
    setA("R5.5","C"); setA("R5.7","B"); BYTAG["R5.7"].textEl.value="St Thomas"; update();
    BYTAG["Q15 Notes"].fs.querySelector("textarea").value="Hospital: matters\nsecond line"; update();
    const a=collect(); const txt=exportText({person:"Mum",savedAt:"2026-10-31T09:00:00.000Z",answers:a});
    const same = p => !p.error && p.errors.length===0 && Object.keys(a).length===Object.keys(p.answers).length && Object.keys(a).every(k=>(BYTAG[k].notes?a[k].replace(/\s*\n\s*/g," / "):a[k])===p.answers[k]);
    const L = txt.split("\n"); const hi = L.findIndex(l=>l.startsWith("ONH v"));
    const out = {};
    out.plain = same(parseImport(txt));
    // 1a iOS multi-message copy: prefix on first line and on the code line (message split in two)
    const ios = L.map((l,i)=> i===0 ? "[31/10/2026, 9:15:22 am] Mum: "+l : i===hi ? "[31/10/2026, 9:16:01 am] Mum: "+l : l).join("\n");
    out.iosPrefix = same(parseImport(ios));
    // 1b Android export-style prefix on code line and on an answer line
    const and = L.map((l,i)=> i===hi ? "31/10/26, 09:16 - Mum: "+l : i===hi+1 ? "31/10/26, 09:16 - Mum: "+l : l).join("\n");
    out.androidPrefix = same(parseImport(and));
    // 2 invisible characters before ONH and inside other lines
    const inv = L.map((l,i)=> i===hi ? "‎⁨"+l+"⁩" : i===hi+2 ? "​"+l+"﻿" : l).join("\n");
    out.invisible = same(parseImport(inv));
    out.backticks = same(parseImport(L.map((l,i)=> i===hi ? "```"+l : i===L.length-1 ? l+"```" : l).join("\n")));
    // 3 old version still rejected, also with prefix/invisible
    out.v13 = parseImport(txt.replace("ONH v14","ONH v13")).error;
    out.v13prefixed = parseImport(ios.replace("ONH v14","ONH v13")).error;
    out.v10invisible = parseImport(inv.replace("ONH v14","ONH v10")).error;
    out.noHeader = parseImport(L.slice(0,hi).join("\n")).error;
    out.churchText = parseImport(ios).answers["R5.7"]; out.note = parseImport(ios).answers["Q15 Notes"];
    // owner panel UI path
    document.getElementById('importBox').hidden=false; document.getElementById('importText').value=ios; document.getElementById('importCheck').click();
    out.panel = document.getElementById('importStatus').textContent;
    out.sample = ios.split("\n").filter((l,i)=>i===0||i===hi);
    return out; });
  console.log(JSON.stringify(res,null,1)); console.log("errors", JSON.stringify(errs)); await b.close();
})();
