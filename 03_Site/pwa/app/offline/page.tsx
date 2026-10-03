import Link from 'next/link';
export const metadata={title:'Você está offline'};
export default function Offline(){return <section className="container not-found"><p className="eyebrow">SEM CONEXÃO</p><h1>Seguimos por aqui.</h1><p>Você pode consultar as informações salvas.<br/>Para falar com Hugo, conecte-se à internet.</p><Link className="button" href="/">Voltar ao início</Link></section>;}
