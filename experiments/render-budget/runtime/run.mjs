import fs from 'node:fs/promises';
import path from 'node:path';
import http from 'node:http';
import {spawn,fork} from 'node:child_process';
import {chromium} from 'playwright';
import {ROOT,MODELS,BUDGETS,io,packed,key,sha,json,readJSON,log,max} from './common.mjs';
import {fingerprint,parseGLB,verifyBindings} from './integrity.mjs';
import {makeControls} from './controls.mjs';
import {byteBound,assertByteBound} from './byte-bound.mjs';
import {runSearches} from './search.mjs';
const freeze=process.argv[2];if(!/^[a-f0-9]{7,40}$/.test(freeze??''))throw Error('A published freeze commit is required as first argument. Do not execute before parent freezes.');
await fs.mkdir(path.join(ROOT,'execution'),{recursive:true});
const began=Date.now();let browser,server;const children=new Set();
function killChild(p){try{process.kill(-p.pid,'SIGKILL');}catch{try{p.kill('SIGKILL');}catch{}}}
async function cleanup(){children.forEach(killChild);await browser?.close().catch(()=>{});server?.close();}
const hard=setTimeout(async()=>{await log({stage:'global-cap',seconds:(Date.now()-began)/1000});await cleanup();process.exit(124);},3*3600000);
function timeout(p,ms,label){let t;return Promise.race([p,new Promise((_,reject)=>{t=setTimeout(()=>reject(Error(label+' timeout')),ms);})]).finally(()=>clearTimeout(t));}
async function command(file,args,ms){await new Promise((resolve,reject)=>{const child=spawn(file,args,{stdio:'inherit',detached:true}),t=setTimeout(()=>killChild(child),ms);children.add(child);child.on('exit',code=>{children.delete(child);clearTimeout(t);code===0?resolve():reject(Error(file+' exit '+code));});child.on('error',error=>{children.delete(child);clearTimeout(t);reject(error);});});}
async function startServer(){server=http.createServer(async(req,res)=>{try{const pathname=decodeURIComponent(new URL(req.url,'http://localhost').pathname),p=path.resolve(ROOT,'.'+pathname);if(!p.startsWith(ROOT+path.sep))throw Error('Invalid path');const b=await fs.readFile(p);const ext=path.extname(p);res.setHeader('Content-Type',({'.mjs':'text/javascript','.js':'text/javascript','.html':'text/html','.json':'application/json','.gltf':'model/gltf+json','.glb':'model/gltf-binary','.wasm':'application/wasm','.png':'image/png','.webp':'image/webp','.ktx2':'image/ktx2'})[ext]??'application/octet-stream');res.end(b);}catch{res.statusCode=404;res.end('Not found');}});await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));return 'http://127.0.0.1:'+server.address().port;}
function rank(rows){return rows.filter(Boolean).sort((a,b)=>a.loss-b.loss||a.bytes-b.bytes||(a.artifact??key(a.vector)).localeCompare(b.artifact??key(b.vector)))[0]??null;}
async function checkFile(bytes,model,vector){verifyBindings(bytes,model,vector);const f=await fingerprint(bytes);if(f.sha256!==model.integrity.sha256)throw Error('Geometry/material/node invariant differs');const {raw}=parseGLB(bytes);if(raw.images.some(i=>!Number.isInteger(i.bufferView)))throw Error('External/missing image');for(const t of raw.textures){if(t.extensions?.KHR_texture_basisu&&!raw.extensionsRequired?.includes('KHR_texture_basisu'))throw Error('BasisU fallback missing');if(t.extensions?.EXT_texture_webp&&!raw.extensionsRequired?.includes('EXT_texture_webp'))throw Error('WebP fallback missing');}return f.sha256;}
try{
 await log({stage:'begin',freeze,node:process.version,argv:process.argv});
 const cases=await makeControls();const url=await startServer();
 browser=await chromium.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:true,args:['--disable-background-timer-throttling']});
 const page=await browser.newPage();page.on('pageerror',e=>log({stage:'browser-error',error:e.message}));await page.goto(url+'/runtime/render.html');await page.waitForFunction(()=>window.pipelineReady);
 const controls=await timeout(page.evaluate(c=>window.textureControls(c),cases),120000,'tiny texture controls');await json(path.join(ROOT,'execution','controls.json'),{freeze,browser:browser.version(),controls});
 await command(process.execPath,[path.join(ROOT,'runtime/prepare.mjs')],40*60000);
 const models=(await readJSON(path.join(ROOT,'execution','prepared.json'))).models,cells=[];
 for(const model of models){
  const setup=await timeout(page.evaluate(m=>window.setup(m),model),120000,'original setup');await json(path.join(ROOT,'execution',model.name+'-setup.json'),setup);
  if([...setup.repeat,...setup.roundtrip].some(r=>r.rawDifferences!==0))throw Error('Original roundtrip or repeat render mismatch: '+model.name);
  const doc=await io.read(path.join(ROOT,model.sourcePath)),sizes=new Map(),evaluations=new Map();
  const size=async v=>{const k=key(v);if(!sizes.has(k)){const b=await packed(doc,model,v);assertByteBound(b,model,v,bound);sizes.set(k,b.length);}return sizes.get(k);};
  const evaluate=async(v,method)=>{
   const k=key(v),cache= evaluations.get(k);if(cache){await log({stage:'configuration',model:model.name,method,cached:true,...cache});return cache;}
   const t=Date.now(),r=await timeout(page.evaluate(x=>window.evaluateVector(x),v),30000,'six-view configuration');const errors=r.views.map(x=>x.mae);
   if(errors.some(x=>!Number.isFinite(x)||x<0||x>1))throw Error('Invalid error metric');
   const result={vector:v.slice(),bytes:await size(v),errors,loss:max(errors),seconds:(Date.now()-t)/1000,formats:r.formats,memory:r.memory,hashes:r.hashes};evaluations.set(k,result);await log({stage:'configuration',model:model.name,method,cached:false,...result});return result;
  };
  const bound=await byteBound(model,v=>packed(doc,model,v));await json(path.join(ROOT,'execution',model.name+'-byte-bound.json'),bound);
  const spatial=[];let comparatorFailure=null,comparatorCalls=0;
  const worker=fork(path.join(ROOT,'runtime/comparator-worker.mjs'),[model.name],{env:{...process.env,PATH:path.join(ROOT,'tools/bin')+path.delimiter+process.env.PATH,TOKTX_OPTIONS:''},stdio:['ignore','inherit','inherit','ipc'],detached:true});children.add(worker);
  const comparatorStart=Date.now(),gateTasks=new Set();
  await new Promise(resolve=>{let finished=false;const timer=setTimeout(()=>{comparatorFailure='15-minute comparator cap';killChild(worker);},900000);worker.on('message',m=>{const task=(async()=>{
   if(m.type==='cap'){comparatorFailure='Combined comparator cap';killChild(worker);}
   if(m.type==='incomplete')comparatorFailure=m.reason+' '+m.preset;
   if(m.type==='done'){finished=true;clearTimeout(timer);resolve();}
   if(m.type==='gate'){let result;try{if(++comparatorCalls>256)throw Error('Combined comparator render cap');const bytes=await fs.readFile(path.join(ROOT,m.path));await checkFile(bytes,model);if(bytes.length>Math.max(...BUDGETS)){result={pass:false,meanAbsoluteError:1,error:'Over all declared byte ceilings'};spatial.push({artifact:m.path,bytes:bytes.length,recipe:m.recipe,preset:m.preset,rejected:result.error});}
    else{const r=await timeout(page.evaluate(url=>window.evaluateFile({url}),'/'+m.path),30000,'comparator render');const errors=r.views.map(v=>v.mae);const row={artifact:m.path,bytes:bytes.length,sha256:sha(bytes),errors,loss:max(errors),recipe:m.recipe,preset:m.preset};spatial.push(row);await log({stage:'spatialpack-configuration',model:model.name,...row});result={pass:true,meanAbsoluteError:row.loss};}
   }catch(e){result={pass:false,meanAbsoluteError:1,error:e.message};comparatorFailure=e.message;spatial.push({artifact:m.path,error:e.message});}if(worker.connected)worker.send({type:'gate-result',result});}
  })().catch(e=>{comparatorFailure=e.message;killChild(worker);}).finally(()=>gateTasks.delete(task));gateTasks.add(task);});worker.on('exit',code=>{children.delete(worker);clearTimeout(timer);if(!finished){comparatorFailure??='Comparator exit '+code;Promise.allSettled([...gateTasks]).then(resolve);}});worker.on('error',e=>{children.delete(worker);comparatorFailure=e.message;clearTimeout(timer);resolve();});});
  const comparatorSeconds=(Date.now()-comparatorStart)/1000;
  if(comparatorSeconds>=900)comparatorFailure??='Comparator final elapsed exceeds 15-minute cap';
  await json(path.join(ROOT,'execution',model.name+'-spatialpack-frontier.json'),{rows:spatial,failure:comparatorFailure,seconds:comparatorSeconds});
  if(comparatorFailure)throw Error('Required comparator incomplete: '+comparatorFailure);
  for(const budget of BUDGETS){
   const results=await runSearches(model,budget,evaluate,size,bound),cell={model:model.name,budget,...results,comparatorFailure};
   cell.spatialpack={winner:rank(spatial.filter(r=>r.loss!==undefined&&r.bytes<=budget)),calls:spatial.filter(r=>r.loss!==undefined).length,seconds:comparatorSeconds};
   if(!results.infeasible){
    for(const method of ['preset','texture','greedy','cpsat']){const w=cell[method]?.winner;if(!w)continue;const bytes=await packed(doc,model,w.vector);await checkFile(bytes,model,w.vector);if(bytes.length>budget)throw Error('Final byte ceiling exceeded');const artifact=path.join('generated',model.name,`${budget}-${method}.glb`);await fs.writeFile(path.join(ROOT,artifact),bytes);Object.assign(w,{artifact,sha256:sha(bytes)});
     const actual=await timeout(page.evaluate(url=>window.evaluateFile({url}),'/'+artifact),30000,'serialized final training check');const errors=actual.views.map(v=>v.mae),difference=max(errors.map((x,i)=>Math.abs(x-w.errors[i])));await log({stage:'serialized-training-control',model:model.name,budget,method,difference,errors});if(difference>1e-9||JSON.stringify(actual.hashes)!==JSON.stringify(w.hashes))throw Error('Cached texture substitution differs from real exported GLB pixels');
    }
   }
   cells.push(cell);await json(path.join(ROOT,'execution','selection-progress.json'),{freeze,cells});
  }
 }
 const seal={freeze,sealedAt:new Date().toISOString(),cells};await json(path.join(ROOT,'execution','selection-seal.json'),seal);const sealHash=sha(await fs.readFile(path.join(ROOT,'execution','selection-seal.json')));await log({stage:'seal',sha256:sealHash});
 // First held-out access happens only after all methods and all assets are sealed above.
 const outputs=[];
 for(const model of models){await timeout(page.evaluate(m=>window.setup(m),model),120000,'heldout setup');for(const cell of cells.filter(c=>c.model===model.name&&!c.infeasible))for(const method of ['preset','texture','greedy','cpsat','spatialpack']){
  const w=cell[method]?.winner;if(!w)continue;const bytes=await fs.readFile(path.join(ROOT,w.artifact));if(sha(bytes)!==w.sha256)throw Error('Sealed artifact changed');const r=await timeout(page.evaluate(url=>window.evaluateFile({url,heldout:true,saveImage:true}),'/'+w.artifact),120000,'heldout render');if(r.worstImage){const img=path.join(ROOT,'execution',`${model.name}-${cell.budget}-${method}-worst.png`);await fs.writeFile(img,Buffer.from(r.worstImage.split(',')[1],'base64'));delete r.worstImage;}outputs.push({model:model.name,budget:cell.budget,method,artifact:w.artifact,bytes:w.bytes,sha256:w.sha256,maximum:max(r.views.map(v=>v.mae)),mean:r.views.reduce((s,v)=>s+v.mae,0)/r.views.length,...r});await json(path.join(ROOT,'execution','heldout-progress.json'),{sealHash,outputs});
 }}
 const decisions=cells.map(c=>{if(c.infeasible)return {model:c.model,budget:c.budget,infeasible:true};const rows=outputs.filter(r=>r.model===c.model&&r.budget===c.budget),candidate=rows.find(r=>r.method==='cpsat'),baselines=rows.filter(r=>r.method!=='cpsat').sort((a,b)=>a.maximum-b.maximum),baseline=baselines[0],censored=c.preset?.censored||c.texture?.censored||c.greedy?.censored||c.cpsat?.censored,complete=rows.length===5&&!c.comparatorFailure&&!censored;return {model:c.model,budget:c.budget,complete,censored,baseline:baseline?.method,candidate:candidate?.maximum,bestBaseline:baseline?.maximum,win:!!(complete&&candidate&&baseline&&baseline.maximum-candidate.maximum>=.001&&candidate.maximum<=.85*baseline.maximum),regression:!!(candidate&&baseline&&candidate.maximum>1.10*baseline.maximum)};});
 const pass=decisions.filter(d=>!d.infeasible).every(d=>d.complete&&!d.regression)&&new Set(decisions.filter(d=>d.win).map(d=>d.model)).size>=2;
 const finalElapsed=Date.now()-began;if(finalElapsed>=3*3600000)throw Error('Whole-run final elapsed exceeds three-hour cap');
 await json(path.join(ROOT,'execution','summary.json'),{freeze,sealHash,seconds:finalElapsed/1000,withinWholeRunCap:true,decisions,technicalSupport:pass,scope:'Four authored public product assets, one pinned renderer, numerical fidelity; not customer or human quality validation'});
 if(Date.now()-began>=3*3600000){await json(path.join(ROOT,'execution','summary.json'),{freeze,sealHash,seconds:(Date.now()-began)/1000,withinWholeRunCap:false,censored:true,technicalSupport:false,decisions});throw Error('Whole-run cap crossed during finalization');}
}catch(e){await json(path.join(ROOT,'execution','failure.json'),{freeze,error:e.message,stack:e.stack,seconds:(Date.now()-began)/1000});throw e;}finally{clearTimeout(hard);await cleanup();}
