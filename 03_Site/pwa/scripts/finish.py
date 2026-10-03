from pathlib import Path
import json
R=Path(r'C:\Users\Fabio\Desktop\HS Eletronicos\03_Site\pwa')
p=R/'app/globals.css';s=p.read_text(encoding='utf-8-sig').replace('color:#c8cfd5;font-weight:400','color:#657282;font-weight:400').replace('color:#75808d;font-weight:400','color:#5d6a79;font-weight:400');p.write_text(s,encoding='utf-8')
p=R/'components/pwa.tsx';s=p.read_text(encoding='utf-8');s=s.replace("type InstallEvent = Event & { prompt:()=>Promise<void>; userChoice:Promise<{outcome:string}> };","type InstallEvent = Event & { prompt:()=>Promise<void>; userChoice:Promise<{outcome:string}> };\nlet deferredInstall: InstallEvent | null = null;")
s=s.replace("useEffect(()=>{setOffline(!navigator.onLine);", "useEffect(()=>{const capture=(event:Event)=>{event.preventDefault();deferredInstall=event as InstallEvent;window.dispatchEvent(new Event('hs-install-ready'));};const clear=()=>{deferredInstall=null;};window.addEventListener('beforeinstallprompt',capture);window.addEventListener('appinstalled',clear);setOffline(!navigator.onLine);")
s=s.replace("return()=>{window.removeEventListener('online',on);window.removeEventListener('offline',on);};},[]);", "return()=>{window.removeEventListener('beforeinstallprompt',capture);window.removeEventListener('appinstalled',clear);window.removeEventListener('online',on);window.removeEventListener('offline',on);};},[]);")
s=s.replace("useEffect(()=>{const media=", "useEffect(()=>{setPrompt(deferredInstall);const sync=()=>setPrompt(deferredInstall);window.addEventListener('hs-install-ready',sync);const media=")
s=s.replace("return()=>{window.removeEventListener('beforeinstallprompt',capture);window.removeEventListener('appinstalled',done);", "return()=>{window.removeEventListener('hs-install-ready',sync);window.removeEventListener('beforeinstallprompt',capture);window.removeEventListener('appinstalled',done);")
s=s.replace("setPrompt(null);}\n return <div", "setPrompt(null);deferredInstall=null;}\n return <div")
p.write_text(s,encoding='utf-8')
p=R/'package.json';d=json.loads(p.read_text());d['scripts']['test:browser']='node tests/browser.mjs';p.write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
p=R.parent.parent/'06_Estrategia_e_PRD/Ficha_negocio.json';d=json.loads(p.read_text(encoding='utf-8'));d['whatsapp']='5531991137969';d['missing']=[x for x in d['missing'] if x!='Canal comercial'];d['notes']+=' WhatsApp confirmado pelo usuário: (31) 99113-7969.';p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
print('Contraste corrigido, instalação aprimorada e número registrado.')
