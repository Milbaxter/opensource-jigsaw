import {io,sha} from './common.mjs';
export function parseGLB(bytes) {
 const b=Buffer.from(bytes);if(b.readUInt32LE(0)!==0x46546c67||b.readUInt32LE(4)!==2||b.readUInt32LE(8)!==b.length)throw Error('Invalid GLB');
 let p=12,raw,bin;while(p<b.length){const n=b.readUInt32LE(p),t=b.readUInt32LE(p+4);if(p+8+n>b.length)throw Error('Invalid chunk');if(t===0x4e4f534a)raw=JSON.parse(b.subarray(p+8,p+8+n).toString());if(t===0x004e4942)bin=b.subarray(p+8,p+8+n);p+=8+n;}return {raw,bin};
}
export function imageIdentity(bytes,sourceHashes) {
 const {raw,bin}=parseGLB(bytes);
 const images=raw.images.map(im=>{const bv=raw.bufferViews[im.bufferView];const h=sha(bin.subarray(bv.byteOffset??0,(bv.byteOffset??0)+bv.byteLength));const matches=sourceHashes.flatMap((x,i)=>x===h?[i]:[]);if(matches.length!==1)throw Error('Ambiguous original image identity '+h);return matches[0];});
 return raw.textures.map(t=>images[t.source]);
}
const stable=x=>JSON.stringify(x,(_,v)=>v&&typeof v==='object'&&!Array.isArray(v)?Object.fromEntries(Object.entries(v).sort(([a],[b])=>a.localeCompare(b))):v);
export async function fingerprint(bytes) {
 const doc=await io.readBinary(new Uint8Array(bytes)),{json:raw}=await io.writeJSON(doc);
 const access=doc.getRoot().listAccessors().map(a=>({type:a.getType(),normalized:a.getNormalized(),componentType:a.getComponentType(),count:a.getCount(),sha256:sha(Buffer.from(a.getArray().buffer,a.getArray().byteOffset,a.getArray().byteLength))}));
 function material(m) {if(m===undefined)return null;const source=raw.materials[m];function visit(x){if(Array.isArray(x))return x.map(visit);if(!x||typeof x!=='object')return x;const out={};for(const [k,v]of Object.entries(x)){if(['name','extras'].includes(k))continue;if(k==='index'&&Number.isInteger(v)){const t=raw.textures[v];out.sampler=raw.samplers?.[t.sampler]??{};const im=raw.images[t.source??t.extensions?.KHR_texture_basisu?.source??t.extensions?.EXT_texture_webp?.source];out.imageIdentity=im.name;}else out[k]=visit(v);}return out;}return visit(source);}
 function primitive(p){return {...p,attributes:Object.fromEntries(Object.entries(p.attributes).map(([k,v])=>[k,access[v]])),indices:p.indices===undefined?null:access[p.indices],material:material(p.material),targets:p.targets?.map(t=>Object.fromEntries(Object.entries(t).map(([k,v])=>[k,access[v]])))};}
 function node(i){const n=raw.nodes[i];if(n.skin!==undefined)throw Error('Unsupported skinned node');return {camera:n.camera===undefined?null:raw.cameras[n.camera],matrix:n.matrix,rotation:n.rotation,translation:n.translation,scale:n.scale,weights:n.weights,extensions:n.extensions,mesh:n.mesh===undefined?null:{weights:raw.meshes[n.mesh].weights,primitives:raw.meshes[n.mesh].primitives.map(primitive)},children:(n.children??[]).map(node)};}
 if(raw.animations?.length)throw Error('Animated asset outside frozen scope');
 const semantic={scenes:raw.scenes.map(s=>(s.nodes??[]).map(node)),scene:raw.scene};
 return {sha256:sha(Buffer.from(stable(semantic))),semantic};
}

export function verifyBindings(bytes,model,vector){
 const {raw,bin}=parseGLB(bytes);
 for(const im of raw.images){const m=/^source-image-(\d+)$/.exec(im.name??'');if(!m)throw Error('Untracked source image name');const i=Number(m[1]);if(!model.images[i])throw Error('Unknown image identity');if(vector){const bv=raw.bufferViews[im.bufferView],actual=sha(bin.subarray(bv.byteOffset??0,(bv.byteOffset??0)+bv.byteLength));if(actual!==model.images[i].options[vector[i]].sha256)throw Error('Selected image payload identity mismatch');}}
}
