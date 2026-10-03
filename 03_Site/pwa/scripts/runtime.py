from pathlib import Path
import shutil
R=Path(r'C:\Users\Fabio\Desktop\HS Eletronicos\03_Site\pwa')
(R/'docs/source-assets').mkdir(exist_ok=True)
shutil.copy2(r'C:\Users\Fabio\.codex\generated_images\01a0fdb7-de8f-7031-92c3-c9f7716fe0d9\exec-33e110cf-18cc-4635-8d4d-5d6303f32a6f.png',R/'docs/source-assets/logic-board.png')
files={
'scripts/assets.mjs':'''import fs from 'node:fs/promises';
import sharp from 'sharp';
await fs.mkdir('public/images',{recursive:true});await fs.mkdir('public/icons',{recursive:true});
await sharp('docs/source-assets/logic-board.png').resize({width:1000,withoutEnlargement:true}).webp({quality:83}).toFile('public/images/logic-board.webp');
const icon=await fs.readFile('public/favicon.svg');
for(const size of [192,512])await sharp(icon).resize(size,size).png().toFile(`public/icons/icon-${size}.png`);
await sharp(icon).resize(180,180).png().toFile('public/icons/apple-touch-icon.png');
const mask=Buffer.from(icon.toString().replace('rx="104"','rx="0"'));
await sharp(mask).resize(512,512).png().toFile('public/icons/icon-maskable.png');
console.log('Imagem otimizada e quatro ícones PNG gerados.');
''',
'scripts/build-sw.mjs':'''import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
const root=path.resolve('out');
async function walk(dir){const list=await fs.readdir(dir,{withFileTypes:true});const groups=await Promise.all(list.map(e=>e.isDirectory()?walk(path.join(dir,e.name)):[path.join(dir,e.name)]));return groups.flat();}
const files=(await walk(root)).filter(f=>!f.endsWith('sw.js') && /\\.(html|js|css|svg|png|webp|webmanifest|txt|json|woff2?)$/.test(f));
const digest=crypto.createHash('sha256');
for(const f of files.sort())digest.update(await fs.readFile(f));
const version=digest.digest('hex').slice(0,12);
const urls=files.map(f=>'/'+path.relative(root,f).split(path.sep).join('/')).map(u=>u.endsWith('/index.html')?u.slice(0,-10):u);
const precache=[...new Set(urls)];
const worker=`const CACHE='hs-eletronicos-${version}';
const PRECACHE=${JSON.stringify(precache)};
self.addEventListener('install',event=>{event.waitUntil(caches.open(CACHE).then(cache=>cache.addAll(PRECACHE)));});
self.addEventListener('activate',event=>{event.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(k=>k.startsWith('hs-eletronicos-')&&k!==CACHE).map(k=>caches.delete(k)))).then(()=>self.clients.claim()));});
self.addEventListener('message',event=>{if(event.data?.type==='SKIP_WAITING')self.skipWaiting();});
async function networkFirst(request, fallback){
 const cache=await caches.open(CACHE);const url=new URL(request.url);const key=url.pathname;
 try {const response=await fetch(request,{signal:AbortSignal.timeout(3500)});if(response.ok)await cache.put(key,response.clone());return response;}
 catch {return await cache.match(key)||await cache.match(fallback)||Response.error();}
}
self.addEventListener('fetch',event=>{
 const request=event.request;const url=new URL(request.url);
 if(request.method!=='GET'||url.origin!==self.location.origin||url.pathname==='/sw.js')return;
 if(request.mode==='navigate'){event.respondWith(networkFirst(request,'/offline/'));return;}
 if(url.pathname.endsWith('.txt')){event.respondWith(networkFirst(request,url.pathname));return;}
 event.respondWith(caches.open(CACHE).then(async cache=>{const hit=await cache.match(url.pathname);if(hit)return hit;return fetch(request);}));
});`;
await fs.writeFile(path.join(root,'sw.js'),worker);
await fs.writeFile('docs/precache-report.json',JSON.stringify({version,files:precache.length,bytes:(await Promise.all(files.map(f=>fs.stat(f)))).reduce((a,s)=>a+s.size,0),urls:precache},null,2));
const config=JSON.parse(await fs.readFile('lib/business.json','utf8'));
if(config.releaseApproved&&config.siteUrl){const routes=precache.filter(u=>u.endsWith('/')&&!u.includes('_next')&&!u.includes('_not-found')&&!u.includes('/offline/'));await fs.writeFile(path.join(root,'sitemap.xml'),'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+routes.map(u=>'<url><loc>'+new URL(u,config.siteUrl).href+'</loc></url>').join('')+'</urlset>');await fs.writeFile(path.join(root,'robots.txt'),'User-agent: *\\nAllow: /\\nSitemap: '+new URL('/sitemap.xml',config.siteUrl).href+'\\n');}
console.log('PWA: '+precache.length+' arquivos públicos disponíveis offline. Versão '+version);
''',
'scripts/serve.mjs':'''import http from 'node:http';import fs from 'node:fs/promises';import path from 'node:path';
const root=path.resolve('out');const port=Number(process.env.PORT||3000);
const mime={'.html':'text/html; charset=utf-8','.js':'application/javascript; charset=utf-8','.css':'text/css; charset=utf-8','.svg':'image/svg+xml','.png':'image/png','.webp':'image/webp','.txt':'text/plain; charset=utf-8','.webmanifest':'application/manifest+json','.json':'application/json','.xml':'application/xml'};
const server=http.createServer(async(req,res)=>{try{if(!['GET','HEAD'].includes(req.method)){res.writeHead(405);res.end();return;}const url=new URL(req.url,'http://localhost');const pathname=decodeURIComponent(url.pathname);let file=path.resolve(root,'.'+pathname);if(file!==root&&!file.startsWith(root+path.sep)){res.writeHead(403);res.end();return;}let status=200;try{const stat=await fs.stat(file);if(stat.isDirectory()){if(!pathname.endsWith('/')){res.writeHead(308,{Location:pathname+'/'+url.search});res.end();return;}file=path.join(file,'index.html');}}catch{if(!path.extname(file)){try{await fs.access(path.join(file,'index.html'));res.writeHead(308,{Location:pathname+'/'+url.search});res.end();return;}catch{}}file=path.join(root,'404.html');status=404;}const data=await fs.readFile(file);res.writeHead(status,{'Content-Type':mime[path.extname(file)]||'application/octet-stream','Cache-Control':file.endsWith('sw.js')?'no-cache, no-store, must-revalidate':'no-cache','X-Content-Type-Options':'nosniff','Service-Worker-Allowed':'/'});res.end(req.method==='HEAD'?undefined:data);}catch{res.writeHead(500);res.end('Erro ao carregar a página.');}});
server.listen(port,'127.0.0.1',()=>console.log('HS Eletrônicos: http://127.0.0.1:'+port));
''',
'scripts/check-release.mjs':'''import fs from 'node:fs/promises';import {normalizePhone} from '../lib/contact.mjs';
const b=JSON.parse(await fs.readFile('lib/business.json','utf8'));const issues=[];
if(!normalizePhone(b.whatsapp))issues.push('WhatsApp inválido.');
if(!b.siteUrl||!/^https:\\/\\//.test(b.siteUrl))issues.push('Definir o domínio HTTPS real em siteUrl.');
if(!b.releaseApproved)issues.push('Revisar conteúdo e privacidade com Hugo e marcar releaseApproved.');
if(issues.length){console.error('Publicação ainda pendente:\\n- '+issues.join('\\n- '));process.exitCode=1;}else{console.log('Configuração de publicação pronta. Execute build e testes antes do deploy.');}
''',
 'tests/contact.test.mjs':'''import test from 'node:test';import assert from 'node:assert/strict';import {normalizePhone,composeMessage,whatsappUrl} from '../lib/contact.mjs';
test('contato correto e rejeição de números incompletos',()=>{assert.equal(normalizePhone('+55 (31) 99113-7969'),'5531991137969');assert.equal(normalizePhone('123'),null);assert.equal(whatsappUrl(null,'oi'),null);});
test('mensagem preserva acentos e codifica texto sem injetar parâmetros',()=>{const msg=composeMessage({category:'iPhone',model:'13 & Pro',symptom:'Não carrega? text=outro #teste'});const url=new URL(whatsappUrl('5531991137969',msg));assert.equal(url.pathname,'/5531991137969');assert.equal(url.searchParams.get('text'),msg);assert.equal([...url.searchParams].length,1);assert.equal(url.hash,'');});
test('mensagem limpa controles e limita entradas',()=>{const msg=composeMessage({model:'A'.repeat(200),symptom:'linha\\nseguinte'});assert.ok(msg.includes('A'.repeat(80)));assert.ok(!msg.includes('A'.repeat(81)));assert.ok(msg.includes('linha seguinte'));});
'''
}
for p,s in files.items():(R/p).write_text(s,encoding='utf-8')
# Normalize package JSON BOM from PowerShell authoring.
p=R/'package.json';p.write_text(p.read_text(encoding='utf-8-sig'),encoding='utf-8')
print('Scripts de PWA, testes e assets preparados.')
