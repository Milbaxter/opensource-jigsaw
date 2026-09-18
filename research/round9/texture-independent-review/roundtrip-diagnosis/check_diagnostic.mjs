// SPDX-License-Identifier: MIT
// Decode saved diagnostic images only. Does not invoke a browser or renderer.
import fs from 'node:fs/promises';import crypto from 'node:crypto';import {createRequire} from 'node:module';
const require=createRequire(new URL('../../round9-render-budget/runtime/package.json',import.meta.url));const sharp=require('sharp');
const root='work/round9-render-budget/diagnostics/roundtrip-001',out='work/texture-independent-review/roundtrip-diagnosis';const sha=b=>crypto.createHash('sha256').update(b).digest('hex');
const f=JSON.parse(await fs.readFile(root+'/diagnostic-source-freeze.json')),r=JSON.parse(await fs.readFile(root+'/result.json'));const sourceChecks=[];
for(const x of f.files){const actual=sha(await fs.readFile(root+'/'+x.path));if(actual!==x.sha256)throw Error('Diagnostic source mismatch');sourceChecks.push({...x,verified:true});}
const views=[];for(let i=0;i<6;i++){const a=await sharp(await fs.readFile(root+`/view-${i}-reference.png`)).ensureAlpha().raw().toBuffer(),b=await sharp(await fs.readFile(root+`/view-${i}-source.png`)).ensureAlpha().raw().toBuffer();let differences=0,max=0;for(let j=0;j<a.length;j++)if(a[j]!==b[j]){differences++;max=Math.max(max,Math.abs(a[j]-b[j]));}if(differences!==r.baseline[i].rawDifferences||max!==r.baseline[i].maxChannel)throw Error('Saved PNG differs from reported raw observation');views.push({view:i,differences,max,reportedMatch:true});}
const interventions=Object.fromEntries(['baseline','matchedMatrices','restoredMatrices','matchedOrder'].map(k=>[k,r[k].map(v=>v.rawDifferences)]));
await fs.writeFile(out+'/DIAGNOSTIC-VERIFICATION.json',JSON.stringify({sourceChecks,resultSHA256:sha(await fs.readFile(root+'/result.json')),views,interventions,scope:'Source hashes and saved baseline PNG counts independently verified; matchedOrder equality inspected in diagnostic results/code, not separately rendered by reviewer.'},null,2)+'\n');console.log(JSON.stringify({views,interventions}));
