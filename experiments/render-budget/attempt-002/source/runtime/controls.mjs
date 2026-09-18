import fs from 'node:fs/promises';
import path from 'node:path';
import sharp from 'sharp';
import {ROOT,json,sha} from './common.mjs';
import {encodeOption,setEncodingDeadline} from './encoding.mjs';
export async function makeControls(){setEncodingDeadline(Date.now()+10*60000);
 const dir=path.join(ROOT,'generated','controls-attempt-002');await fs.mkdir(dir,{recursive:true});const cases=[];
 for(const kind of ['color','data','normal']){
  const raw=Buffer.alloc(64*64*4),colors=kind==='normal'?[[218,128,218,255],[128,218,218,255],[38,128,218,255],[128,38,218,255]]:[[220,30,60,255],[20,180,70,255],[40,70,210,255],[140,90,40,64]];
  for(let y=0;y<64;y++)for(let x=0;x<64;x++){const c=colors[(y>=32?2:0)+(x>=32?1:0)];for(let k=0;k<4;k++)raw[(y*64+x)*4+k]=c[k];}
  const source=path.join(dir,kind+'.png');await sharp(raw,{raw:{width:64,height:64,channels:4}}).png().toFile(source);const buffer=await fs.readFile(source);
  for(const codec of ['webp','etc1s','uastc']){
   const outfile=path.join(dir,kind+'-'+codec+(codec==='webp'?'.webp':'.ktx2'));
   const result=await encodeOption({buffer,width:32,height:32,normal:kind==='normal',color:kind==='color',codec,outfile});
   cases.push({kind,codec,source:path.relative(ROOT,source),candidate:path.relative(ROOT,outfile),sha256:sha(result.encoded),metadata:result.metadata});
  }
 }
 await fs.writeFile(path.join(dir,'invalid.ktx2'),'This is deliberately not KTX');
 await json(path.join(ROOT,'execution-attempt-002','control-inputs.json'),cases);return cases;
}
