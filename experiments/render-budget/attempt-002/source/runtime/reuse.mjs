import fs from 'node:fs/promises';
import path from 'node:path';
import {ROOT,sha,readJSON} from './common.mjs';
export async function reusePrepared(spec){
 const verified=[];
 for(const entry of spec.files){const b=await fs.readFile(path.join(ROOT,entry.path));if(b.length!==entry.bytes||sha(b)!==entry.sha256)throw Error('Retained attempt001 input hash mismatch: '+entry.path);verified.push({path:entry.path,bytes:b.length,sha256:entry.sha256});}
 const prepared=await readJSON(path.join(ROOT,spec.preparedPath));
 if(prepared.seconds!==spec.encodingSeconds)throw Error('Original preprocessing charge differs from pinned record');
 if(prepared.models.reduce((s,m)=>s+m.images.reduce((n,i)=>n+i.options.filter(o=>o.codec!=='original').length,0),0)!==279)throw Error('Reused finite option count differs');
 return {prepared,verified,encodingSeconds:prepared.seconds};
}
