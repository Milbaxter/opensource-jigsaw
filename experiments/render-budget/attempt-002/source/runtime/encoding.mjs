import fs from 'node:fs/promises';
import path from 'node:path';
import {spawnSync} from 'node:child_process';
import sharp from 'sharp';
import {read as readKTX} from 'ktx-parse';
import {ROOT,log} from './common.mjs';
let deadline=Infinity;
export function setEncodingDeadline(value){deadline=value;}
function remaining(){const ms=deadline-Date.now();if(ms<=0)throw Error('Encoding absolute deadline');return Math.min(120000,ms);}
const bin=n=>path.join(ROOT,'tools','bin',n);
export async function command(argv) {
  const before=Date.now(); const r=spawnSync(argv[0],argv.slice(1),{encoding:'utf8',timeout:remaining(),env:{...process.env,TOKTX_OPTIONS:''}});
  await log({stage:'encode-command',argv,status:r.status,error:r.error?.message,stdout:r.stdout,stderr:r.stderr,seconds:(Date.now()-before)/1000});
  remaining();
  if(r.status!==0) throw Error('Command failed: '+argv.join(' '));
}
export async function normalizedPNG(buffer,w,h,normal) {
  let b=await sharp(buffer).resize(w,h,{kernel:'lanczos3',fit:'fill'}).ensureAlpha().raw().toBuffer();
  if(normal) for(let p=0;p<b.length;p+=4) {
    let x=b[p]/127.5-1,y=b[p+1]/127.5-1,z=b[p+2]/127.5-1;
    const n=Math.hypot(x,y,z); if(n>1e-12){x/=n;y/=n;z/=n;}else{x=0;y=0;z=1;}
    b[p]=Math.round((x+1)*127.5);b[p+1]=Math.round((y+1)*127.5);b[p+2]=Math.round((z+1)*127.5);
  }
  return sharp(b,{raw:{width:w,height:h,channels:4}}).png().toBuffer();
}

export function checkKTX(encoded,color) {
 const c=readKTX(new Uint8Array(encoded)),d=c.dataFormatDescriptor[0];
 const text=v=>typeof v==='string'?v:Buffer.from(v??[]).toString().replace(/\0+$/,'');
 const orientation=text(c.keyValue.KTXorientation),swizzle=text(c.keyValue.KTXswizzle);
 if(c.pixelWidth%4||c.pixelHeight%4||c.pixelDepth||c.layerCount||c.faceCount!==1||!c.levels.length||c.vkFormat!==0)throw Error('KTX dimensions/container mismatch');
 if((orientation&&orientation!=='rd')||(swizzle&&swizzle!=='rgba')||d.colorPrimaries!==(color?1:0)||d.transferFunction!==(color?2:1)||(d.flags&1))throw Error('KTX color/orientation/alpha metadata mismatch');
 return {width:c.pixelWidth,height:c.pixelHeight,levels:c.levels.length,orientation,swizzle,descriptor:d};
}
export async function encodeOption({buffer,width,height,normal,color,codec,outfile}) {
 remaining();
 const png=await normalizedPNG(buffer,width,height,normal),tmp=outfile+'.input.png';await fs.writeFile(tmp,png);let decoded,metadata=null;
 if(codec==='webp'){await sharp(png).webp({quality:80}).toFile(outfile);decoded=await fs.readFile(outfile);}
 else {
  const args=[bin('toktx'),'--t2','--encode',codec==='etc1s'?'etc1s':'uastc','--genmipmap','--assign_oetf',color?'srgb':'linear','--assign_primaries',color?'bt709':'none','--upper_left_maps_to_s0t0'];
  if(normal)args.push('--normalize');
  if(codec==='etc1s')args.push('--qlevel','128','--clevel','1');else args.push('--uastc_quality','1','--zcmp','18');
  args.push(outfile,tmp);await command(args);await command([bin('ktx'),'validate',outfile]);
  metadata=checkKTX(await fs.readFile(outfile),color);
  const dec=outfile+'.decoded.png';await command([bin('ktx'),'extract','--transcode','rgba8','--level','0',outfile,dec]);decoded=await fs.readFile(dec);
 }
 remaining();
 return {encoded:await fs.readFile(outfile),decoded,metadata};
}
