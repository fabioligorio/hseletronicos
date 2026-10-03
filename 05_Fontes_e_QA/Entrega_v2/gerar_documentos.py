from pathlib import Path
import re, json, math, html
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from pypdf import PdfReader
import pypdfium2 as pdfium
from PIL import Image, ImageDraw
R=Path(r'C:\Users\Fabio\Desktop\HS Eletronicos')
Q=R/'05_Fontes_e_QA/Entrega_v2'; Q.mkdir(exist_ok=True)
B=R/'01_Brandbook/HS_Eletronicos_Brandbook_v2.md'
P=R/'06_Estrategia_e_PRD/HS_Eletronicos_PRD_v1.md'
REF=R/'02_Identidade/Proposta_v6_Azul_Verde/HS_Eletronicos_Preto_Prata_Azul_Verde_v6.png'
for n,f in [('A','arial.ttf'),('AB','arialbd.ttf')]:pdfmetrics.registerFont(TTFont(n,'C:/Windows/Fonts/'+f))
BLACK='#101010'; SILVER='#BFC3C7'; LIGHT='#F5F5F5'; BLUE='#268CFF'; GREEN='#26C985'; TEXT='#40464D'
SOURCES=[
('F01','Vercel | Ambientes','https://vercel.com/docs/deployments/environments','Desenvolvimento, preview e produção; fundamenta a separação de ambientes.'),
('F02','Vercel | Plano Hobby','https://vercel.com/docs/plans/hobby','Restrição a uso pessoal não comercial. Plano comercial e custo devem ser definidos na contratação.'),
('F03','W3C | WCAG 2.2','https://www.w3.org/TR/WCAG22/','Referência normativa para acessibilidade; os critérios do projeto não constituem certificação.'),
('F04','web.dev | Web Vitals','https://web.dev/articles/vitals','Métricas e limiares de experiência. Valores do PRD são metas, não resultados já obtidos.'),
('F05','TikTok | Uso comercial de música','https://support.tiktok.com/en/business-and-creator/creator-and-business-accounts/commercial-use-of-music-on-tiktok','Direitos de áudio em conteúdo comercial; verificar licença, região e destino.'),
('F06','YouTube | Identidade do canal','https://support.google.com/youtube/answer/10456525?hl=pt-BR','Dimensões, tamanho de arquivo e recortes do banner.'),
('F07','YouTube | Shorts de três minutos','https://support.google.com/youtube/answer/15424877?hl=pt-BR','Regra de classificação de vídeos verticais/quadrados e duração. Cadência é decisão editorial.'),
('F08','Kwai | Central de segurança','https://www.kwai.com/safety?id=community','Ponto oficial de consulta; página dinâmica. Recursos e limites devem ser conferidos no aplicativo.'),
('F09','ANPD | Cookies e proteção de dados','https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/guia_orientativo_cookies_e_protecao_de_dados_pessoais','Referência orientativa; configuração concreta, finalidades e política devem ser validadas pelo responsável.'),
('F10','Next.js | Exportação estática','https://nextjs.org/docs/app/guides/static-exports','Base técnica para conteúdo estático; decidir pré-renderização ou exportação na implementação.'),
('F11','Instagram | Central de ajuda','https://www.facebook.com/help/instagram/138925576505882','Consulta redirecionou ao login. Tipo de conta, campos e recursos serão validados no app; formatos citados são matrizes internas, não limites oficiais verificados.')]
# Source registry is also available in editable form.
srcmd='# Fontes e método\n\nConsulta: 02/10/2026. Prioridade a documentação oficial. Estratégia, calendário, prazos e metas internas são propostas, não fatos estatísticos das plataformas.\n\n'
for id,t,u,n in SOURCES:srcmd+=f'## {id} | {t}\n\n[{t}]({u})\n\n{n}\n\n'
(R/'06_Estrategia_e_PRD/Fontes_e_referencias.md').write_text(srcmd,encoding='utf-8')
# Add specific source links by section and preserve local source authority.
ptext=P.read_text(encoding='utf-8-sig').replace('Não fixar versão sem inspeção do projeto. [F10]','Não fixar versão sem inspeção do projeto.').replace('Não fixar versão sem inspeção do projeto.','Não fixar versão sem inspeção do projeto. [F10]').replace('Propor conta profissional do tipo empresa e conferir opções reais no aplicativo.','Propor conta profissional do tipo empresa e conferir opções reais no aplicativo; documentação pública consultada exigiu login. [F11]')
P.write_text(ptext,encoding='utf-8')

def sections(path):
 parts=re.split(r'^## ',path.read_text(encoding='utf-8-sig'),flags=re.M)[1:]
 out=[]
 for part in parts:
  title,body=part.split('\n',1)
  blocks=[]
  matches=list(re.finditer(r'^\*\*(.*?)\*\*\s*\n',body,flags=re.M))
  for i,m in enumerate(matches):
   txt=body[m.end():matches[i+1].start() if i+1<len(matches) else len(body)].strip().replace('\\n',' / ')
   blocks.append((m.group(1),txt))
  out.append((title.strip(),blocks))
 return out
bs=sections(B); ps=sections(P)
assert len(bs)==23 and len(ps)==36
OVER=[]
def clean(s):return s.replace('–','-').replace('—','-').replace('\u2011','-')
def para(c,s,x,top,w,size=12,color=TEXT,bold=False,leading=None):
 p=Paragraph(html.escape(clean(s)).replace('\n','<br/>'),ParagraphStyle('p',fontName='AB' if bold else 'A',fontSize=size,leading=leading or size*1.4,textColor=HexColor(color),splitLongWords=1))
 _,h=p.wrap(w,2000);p.drawOn(c,x,top-h)
 if top-h<10:OVER.append((c.getPageNumber(),s[:60],top-h))
 return h

def bg(c,w,h,dark=False):
 c.setFillColor(HexColor(BLACK if dark else LIGHT));c.rect(0,0,w,h,fill=1,stroke=0)

def foot(c,w,label,dark=False):
 col=SILVER if dark else TEXT
 c.setStrokeColor(HexColor('#373B40' if dark else '#D6D9DC'));c.line(42,39,w-42,39)
 para(c,'HS ELETRÔNICOS  /  '+label,42,29,w-115,8,col)
 para(c,f'{c.getPageNumber():02}',w-70,29,30,8,col,True)

def circuit(c,x,y,w,h):
 for j,col in enumerate([BLUE,GREEN,SILVER]):
  c.setStrokeColor(HexColor(col));c.setFillColor(HexColor(col));c.setLineWidth(2)
  p=c.beginPath();p.moveTo(x,y+j*24);p.lineTo(x+w*.45,y+j*24);p.lineTo(x+w*.62,y+h*.48+j*24);p.lineTo(x+w,y+h*.48+j*24);c.drawPath(p);c.circle(x+w,y+h*.48+j*24,4,fill=1,stroke=0)

def cover(c,w,h,kind,version,sub):
 bg(c,w,h,True)
 para(c,'HS ELETRÔNICOS',44,h-47,w-88,15,SILVER,True)
 para(c,'BELO HORIZONTE E REGIÃO  /  HUGO  /  24H',44,h-82,w-88,9,SILVER)
 para(c,kind,44,h*.66,w-88,54 if w>700 else 42,LIGHT,True,58 if w>700 else 47)
 para(c,sub,46,h*.66-135,w-100,17,SILVER)
 circuit(c,46,100,w-100,100)
 para(c,version+'  •  02 OUT 2026',44,70,w-88,10,SILVER,True)
 c.showPage()

def heading(c,title,w,h,tag):
 bg(c,w,h)
 para(c,tag,44,h-34,w-88,9,BLUE,True)
 c.setFillColor(HexColor(GREEN));c.rect(w-94,h-44,50,4,fill=1,stroke=0)
 para(c,title,44,h-62,w-88,30 if w>700 else 24,BLACK,True)

def sectionland(c,title,blocks):
 w,h=1000,650;heading(c,title,w,h,'MANUAL DA MARCA / DIRETRIZES')
 for idx,(label,body) in enumerate(blocks):
  x=44+(idx%2)*470;top=510-(idx//2)*213
  c.setFillColor(HexColor('#FFFFFF'));c.roundRect(x,top-190,442,190,12,fill=1,stroke=0)
  c.setFillColor(HexColor(BLUE if idx%2==0 else GREEN));c.rect(x+20,top-28,24,3,fill=1,stroke=0)
  a=para(c,label,x+20,top-42,402,14,BLACK,True)
  b=para(c,body,x+20,top-48-a,402,12,TEXT)
  if a+b+55>190:OVER.append(('brand card',title,idx,a+b))
 foot(c,w,'BRANDBOOK 2.0');c.showPage()

def toc(c,entries,w,h,label):
 heading(c,'Guia de leitura',w,h,label)
 split=(len(entries)+1)//2
 for i,(t,pn) in enumerate(entries):
  col=i//split;row=i%split
  x=44+col*(w-88)/2;ww=(w-112)/2;top=h-133-row*30
  para(c,t,x,top,ww-38,10,BLACK)
  para(c,str(pn).zfill(2),x+ww-28,top,28,10,BLUE,True)
 foot(c,w,label);c.showPage()

def sourcepages(c,w,h,label,ids=None):
 data=[s for s in SOURCES if ids is None or s[0] in ids]
 per=5 if w>700 else 6
 for offset in range(0,len(data),per):
  heading(c,'Fontes e notas de produção',w,h,label)
  y=h-125
  for id,t,u,n in data[offset:offset+per]:
   a=para(c,f'{id} | {t}',44,y,w-88,12,BLACK,True);y-=a+6
   a=para(c,n,44,y,w-88,10,TEXT);y-=a+5
   # short visible title, clickable URL retained in PDF annotation
   a=para(c,'Abrir documentação oficial',44,y,w-88,9,BLUE);c.linkURL(u,(44,y-a,250,y),relative=0);y-=a+18
  para(c,'Consulta em 02/10/2026. Recursos de conta e recortes devem ser conferidos no aplicativo. Fontes completas em Fontes_e_referencias.md.',44,82,w-88,9,TEXT)
  foot(c,w,label);c.showPage()

def ratio(a,b):
 def lum(h):
  z=[int(h[i:i+2],16)/255 for i in (1,3,5)];v=[x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4 for x in z];return .2126*v[0]+.7152*v[1]+.0722*v[2]
 x,y=sorted([lum(a),lum(b)]);return (y+.05)/(x+.05)

c=canvas.Canvas(str(R/'01_Brandbook/HS_Eletronicos_Brandbook_v2.pdf'),pagesize=(1000,650));c.setTitle('HS Eletrônicos | Brandbook 2.0');c.setAuthor('HS Eletrônicos | Documento de projeto')
cover(c,1000,650,'Brandbook','VERSÃO 2.0','Identidade, linguagem e experiência de marca.\nPreto e prata. Azul e verde nos detalhes.')
heading(c,'A identidade de referência',1000,650,'PLACA ELETRÔNICA / PROPOSTA V6')
c.drawImage(str(REF),140,66,width=720,height=480,mask='auto')
foot(c,1000,'REFERÊNCIA RASTER / FINALIZAÇÃO VETORIAL NA PRODUÇÃO');c.showPage()
# Planned section page map with inserted visual plates.
extra_after={9:1,10:1,11:1,17:1,18:1}
entries=[];pn=4
for i,(t,bl) in enumerate(bs):entries.append((t,pn));pn+=1+extra_after.get(i,0)
toc(c,entries,1000,650,'BRANDBOOK 2.0')
for i,(t,blocks) in enumerate(bs):
 c.bookmarkPage('brand'+str(i));c.addOutlineEntry(t,'brand'+str(i),0);sectionland(c,t,blocks)
 if i==9:
  heading(c,'Preto e prata. Energia nos detalhes.',1000,650,'PALETA / REFERÊNCIAS DIGITAIS')
  colors=[('Preto',BLACK),('Prata',SILVER),('Prata claro','#E1E3E6'),('Branco frio',LIGHT),('Azul',BLUE),('Verde',GREEN)]
  for j,(name,col) in enumerate(colors):
   x=44+j*154;c.setFillColor(HexColor(col));c.setStrokeColor(HexColor('#D6D9DC'));c.roundRect(x,254,142,267,10,fill=1,stroke=1)
   fg=LIGHT if j==0 else BLACK;para(c,name,x+12,328,118,14,fg,True);para(c,col,x+12,295,118,12,fg)
  para(c,'Base neutra predominante. Azul e verde concentrados em trilhas, contatos e detalhes de apoio.',44,217,900,19,BLACK,True)
  para(c,'Cinza representa prata em tela. Acabamento metálico físico requer processo próprio e prova do fornecedor.',44,142,900,13,TEXT)
  foot(c,1000,'PALETA 2.0');c.showPage()
 if i==10:
  heading(c,'Combinações que sustentam a leitura',1000,650,'CONTRASTE / CÁLCULO SOBRE CORES SÓLIDAS')
  pairs=[(BLACK,LIGHT),(SILVER,BLACK),(BLACK,BLUE),(BLACK,GREEN),('#FFFFFF',BLUE),('#FFFFFF',GREEN)]
  for j,(fg,bgc) in enumerate(pairs):
   x=44+(j%3)*314;y=324-(j//3)*200;c.setFillColor(HexColor(bgc));c.roundRect(x,y,286,164,10,fill=1,stroke=0)
   rr=ratio(fg,bgc);para(c,'Aa  Assistência',x+16,y+131,254,20,fg,True);para(c,f'{rr:.2f}:1',x+16,y+80,254,24,fg,True)
   para(c,'Texto normal: '+('atende 4,5:1' if rr>=4.5 else 'não atende 4,5:1'),x+16,y+35,254,10,fg)
  foot(c,1000,'PALETA / WCAG 2.2 [F03]');c.showPage()
 if i==11:
  heading(c,'Hierarquia que explica',1000,650,'TIPOGRAFIA / ARIAL REGULAR E BOLD')
  para(c,'Cuidado técnico.\nConversa clara.',44,491,900,53,BLACK,True,60)
  para(c,'Assistência para celulares e eletrônicos',44,323,900,29,BLACK,True)
  para(c,'Hugo • Belo Horizonte e região • Atendimento presencial e reparação 24h',44,259,900,17,TEXT)
  para(c,'Entre em contato para combinar o atendimento e orientar a avaliação do seu aparelho.',44,207,770,16,TEXT)
  circuit(c,44,89,900,70);foot(c,1000,'TIPOGRAFIA DE COMUNICAÇÃO / LETTERING DA MARCA É PRÓPRIO');c.showPage()
 if i==17:
  heading(c,'Direção de interface',1000,650,'EXEMPLO CONCEITUAL / SITE DE SERVIÇOS SEM CATÁLOGO')
  c.setFillColor(HexColor(BLACK));c.roundRect(44,120,590,400,14,fill=1,stroke=0)
  para(c,'HS ELETRÔNICOS',68,490,450,16,SILVER,True)
  para(c,'Seu celular merece\natenção técnica.',68,423,520,38,LIGHT,True,45)
  para(c,'BH e região • Atendimento presencial e reparação 24h',68,300,490,15,SILVER)
  c.setFillColor(HexColor(BLUE));c.roundRect(68,182,245,50,9,fill=1,stroke=0);para(c,'Combinar atendimento',83,215,215,16,BLACK,True)
  c.setFillColor(HexColor('#FFFFFF'));c.roundRect(660,120,296,400,14,fill=1,stroke=0)
  para(c,'Como começar',684,484,248,26,BLACK,True)
  for j,txt in enumerate(['Informe o modelo','Descreva o sintoma','Combine a avaliação']):
   yy=414-j*85;c.setFillColor(HexColor(GREEN));c.circle(695,yy-7,10,fill=1,stroke=0);para(c,txt,716,yy+1,215,16,BLACK,True)
  para(c,'Exemplo de layout. Identidade completa será aplicada com os arquivos finais; fotos e canais reais ainda serão inseridos.',44,88,900,10,TEXT)
  foot(c,1000,'APLICAÇÃO / REFERÊNCIA DE COMPOSIÇÃO');c.showPage()
 if i==18:
  heading(c,'Uma linguagem em quatro canais',1000,650,'EXEMPLOS EDITORIAIS / CAPAS E VÍDEO')
  for j,(lab,title,col) in enumerate([('INSTAGRAM','Como funciona\na avaliação?',BLUE),('TIKTOK / KWAI','Sintoma não é\ndiagnóstico.',GREEN),('YOUTUBE','Conheça a HS\ne o Hugo.',SILVER)]):
   x=44+j*314;c.setFillColor(HexColor(BLACK));c.roundRect(x,110,286,410,12,fill=1,stroke=0)
   para(c,lab,x+20,485,246,11,col,True);para(c,title,x+20,402,246,31,LIGHT,True,37);circuit(c,x+20,210,246,70);para(c,'HS ELETRÔNICOS\nBH E REGIÃO • 24H',x+20,167,246,11,SILVER,True)
  foot(c,1000,'LAYOUTS CONCEITUAIS / CONTEÚDO E RECORTES A VALIDAR');c.showPage()
sourcepages(c,1000,650,'BRANDBOOK 2.0',{'F03','F05','F06','F08','F09'})
c.save()

# Operational backlog, traceable to PRD and tests.
raw=[
('BR-01','P0','Finalizar marca vetorial','Design','Brandbook 06-09','Referência v6','SVG/PDF sem fontes dependentes, variantes consistentes e prova de tamanho.','T11,T12'),
('BR-02','P0','Avatar, favicon e templates','Design','Brandbook 09/19','BR-01','Microversão legível, avatares circulares e capas revisadas.','T12,T16'),
('OPS-01','P0','Confirmar ficha comercial','Hugo','PRD 05','Nenhuma','Contato, local/procedimento, serviços e condições documentados; 24h sem promessa de prazo imediato.','T04,T13'),
('OPS-02','P0','Titularidade e acessos','Hugo','PRD 04/21','Nenhuma','URLs, e-mail de recuperação e 2FA registrados sem senhas no projeto.','T19'),
('WEB-01','P0','Navegação e responsividade','Desenvolvimento','PRD 11','Design de telas','Menu por teclado/toque, Escape e foco; sem overflow nos quatro tamanhos.','T01,T05,T06'),
('WEB-02','P0','Páginas e conteúdo aprovado','Conteúdo/Hugo','PRD 08-11','OPS-01','Rotas úteis e serviços confirmados; nenhuma interface de catálogo ou fato inventado.','T03,T04,T13'),
('WEB-03','P0','CTA contextual','Desenvolvimento','PRD 11/12','OPS-01','Destino real e mensagem do serviço sem envio automático ou dado privado.','T02'),
('WEB-04','P0','Estados vazios e erro','Desenvolvimento','PRD 11','WEB-01','404 útil, sem seção vazia, CTA ou formulário falso.','T07'),
('WEB-05','P0','Configurar contato e 24h','Hugo/Desenvolvimento','PRD 12','OPS-01','Número testado em três ambientes e redação coerente com atendimento presencial 24h.','T02,T04'),
('DS-01','P0','Componentes e tokens','Design/Desenvolvimento','PRD 13','BR-01','Estados, foco, contraste e tokens consistentes com brandbook.','T05,T11'),
('CMS-01','P0','Conteúdo versionado','Desenvolvimento','PRD 14','OPS-01','Validação de campos, rascunhos não públicos e instrução de edição.','T04,T13'),
('DEP-01','P0','Vercel e domínio','Desenvolvimento/Hugo','PRD 15','OPS-02','Plano comercial, DNS/HTTPS, preview e produção separados.','T01,T09'),
('ACC-01','P0','Navegação acessível','Desenvolvimento/QA','PRD 16','WEB-01','Teclado, semântica, skip link e zoom revisados manualmente.','T05,T06'),
('ACC-02','P0','Contraste e estados','Design/QA','PRD 16','DS-01','Contraste verificado; informação não depende apenas da cor.','T05,T11'),
('ACC-03','P0','Imagens e movimento','Conteúdo/QA','PRD 16','WEB-02','Alt e nomes acessíveis, movimento reduzido e legendas.','T05,T15'),
('PERF-01','P0','Desempenho','Desenvolvimento/QA','PRD 17','DEP-01','Três medições por template; mediana e limites documentados.','T10'),
('SEO-01','P0','SEO técnico/local','Desenvolvimento/Conteúdo','PRD 18','WEB-02','Metadados/sitemap e produção indexável, sem local fictício.','T09'),
('PRIV-01','P0','Privacidade e scripts','Hugo/Desenvolvimento','PRD 19','Analytics escolhido','Inventário e aviso verdadeiros; consentimento quando aplicável testado.','T08,T14'),
('ANA-01','P0','Eventos e UTMs','Desenvolvimento/Operação','PRD 20','PRIV-01','Eventos sem duplicação ou dados pessoais; clique separado de conversa.','T10'),
('SOC-01','P0','Padrão de contas','Operação/Hugo','PRD 21','OPS-02,BR-02','@ verificado, bio correta, proprietário e recuperação confirmados.','T17,T18,T19'),
('IG-01','P0','Configurar Instagram','Operação','PRD 22','SOC-01','Perfil, bio, contato, destaque real e peças inaugurais revisados.','T16,T17,T18,T20'),
('TT-01','P0','Configurar TikTok','Operação','PRD 23','SOC-01','Recursos reais, bio e três vídeos com áudio autorizado.','T15,T17,T18,T20'),
('KW-01','P0','Configurar Kwai','Operação','PRD 24','SOC-01','Campos documentados e três vídeos, sem depender de monetização.','T15,T17,T18,T20'),
('YT-01','P0','Configurar YouTube','Operação','PRD 25','SOC-01','Banner em recortes, descrição, trailer e três Shorts revisados.','T17,T18,T20,T21'),
('CNT-01','P0','Lote inaugural e calendário','Editorial/Hugo','PRD 26-30','OPS-01,BR-02','Três mestres, adaptações, trailer e carrossel com legendas e direitos.','T13,T14,T15,T20'),
('QA-01','P0','Aceite integrado','QA/Hugo','PRD 34','Todos os P0 de implementação','Evidências T01-T22, zero falha crítica de contato e acesso.','T01-T22'),
('REL-01','P0','Lançamento e handoff','Coordenação','PRD 35','QA-01','Domínio e canais finais verificados; recuperação e manual entregues.','T01,T02,T18,T22'),
('GROW-01','P1','Artigos e casos reais','Editorial','PRD 03','Lançamento','Conteúdo original, autorizado e alinhado às dúvidas medidas.','Revisão editorial'),
('FORM-01','P1','Formulário ou agenda','Produto/Desenvolvimento','PRD 12','Nova descoberta','Campos, retenção, operador e critérios específicos aprovados antes de implementar.','Plano de teste próprio'),
('COM-01','P2','Catálogo e comércio','Produto/Hugo','PRD 03','Novo escopo','Descoberta de estoque, atualização e condições; fora do MVP.','Plano de teste próprio')]
back=[dict(id=a,prioridade=b,entrega=d,responsavel=e,referencia=f,dependencias=g,aceite=h,testes=i,status='Não iniciado') for a,b,d,e,f,g,h,i in raw]
(R/'06_Estrategia_e_PRD/Backlog_execucao.json').write_text(json.dumps(back,ensure_ascii=False,indent=2),encoding='utf-8')
bmd='# Backlog de execução\n\nStatus inicial: não iniciado. Documentação concluída não equivale a implementação.\n\n'
for t in back:bmd+=f"## {t['id']} | {t['prioridade']} | {t['entrega']}\n\nResponsável: {t['responsavel']}. Referência: {t['referencia']}.\n\nDependências: {t['dependencias']}.\n\nAceite: {t['aceite']}\n\nTestes: {t['testes']}. Status: {t['status']}.\n\n"
(R/'06_Estrategia_e_PRD/Backlog_execucao.md').write_text(bmd,encoding='utf-8')

# PRD: concise numbered sections on portrait pages; appendix makes requirements executable.
w,h=595.28,841.89
c=canvas.Canvas(str(R/'06_Estrategia_e_PRD/HS_Eletronicos_PRD_v1.pdf'),pagesize=(w,h));c.setTitle('HS Eletrônicos | PRD de presença digital 1.0');c.setAuthor('HS Eletrônicos | Documento de projeto')
cover(c,w,h,'PRD\nPresença digital','VERSÃO 1.0','Site de serviços + Instagram, TikTok, Kwai e YouTube.\nRequisitos, operação e critérios de aceite.')
# two table-of-contents pages, accurate fixed pagination.
for offset in [0,18]:
 heading(c,'Guia de leitura',w,h,'PRD / SEÇÕES '+str(offset+1)+' A '+str(offset+18))
 y=712
 for ix in range(offset,offset+18):
  t=ps[ix][0];para(c,t,44,y,440,10,BLACK);para(c,f'{ix+4:02}',509,y,40,10,BLUE,True);y-=30
 if offset==18:para(c,'Apêndices: backlog de execução, fontes e notas de validação.',44,127,507,11,TEXT)
 foot(c,w,'PRD 1.0');c.showPage()
for idx,(title,blocks) in enumerate(ps):
 c.bookmarkPage('prd'+str(idx));c.addOutlineEntry(title,'prd'+str(idx),0)
 heading(c,title,w,h,'PRD / ESPECIFICAÇÃO DE PRODUTO')
 y=704
 for j,(lab,body) in enumerate(blocks):
  c.setFillColor(HexColor(BLUE if j%2==0 else GREEN));c.rect(44,y-4,21,3,fill=1,stroke=0)
  a=para(c,lab,44,y-16,w-88,12,BLACK,True);y-=a+24
  a=para(c,body,44,y,w-88,11,TEXT,leading=16);y-=a+24
 if y<70:OVER.append(('prd',title,y))
 para(c,'Referências de requisito e testes no backlog. Dados comerciais pendentes não devem ser inventados.',44,73,w-88,8,TEXT)
 foot(c,w,'PRD 1.0');c.showPage()
for offset in range(0,len(back),5):
 heading(c,'Backlog de execução',w,h,'APÊNDICE A / PRIORIDADE, RESPONSÁVEL E ACEITE')
 y=712
 for item in back[offset:offset+5]:
  a=para(c,f"{item['id']}  /  {item['prioridade']}  /  {item['entrega']}",44,y,w-88,12,BLACK,True);y-=a+5
  a=para(c,f"{item['responsavel']} • {item['referencia']} • Dep.: {item['dependencias']}",44,y,w-88,9,TEXT);y-=a+5
  a=para(c,item['aceite'],44,y,w-88,10,TEXT);y-=a+5
  a=para(c,'Testes: '+item['testes']+' | Não iniciado',44,y,w-88,8,BLUE);y-=a+19
 foot(c,w,'PRD 1.0 / APÊNDICE A');c.showPage()
sourcepages(c,w,h,'PRD 1.0 / APÊNDICE B')
c.save()
assert not OVER,OVER
print('PDFs gerados; nenhum bloco excedeu o espaço previsto.')
# Produce full-page previews + contact sheets for every page of each document.
report={}
for name,path in [('brandbook',R/'01_Brandbook/HS_Eletronicos_Brandbook_v2.pdf'),('prd',R/'06_Estrategia_e_PRD/HS_Eletronicos_PRD_v1.pdf')]:
 d=pdfium.PdfDocument(str(path));reader=PdfReader(path);thumbs=[]
 for i in range(len(d)):
  im=d[i].render(scale=1.0).to_pil().convert('RGB');im.save(Q/f'{name}-{i+1:02}.png');im.thumbnail((250,300));thumbs.append(im)
 for offset in range(0,len(thumbs),16):
  sheet=Image.new('RGB',(1040,1320),'#DDE1E4');dr=ImageDraw.Draw(sheet)
  for j,im in enumerate(thumbs[offset:offset+16]):
   x=10+(j%4)*260;y=10+(j//4)*330;sheet.paste(im,(x,y));dr.text((x+3,y+305),f'{name} {offset+j+1}',fill='black')
  sheet.save(Q/f'{name}-contato-{offset//16+1}.png')
 text='\n'.join(p.extract_text() for p in reader.pages)
 report[name]={'pages':len(d),'all_pages_have_text':all(len(p.extract_text())>30 for p in reader.pages),'text_characters':len(text),'pdf_bytes':path.stat().st_size,'path':str(path)}
(Q/'validacao_automatica.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(report,ensure_ascii=False,indent=2))

