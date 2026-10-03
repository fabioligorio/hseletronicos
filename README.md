# HS Eletrônicos

Projeto da marca e MVP PWA da HS Eletrônicos, responsável Hugo, com atuação em Belo Horizonte e região e atendimento presencial e reparação 24 horas.

## Aplicativo

O projeto Next.js está em [`03_Site/pwa`](03_Site/pwa/README.md). Para rodar:

```sh
cd 03_Site/pwa
npm ci
npm run build
npm start
```

Prévia: http://127.0.0.1:3000. Leia o README do aplicativo para testes, instalação PWA e publicação na Vercel. Ao importar na Vercel, mantenha Root Directory na raiz do repositório (`.`): o `vercel.json` da raiz instala e compila `03_Site/pwa`, publicando somente `03_Site/pwa/out`. Projetos já configurados com Root Directory `03_Site/pwa` também possuem configuração própria. Não publique a pasta de documentos como saída do site.

## Documentação e identidade

- [`LEIA-ME.md`](LEIA-ME.md): índice e decisões do projeto.
- [`01_Brandbook`](01_Brandbook): brandbook vigente e versões editáveis.
- [`02_Identidade`](02_Identidade): propostas, referência v6 e tokens.
- [`04_Redes_Sociais`](04_Redes_Sociais): calendário e roteiros.
- [`06_Estrategia_e_PRD`](06_Estrategia_e_PRD): PRD, backlog e fontes.
- [`05_Fontes_e_QA`](05_Fontes_e_QA): geradores e evidências de revisão.

As versões antigas foram preservadas e sinalizadas como históricas. Dependências, caches e builds não são versionados. O WhatsApp comercial é público e faz parte da configuração do atendimento; não há credenciais de acesso no projeto.
