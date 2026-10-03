import Link from 'next/link';
import { MessageCircle, Cpu, Download } from 'lucide-react';
import { Breadcrumb, Eyebrow } from '@/components/ui';
export const metadata={title:'Acesse a HS',description:'Serviços, atendimento e aplicativo da HS Eletrônicos.'};
export default function Links(){return <div className="container"><Breadcrumb label="Acesso rápido"/><div className="page-intro"><Eyebrow>HS ELETRÔNICOS</Eyebrow><h1>Como podemos ajudar?</h1><p>Belo Horizonte e região. Atendimento presencial e reparação 24 horas.</p></div><div className="page-content links-stack"><Link href="/contato/"><MessageCircle/>Combinar atendimento com Hugo</Link><Link href="/servicos/"><Cpu/>Conhecer os serviços</Link><Link href="/instalar/"><Download/>Instalar o aplicativo</Link></div></div>;}
