# Validação da publicação na Vercel

Data: 03/10/2026. Domínio: https://hseletronicos.vercel.app/

A versão anterior respondia HTTP 404 NOT_FOUND da Vercel. A correção 41416aa adicionou vercel.json na raiz do repositório com instalação e build em 03_Site/pwa e saída exclusiva em 03_Site/pwa/out. A integração GitHub/Vercel concluiu a publicação e o domínio passou a responder HTTP 200.

Build de produção local concluído. Os 15 testes de navegador foram executados contra o domínio HTTPS publicado e passaram: página inicial, manifest e ícones, acessibilidade em quatro rotas, composição do link WhatsApp para 5531991137969, FAQ, links internos e 404 de rota inexistente, menu móvel, ausência de overflow em 320/390/768/1440 px, service worker, rotas offline, instruções de instalação e ausência de erros JavaScript.

Comando de teste: TEST_URL=https://hseletronicos.vercel.app npm run test:browser (definir a variável conforme o shell).

Evidências: docs/qa/browser-report.json e capturas em docs/qa. Testes em Chrome automatizado; não houve envio de mensagem nem instalação em aparelho físico. As restrições de indexação existentes continuam configuradas em lib/business.json até a revisão de lançamento.