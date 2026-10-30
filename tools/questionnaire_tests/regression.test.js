const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const pg = await b.newPage({viewport:{width:390,height:844}});
  const errs = []; pg.on('pageerror', e=>errs.push(e.message)); pg.on('console', m=>{ if(m.type()==='error') errs.push('console: '+m.text()); });
  await pg.goto('file://'+process.cwd()+'/page.html#test'); await pg.click('#who-TEST');
  const fails = []; const ok = (c,msg)=>{ if(!c) fails.push(msg); };
  // helpers in page
  await pg.evaluate(()=>{
    window.setA = (tag, letter) => { const it=BYTAG[tag]; const i=it.opts.findIndex(o=>o.charAt(0)===letter); document.getElementById(safeId(tag)+"_"+i).checked=true; update(); };
    window.reset = () => { clearForm(); update(); };
    window.vis = () => ITEMS.filter(it=>!it.fs.hidden).map(it=>it.tag);
  });
  // structure
  const info = await pg.evaluate(()=>({parts:SECTIONS.map(s=>s.title), tags:ITEMS.map(i=>i.tag), v:PAGE_VERSION, mode:MODE, dk:DKEY("Mum"),
    q155:BYTAG["Q15.5"].q, sep:SEP[3], lede:document.querySelector(".lede").textContent}));
  console.log(JSON.stringify(info,null,0));
  ok(!info.tags.includes("Q10") && !info.tags.includes("Q13d"), "Q10/Q13d still present");
  // ladder: all limits x thresholds
  const LIM={A:25,B:35,C:45,D:60,E:90};
  function expected(lim,t){ const L=LIM[lim]; const rungs={};
    if(30<=L){ rungs["30"]=t>=30?"A":"B"; if(t>=30){ let b=2; for(const m of [45,60,75]){ if(m>L){ return {br:"ABCDEF"[b],cap:"Y",rungs}; } rungs[m]= t>=m?"A":"B"; if(t>=m) b++; else return {br:"ABCDEF"[b],cap:"N",rungs}; } return {br:"F",cap:"N",rungs}; } }
    rungs["20"]=t>=20?"A":"B"; return {br:t>=20?"B":"A", cap:(t>=20 && 30>L)?"Y":"N", rungs}; }
  for(const lim of "ABCDE") for(const t of [15,20,30,45,60,75,90]){
    const res = await pg.evaluate(([lim,t])=>{ reset(); setA("R5.2",lim); const asked=[]; let guard=0;
      while(guard++<10){ const s=SECTIONS.find(x=>x.title==="Family drive"); const l=stepItems(s); const cur=l.find(it=>raw(it.tag)==="");
        const shownNow = ITEMS.filter(it=>it.sec===s && !it.fs.hidden).map(i=>i.tag);
        if(shownNow.length>1) return {err:"more than one displayed "+shownNow};
        if(!cur) break; const m=+cur.tag.split("-")[1]; asked.push(cur.tag); setA(cur.tag, t>=m?"A":"B"); s.next.click && s.pos++; update(); }
      const a=collect(); const o={}; Object.keys(a).filter(k=>k.startsWith("R8.3")).forEach(k=>o[k]=a[k].charAt(0)); return {o,asked}; },[lim,t]);
    if(res.err){ fails.push(res.err); continue; }
    const e = expected(lim,t);
    ok(res.o["R8.3"]===e.br && res.o["R8.3c"]===e.cap, `lim ${lim} t ${t}: got ${res.o["R8.3"]}/${res.o["R8.3c"]} want ${e.br}/${e.cap}`);
    for(const m of ["30","20","45","60","75"]){ const want = e.rungs[m] || null; const got=res.o["R8.3-"+m];
      if(want) ok(got===want, `lim ${lim} t ${t} rung ${m}: got ${got} want ${want}`);
      else { const reached = (m==="30") || (m==="20" ? false : null); ok(got==="X"||got==="L", `lim ${lim} t ${t} rung ${m}: got ${got} want X/L`); } }
    if(lim==="A" && t===90) console.log("A/90", JSON.stringify(res.o));
    if(lim==="B" && t===90) console.log("B/90", JSON.stringify(res.o));
    if(lim==="E" && t===90) console.log("E/90", JSON.stringify(res.o));
  }
  // L vs X specifics
  const lx = await pg.evaluate(()=>{ reset(); setA("R5.2","B"); setA("R8.3-30","A"); const a=collect(); return [a["R8.3-45"].charAt(0), a["R8.3-60"].charAt(0), a["R8.3-20"].charAt(0)]; });
  ok(lx.join("")==="LXX", "limit B green30: want L,X,X got "+lx);
  const lx2 = await pg.evaluate(()=>{ reset(); setA("R5.2","A"); const a=collect(); return [a["R8.3-30"].charAt(0), "R8.3" in a]; });
  ok(lx2[0]==="L" && lx2[1]===false, "limit A unanswered: want 30=L, no result; got "+lx2);
  // changing an earlier answer re-routes
  const rr = await pg.evaluate(()=>{ reset(); setA("R5.2","E"); setA("R8.3-30","A"); setA("R8.3-45","A"); setA("R8.3-60","B"); setA("R8.3-30","B"); setA("R8.3-20","A"); const a=collect(); return ["45","60","75"].map(m=>a["R8.3-"+m].charAt(0)).join("")+a["R8.3"].charAt(0); });
  ok(rr==="XXXB", "re-route after change: "+rr);
  // nature / area exclusion
  const ex = await pg.evaluate(()=>{ reset(); setA("R8.1","B"); const hid=BYTAG["R8.2"].optEls.map(l=>l.hidden?1:0).join(""); setA("R8.1","G"); const a=collect(); setA("R8.4","C"); const h5=BYTAG["R8.5"].optEls.map(l=>l.hidden?1:0).join(""); return {hid, r82:a["R8.2"], h5}; });
  ok(ex.hid==="01000001", "R8.2 hidden pattern "+ex.hid); ok(ex.r82 && ex.r82.startsWith("X"), "R8.2 auto X "+ex.r82); ok(ex.h5==="001000", "R8.5 hidden "+ex.h5);
  const ex2 = await pg.evaluate(()=>{ reset(); setA("R8.1","A"); setA("R8.2","B"); setA("R8.1","B"); return raw("R8.2"); });
  ok(ex2==="", "R8.2 pick cleared when it matches new R8.1: "+ex2);
  // real clicks through Kinds of nature with Next/Back
  await pg.evaluate(()=>reset());
  const nat = pg.locator('section.sec', {hasText:'Kinds of nature'});
  ok(await nat.locator('fieldset:visible').count()===1, "one visible in nature part");
  ok(await nat.locator('button:has-text("Next")').isDisabled(), "Next disabled before answer");
  await nat.locator('label:has-text("Bush and forest walks")').first().click();
  await nat.locator('button:has-text("Next")').click();
  const v2 = await pg.evaluate(()=>vis().filter(t=>t.startsWith("R8.1")||t.startsWith("R8.2")));
  ok(JSON.stringify(v2)==='["R8.2"]', "after Next shows R8.2: "+v2);
  ok(await nat.locator('button:has-text("Next")').isHidden(), "Next hidden on last");
  await nat.locator('button:has-text("Back")').click();
  ok(JSON.stringify(await pg.evaluate(()=>vis().filter(t=>t.startsWith("R8.")&&+t.charAt(3)<3)))==='["R8.1"]', "Back shows R8.1");
  // finish with missing jumps into step part
  await pg.evaluate(()=>{ reset(); ITEMS.forEach(it=>{ if(it.notes||!isShown(it)) return; if(it.sec.step) return; const i=it.opts.findIndex((o,oi)=>!(it.hideOpts||[]).includes(oi)); document.getElementById(safeId(it.tag)+"_"+i).checked=true; }); update(); });
  await pg.click('#finish');
  ok(JSON.stringify(await pg.evaluate(()=>vis().filter(t=>t.startsWith("R8.")))).includes("R8.1"), "finish shows first missing R8.1");
  // full record + export/import round trip
  const rt = await pg.evaluate(()=>{ reset();
    ITEMS.forEach(it=>{ if(it.notes||it.sec.step) return; if(!isShown(it)) return; const i=it.opts.findIndex((o,oi)=>!(it.hideOpts||[]).includes(oi)); document.getElementById(safeId(it.tag)+"_"+i).checked=true; update(); });
    setA("R5.2","D"); setA("R8.1","A"); setA("R8.2","C"); setA("R8.4","B"); setA("R8.5","E"); setA("R8.6","B"); setA("R8.3-30","A"); setA("R8.3-45","A"); setA("R8.3-60","A");
    const a=collect(); const rec={person:"TEST",savedAt:"2026-10-31T00:00:00Z",answers:a}; const txt=exportText(rec); const p=parseImport(txt);
    const same = Object.keys(a).length===Object.keys(p.answers).length && Object.keys(a).every(k=>a[k]===p.answers[k]);
    const old = parseImport(txt.replace("ONH v14","ONH v13"));
    return {n:Object.keys(a).length, missing:missing(a).map(i=>i.tag), same, errors:p.errors, old:old.error, code:txt.split("\n").filter(l=>/^R8|^ONH/.test(l)), r83:a["R8.3"], cap:a["R8.3c"]}; });
  console.log(JSON.stringify(rt));
  ok(rt.same && rt.errors.length===0 && rt.missing.length===0, "round trip");
  ok(/version 13/.test(rt.old||""), "v13 message rejected");
  const vv = await pg.evaluate(()=>{ reset(); setA("R8.1","B"); BYTAG["R8.2"].sec.pos=1; update(); const r82=BYTAG["R8.2"].optEls.filter(l=>l.getBoundingClientRect().height>0).length; setA("Q7a","B"); const r6=["R6.1","R6.2","R6.3"].map(t=>BYTAG[t].fs.getBoundingClientRect().height); const r56=BYTAG["R5.6"].fs.getBoundingClientRect().height; const rung=ITEMS.filter(i=>i.tag.startsWith("R8.3")).filter(i=>i.fs.getBoundingClientRect().height>0).map(i=>i.tag); return {r82,r6,r56,rung}; }); console.log(JSON.stringify(vv)); ok(vv.r82===6 && vv.r6.every(h=>h===0) && vv.r56===0 && JSON.stringify(vv.rung)==="[\"R8.3-30\"]","on-screen visibility "+JSON.stringify(vv));
  // screenshots
  for(const [t,f] of [["Kinds of nature","p4.png"],["Kinds of area","p5.png"],["Family drive","p6.png"]]){
    await pg.evaluate(()=>{ reset(); setA("R5.2","E"); }); const s=pg.locator('section.sec',{hasText:t}).first(); await s.screenshot({path:f}); }
  console.log("errors:", JSON.stringify(errs)); console.log("FAILS:", fails.length, JSON.stringify(fails,null,1));
  await b.close();
})();
