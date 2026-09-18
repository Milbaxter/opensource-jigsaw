// SPDX-License-Identifier: MIT
// Static image decoding only; no NodeIO, canvas, browser, encoding or search.
import fs from 'node:fs/promises';import crypto from 'node:crypto';import path from 'node:path';
import {createRequire} from 'node:module';
const require=createRequire(new URL('../../round9-render-budget/runtime/package.json',import.meta.url));const sharp=require('sharp');
const root=path.resolve('work/round9-render-budget'),out=path.resolve('work/texture-independent-review/roundtrip-diagnosis');
const h=b=>crypto.createHash('sha256').update(b).digest('hex'),s=JSON.parse(await fs.readFile(root+'/inputs/FlightHelmet/glTF/FlightHelmet.gltf','utf8')),g=await fs.readFile(root+'/generated/FlightHelmet/original.glb');
let pos=12,raw,bin;while(pos<g.length){const n=g.readUInt32LE(pos),t=g.readUInt32LE(pos+4);if(t===0x4e4f534a)raw=JSON.parse(g.subarray(pos+8,pos+8+n));if(t===0x004e4942)bin=g.subarray(pos+8,pos+8+n);pos+=8+n;}
const rows=[];for(let i=0;i<s.images.length;i++){const sb=await fs.readFile(root+'/inputs/FlightHelmet/glTF/'+s.images[i].uri),bv=raw.bufferViews[raw.images[i].bufferView],gb=bin.subarray(bv.byteOffset??0,(bv.byteOffset??0)+bv.byteLength);const a=await sharp(sb).ensureAlpha().raw().toBuffer({resolveWithObject:true}),b=await sharp(gb).ensureAlpha().raw().toBuffer({resolveWithObject:true});rows.push({index:i,source:s.images[i].uri,sourceInfo:a.info,glbInfo:b.info,sourcePixelSHA256:h(a.data),glbPixelSHA256:h(b.data),exactDecodedPixels:a.data.equals(b.data)});}
await fs.writeFile(out+'/DECODED-IMAGE-DIFF.json',JSON.stringify({scope:'Sharp CPU decoding only, not browser ImageBitmap decoding or shader evaluation.',sharpVersions:sharp.versions,rows},null,2)+'\n');console.log(JSON.stringify({images:rows.length,allExact:rows.every(x=>x.exactDecodedPixels)}));
