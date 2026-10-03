import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
const root=path.resolve('out');
async function walk(dir){const list=await fs.readdir(dir,{withFileTypes:true});const groups=await Promise.all(list.map(e=>e.isDirectory()?walk(path.join(dir,e.name)):[path.join(dir,e.name)]));return groups.flat();}
const files=(await walk(root)).filter(f=>!f.endsWith('sw.js') && /\.(html|js|css|svg|png|webp|webmanifest|txt|json|woff2?)$/.test(f));
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
if(config.releaseApproved&&config.siteUrl){const routes=precache.filter(u=>u.endsWith('/')&&!u.includes('_next')&&!u.includes('_not-found')&&!u.includes('/offline/'));await fs.writeFile(path.join(root,'sitemap.xml'),'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+routes.map(u=>'<url><loc>'+new URL(u,config.siteUrl).href+'</loc></url>').join('')+'</urlset>');await fs.writeFile(path.join(root,'robots.txt'),'User-agent: *\nAllow: /\nSitemap: '+new URL('/sitemap.xml',config.siteUrl).href+'\n');}
console.log('PWA: '+precache.length+' arquivos públicos disponíveis offline. Versão '+version);
