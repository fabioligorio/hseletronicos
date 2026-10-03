import Link from 'next/link';
export function Brand({ small = false }: { small?: boolean }) {
 return <Link className={`brand ${small ? 'brand-small' : ''}`} href="/" aria-label="HS Eletrônicos, início"><img src="/brand-mark.svg" alt="" width="43" height="52"/><span><strong>HS <span>ELETRÔNICOS</span></strong><small>ASSISTÊNCIA TÉCNICA</small></span></Link>;
}
