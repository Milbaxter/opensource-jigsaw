import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import crypto from 'node:crypto';
import {NodeIO} from '@gltf-transform/core';
import {ALL_EXTENSIONS, KHRTextureBasisu, EXTTextureWebP} from '@gltf-transform/extensions';
import {cloneDocument} from '@gltf-transform/functions';

export const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
export const MODELS = ['FlightHelmet','ToyCar','WaterBottle','BoomBox'];
export const BUDGETS = [1000000,2000000,5000000];
export const CAP = 256;
export const io = new NodeIO().registerExtensions(ALL_EXTENSIONS);
export const sha = b => crypto.createHash('sha256').update(b).digest('hex');
export const round4 = n => Math.ceil(n/4)*4;
export const key = a => a.join(',');
export const max = a => Math.max(...a);
export async function json(p, x) {await fs.mkdir(path.dirname(p),{recursive:true}); await fs.writeFile(p,JSON.stringify(x,null,2)+'\n');}
export async function readJSON(p) {return JSON.parse(await fs.readFile(p,'utf8'));}
export async function log(x) {await fs.appendFile(path.join(ROOT,'execution-attempt-002','events.jsonl'),JSON.stringify({time:new Date().toISOString(),...x})+'\n');}
export function roles(raw) {
  const result = raw.images.map(()=>[]);
  function add(t,role,channels) {if(t && Number.isInteger(t.index)) result[raw.textures[t.index].source].push({role,channels});}
  for(const m of raw.materials??[]) {
    const p=m.pbrMetallicRoughness??{};
    add(p.baseColorTexture,'color',m.alphaMode && m.alphaMode!=='OPAQUE'?[0,1,2,3]:[0,1,2]);
    add(p.metallicRoughnessTexture,'data',[1,2]); add(m.normalTexture,'normal',[0,1,2]);
    add(m.occlusionTexture,'data',[0]);add(m.emissiveTexture,'color',[0,1,2]);
    const e=m.extensions??{};
    add(e.KHR_materials_clearcoat?.clearcoatTexture,'data',[0]);
    add(e.KHR_materials_clearcoat?.clearcoatRoughnessTexture,'data',[1]);
    add(e.KHR_materials_clearcoat?.clearcoatNormalTexture,'normal',[0,1,2]);
    add(e.KHR_materials_transmission?.transmissionTexture,'data',[0]);
    add(e.KHR_materials_sheen?.sheenColorTexture,'color',[0,1,2]);
    add(e.KHR_materials_sheen?.sheenRoughnessTexture,'data',[3]);
  }
  return result.map(list=>[...new Set(list.map(r=>r.role))].map(role=>({role,channels:[...new Set(list.filter(r=>r.role===role).flatMap(r=>r.channels))].sort()})));
}
export async function packed(doc, model, vector) {
  const out=cloneDocument(doc); const textures=out.getRoot().listTextures();
  if(textures.length!==model.images.length) throw Error('Texture/image identity count mismatch');
  textures.forEach((t,i)=>{if(sha(t.getImage())!==model.images[i].options[0].sha256)throw Error('Original NodeIO image ordinal identity mismatch');});
  let ktx=false,webp=false;
  for(let i=0;i<vector.length;i++) {
    const o=model.images[i].options[vector[i]];
    const b=await fs.readFile(path.join(ROOT,o.path));
    textures[i].setName('source-image-'+i).setImage(new Uint8Array(b)).setMimeType(o.mime);
    ktx ||= o.mime==='image/ktx2';webp ||= o.mime==='image/webp';
  }
  if(ktx) out.createExtension(KHRTextureBasisu).setRequired(true);
  if(webp) out.createExtension(EXTTextureWebP).setRequired(true);
  return io.writeBinary(out);
}
export function smallest(model) {return model.images.map(i=>i.options.reduce((best,o,k)=>o.bytes<i.options[best].bytes?k:best,0));}
export function presets(model) {
  const list=[];
  const find=(i,f,r)=>{const k=i.options.findIndex(o=>o.codec===f&&o.fraction===r);return k<0?0:k;};
  for(const cr of [1,.5,.25]) for(const dr of [1,.5,.25]) list.push(model.images.map(i=>find(i,i.color?'etc1s':'uastc',i.color?cr:dr)));
  for(const f of ['etc1s','uastc','webp']) for(const r of [1,.5,.25]) list.push(model.images.map(i=>find(i,f,r)));
  for(const r of [1,.5,.25]) list.push(model.images.map(i=>i.normal?0:find(i,'webp',r)));
  list.push(model.images.map(()=>0));
  return [...new Map(list.map(v=>[key(v),v])).values()];
}
