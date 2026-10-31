const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const pg = await b.newPage({viewport:{width:390,height:844}});
  const errs=[]; pg.on('pageerror',e=>errs.push(e.message));
  await pg.goto('file://'+process.cwd()+'/page.html#test'); await pg.click('#who-TEST');
  const fails=[]; const ok=(c,m)=>{ if(!c) fails.push(m); };
  const r = await pg.evaluate(()=>{
    const setA=(tag,L)=>{ const it=BYTAG[tag]; const i=it.opts.findIndex(o=>o.charAt(0)===L); document.getElementById(safeId(tag)+"_"+i).checked=true; update(); };
    const reset=()=>{ clearForm(); update(); };
    const o={parts:SECTIONS.map(s=>s.title), v:PAGE_VERSION, dk:DKEY("Mum")};
    for(const L of "ABCD"){ reset(); setA("R9.3",L); const a=collect(); o["r93"+L]={r94:a["R9.4"]||null, shown:isShown(BYTAG["R9.4"]), req:requiredShown().some(i=>i.tag==="R9.4")}; }
    reset(); o.blank = "R9.4" in collect();
    reset(); setA("R9.3","A"); setA("R9.4","C"); setA("R9.3","B"); o.switch = collect()["R9.4"];
    reset(); o.nums = SECTIONS.find(s=>s.title==="Timing").items.filter(i=>!i.notes).map(i=>i.noEl.textContent);
    setA("R9.3","A"); o.nums2 = SECTIONS.find(s=>s.title==="Timing").items.filter(i=>!i.notes).map(i=>i.noEl.textContent);
    o.prioNums = SECTIONS.find(s=>s.title==="Priorities").items.filter(i=>!i.notes).map(i=>i.noEl.textContent).slice(0,3);
    reset(); setA("R9.3","A"); setA("R9.4","A"); BYTAG["R9 Notes"].fs.querySelector("textarea").value="Before Mum's knee op"; update();
    const t=exportText({person:"TEST",savedAt:"x",answers:collect()}); o.exp=t.split("\n").filter(l=>/^R9|Notes on timing|Sell Beachmere|Where to live/.test(l));
    const p=parseImport(t); o.imp = p.errors.length===0 && p.answers["R9.4"].startsWith("A") && p.answers["R9 Notes"]==="Before Mum's knee op";
    return o; });
  console.log(JSON.stringify(r,null,1));
  ok(r.v===15 && r.dk==="onh-v15-draft-Mum","version/draft key");
  ok(JSON.stringify(r.parts.slice(-3))==='["Later on","Timing","Priorities"]',"Timing before Priorities");
  for(const L of "AC") ok(r["r93"+L].shown && r["r93"+L].req && r["r93"+L].r94===null, L+" asks R9.4");
  for(const L of "BD") ok(!r["r93"+L].shown && r["r93"+L].r94 && r["r93"+L].r94.startsWith("X"), L+" stores X");
  ok(r.blank===false,"R9.4 not stored while R9.3 blank"); ok(r.switch.startsWith("X"),"switch to B stores X");
  ok(JSON.stringify(r.nums)==='["Question 1","Question 2","Question 3",""]' && JSON.stringify(r.nums2)==='["Question 1","Question 2","Question 3","Question 4"]',"numbering");
  ok(JSON.stringify(r.prioNums)==='["Question 1","Question 2","Question 3"]',"priorities numbering");
  ok(r.imp,"export/import round trip with notes");
  const sec = pg.locator('section.sec',{hasText:'About when and how we move'}); await pg.evaluate(()=>{ clearForm(); update(); });
  await sec.locator('fieldset[data-tag="R9.3"] label:has-text("Sell first")').click(); await sec.screenshot({path:"timing.png"});
  const sw = await pg.evaluate(()=>document.documentElement.scrollWidth>innerWidth); ok(!sw,"no sideways scroll");
  console.log("errors",JSON.stringify(errs)); console.log("FAILS:",fails.length,JSON.stringify(fails)); await b.close();
})();
