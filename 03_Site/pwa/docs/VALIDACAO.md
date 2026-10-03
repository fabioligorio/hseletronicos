# Validação do MVP

- Compilação de produção Next.js: aprovada.
- Verificação TypeScript: aprovada.
- Testes unitários de contato: 3 aprovados.
- Testes de navegador: 15 aprovados; zero erros de JavaScript registrados.
- Axe: zero violações nas quatro páginas auditadas, após correção de contraste.
- Responsividade: 320, 390, 768 e 1440 px sem overflow horizontal nas rotas verificadas.
- Offline: service worker ativo e navegação em sobre, serviço iPhone e contato sem conexão.
- WhatsApp: URL correta e texto codificado; nenhum envio realizado pelo teste.
- Manifest e ícones: presentes, válidos e acessíveis.
- Cache público: 84 arquivos, 1381716 bytes antes de compressão de transporte.
- Imagem principal: 70552 bytes WebP.

## Limites

Não houve instalação em aparelho físico, envio real de mensagem ou publicação em Vercel. Não foi executado Lighthouse nem medição de Core Web Vitals em campo. A auditoria automática não substitui revisão integral por tecnologia assistiva. A configuração do domínio e a aprovação dos dados operacionais ficam para implantação.
