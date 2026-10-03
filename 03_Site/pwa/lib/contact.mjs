export function normalizePhone(value) {
  const phone = String(value ?? '').replace(/\D/g, '');
  if (!/^55\d{10,11}$/.test(phone)) return null;
  return phone;
}
export function composeMessage({ category = 'Celular', model = '', symptom = '' } = {}) {
  const clean = (value, max) => String(value ?? '').replace(/[\u0000-\u001F\u007F]/g, ' ').trim().slice(0, max);
  const parts = ['Olá, Hugo! Vim pelo site da HS Eletrônicos e gostaria de combinar um atendimento.', `Equipamento: ${clean(category, 80)}.`];
  if (clean(model,80)) parts.push(`Modelo: ${clean(model,80)}.`);
  if (clean(symptom,500)) parts.push(`O que aconteceu: ${clean(symptom,500)}`);
  return parts.join('\n');
}
export function whatsappUrl(phone, message) {
  const valid = normalizePhone(phone);
  return valid ? `https://wa.me/${valid}?text=${encodeURIComponent(message)}` : null;
}
