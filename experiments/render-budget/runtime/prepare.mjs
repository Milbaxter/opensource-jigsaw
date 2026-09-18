import fs from 'node:fs/promises';
import path from 'node:path';
import sharp from 'sharp';
import {ROOT,MODELS,io,json,readJSON,sha,roles,log} from './common.mjs';

import {encodeOption,setEncodingDeadline} from './encoding.mjs';
import {imageIdentity,fingerprint} from './integrity.mjs';
const t0=Date.now();setEncodingDeadline(t0+40*60000);
async function distortion(source,decoded,roleList,w,h) {
  const a=await sharp(source).ensureAlpha().raw().toBuffer();
  const b=await sharp(decoded).resize(w,h,{kernel:'lanczos3',fit:'fill'}).ensureAlpha().raw().toBuffer();
  let sum=0;
  for(const role of roleList) {
    let v=0;
    for(let k=0;k<a.length;k+=4) {
      if(role.role==='normal') {
        const n=x=>{const q=[x[k]/127.5-1,x[k+1]/127.5-1,x[k+2]/127.5-1];const d=Math.hypot(...q);return d>1e-12?q.map(t=>t/d):[0,0,1];};
        const x=n(a),y=n(b);v+=Math.acos(Math.max(-1,Math.min(1,x.reduce((z,t,i)=>z+t*y[i],0))))/Math.PI;
      }else v+=role.channels.reduce((z,c)=>z+Math.abs(a[k+c]-b[k+c])/255,0)/role.channels.length;
    }
    sum+=v/(a.length/4);
  }
  return sum/Math.max(1,roleList.length);
}
await fs.mkdir(path.join(ROOT,'execution'),{recursive:true});
const models=[];
for(const name of MODELS) {
  const src=path.join(ROOT,'inputs',name,'glTF',name+'.gltf');const raw=await readJSON(src);const rr=roles(raw);
  const doc=await io.read(src);doc.getRoot().listTextures().forEach((t,i)=>t.setName('source-image-'+i)); const original=await io.writeBinary(doc);
  const dir=path.join(ROOT,'generated',name);await fs.mkdir(dir,{recursive:true});await fs.writeFile(path.join(dir,'original.glb'),original);
  const images=[];
  for(let i=0;i<raw.images.length;i++) {
    if(Date.now()-t0>40*60000)throw Error('Encoding stage cap');
    const srcImage=path.join(path.dirname(src),raw.images[i].uri);const b=await fs.readFile(srcImage);const m=await sharp(b).metadata();
    if(!m.width||!m.height)throw Error('Missing image dimensions');
    const color=rr[i].some(r=>r.role==='color'),normal=rr[i].some(r=>r.role==='normal');
    const mixed=color&&rr[i].some(r=>r.role!=='color');
    const options=[{codec:'original',fraction:1,path:path.relative(ROOT,srcImage),mime:m.format==='jpeg'?'image/jpeg':'image/png',bytes:b.length,sha256:sha(b),distortion:0,width:m.width,height:m.height}];
    if(!mixed && rr[i].length) for(const codec of ['webp','etc1s','uastc']) for(const fraction of [1,.5,.25]) {
      const ktx=codec!=='webp';if(ktx&&(m.width<4||m.height<4))continue;
      const w=ktx?Math.max(4,Math.floor(m.width*fraction/4)*4):Math.max(1,Math.floor(m.width*fraction));
      const h=ktx?Math.max(4,Math.floor(m.height*fraction/4)*4):Math.max(1,Math.floor(m.height*fraction));
      const outfile=path.join(dir,`image-${i}-${codec}-${fraction}.`+(ktx?'ktx2':'webp'));
      const {encoded,decoded,metadata}=await encodeOption({buffer:b,width:w,height:h,normal,color,codec,outfile});
      const d=await distortion(b,decoded,rr[i],m.width,m.height);
      options.push({codec,fraction,path:path.relative(ROOT,outfile),mime:ktx?'image/ktx2':'image/webp',bytes:encoded.length,sha256:sha(encoded),distortion:d,width:w,height:h,metadata});
      await log({stage:'option',model:name,image:i,codec,fraction,bytes:encoded.length,distortion:d});
    }
    images.push({source:raw.images[i].uri,roles:rr[i],color,normal,mixed,options});
  }
  const sourceHashes=images.map(i=>i.options[0].sha256);
  doc.getRoot().listTextures().forEach((t,i)=>{if(sha(t.getImage())!==sourceHashes[i])throw Error('NodeIO original ordinal identity mismatch');});
  const model={name,images,textureIndexToImage:imageIdentity(original,sourceHashes),integrity:await fingerprint(original),originalBytes:original.length,originalSha256:sha(original),sourceJSON:raw,sourcePath:path.relative(ROOT,src)};
  await json(path.join(dir,'model.json'),model);models.push(model);
}
await json(path.join(ROOT,'execution','prepared.json'),{models,seconds:(Date.now()-t0)/1000});
