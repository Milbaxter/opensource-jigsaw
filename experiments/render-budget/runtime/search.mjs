import fs from 'node:fs/promises';
import path from 'node:path';
import {solverClient} from './solver-client.mjs';
import {ROOT,CAP,key,max,round4,presets,smallest,json,log} from './common.mjs';

const best = rows=>rows.filter(r=>r&&r.eligible!==false).sort((a,b)=>a.loss-b.loss||a.bytes-b.bytes||key(a.vector).localeCompare(key(b.vector)))[0]??null;
export async function runSearches(model,budget,evaluate,size,bound) {
  const start=smallest(model);const initialPresets=presets(model);
  const results={};
  const smallestSize=await size(start);
  if(bound.nonimage>budget) return {infeasible:true,reason:'This fixed writer family preserves more nonimage binary bytes than the ceiling; not a universal packing certificate',nonimageBytes:bound.nonimage};
  const presetStart=Date.now(),purePreset=[];
  const presetExpired=()=>Date.now()-presetStart>=900000;
  for(const v of initialPresets) {
    if(presetExpired())break;
    const bytes=await size(v);if(presetExpired())break;
    if(bytes<=budget)purePreset.push(await evaluate(v,'preset'));
    if(presetExpired())break;
  }
  results.preset={winner:best(purePreset),calls:purePreset.length,seconds:(Date.now()-presetStart)/1000,censored:presetExpired()};
  const textureStart=Date.now(),tex=start.slice();let steps=0;
  const textureExpired=()=>Date.now()-textureStart>=900000;
  textureLoop: while(steps++<1000) {
    if(textureExpired())break;
    let winner=null;
    for(let i=0;i<tex.length;i++) for(let o=0;o<model.images[i].options.length;o++) {
      if(textureExpired())break textureLoop;
      const old=model.images[i].options[tex[i]],next=model.images[i].options[o];
      const gain=old.distortion-next.distortion;if(gain<=0)continue;
      const v=tex.slice();v[i]=o;const bytes=await size(v);
      if(textureExpired())break textureLoop;
      if(bytes>budget)continue;
      const cost=next.bytes-old.bytes;const score=cost<=0?1e9+gain:gain/cost;
      if(!winner||score>winner.score)winner={v,score};
    }
    if(!winner)break;tex.splice(0,tex.length,...winner.v);
  }
  let textureWinner=null;
  if(!textureExpired()) {
    const bytes=await size(tex);
    if(!textureExpired()&&bytes<=budget)textureWinner=await evaluate(tex,'texture');
  }
  results.texture={winner:textureWinner,calls:textureWinner?1:0,seconds:(Date.now()-textureStart)/1000,censored:textureExpired()};

  async function context(method) {
    const began=Date.now(),seen=new Map();let censored=false;
    const isCensored=()=>{censored ||= Date.now()-began>=900000;return censored;};
    const get=async (v,calibration=false)=>{
      if(isCensored())return null;
      const k=key(v);if(seen.has(k))return seen.get(k);
      if(seen.size>=CAP)return null;
      const bytes=await size(v);if(isCensored())return null;
      if(!calibration&&bytes>budget)return null;
      const actual=await evaluate(v,method),r={...actual,eligible:actual.bytes<=budget};seen.set(k,r);isCensored();return r;
    };
    for(const v of initialPresets)await get(v);
    const base=await get(start,true);if(!base)throw Error('Missing feasible minimum');
    const domains=model.images.map((_,i)=>[start[i]]);
    const effects=model.images.map(im=>im.options.map(()=>null));
    for(let i=0;i<model.images.length;i++) {
      effects[i][start[i]]=Array(6).fill(0);
      for(let o=0;o<model.images[i].options.length;o++) if(o!==start[i]) {
        const v=start.slice();v[i]=o;
        const r=await get(v,true);if(!r)throw Error('Initial pool exceeds call/time cap');
        domains[i].push(o);effects[i][o]=r.errors.map((x,j)=>x-base.errors[j]);
      }
    }
    const predict=v=>max(base.errors.map((e,j)=>e+v.reduce((s,o,i)=>s+(effects[i][o]?.[j]??0),0)));
    return {get,seen,base,domains,effects,predict,began,isCensored};
  }
  {
    const c=await context('greedy');let current=best([...c.seen.values()]);
    while(current&&c.seen.size<CAP&&!c.isCensored()) {
      const proposals=[];
      neighborhood: for(let i=0;i<current.vector.length;i++) for(const o of c.domains[i]) if(o!==current.vector[i]) {
        if(c.isCensored())break neighborhood;
        const v=current.vector.slice();v[i]=o;const b=await size(v);
        if(c.isCensored())break neighborhood;
        if(b<=budget)proposals.push({v,b,p:c.predict(v)});
      }
      if(c.isCensored())break;
      proposals.sort((a,b)=>a.p-b.p||a.b-b.b||key(a.v).localeCompare(key(b.v)));
      let move=null,complete=true;
      for(const p of proposals) {
        const r=await c.get(p.v);if(!r){complete=false;break;}
        const gain=current.loss-r.loss,cost=r.bytes-current.bytes;if(gain<=0)continue;
        const score=cost<=0?1e9+gain:gain/cost;
        if(!move||score>move.score)move={r,score};
      }
      if(!complete||!move)break;current=move.r;
    }
    results.greedy={winner:best([...c.seen.values()]),calls:c.seen.size,seconds:(Date.now()-c.began)/1000,censored:c.isCensored()};
  }
  {
    const c=await context('cpsat');const impact=c.domains.map((ds,i)=>({i,value:Math.max(0,...ds.map(o=>c.base.loss-max(c.base.errors.map((v,k)=>v+c.effects[i][o][k]))))})).sort((a,b)=>b.value-a.value||a.i-b.i).slice(0,3);
    const selected=impact.map(({i})=>({i,options:c.domains[i].filter(o=>o!==start[i]).map(o=>{
      const gain=c.base.loss-max(c.base.errors.map((v,k)=>v+c.effects[i][o][k]));const cost=model.images[i].options[o].bytes-model.images[i].options[start[i]].bytes;
      return {o,gain,score:cost<=0?1e9+gain:gain/cost};
    }).filter(x=>x.gain>0).sort((a,b)=>b.score-a.score||model.images[i].options[a.o].bytes-model.images[i].options[b.o].bytes||a.o-b.o).slice(0,2).map(x=>x.o)}));
    const measuredPairs=[];
    for(let a=0;a<selected.length;a++)for(let b=a+1;b<selected.length;b++)for(const o of selected[a].options)for(const p of selected[b].options) {
      const i=selected[a].i,j=selected[b].i,v=start.slice();v[i]=o;v[j]=p;
      const r=await c.get(v,true);if(!r)break;
      measuredPairs.push({i,o,j,p,correction:r.errors.map((x,k)=>x-c.base.errors[k]-c.effects[i][o][k]-c.effects[j][p][k]),actual:r.errors,vector:v});
    }
    const costs=c.domains.map((ds,i)=>ds.map(o=>round4(model.images[i].options[o].bytes)));
    const overhead=bound.overhead;
    const toLocal=v=>v.map((o,i)=>c.domains[i].indexOf(o));
    const problem={costs,overhead,budget,e0:c.base.errors,delta:c.domains.map((ds,i)=>ds.map(o=>c.effects[i][o])),pairs:measuredPairs.map(p=>({...p,o:c.domains[p.i].indexOf(p.o),p:c.domains[p.j].indexOf(p.p)})),exclude:[...c.seen.values()].map(r=>toLocal(r.vector)).filter(v=>v.every(o=>o>=0))};
    await json(path.join(ROOT,'execution',`${model.name}-${budget}-surrogate.json`),{...problem,domains:c.domains,selected,measuredPairs,byteBound:bound});
    let iterations=0;const client=solverClient();
    try {
    while(c.seen.size<CAP&&!c.isCensored()&&Date.now()-c.began<900000) {
      const sol=await client.request(problem);await log({stage:'solver',model:model.name,budget,iteration:iterations++,...sol});
      if(!sol.vector)break;
      problem.exclude.push(sol.vector);
      const v=sol.vector.map((o,i)=>c.domains[i][o]);
      if(await size(v)>budget)throw Error('Conservative byte constraint violated by actual GLB');
      const r=await c.get(v);if(!r)break;
      await log({stage:'surrogate-check',model:model.name,budget,vector:v,predictedMax:sol.objective/1e6,actualMax:r.loss,absoluteError:Math.abs(sol.objective/1e6-r.loss)});
    }
    } finally {client.close();}
    results.cpsat={winner:best([...c.seen.values()]),calls:c.seen.size,seconds:(Date.now()-c.began)/1000,censored:c.isCensored()||Date.now()-c.began>=900000,pairProbes:measuredPairs.length,solverIterations:iterations,overhead};
  }
  return results;
}
