import fs from 'node:fs/promises';
import path from 'node:path';
import http from 'node:http';
import {chromium} from '../../runtime/node_modules/playwright/index.mjs';
import {ROOT,json,readJSON} from '../../runtime/common.mjs';
const out=path.join(ROOT,'diagnostics/roundtrip-001');let browser,server;
const timer=setTimeout(async()=>{await browser?.close();server?.close();process.exit(124);},180000);
try {
 server=http.createServer(async(req,res)=>{try{const pathname=decodeURIComponent(new URL(req.url,'http://localhost').pathname),p=path.resolve(ROOT,'.'+pathname);if(!p.startsWith(ROOT+path.sep))throw Error('Path');const b=await fs.readFile(p);res.setHeader('Content-Type',({'.mjs':'text/javascript','.js':'text/javascript','.html':'text/html','.json':'application/json','.gltf':'model/gltf+json','.glb':'model/gltf-binary','.wasm':'application/wasm','.png':'image/png','.webp':'image/webp','.ktx2':'image/ktx2'})[path.extname(p)]??'application/octet-stream');res.end(b);}catch{res.statusCode=404;res.end('Not found');}});await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
 browser=await chromium.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true,args:['--disable-background-timer-throttling']});const page=await browser.newPage();await page.goto('http://127.0.0.1:'+server.address().port+'/diagnostics/roundtrip-001/render-diagnostic.html');await page.waitForFunction(()=>window.pipelineReady);const model=await readJSON(path.join(ROOT,'generated/FlightHelmet/model.json'));const result=await page.evaluate(m=>window.diagnose(m),model);
 for(let i=0;i<result.baseline.length;i++)for(const kind of ['reference','source']){const k=kind+'PNG';await fs.writeFile(path.join(out,`view-${i}-${kind}.png`),Buffer.from(result.baseline[i][k].split(',')[1],'base64'));delete result.baseline[i][k];}
 await json(path.join(out,'result.json'),result);console.log(JSON.stringify(Object.fromEntries(['baseline','matchedMatrices','restoredMatrices','matchedOrder'].map(k=>[k,result[k].map(r=>r.rawDifferences)]))));
}catch(e){await json(path.join(out,'failure.json'),{error:e.message,stack:e.stack});throw e;}finally{clearTimeout(timer);await browser?.close();server?.close();}
