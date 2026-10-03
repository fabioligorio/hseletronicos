from pathlib import Path
import json,re
from pypdf import PdfReader
R=Path(r'C:\Users\Fabio\Desktop\HS Eletronicos')
files=[R/'01_Brandbook/HS_Eletronicos_Brandbook_v2.pdf',R/'06_Estrategia_e_PRD/HS_Eletronicos_PRD_v1.pdf']
for f in files:
 r=PdfReader(f);t='\n'.join(p.extract_text() for p in r.pages)
 assert all(x in t for x in ['Hugo','Belo Horizonte','24','catálogo'])
 assert '\ufffd' not in t
 assert '[F10] [F10]' not in t
 print(f.name,len(r.pages),'páginas; texto e dados confirmados OK')
b=json.loads((R/'06_Estrategia_e_PRD/Backlog_execucao.json').read_text(encoding='utf-8'))
assert len(b)==30 and len({x['id'] for x in b})==30
assert all(x['aceite'] and x['responsavel'] and x['testes'] for x in b)
print('Backlog: 30 IDs únicos com critérios de aceite e responsáveis.')
(R/'02_Identidade/logos/LEIA-ME_HISTORICO.md').write_text('''# Logos da proposta inicial rejeitada

Esta pasta contém os SVGs do primeiro conceito. Não usar na produção atual.

Referência vigente: ../Proposta_v6_Azul_Verde/HS_Eletronicos_Preto_Prata_Azul_Verde_v6.png.

Diretrizes: brandbook 2.0. O novo símbolo de placa ainda precisa da finalização vetorial especificada no PRD.
''',encoding='utf-8')
(R/'05_Fontes_e_QA/Entrega_v2/Relatorio_QA.md').write_text('''# Revisão da entrega documental

Data de referência: 02/10/2026.

## Arquivos revisados

- Brandbook 2.0: 32 páginas.
- PRD 1.0: 47 páginas.
- Backlog: 30 IDs únicos, responsáveis, dependências, critérios e testes.
- Calendário: 12 vídeos, 4 carrosséis e trailer inaugural adicional.

## Verificações concluídas

- Todas as páginas renderizadas em PNG; conjunto completo inspecionado por pranchas e amostra ampliada de páginas de texto, aplicação e referências.
- Sem blocos fora das áreas previstas; fonte com suporte aos acentos; texto extraível em todas as páginas.
- Dados coerentes: Hugo, Belo Horizonte e região, atendimento presencial e reparação 24h, site sem catálogo.
- Paleta atual: preto/prata com azul/verde. Referência visual v6.
- Fontes oficiais identificadas com links; limitação de acesso público à documentação do Instagram registrada.
- Backlog e roteiro não apresentados como tarefas executadas.
- Propostas antigas preservadas e sinalizadas como históricas.

## Limites da verificação

Esta revisão trata dos documentos. Não houve teste de site, contato comercial, contas, domínio ou métricas reais, pois esses produtos ainda não foram implementados. A referência da logomarca é raster; vetores e variantes de produção continuam como entregas especificadas, não concluídas.
''',encoding='utf-8')
