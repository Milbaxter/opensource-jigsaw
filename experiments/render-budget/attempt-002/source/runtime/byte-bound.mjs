import {parseGLB} from './integrity.mjs';
import {round4} from './common.mjs';
// Component-wise upper bound on this pinned writer's unchanged JSON schema.
// Every finite single option is serialized; field sets/counts are checked unchanged.
export async function byteBound(model,serialize){
 const original=await serialize(model.images.map(()=>0)),base=parseGLB(original),samples=[base.raw];
 for(let i=0;i<model.images.length;i++)for(let o=1;o<model.images[i].options.length;o++){const v=model.images.map(()=>0);v[i]=o;samples.push(parseGLB(await serialize(v)).raw);}
 const changing=['images','textures','bufferViews','buffers','extensionsUsed','extensionsRequired'];
 const invariant=r=>JSON.stringify(Object.fromEntries(Object.entries(r).filter(([k])=>!changing.includes(k))));
 for(const r of samples){if(invariant(r)!==invariant(base.raw))throw Error('Unexpected writer schema variation');for(const k of ['images','textures','bufferViews','buffers'])if(r[k].length!==base.raw[k].length)throw Error('Variable writer array topology');}
 const payloadOriginal=model.images.reduce((s,i)=>s+round4(i.options[0].bytes),0),nonimage=base.bin.length-payloadOriginal;
 if(nonimage<0)throw Error('Negative unchanged binary floor');
 const maxTotal=nonimage+model.images.reduce((s,i)=>s+Math.max(...i.options.map(o=>round4(o.bytes))),0),maxNumber=10**String(maxTotal).length-1;
 const template={...base.raw};let extra=0;
 for(const field of ['images','textures','bufferViews','buffers']){
  template[field]=base.raw[field].map((entry,i)=>{const options=samples.map(r=>structuredClone(r[field][i]));
   if(field==='bufferViews')for(const v of options){v.byteOffset=maxNumber;v.byteLength=maxNumber;}
   if(field==='buffers')for(const v of options)v.byteLength=maxNumber;
   return options.sort((a,b)=>Buffer.byteLength(JSON.stringify(b))-Buffer.byteLength(JSON.stringify(a)))[0];});
 }
 for(const field of ['extensionsUsed','extensionsRequired']){const union=[...new Set(samples.flatMap(r=>r[field]??[]))].sort();if(union.length)template[field]=union;}
 const jsonBound=Buffer.byteLength(JSON.stringify(template)),overhead=12+8+round4(jsonBound)+8+nonimage;
 return {overhead,nonimage,jsonBound,maxTotal,arrayCounts:Object.fromEntries(['images','textures','bufferViews','buffers'].map(k=>[k,base.raw[k].length])),schemaInvariant:invariant(base.raw),probeCount:samples.length,method:'Maximum independent image/texture entry lengths, union extension declarations, maximal numeric buffer/offset fields, unchanged remaining schema; GLB headers and four-byte padding'};
}

export function assertByteBound(bytes,model,vector,bound){
 const {raw,bin}=parseGLB(bytes),changing=['images','textures','bufferViews','buffers','extensionsUsed','extensionsRequired'];
 const invariant=JSON.stringify(Object.fromEntries(Object.entries(raw).filter(([k])=>!changing.includes(k))));
 if(invariant!==bound.schemaInvariant)throw Error('Byte-bound unchanged schema violated');
 for(const [k,n]of Object.entries(bound.arrayCounts))if(raw[k].length!==n)throw Error('Byte-bound topology violated');
 const payload=vector.reduce((s,o,i)=>s+round4(model.images[i].options[o].bytes),0);
 if(Buffer.byteLength(JSON.stringify(raw))>bound.jsonBound||bin.length-payload>bound.nonimage||bytes.length>bound.overhead+payload)throw Error('Serialized conservative size bound violated');
}
