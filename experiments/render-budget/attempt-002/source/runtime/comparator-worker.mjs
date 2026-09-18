// Separately invoked FSL comparator API. No comparator implementation is copied here.
import fs from 'node:fs/promises';
import path from 'node:path';
import {runRecipeSearch} from '@spatialpack/core/recipe-search';
import {ROOT,json} from './common.mjs';
const model=process.argv[2],dir=path.join(ROOT,'generated',model,'spatialpack');await fs.mkdir(dir,{recursive:true});
let serial=0,pending;const grids=[];
process.on('message',m=>{if(m.type==='gate-result'&&pending){const p=pending;pending=null;p(m.result);}});
for(const preset of ['web-mobile','web-desktop','quality-max']){
 const report=await runRecipeSearch({inputPath:path.join(ROOT,'generated',model,'original.glb'),outPath:path.join(dir,preset+'-internal-winner.glb'),preset,allowKtx2:true,searchDecimate:false,searchStrategy:'grid',maxRecipes:256,dryRun:true,recipeOrdering:grid=>{const chosen=grid.filter(r=>r.meshopt===false&&!r.decimate);grids.push({preset,original:grid.length,retained:chosen.length,recipes:chosen});return chosen;},qualityGate:async ({afterPath,recipe})=>{
  if(serial>=256){process.send({type:'cap'});throw Error('Combined recipe cap exceeded');}
  const dest=path.join(dir,preset+'-'+(serial++)+'-'+recipe.id+'.glb');await fs.copyFile(afterPath,dest);
  const result=await new Promise(resolve=>{pending=resolve;process.send({type:'gate',path:path.relative(ROOT,dest),recipe,preset});});return result;
 }});
 await json(path.join(ROOT,'execution-attempt-002',model+'-spatialpack-'+preset+'.json'),report);
 if(report.recipes.some(r=>r.status==='errored'))process.send({type:'incomplete',preset,reason:'Actual comparator recipe error'});
}
await json(path.join(ROOT,'execution-attempt-002',model+'-spatialpack-grids.json'),grids);
process.send({type:'done'});process.disconnect();
