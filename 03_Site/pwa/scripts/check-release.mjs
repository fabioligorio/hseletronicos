import fs from 'node:fs/promises';import {normalizePhone} from '../lib/contact.mjs';
const b=JSON.parse(await fs.readFile('lib/business.json','utf8'));const issues=[];
if(!normalizePhone(b.whatsapp))issues.push('WhatsApp inválido.');
if(!b.siteUrl||!/^https:\/\//.test(b.siteUrl))issues.push('Definir o domínio HTTPS real em siteUrl.');
if(!b.releaseApproved)issues.push('Revisar conteúdo e privacidade com Hugo e marcar releaseApproved.');
if(issues.length){console.error('Publicação ainda pendente:\n- '+issues.join('\n- '));process.exitCode=1;}else{console.log('Configuração de publicação pronta. Execute build e testes antes do deploy.');}
