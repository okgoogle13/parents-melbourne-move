const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://'+process.argv[2]);await p.emulateMedia({media:'print'});
await p.pdf({path:process.argv[3],preferCSSPageSize:true,printBackground:true});
await p.emulateMedia({media:'screen'});await p.setViewportSize({width:1000,height:1200});
await p.screenshot({path:process.argv[4],fullPage:false});await b.close();})();
