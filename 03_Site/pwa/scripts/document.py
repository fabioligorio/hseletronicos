from pathlib import Path
import json,gzip
R=Path(r'C:\Users\Fabio\Desktop\HS Eletronicos\03_Site\pwa')
report=json.loads((R/'docs/qa/browser-report.json').read_text())
assert all(c['pass'] for c in report['checks'])
checks=len(report['checks']);cache=json.loads((R/'docs/precache-report.json').read_text())
js=list((R/'out/_next/static').rglob('*.js'));css=list((R/'out/_next/static').rglob('*.css'))
stats={'js_all_routes_gzip_bytes':sum(len(gzip.compress(p.read_bytes())) for p in js),'css_gzip_bytes':sum(len(gzip.compress(p.read_bytes())) for p in css),'hero_webp_bytes':(R/'public/images/logic-board.webp').stat().st_size,'offline_cache_uncompressed_bytes':cache['bytes'],'browser_checks_passed':checks}
(R/'docs/qa/build-metrics.json').write_text(json.dumps(stats,indent=2),encoding='utf-8')
(R/'README.md').write_text('''# HS Eletrônicos | MVP PWA

PWA de assistência técnica baseado no brandbook 2.0 e no PRD do projeto. Responsável: Hugo. Região: Belo Horizonte e região. Atendimento presencial e reparação 24h. WhatsApp: +55 31 99113-7969.

## Executar

Requer Node.js 20.9 ou superior e npm. Na pasta do projeto:

```sh
npm ci
npm run build
npm start
```

Prévia: http://127.0.0.1:3000. O servidor serve o build de produção, incluindo service worker. Para editar com recarga automática: `npm run dev`. A configuração offline só registra o service worker no build de produção.

No Windows, `INICIAR_PREVIA.cmd` abre a prévia com o build já gerado. Não executar o servidor de desenvolvimento e o de produção simultaneamente na mesma porta. Se testar alterações após uma versão instalada, usar o aviso de atualização ou limpar os dados do site.

## Implementado

- Home, serviços e três páginas de atendimento, sobre, contato, privacidade, instalação, links, offline e 404.
- Visual preto/prata com azul/verde, marca vetorial compacta adaptada ao aplicativo e ícones PNG.
- Mensagem contextual de atendimento: seleção de categoria, modelo e sintoma opcionais; revisão, cópia e saída para WhatsApp. Sem envio automático, banco de leads ou diagnóstico automatizado.
- Link telefônico para o mesmo número comercial.
- Manifest com ícones 192/512, maskable, apple-touch-icon, shortcuts e modo standalone.
- Service worker versionado pelo conteúdo do build. Pré-cache das páginas e arquivos públicos, consulta offline, estado de conexão e atualização mediante ação do usuário.
- Orientações de instalação para iOS e navegadores desktop/Android; captura do prompt quando suportado.
- Navegação mobile inferior, menu acessível, FAQ nativo, foco visível e redução de movimento.
- Nenhum catálogo, carrinho, autenticação, pagamento, push, formulário de servidor ou analytics nesta versão.

## Conteúdo e configuração

`lib/business.json`: nome, telefone, região, domínio e estado de publicação. `lib/data.ts`: serviços e FAQ. `app/globals.css`: tokens e layout. `components/ContactForm.tsx`: experiência de preparo da mensagem.

Endereço físico e perfis sociais não foram informados. Não há mapa, pin ou perfis fictícios. O texto orienta combinar local com Hugo. O atendimento 24h não é promessa de conclusão imediata do reparo.

O texto digitado fica na memória da página e não é persistido no armazenamento do aplicativo. Ao abrir WhatsApp, ele entra no parâmetro do link externo. A confirmação de envio acontece no WhatsApp, fora do PWA.

## PWA e offline

O primeiro acesso online precisa terminar a instalação do service worker. Depois, as páginas públicas podem ser consultadas offline. WhatsApp e ligações dependem dos serviços e conectividade do dispositivo. Conteúdo antigo pode permanecer até uma atualização; a marcação de versão é gerada em cada build.

HTTPS é necessário para instalação fora de localhost. Abrir `index.html` como arquivo local não equivale a testar o PWA. A instalação física em iPhone/Android ainda deve ser conferida no domínio HTTPS final; o comportamento offline foi testado em Chromium.

Não existe fila de envio offline, push ou acompanhamento de ordem de serviço. Nenhuma solicitação é marcada como recebida pela HS só porque houve clique.

## Testes

```sh
npm run typecheck
npm test
npm run test:browser
```

O teste de navegador espera `npm start` ativo em 127.0.0.1:3000 e Chrome instalado. `TEST_URL` pode apontar para outro ambiente. Evidências e capturas estão em `docs/qa`. Auditoria axe cobre home, serviços, contato e instalação; não é certificação completa de acessibilidade.

## Publicar na Vercel

1. Usar conta/plano compatível com uso comercial e manter titularidade com Hugo.
2. Importar esta pasta como projeto Next.js. Build: `npm run build`; diretório: `out`; dependências via lockfile npm.
3. Conferir canais, conteúdo de serviços, local/procedimento do plantão e aviso de privacidade com Hugo.
4. Definir `siteUrl` como domínio HTTPS real em `lib/business.json` e marcar `releaseApproved: true` após revisão. Executar `npm run check:release`, build e testes.
5. Configurar DNS/HTTPS na Vercel e verificar navegação, WhatsApp, instalação, offline e atualização no domínio final.

Enquanto `releaseApproved` é false, o MVP fica com noindex e robots bloqueando indexação. Isso não é autenticação; usar proteção de preview da hospedagem quando necessário. O build gera sitemap e libera robots quando domínio e aprovação estão configurados. O arquivo `vercel.json` aplica cabeçalhos, incluindo atualização sem cache de sw.js.

O PWA está pronto para revisão e implantação; não foi publicado em uma conta Vercel nesta entrega. Domínio e conta não foram fornecidos.

## Assets

`public/brand-mark.svg` é uma adaptação vetorial compacta do conceito de placa aprovado para uso no aplicativo; não é reprodução tipográfica integral nem substitui a finalização do kit institucional. `public/favicon.svg` e `public/icons` são os ícones do PWA.

`public/images/logic-board.webp` é ilustração gerada com image_gen nativo, identificada no site como ilustrativa. Não representa bancada ou reparo real da HS. Original em `docs/source-assets/logic-board.png`; prompt em `docs/assets.md`. `node scripts/assets.mjs` recria a otimização e os ícones, usando sharp instalado com Next.js.

## Referências técnicas

- [Next.js: Progressive Web Apps](https://nextjs.org/docs/app/guides/progressive-web-apps)
- [MDN: Using Service Workers](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API/Using_Service_Workers)

Os scripts Python de scaffold em `scripts` são histórico de autoria. A fonte atual são os arquivos do projeto; não reexecutá-los para manutenção, pois podem sobrescrever alterações posteriores.
''',encoding='utf-8')
(R/'INICIAR_PREVIA.cmd').write_text('@echo off\ncd /d "%~dp0"\nnpm start\npause\n',encoding='utf-8')
qa=f'''# Validação do MVP

- Compilação de produção Next.js: aprovada.
- Verificação TypeScript: aprovada.
- Testes unitários de contato: 3 aprovados.
- Testes de navegador: {checks} aprovados; zero erros de JavaScript registrados.
- Axe: zero violações nas quatro páginas auditadas, após correção de contraste.
- Responsividade: 320, 390, 768 e 1440 px sem overflow horizontal nas rotas verificadas.
- Offline: service worker ativo e navegação em sobre, serviço iPhone e contato sem conexão.
- WhatsApp: URL correta e texto codificado; nenhum envio realizado pelo teste.
- Manifest e ícones: presentes, válidos e acessíveis.
- Cache público: {cache['files']} arquivos, {cache['bytes']} bytes antes de compressão de transporte.
- Imagem principal: {stats['hero_webp_bytes']} bytes WebP.

## Limites

Não houve instalação em aparelho físico, envio real de mensagem ou publicação em Vercel. Não foi executado Lighthouse nem medição de Core Web Vitals em campo. A auditoria automática não substitui revisão integral por tecnologia assistiva. A configuração do domínio e a aprovação dos dados operacionais ficam para implantação.
'''
(R/'docs/VALIDACAO.md').write_text(qa,encoding='utf-8')
p=R.parent.parent/'LEIA-ME.md';s=p.read_text(encoding='utf-8');s+='\n## MVP PWA implementado\n\nProjeto: [03_Site/pwa](03_Site/pwa/README.md). Prévia local: http://127.0.0.1:3000. WhatsApp confirmado: (31) 99113-7969. O PWA foi implementado e testado; ainda não publicado. Os documentos anteriores descrevem a etapa de planejamento e devem ser lidos com esse registro de evolução.\n';p.write_text(s,encoding='utf-8')
print(json.dumps(stats,indent=2))
