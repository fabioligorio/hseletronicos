# Backlog de execução

Status inicial: não iniciado. Documentação concluída não equivale a implementação.

## BR-01 | P0 | Finalizar marca vetorial

Responsável: Design. Referência: Brandbook 06-09.

Dependências: Referência v6.

Aceite: SVG/PDF sem fontes dependentes, variantes consistentes e prova de tamanho.

Testes: T11,T12. Status: Não iniciado.

## BR-02 | P0 | Avatar, favicon e templates

Responsável: Design. Referência: Brandbook 09/19.

Dependências: BR-01.

Aceite: Microversão legível, avatares circulares e capas revisadas.

Testes: T12,T16. Status: Não iniciado.

## OPS-01 | P0 | Confirmar ficha comercial

Responsável: Hugo. Referência: PRD 05.

Dependências: Nenhuma.

Aceite: Contato, local/procedimento, serviços e condições documentados; 24h sem promessa de prazo imediato.

Testes: T04,T13. Status: Não iniciado.

## OPS-02 | P0 | Titularidade e acessos

Responsável: Hugo. Referência: PRD 04/21.

Dependências: Nenhuma.

Aceite: URLs, e-mail de recuperação e 2FA registrados sem senhas no projeto.

Testes: T19. Status: Não iniciado.

## WEB-01 | P0 | Navegação e responsividade

Responsável: Desenvolvimento. Referência: PRD 11.

Dependências: Design de telas.

Aceite: Menu por teclado/toque, Escape e foco; sem overflow nos quatro tamanhos.

Testes: T01,T05,T06. Status: Não iniciado.

## WEB-02 | P0 | Páginas e conteúdo aprovado

Responsável: Conteúdo/Hugo. Referência: PRD 08-11.

Dependências: OPS-01.

Aceite: Rotas úteis e serviços confirmados; nenhuma interface de catálogo ou fato inventado.

Testes: T03,T04,T13. Status: Não iniciado.

## WEB-03 | P0 | CTA contextual

Responsável: Desenvolvimento. Referência: PRD 11/12.

Dependências: OPS-01.

Aceite: Destino real e mensagem do serviço sem envio automático ou dado privado.

Testes: T02. Status: Não iniciado.

## WEB-04 | P0 | Estados vazios e erro

Responsável: Desenvolvimento. Referência: PRD 11.

Dependências: WEB-01.

Aceite: 404 útil, sem seção vazia, CTA ou formulário falso.

Testes: T07. Status: Não iniciado.

## WEB-05 | P0 | Configurar contato e 24h

Responsável: Hugo/Desenvolvimento. Referência: PRD 12.

Dependências: OPS-01.

Aceite: Número testado em três ambientes e redação coerente com atendimento presencial 24h.

Testes: T02,T04. Status: Não iniciado.

## DS-01 | P0 | Componentes e tokens

Responsável: Design/Desenvolvimento. Referência: PRD 13.

Dependências: BR-01.

Aceite: Estados, foco, contraste e tokens consistentes com brandbook.

Testes: T05,T11. Status: Não iniciado.

## CMS-01 | P0 | Conteúdo versionado

Responsável: Desenvolvimento. Referência: PRD 14.

Dependências: OPS-01.

Aceite: Validação de campos, rascunhos não públicos e instrução de edição.

Testes: T04,T13. Status: Não iniciado.

## DEP-01 | P0 | Vercel e domínio

Responsável: Desenvolvimento/Hugo. Referência: PRD 15.

Dependências: OPS-02.

Aceite: Plano comercial, DNS/HTTPS, preview e produção separados.

Testes: T01,T09. Status: Não iniciado.

## ACC-01 | P0 | Navegação acessível

Responsável: Desenvolvimento/QA. Referência: PRD 16.

Dependências: WEB-01.

Aceite: Teclado, semântica, skip link e zoom revisados manualmente.

Testes: T05,T06. Status: Não iniciado.

## ACC-02 | P0 | Contraste e estados

Responsável: Design/QA. Referência: PRD 16.

Dependências: DS-01.

Aceite: Contraste verificado; informação não depende apenas da cor.

Testes: T05,T11. Status: Não iniciado.

## ACC-03 | P0 | Imagens e movimento

Responsável: Conteúdo/QA. Referência: PRD 16.

Dependências: WEB-02.

Aceite: Alt e nomes acessíveis, movimento reduzido e legendas.

Testes: T05,T15. Status: Não iniciado.

## PERF-01 | P0 | Desempenho

Responsável: Desenvolvimento/QA. Referência: PRD 17.

Dependências: DEP-01.

Aceite: Três medições por template; mediana e limites documentados.

Testes: T10. Status: Não iniciado.

## SEO-01 | P0 | SEO técnico/local

Responsável: Desenvolvimento/Conteúdo. Referência: PRD 18.

Dependências: WEB-02.

Aceite: Metadados/sitemap e produção indexável, sem local fictício.

Testes: T09. Status: Não iniciado.

## PRIV-01 | P0 | Privacidade e scripts

Responsável: Hugo/Desenvolvimento. Referência: PRD 19.

Dependências: Analytics escolhido.

Aceite: Inventário e aviso verdadeiros; consentimento quando aplicável testado.

Testes: T08,T14. Status: Não iniciado.

## ANA-01 | P0 | Eventos e UTMs

Responsável: Desenvolvimento/Operação. Referência: PRD 20.

Dependências: PRIV-01.

Aceite: Eventos sem duplicação ou dados pessoais; clique separado de conversa.

Testes: T10. Status: Não iniciado.

## SOC-01 | P0 | Padrão de contas

Responsável: Operação/Hugo. Referência: PRD 21.

Dependências: OPS-02,BR-02.

Aceite: @ verificado, bio correta, proprietário e recuperação confirmados.

Testes: T17,T18,T19. Status: Não iniciado.

## IG-01 | P0 | Configurar Instagram

Responsável: Operação. Referência: PRD 22.

Dependências: SOC-01.

Aceite: Perfil, bio, contato, destaque real e peças inaugurais revisados.

Testes: T16,T17,T18,T20. Status: Não iniciado.

## TT-01 | P0 | Configurar TikTok

Responsável: Operação. Referência: PRD 23.

Dependências: SOC-01.

Aceite: Recursos reais, bio e três vídeos com áudio autorizado.

Testes: T15,T17,T18,T20. Status: Não iniciado.

## KW-01 | P0 | Configurar Kwai

Responsável: Operação. Referência: PRD 24.

Dependências: SOC-01.

Aceite: Campos documentados e três vídeos, sem depender de monetização.

Testes: T15,T17,T18,T20. Status: Não iniciado.

## YT-01 | P0 | Configurar YouTube

Responsável: Operação. Referência: PRD 25.

Dependências: SOC-01.

Aceite: Banner em recortes, descrição, trailer e três Shorts revisados.

Testes: T17,T18,T20,T21. Status: Não iniciado.

## CNT-01 | P0 | Lote inaugural e calendário

Responsável: Editorial/Hugo. Referência: PRD 26-30.

Dependências: OPS-01,BR-02.

Aceite: Três mestres, adaptações, trailer e carrossel com legendas e direitos.

Testes: T13,T14,T15,T20. Status: Não iniciado.

## QA-01 | P0 | Aceite integrado

Responsável: QA/Hugo. Referência: PRD 34.

Dependências: Todos os P0 de implementação.

Aceite: Evidências T01-T22, zero falha crítica de contato e acesso.

Testes: T01-T22. Status: Não iniciado.

## REL-01 | P0 | Lançamento e handoff

Responsável: Coordenação. Referência: PRD 35.

Dependências: QA-01.

Aceite: Domínio e canais finais verificados; recuperação e manual entregues.

Testes: T01,T02,T18,T22. Status: Não iniciado.

## GROW-01 | P1 | Artigos e casos reais

Responsável: Editorial. Referência: PRD 03.

Dependências: Lançamento.

Aceite: Conteúdo original, autorizado e alinhado às dúvidas medidas.

Testes: Revisão editorial. Status: Não iniciado.

## FORM-01 | P1 | Formulário ou agenda

Responsável: Produto/Desenvolvimento. Referência: PRD 12.

Dependências: Nova descoberta.

Aceite: Campos, retenção, operador e critérios específicos aprovados antes de implementar.

Testes: Plano de teste próprio. Status: Não iniciado.

## COM-01 | P2 | Catálogo e comércio

Responsável: Produto/Hugo. Referência: PRD 03.

Dependências: Novo escopo.

Aceite: Descoberta de estoque, atualização e condições; fora do MVP.

Testes: Plano de teste próprio. Status: Não iniciado.

