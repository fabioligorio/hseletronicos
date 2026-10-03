from pathlib import Path
import json
R=Path(r'C:\Users\Fabio\Desktop\HS Eletronicos\03_Site\pwa')
files={
'next.config.ts':'''import type { NextConfig } from 'next';
const config: NextConfig = { output: 'export', trailingSlash: true, images: { unoptimized: true }, poweredByHeader: false };
export default config;
''',
'lib/business.json':json.dumps({'name':'HS Eletrônicos','responsible':'Hugo','whatsapp':'5531991137969','phoneDisplay':'(31) 99113-7969','area':'Belo Horizonte e região','hours':'Atendimento presencial e reparação 24h','siteUrl':None,'address':None,'socials':{},'releaseApproved':False},ensure_ascii=False,indent=2),
'lib/contact.mjs':'''export function normalizePhone(value) {
  const phone = String(value ?? '').replace(/\\D/g, '');
  if (!/^55\\d{10,11}$/.test(phone)) return null;
  return phone;
}
export function composeMessage({ category = 'Celular', model = '', symptom = '' } = {}) {
  const clean = (value, max) => String(value ?? '').replace(/[\\u0000-\\u001F\\u007F]/g, ' ').trim().slice(0, max);
  const parts = ['Olá, Hugo! Vim pelo site da HS Eletrônicos e gostaria de combinar um atendimento.', `Equipamento: ${clean(category, 80)}.`];
  if (clean(model,80)) parts.push(`Modelo: ${clean(model,80)}.`);
  if (clean(symptom,500)) parts.push(`O que aconteceu: ${clean(symptom,500)}`);
  return parts.join('\\n');
}
export function whatsappUrl(phone, message) {
  const valid = normalizePhone(phone);
  return valid ? `https://wa.me/${valid}?text=${encodeURIComponent(message)}` : null;
}
''',
'lib/contact.d.mts':'''export function normalizePhone(value: unknown): string | null;
export function composeMessage(input?: { category?: string; model?: string; symptom?: string }): string;
export function whatsappUrl(phone: unknown, message: string): string | null;
''',
'lib/data.ts':'''export const services = [
 { slug: 'iphone', title: 'iPhone', label: 'FOCO NO SEU IPHONE', description: 'Seu iPhone merece atenção em cada detalhe. Conte o que aconteceu para orientar a avaliação.', icon: 'phone', topics: ['Informe o modelo', 'Descreva o sintoma', 'Combine o atendimento'], intro: 'Quando algo muda no funcionamento do seu iPhone, o primeiro passo é entender o que aconteceu. Hugo orienta como começar a avaliação.', examples: ['Mudanças no funcionamento', 'Dificuldade para carregar', 'Problemas percebidos na tela'], note: 'Os sintomas ajudam a iniciar a conversa. A causa e as possibilidades de reparação dependem de avaliação.' },
 { slug: 'celulares', title: 'Celulares', label: 'CUIDADO COM A SUA ROTINA', description: 'Assistência para o aparelho que acompanha você. Consulte o atendimento para sua marca e modelo.', icon: 'phone', topics: ['Consulte marca e modelo', 'Explique o que mudou', 'Entenda o próximo passo'], intro: 'Seu celular faz parte da sua rotina. Se ele apresentou uma falha, informe a marca, o modelo e quando o problema começou para combinar a avaliação.', examples: ['Falhas de funcionamento', 'Problemas de energia', 'Danos percebidos no aparelho'], note: 'A disponibilidade do serviço e de peças é confirmada conforme o equipamento e a avaliação.' },
 { slug: 'eletronicos', title: 'Outros eletrônicos', label: 'CADA EQUIPAMENTO, UMA AVALIAÇÃO', description: 'Tem outro equipamento precisando de atenção? Consulte Hugo sobre a possibilidade de atendimento.', icon: 'circuit', topics: ['Identifique o equipamento', 'Informe marca e modelo', 'Confirme se é atendido'], intro: 'A HS também trabalha com eletrônicos. Entre em contato com os dados do seu equipamento para confirmar se a categoria e o serviço são atendidos.', examples: ['Tipo de equipamento', 'Marca e modelo', 'Sintoma e histórico percebido'], note: 'O atendimento de outras categorias é confirmado caso a caso. Não há promessa de reparo para todo tipo de equipamento.' }
] as const;
export const faqs = [
 ['Como funciona o atendimento 24 horas?', 'A HS oferece atendimento presencial e reparação 24 horas. Entre em contato com Hugo para combinar o local e orientar a avaliação. O tempo para concluir o reparo depende do aparelho, da avaliação e das condições do serviço.'],
 ['Onde a HS atende?', 'Em Belo Horizonte e região. Combine o atendimento diretamente com Hugo pelo WhatsApp. O local e a possibilidade de atendimento na sua região são confirmados na conversa.'],
 ['Vocês atendem iPhones?', 'Sim. A HS tem foco em reparação de celulares, especialmente iPhones. Informe o modelo e o que aconteceu para entender o próximo passo.'],
 ['Posso saber o valor antes da avaliação?', 'Conte o sintoma e informe o modelo para iniciar a conversa. O valor, as condições de avaliação e o prazo precisam ser confirmados com Hugo conforme o caso.'],
 ['O que devo informar no primeiro contato?', 'Marca, modelo, sintoma e quando o problema começou. Não envie senhas, códigos de verificação ou dados pessoais armazenados no aparelho.'],
 ['A HS também compra e vende aparelhos?', 'Sim, a compra e venda de equipamentos novos e seminovos também faz parte do negócio. Consulte Hugo para saber as condições e a disponibilidade. Este site é dedicado aos serviços de assistência.']
] as const;
''',
'components/Brand.tsx':'''import Link from 'next/link';
export function Brand({ small = false }: { small?: boolean }) {
 return <Link className={`brand ${small ? 'brand-small' : ''}`} href="/" aria-label="HS Eletrônicos, início"><img src="/brand-mark.svg" alt="" width="43" height="52"/><span><strong>HS <span>ELETRÔNICOS</span></strong><small>ASSISTÊNCIA TÉCNICA</small></span></Link>;
}
''',
'components/Shell.tsx':'''"use client";
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { useEffect, useRef, useState } from 'react';
import { Menu, X, Home, Cpu, MessageCircle, Download, Clock3, MapPin } from 'lucide-react';
import { Brand } from './Brand';
import { PwaStatus } from './pwa';
import business from '@/lib/business.json';
export function Header() {
 const [open,setOpen]=useState(false);const path=usePathname();const trigger=useRef<HTMLButtonElement>(null);
 useEffect(()=>setOpen(false),[path]);
 useEffect(()=>{const handle=(e:KeyboardEvent)=>{if(e.key==='Escape' && open){setOpen(false);trigger.current?.focus();}};document.addEventListener('keydown',handle);return()=>document.removeEventListener('keydown',handle);},[open]);
 return <><a className="skip-link" href="#main">Pular para o conteúdo</a><header className="header"><div className="container header-inner"><Brand/><nav className="desktop-nav" aria-label="Navegação principal"><Link href="/servicos/" aria-current={path.startsWith('/servicos')?'page':undefined}>Serviços</Link><Link href="/#como-funciona">Como funciona</Link><Link href="/sobre/" aria-current={path==='/sobre/'?'page':undefined}>Sobre a HS</Link><Link href="/#duvidas">Dúvidas</Link></nav><Link className="button small header-contact" href="/contato/"><MessageCircle size={17}/>Falar com Hugo</Link><button ref={trigger} type="button" className="icon-button menu-trigger" aria-label={open?'Fechar menu':'Abrir menu'} aria-expanded={open} aria-controls="mobile-menu" onClick={()=>setOpen(!open)}>{open?<X/>:<Menu/>}</button></div>{open&&<nav id="mobile-menu" className="mobile-menu" aria-label="Menu mobile"><Link href="/servicos/" onClick={()=>setOpen(false)}>Serviços</Link><Link href="/#como-funciona" onClick={()=>setOpen(false)}>Como funciona</Link><Link href="/sobre/" onClick={()=>setOpen(false)}>Sobre a HS</Link><Link href="/#duvidas" onClick={()=>setOpen(false)}>Dúvidas</Link><Link href="/contato/" onClick={()=>setOpen(false)}>Falar com Hugo</Link></nav>}</header><PwaStatus/></>;
}
export function Footer(){return <><footer className="footer"><div className="container footer-grid"><div><Brand/><p>Cuidado técnico.<br/>Conversa clara.</p></div><div><h2>Atendimento</h2><p><MapPin size={16}/>Belo Horizonte e região</p><p><Clock3 size={16}/>Presencial e reparação 24h</p><Link href="/contato/">{business.phoneDisplay}</Link></div><div><h2>Acesso rápido</h2><Link href="/servicos/">Nossos serviços</Link><Link href="/instalar/">Instalar o aplicativo</Link><Link href="/privacidade/">Privacidade</Link></div></div><div className="container footer-bottom"><span>© {new Date().getFullYear()} HS Eletrônicos</span><span>Entre em contato para combinar o atendimento.</span></div></footer><MobileTabs/></>;}
function MobileTabs(){const path=usePathname();const tabs=[{href:'/',label:'Início',icon:Home},{href:'/servicos/',label:'Serviços',icon:Cpu},{href:'/contato/',label:'Atendimento',icon:MessageCircle},{href:'/instalar/',label:'Aplicativo',icon:Download}];return <nav className="bottom-tabs" aria-label="Navegação do aplicativo">{tabs.map(t=><Link key={t.href} href={t.href} aria-current={(t.href==='/'?path==='/':path.startsWith(t.href))?'page':undefined}><t.icon size={21}/><span>{t.label}</span></Link>)}</nav>;}
''',
'components/ui.tsx':'''import Link from 'next/link';
import { Clock3, MessageCircle, Smartphone, Cpu, Check, MapPin, Headphones } from 'lucide-react';
import { faqs, services } from '@/lib/data';
export function Eyebrow({children}:{children:React.ReactNode}){return <p className="eyebrow">{children}</p>;}
export function Breadcrumb({label}:{label:string}){return <nav className="breadcrumb" aria-label="Caminho da página"><Link href="/">Início</Link><span>/</span><span aria-current="page">{label}</span></nav>;}
export function ServiceCards(){return <div className="service-grid">{services.map((s,i)=><article className={`service-card service-card-${i}`} key={s.slug}><span className="card-index">0{i+1}</span><div className="service-icon">{s.icon==='phone'?<Smartphone size={30}/>:<Cpu size={30}/>}</div><h3>{s.title}</h3><p>{s.description}</p><Link className="text-link" href={`/servicos/${s.slug}/`}>Conhecer atendimento<span className="visually-hidden"> para {s.title}</span></Link></article>)}</div>;}
export function Process(){return <section className="section process-section" id="como-funciona"><div className="container"><div className="section-heading"><div><Eyebrow>UM PASSO DE CADA VEZ</Eyebrow><h2>Da primeira conversa<br/>ao próximo passo.</h2></div><p>Clareza para entender o que seu aparelho precisa, começando pelo contato.</p></div><div className="process-grid">{[{icon:MessageCircle,title:'Conte o que aconteceu',body:'Informe o modelo do aparelho e o sintoma percebido.'},{icon:MapPin,title:'Combine o atendimento',body:'Fale com Hugo sobre o local e como iniciar a avaliação.'},{icon:Check,title:'Entenda as possibilidades',body:'Confirme o serviço, as condições e o prazo antes de decidir.'}].map((s,i)=><article key={s.title}><span className="step-number">0{i+1}</span><s.icon size={25}/><h3>{s.title}</h3><p>{s.body}</p></article>)}</div></div></section>;}
export function Faq(){return <section className="section" id="duvidas"><div className="container faq-layout"><div><Eyebrow>SEM COMPLICAÇÃO</Eyebrow><h2>Antes de<br/>entrar em contato.</h2><p>Respostas para começar a conversa com mais tranquilidade.</p><Link className="text-link" href="/contato/">Minha dúvida é outra</Link></div><div className="faqs">{faqs.map(([q,a],i)=><details key={q}><summary><span className="faq-number">0{i+1}</span>{q}<span className="faq-plus" aria-hidden="true">+</span></summary><p>{a}</p></details>)}</div></div></section>;}
export function ContactBanner(){return <section className="container contact-banner"><div><span className="availability"><Clock3 size={15}/>ATENDIMENTO 24H</span><h2>Vamos cuidar do<br/>seu próximo passo?</h2><p>Converse com Hugo e combine o atendimento em BH e região.</p></div><Link className="button" href="/contato/"><MessageCircle size={20}/>Combinar atendimento</Link></section>;}
''',
'components/pwa.tsx':'''"use client";
import { useEffect, useState } from 'react';
import { Download, WifiOff, RefreshCw, CheckCircle2, Share2 } from 'lucide-react';
type InstallEvent = Event & { prompt:()=>Promise<void>; userChoice:Promise<{outcome:string}> };
export function PwaStatus(){const [offline,setOffline]=useState(false);const [worker,setWorker]=useState<ServiceWorker|null>(null);
 useEffect(()=>{setOffline(!navigator.onLine);const on=()=>setOffline(!navigator.onLine);window.addEventListener('online',on);window.addEventListener('offline',on);
 if('serviceWorker' in navigator && process.env.NODE_ENV==='production') {navigator.serviceWorker.register('/sw.js',{scope:'/'}).then(reg=>{const check=()=>{if(reg.waiting && navigator.serviceWorker.controller)setWorker(reg.waiting);};check();reg.addEventListener('updatefound',()=>{reg.installing?.addEventListener('statechange',check);});reg.update().catch(()=>{});}).catch(()=>{});}
 return()=>{window.removeEventListener('online',on);window.removeEventListener('offline',on);};},[]);
 const update=()=>{if(!worker)return; navigator.serviceWorker.addEventListener('controllerchange',()=>window.location.reload(),{once:true});worker.postMessage({type:'SKIP_WAITING'});};
 return <>{offline&&<div className="connection-banner" role="status"><WifiOff size={16}/>Você está offline. As informações salvas continuam disponíveis; o WhatsApp precisa de conexão.</div>}{worker&&<div className="update-banner" role="status"><RefreshCw size={16}/><span>Uma nova versão está disponível.</span><button onClick={update}>Atualizar agora</button><button onClick={()=>setWorker(null)} aria-label="Dispensar atualização">Depois</button></div>}</>;
}
export function InstallControl(){const [prompt,setPrompt]=useState<InstallEvent|null>(null);const [installed,setInstalled]=useState(false);const [ios,setIos]=useState(false);const [notice,setNotice]=useState('');
 useEffect(()=>{const media=window.matchMedia('(display-mode: standalone)');setInstalled(media.matches || Boolean((navigator as Navigator & {standalone?:boolean}).standalone));setIos(/iPad|iPhone|iPod/.test(navigator.userAgent)|| (navigator.platform==='MacIntel' && navigator.maxTouchPoints>1));const capture=(event:Event)=>{event.preventDefault();setPrompt(event as InstallEvent);};const done=()=>{setInstalled(true);setPrompt(null);};window.addEventListener('beforeinstallprompt',capture);window.addEventListener('appinstalled',done);const change=()=>setInstalled(media.matches);media.addEventListener('change',change);return()=>{window.removeEventListener('beforeinstallprompt',capture);window.removeEventListener('appinstalled',done);media.removeEventListener('change',change);};},[]);
 async function install(){if(!prompt)return;await prompt.prompt();const choice=await prompt.userChoice;setNotice(choice.outcome==='accepted'?'Siga a confirmação do navegador para concluir a instalação.':'Você pode continuar usando pelo navegador.');setPrompt(null);}
 return <div className="install-control">{installed?<div className="success-note"><CheckCircle2/>Você já está usando o aplicativo instalado.</div>:prompt?<button className="button" onClick={install}><Download size={20}/>Instalar HS Eletrônicos</button>:<div className="install-instructions"><h2>{ios?'No iPhone ou iPad':'Instalar pelo navegador'}</h2>{ios?<ol><li>Abra este site no Safari.</li><li>Toque em Compartilhar <Share2 size={15}/>.</li><li>Selecione Adicionar à Tela de Início e confirme.</li></ol>:<ol><li>Abra este site no Chrome ou Edge atualizado.</li><li>No menu, procure Instalar aplicativo ou Adicionar à tela inicial.</li><li>Confirme para criar o atalho da HS.</li></ol>}<p className="muted">A opção depende do navegador. Você pode usar todos os serviços pelo site sem instalar.</p></div>}<p role="status">{notice}</p></div>;
}
''',
'app/layout.tsx':'''import type { Metadata, Viewport } from 'next';
import { Header, Footer } from '@/components/Shell';
import business from '@/lib/business.json';
import './globals.css';
export const metadata: Metadata = { title: { default: 'HS Eletrônicos | Assistência técnica 24h em BH', template: '%s | HS Eletrônicos' }, description: 'Assistência técnica de celulares e eletrônicos com foco em iPhones. Hugo, Belo Horizonte e região. Atendimento presencial e reparação 24 horas.', manifest: '/manifest.webmanifest', applicationName: 'HS Eletrônicos', appleWebApp: { capable:true, statusBarStyle:'black-translucent', title:'HS Eletrônicos' }, icons:{icon:'/favicon.svg',apple:'/icons/apple-touch-icon.png'}, robots: {index:business.releaseApproved,follow:business.releaseApproved} };
export const viewport: Viewport = {width:'device-width',initialScale:1,viewportFit:'cover',themeColor:'#101010'};
export default function Layout({children}:{children:React.ReactNode}){return <html lang="pt-BR"><body><Header/><main id="main" tabIndex={-1}>{children}</main><Footer/></body></html>;}
''',
'app/page.tsx':'''import Link from 'next/link';
import { MessageCircle, Clock3, MapPin, Cpu, Smartphone } from 'lucide-react';
import { Eyebrow, ServiceCards, Process, Faq, ContactBanner } from '@/components/ui';
export default function Home(){return <><section className="hero"><div className="container hero-grid"><div className="hero-copy"><span className="availability"><Clock3 size={15}/>PRESENCIAL • 24 HORAS</span><h1>Seu celular.<br/><span>Em boas mãos.</span></h1><p>Assistência técnica de celulares e eletrônicos, com foco em iPhones. Cuidado com o seu aparelho. Clareza na conversa.</p><div className="hero-actions"><Link className="button" href="/contato/"><MessageCircle size={19}/>Combinar atendimento</Link><Link className="button secondary" href="/servicos/">Conhecer serviços</Link></div><span className="hero-location"><MapPin size={16}/>Belo Horizonte e região</span></div><div className="hero-visual"><div className="technical-label"><span>HS / CUIDADO EM CADA DETALHE</span><Cpu size={18}/></div><img className="hero-board" src="/images/logic-board.webp" alt="Ilustração de uma placa eletrônica de celular com componentes prateados" width="900" height="600" fetchPriority="high"/><div className="visual-caption"><span><Smartphone size={16}/>Foco em iPhones</span><span>Imagem ilustrativa</span></div></div></div></section><div className="service-strip"><div className="container strip-grid"><div><strong>24h</strong><span>Atendimento presencial<br/>e reparação</span></div><div><strong>BH</strong><span>Belo Horizonte<br/>e região</span></div><div><strong>Hugo</strong><span>Conversa direta com<br/>o responsável</span></div></div></div><section className="section" id="servicos"><div className="container"><div className="section-heading"><div><Eyebrow>ASSISTÊNCIA TÉCNICA</Eyebrow><h2>Para o que faz parte<br/>do seu dia.</h2></div><p>Do primeiro sintoma à avaliação. Encontre o atendimento para o seu equipamento.</p></div><ServiceCards/></div></section><Process/><section className="section about-preview"><div className="container about-grid"><div><Eyebrow>POR TRÁS DA HS</Eyebrow><h2>Precisão no cuidado.<br/>Proximidade na conversa.</h2></div><div><p>Hugo é o responsável pela HS Eletrônicos. O atendimento começa ouvindo o que aconteceu com o seu aparelho e combinando o próximo passo.</p><p>Em Belo Horizonte e região, com atendimento presencial e reparação 24 horas.</p><Link className="text-link" href="/sobre/">Conheça a HS</Link></div></div></section><Faq/><ContactBanner/></>;}
''',
'public/manifest.webmanifest':json.dumps({'id':'/','name':'HS Eletrônicos','short_name':'HS Eletrônicos','description':'Assistência técnica de celulares 24h em Belo Horizonte e região.','lang':'pt-BR','start_url':'/','scope':'/','display':'standalone','background_color':'#101010','theme_color':'#101010','categories':['business','utilities'],'icons':[{'src':'/icons/icon-192.png','sizes':'192x192','type':'image/png','purpose':'any'},{'src':'/icons/icon-512.png','sizes':'512x512','type':'image/png','purpose':'any'},{'src':'/icons/icon-maskable.png','sizes':'512x512','type':'image/png','purpose':'maskable'}],'shortcuts':[{'name':'Combinar atendimento','url':'/contato/','description':'Prepare uma mensagem para Hugo'},{'name':'Nossos serviços','url':'/servicos/'}]},ensure_ascii=False,indent=2),
'.gitignore':'''node_modules/\n.next/\nout/\n.env*\n!.env.example\n.vercel/\ntest-results/\n'''
}
for path,content in files.items():
 p=R/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(content,encoding='utf-8')
# Refined compact SVG adaptation of the approved logic-board concept for UI use.
mark='''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 120"><path d="M17 5H31Q36 5 36 11V19H52L59 26V60H89Q95 60 95 66V110Q95 116 89 116H45L36 106H14Q8 106 8 100V66H16V58H8V12Q8 5 17 5Z" fill="#BFC3C7"/><g fill="#101010"><rect x="17" y="77" width="27" height="24" rx="3"/><rect x="63" y="70" width="22" height="19" rx="2"/><rect x="35" y="28" width="15" height="20" rx="2"/><rect x="64" y="96" width="19" height="13" rx="2"/></g><g fill="none" stroke-linejoin="round" stroke-linecap="round" stroke-width="3"><path d="M20 25V46L28 54V68L53 93V104" stroke="#268CFF"/><path d="M30 26V46L37 54V63L55 81H60M50 103H57V88L48 79V72L37 62" stroke="#101010"/><path d="M89 91V105M13 70H23" stroke="#26C985"/></g><g fill="#26C985"><circle cx="20" cy="25" r="4"/><circle cx="53" cy="104" r="4"/><circle cx="89" cy="91" r="3"/><circle cx="13" cy="70" r="3"/></g><g stroke="#101010" stroke-width="2"><path d="M22 73V77M29 73V77M36 73V77M44 82H49M44 89H49M44 96H49M68 66V70M75 66V70M82 66V70M59 76H63M59 83H63"/></g><g stroke="#101010" stroke-width="2.5" fill="none"><circle cx="20" cy="14" r="4"/><circle cx="87" cy="65" r="3"/></g></svg>'''
(R/'public/brand-mark.svg').write_text(mark,encoding='utf-8')
icon='''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><rect width="512" height="512" rx="104" fill="#101010"/><g transform="translate(113 84) scale(2.85)">'''+mark.split('>',1)[1].rsplit('</svg>',1)[0]+'''</g></svg>'''
(R/'public/favicon.svg').write_text(icon,encoding='utf-8')
print('Estrutura, conteúdo e componentes iniciais criados.')
