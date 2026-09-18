import {spawn} from 'node:child_process';
import readline from 'node:readline';
import path from 'node:path';
import {ROOT} from './common.mjs';
export function solverClient(){
 const p=spawn(path.join(ROOT,'venv/bin/python'),[path.join(ROOT,'solve.py'),'--jsonl'],{stdio:['pipe','pipe','pipe']});let pending=null,stderr='';
 const lines=readline.createInterface({input:p.stdout});p.stderr.on('data',b=>stderr+=b);
 lines.on('line',line=>{if(!pending)return;const {resolve,reject,timer}=pending;pending=null;clearTimeout(timer);try{const r=JSON.parse(line);if(Object.hasOwn(r,'error')||r.exception)reject(Error(r.exception+': '+r.error));else if(!['OPTIMAL','FEASIBLE','INFEASIBLE','UNKNOWN'].includes(r.status))reject(Error('Unexpected solver status/schema'));else resolve(r);}catch(e){reject(e);}});
 p.on('exit',code=>{if(pending){clearTimeout(pending.timer);pending.reject(Error('Allocator exit '+code+' '+stderr));pending=null;}});
 return {request:data=>new Promise((resolve,reject)=>{if(pending)throw Error('Concurrent allocator request');const timer=setTimeout(()=>{p.kill('SIGKILL');reject(Error('Allocator 15s request timeout'));pending=null;},15000);pending={resolve,reject,timer};p.stdin.write(JSON.stringify(data)+'\n');}),close:()=>{p.stdin.end();}};
}
