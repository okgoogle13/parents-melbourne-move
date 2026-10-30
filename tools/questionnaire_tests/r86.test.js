const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const pg = await b.newPage({viewport:{width:390,height:844}});
  const errs=[]; pg.on('pageerror',e=>errs.push(e.message));
  await pg.goto('file://'+process.cwd()+'/page.html#test'); await pg.click('#who-TEST');
  const fails=[]; const ok=(c,m)=>{ if(!c) fails.push(m); };
  const r = await pg.evaluate(()=>{
    const setA=(tag,L)=>{ const it=BYTAG[tag]; const i=it.opts.findIndex(o=>o.charAt(0)===L); document.getElementById(safeId(tag)+"_"+i).checked=true; update(); };
    const reset=()=>{ clearForm(); update(); };
    const s=BYTAG["R8.4"].sec; const out={};
    reset(); out.none = {stored:"R8.6" in collect(), steps:stepItems(s).map(i=>i.tag)};
    for(const L of "ABCDE"){ reset(); setA("R8.4",L); const a=collect(); out[L]={v:a["R8.6"]||null, steps:stepItems(s).map(i=>i.tag), req:requiredShown().some(i=>i.tag==="R8.6")}; }
    // B then switch to A after answering: stored X, radio not used
    reset(); setA("R8.4","B"); setA("R8.6","C"); setA("R8.4","A"); out.switch = collect()["R8.6"];
    // visible options when shown
    reset(); setA("R8.4","C"); s.pos=2; update(); out.visOpts = BYTAG["R8.6"].optEls.filter(l=>l.getBoundingClientRect().height>0).length; out.shownNow = s.items.filter(i=>!i.fs.hidden).map(i=>i.tag);
    // export readable lines include R8.6 only when asked
    reset(); setA("R8.4","B"); setA("R8.6","B"); let t=exportText({person:"TEST",savedAt:"x",answers:collect()}); out.expAsked=t.split("\n").filter(l=>/Bushfire|^R8\.6/.test(l));
    reset(); setA("R8.4","D"); t=exportText({person:"TEST",savedAt:"x",answers:collect()}); out.expAuto=t.split("\n").filter(l=>/Bushfire|^R8\.6/.test(l));
    out.importAuto = parseImport(t.replace("ONH v14 | TEST | x","ONH v14 | TEST | x")).answers["R8.6"];
    out.q12 = BYTAG["Q12"].opts[1]; out.cardB = CARDS[1].split("\n")[3]; out.cardE = CARDS[4].split("\n")[3];
    out.v=PAGE_VERSION; out.n=ITEMS.length;
    return out; });
  console.log(JSON.stringify(r,null,1));
  ok(r.none.stored===false && JSON.stringify(r.none.steps)==='["R8.4","R8.5"]',"unanswered R8.4");
  for(const L of "BC") ok(r[L].v===null && r[L].req && r[L].steps.length===3, L+" asks R8.6");
  for(const L of "ADE") ok(r[L].v && r[L].v.startsWith("X") && !r[L].req && r[L].steps.length===2, L+" stores X");
  ok(r.switch.startsWith("X"),"switch to A stores X");
  ok(r.visOpts===3 && JSON.stringify(r.shownNow)==='["R8.6"]',"3 visible options, one question on screen");
  ok(r.expAsked.length===2 && r.expAuto.length===1 && r.expAuto[0]==="R8.6=X","export lines");
  ok(r.importAuto && r.importAuto.startsWith("X"),"import X");
  // real clicks: Kinds of area with B → three steps, Next/Back
  await pg.evaluate(()=>{ clearForm(); update(); });
  const sec = pg.locator('section.sec',{hasText:'Kinds of area'});
  await sec.locator('fieldset[data-tag="R8.4"] label:has-text("Bush-edge hills")').click(); await sec.locator('button:has-text("Next")').click();
  await sec.locator('fieldset[data-tag="R8.5"] label:has-text("Peninsula seaside")').click();
  ok(await sec.locator('button:has-text("Next")').isVisible(),"Next visible on R8.5 when B chosen");
  await sec.locator('button:has-text("Next")').click();
  ok(await sec.locator('legend:has-text("bushfire-prone")').isVisible(),"R8.6 on screen after Next");
  await sec.locator('label:has-text("Some risk is OK")').click();
  ok(await sec.locator('.step-done').isVisible(),"done message after R8.6");
  await sec.screenshot({path:"p5b.png"});
  console.log("errors",JSON.stringify(errs)); console.log("FAILS:",fails.length,JSON.stringify(fails)); await b.close();
})();
