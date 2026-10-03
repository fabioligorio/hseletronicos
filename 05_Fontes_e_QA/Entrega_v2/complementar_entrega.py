from pathlib import Path
import json,re,shutil
R=Path(r'C:\Users\Fabio\Desktop\HS Eletronicos')
B=R/'01_Brandbook/HS_Eletronicos_Brandbook_v2.md'
s=B.read_text(encoding='utf-8-sig').replace('Item vendido deve mudar de estado no catálogo e nas peças de oferta.','Item vendido deve ser retirado das ofertas ativas; em um futuro catálogo, atualizar também seu estado. O site inicial será de serviços, sem catálogo.')
B.write_text(s,encoding='utf-8')
P=R/'06_Estrategia_e_PRD/HS_Eletronicos_PRD_v1.md'
s=P.read_text(encoding='utf-8-sig');s=re.sub(r'(\[F10\]\s*){2,}','[F10] ',s);P.write_text(s,encoding='utf-8')
G=R/'05_Fontes_e_QA/Entrega_v2/gerar_documentos.py'
s=G.read_text(encoding='utf-8-sig').replace("per=5 if w>700 else 5","per=5 if w>700 else 6")
s=s.replace("ptext=P.read_text(encoding='utf-8-sig').replace('Não fixar versão sem inspeção do projeto.','Não fixar versão sem inspeção do projeto. [F10]')","ptext=P.read_text(encoding='utf-8-sig').replace('Não fixar versão sem inspeção do projeto. [F10]','Não fixar versão sem inspeção do projeto.').replace('Não fixar versão sem inspeção do projeto.','Não fixar versão sem inspeção do projeto. [F10]')")
G.write_text(s,encoding='utf-8')
# Keep the superseded implementation briefing available as history.
old=R/'03_Site/Briefing.md'; hist=R/'03_Site/Briefing_v1_historico.md'
if old.exists() and not hist.exists():shutil.copy2(old,hist)
old.write_text('''# Site de serviços | Direção vigente

A fonte de verdade é ../06_Estrategia_e_PRD/HS_Eletronicos_PRD_v1.md e seu PDF.

- Site inicial de serviços, sem catálogo, carrinho ou pagamento on-line.
- Responsável: Hugo.
- Área: Belo Horizonte e região; endereço físico ainda não informado.
- Atendimento presencial e reparação 24h, conforme confirmação do usuário.
- CTA: Combinar atendimento. WhatsApp comercial ainda pendente.
- Hospedagem prevista na Vercel, em plano compatível com uso comercial.
- Identidade: placa eletrônica, preto/prata e detalhes azul/verde; brandbook 2.0.

Briefing_v1_historico.md registra uma direção anterior e não deve orientar implementação.
''',encoding='utf-8')
tok=R/'02_Identidade/tokens.css';hist=R/'02_Identidade/tokens_v1_historico.css'
if tok.exists() and not hist.exists():shutil.copy2(tok,hist)
tok.write_text('''/* HS Eletrônicos | Brandbook 2.0 | Paleta de referência */
:root {
  --hs-black: #101010;
  --hs-silver: #BFC3C7;
  --hs-silver-light: #E1E3E6;
  --hs-white: #F5F5F5;
  --hs-blue: #268CFF;
  --hs-green: #26C985;
  --hs-text: #101010;
  --hs-background: #F5F5F5;
  --hs-action-bg: #268CFF;
  --hs-action-text: #101010;
  --hs-font: Arial, Helvetica, sans-serif;
  --hs-radius: 16px;
  --hs-space: 8px;
}
''',encoding='utf-8')
config={'brandName':'HS Eletrônicos','responsibleName':'Hugo','serviceArea':'Belo Horizonte e região','hoursLabel':'Atendimento presencial e reparação 24 horas','hoursMode':'presencial_reparacao_24h','hoursSource':'Confirmado pelo usuário nesta conversa','physicalAddress':None,'whatsapp':None,'email':None,'domain':None,'socialLinks':{'instagram':None,'tiktok':None,'kwai':None,'youtube':None},'siteScope':'servicos_sem_catalogo','publicationReady':False,'missing':['Canal comercial','Local ou procedimento para combinar atendimento','Serviços específicos','Domínio e contas','Condições comerciais','Política de dados','Assets finais'],'notes':'Dados de planejamento. Null significa não informado. Não publicar campos pendentes nem prometer conclusão imediata do reparo.'}
(R/'06_Estrategia_e_PRD/Ficha_negocio.json').write_text(json.dumps(config,ensure_ascii=False,indent=2),encoding='utf-8')
posts=[
(1,'V01','Apresentação de Hugo','Seu celular apresentou um problema?','Hugo se apresenta, situa BH e região e explica o foco em celulares/iPhones.','Combinar atendimento','Retrato e bancada real'),
(1,'V02','Como combinar atendimento 24h','Precisou de assistência fora do horário comum?','Explicar presencial/reparação 24h e contato prévio para combinar local.','Falar com Hugo','Canal e procedimento confirmados'),
(1,'V03','Informações para iniciar','Três informações ajudam a começar.','Modelo, sintoma e quando começou. Não pedir senhas.','Solicitar orientação','Aparelho de demonstração'),
(1,'C01','Conheça a HS em cinco quadros','Assistência em BH e região','Nome, celulares, iPhones, 24h, contato.','Combinar atendimento','Categorias confirmadas'),
(2,'V04','Sintoma não é diagnóstico','O mesmo sintoma pode ter causas diferentes.','Explicar necessidade de avaliação sem indicar diagnóstico universal.','Solicitar avaliação','Revisão técnica de Hugo'),
(2,'V05','Por que testar','Trocar uma peça começa por entender o problema.','Mostrar uma etapa de teste real adotada pela HS.','Conhecer o processo','Rotina real e autorização'),
(2,'V06','Dados em imagens','Antes de mostrar seu aparelho, cuide dos seus dados.','Ocultar notificações e identificadores ao enviar imagens.','Salvar a orientação','Demonstração sem dados reais'),
(2,'C02','Etapas do atendimento','O que acontece depois do contato?','Contato, avaliação, orçamento, autorização e entrega conforme rotina real.','Falar com a HS','Fluxo validado por Hugo'),
(3,'V07','Detalhe de bancada','O que este instrumento ajuda a verificar?','Hugo explica uma ferramenta realmente usada, sem tutorial arriscado.','Enviar uma dúvida','Ferramenta e uso confirmados'),
(3,'V08','Dúvida sobre iPhone','Uma dúvida comum de quem usa iPhone.','Responder pergunta real; separar sinais percebidos de diagnóstico.','Solicitar avaliação','Pergunta e resposta validadas'),
(3,'V09','Escolher seminovo','Antes de escolher, confira estas informações.','Estado, capacidade, acessórios e verificações, sem produto fictício.','Consultar a HS','Item real ou abordagem educativa'),
(3,'C03','Compra e venda','A HS também compra e vende eletrônicos.','Explicar avaliação e informações para consulta sem listar estoque.','Consultar condições','Condições comerciais confirmadas'),
(4,'V10','Autorizar um serviço','O que perguntar antes de autorizar?','Escopo, valor, previsão e condições.','Salvar e conversar','Revisão de Hugo'),
(4,'V11','Resposta à comunidade','Você perguntou, Hugo responde.','Selecionar dúvida real sem identificar cliente.','Comentar dúvida geral','Pergunta real anonimizada'),
(4,'V12','Contato e atendimento','Como combinar seu atendimento com a HS.','Explicar canal e local/procedimento confirmados, inclusive no plantão.','Combinar atendimento','Canal e operação testados'),
(4,'C04','Dúvidas do mês','As perguntas que mais recebemos','Resumir dúvidas reais; se não houver amostra, usar perguntas frequentes validadas.','Falar com a HS','Revisão editorial')]
cal='# Calendário operacional | 4 semanas\n\nSem datas fixas: semana 1 começa no lançamento. Cadência proposta, dependente da capacidade de Hugo/equipe. Vídeos: Instagram, TikTok, Kwai e YouTube Shorts; carrosséis: Instagram. Adaptar áudio, título e recorte. Não publicar enquanto dependências não forem atendidas.\n\n'
for wk,id,t,hook,body,cta,dep in posts:
 cal+=f'## Semana {wk} | {id} | {t}\n\nGancho: {hook}\n\nConteúdo: {body}\n\nCTA: {cta}. Dependência: {dep}.\n\nFormato: '+('vídeo vertical de 20-45 s; mestre limpo e versões por rede' if id.startswith('V') else 'carrossel de 5-7 quadros')+'.\n\nResponsável técnico: Hugo. Produção/publicação: a designar. Status: roteiro proposto.\n\n'
cal+='## Trailer do YouTube | entrega inaugural adicional\n\n45-60 s: Hugo se apresenta; explica escopo, BH e região e atendimento presencial/reparação 24h; mostra bancada real; convida a combinar atendimento. Captação horizontal própria, legendas revisadas e contato confirmado. Não contar como um dos três Shorts inaugurais.\n'
(R/'04_Redes_Sociais/Calendario_4_semanas_v2.md').write_text(cal,encoding='utf-8')
old=R/'04_Redes_Sociais/Direcao_e_roteiros.md';hist=R/'04_Redes_Sociais/Direcao_e_roteiros_v1_historico.md'
if old.exists() and not hist.exists():shutil.copy2(old,hist)
old.write_text('''# Direção de redes vigente

Consultar o PRD 1.0, seções 21-30, e Calendario_4_semanas_v2.md.

Canais: Instagram, TikTok, Kwai e YouTube. Marca: placa eletrônica, preto/prata com azul/verde. Hugo; BH e região; atendimento presencial e reparação 24h. Contato e local ainda não informados.

O arquivo v1_historico conserva as primeiras propostas. Não utilizar as cores ou roteiros antigos sem revisão.
''',encoding='utf-8')
(R/'LEIA-ME.md').write_text('''# HS Eletrônicos | Entrega documental vigente

## Comece por aqui

1. [Brandbook 2.0](01_Brandbook/HS_Eletronicos_Brandbook_v2.pdf) - 32 páginas de estratégia, identidade, linguagem e aplicações.
2. [PRD de presença digital](06_Estrategia_e_PRD/HS_Eletronicos_PRD_v1.pdf) - requisitos para site de serviços e Instagram, TikTok, Kwai e YouTube.
3. [Backlog de execução](06_Estrategia_e_PRD/Backlog_execucao.md) - prioridades, dependências e critérios de aceite.
4. [Calendário de quatro semanas](04_Redes_Sociais/Calendario_4_semanas_v2.md) - 12 vídeos, 4 carrosséis e trailer adicional.

## Decisões confirmadas

- Responsável: Hugo.
- Área de atendimento: Belo Horizonte e região. Endereço físico não informado.
- Atendimento presencial e reparação 24 horas; conclusão depende de avaliação e condições reais.
- Site inicial de serviços, sem catálogo. Hospedagem prevista na Vercel.
- Marca: placa eletrônica; preto e prata, azul e verde nos detalhes. Referência visual v6.

## Arquivos e limites

Os PDFs têm versões editáveis Markdown. Fontes oficiais estão em 06_Estrategia_e_PRD/Fontes_e_referencias.md. Ficha_negocio.json registra dados confirmados e pendências. Tokens CSS foram atualizados.

A logo atual é uma apresentação raster. Vetores, microversão e assets finais são entregáveis de produção especificados no PRD. Nenhum perfil foi criado, site publicado ou conteúdo enviado nesta etapa.

Brandbook v1, propostas v1-v5 e arquivos com sufixo historico estão preservados. Não devem orientar a produção atual. O gerador antigo gerar_brandbook.py recria a identidade rejeitada e não deve ser executado para atualizar esta entrega.

## Revisão

Gerador atual, renderizações e relatório: 05_Fontes_e_QA/Entrega_v2. Atualizar as fontes Markdown e executar gerar_documentos.py para regenerar os PDFs; script não cria perfis nem publica nada.
''',encoding='utf-8')
print('Fontes e arquivos de apoio atualizados.')
