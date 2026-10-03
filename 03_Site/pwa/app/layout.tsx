import type { Metadata, Viewport } from 'next';
import { Header, Footer } from '@/components/Shell';
import business from '@/lib/business.json';
import './globals.css';
export const metadata: Metadata = { title: { default: 'HS Eletrônicos | Assistência técnica 24h em BH', template: '%s | HS Eletrônicos' }, description: 'Assistência técnica de celulares e eletrônicos com foco em iPhones. Hugo, Belo Horizonte e região. Atendimento presencial e reparação 24 horas.', manifest: '/manifest.webmanifest', applicationName: 'HS Eletrônicos', appleWebApp: { capable:true, statusBarStyle:'black-translucent', title:'HS Eletrônicos' }, icons:{icon:'/favicon.svg',apple:'/icons/apple-touch-icon.png'}, robots: {index:business.releaseApproved,follow:business.releaseApproved} };
export const viewport: Viewport = {width:'device-width',initialScale:1,viewportFit:'cover',themeColor:'#101010'};
export default function Layout({children}:{children:React.ReactNode}){return <html lang="pt-BR"><body><Header/><main id="main" tabIndex={-1}>{children}</main><Footer/></body></html>;}
