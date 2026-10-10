const $ = (s) => document.querySelector(s);
const services = {
  web: { kicker: '01 — PRODUCTO DIGITAL', title: 'Desarrollo web', lead: 'Diseñamos plataformas rápidas, claras y preparadas para crecer junto con tu negocio.', number: '01', label: 'WEB SYSTEMS', foot: 'De la estrategia al código: creamos productos digitales que resuelven necesidades reales.', drawer: 'Servicios web', list: [
    { title: 'Sitios y e-commerce', detail: 'Presenta tu negocio con una experiencia clara, catálogo fácil de administrar y un proceso de compra preparado para convertir visitas en clientes.', tags: ['Diseño adaptable', 'Ventas en línea'], image: 0 },
    { title: 'Aplicaciones web a medida', detail: 'Digitalizamos procesos con herramientas creadas para tu operación: cotizadores, portales privados, paneles administrativos y más.', tags: ['A tu operación', 'Escalables'], image: 1 },
    { title: 'UX / UI y prototipado', detail: 'Definimos los flujos y la apariencia antes de programar para que el producto sea intuitivo para tus clientes y tu equipo.', tags: ['Experiencia clara', 'Prototipo visual'], image: 2 },
    { title: 'APIs y automatización', detail: 'Conectamos plataformas y automatizamos tareas repetitivas para reducir capturas manuales y mantener la información sincronizada.', tags: ['Integraciones', 'Menos tareas manuales'], image: 0 }
  ], images: ['https://images.unsplash.com/photo-1461749280684-dccba630e2f6?auto=format&fit=crop&w=1000&q=85', 'https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=700&q=85', 'https://images.unsplash.com/photo-1555099962-4199c345e5dd?auto=format&fit=crop&w=700&q=85'], alts: ['Código de una aplicación web', 'Diseñador desarrollando una web', 'Pantalla con código'] },
  data: { kicker: '02 — ARQUITECTURA', title: 'Bases de datos', lead: 'Transformamos información en un sistema ordenado y estructurado, para que tengas el control de todo en tu empresa.', number: '02', label: 'DATA ARCHITECTURE', foot: 'Organizamos, protegemos y conectamos el activo más valioso de tu empresa: sus datos.', drawer: 'Servicios de bases de datos', list: [
    { title: 'Modelado y normalización', detail: 'Diseñamos una estructura consistente para evitar duplicados, relacionar registros y hacer que la información sea confiable.', tags: ['Datos ordenados', 'Estructura clara'], image: 0 },
    { title: 'Migración de información', detail: 'Movemos tus datos desde hojas de cálculo o sistemas anteriores con un plan para validar su integridad durante el cambio.', tags: ['Migración segura', 'Validación'], image: 1 },
    { title: 'Dashboards y reportes', detail: 'Convertimos datos operativos en indicadores visuales para identificar tendencias y tomar decisiones con mayor claridad.', tags: ['Indicadores clave', 'Decisiones ágiles'], image: 2 },
    { title: 'Backups y seguridad', detail: 'Definimos respaldos y permisos de acceso adecuados para reducir riesgos y proteger la continuidad de tu operación.', tags: ['Respaldo', 'Accesos controlados'], image: 0 }
  ], images: ['https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=1000&q=85', 'https://images.unsplash.com/photo-1543286386-713bdd548da4?auto=format&fit=crop&w=700&q=85', 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=700&q=85'], alts: ['Tablero de datos', 'Visualización de métricas', 'Analítica de negocio'] },
  access: { kicker: '03 — SEGURIDAD FÍSICA', title: 'Control de acceso', lead: 'Integramos personas, espacios y reglas en una operación segura y visible.', number: '03', label: 'ACCESS CONTROL', foot: 'Controla entradas, horarios y permisos con una solución conectada a tu negocio.', drawer: 'Servicios de control de acceso', list: [
    { title: 'Biométricos y lectores', detail: 'Administra entradas con credenciales o dispositivos biométricos, asignando permisos según perfiles y horarios.', tags: ['Acceso controlado', 'Permisos por perfil'], image: 0 },
    { title: 'Control de visitantes', detail: 'Lleva un registro claro de visitas, autorizaciones y horarios para cuidar tus instalaciones y saber quién está dentro.', tags: ['Registro digital', 'Trazabilidad'], image: 1 },
    { title: 'Reportes en tiempo real', detail: 'Consulta eventos e incidencias desde una vista central para responder con rapidez y tener mejor visibilidad de tus espacios.', tags: ['Visibilidad', 'Alertas útiles'], image: 2 },
    { title: 'Integración con nómina', detail: 'Conecta registros de asistencia con tus procesos administrativos para reducir capturas repetidas y simplificar los cierres.', tags: ['Menos captura', 'Flujos conectados'], image: 0 }
  ], images: ['https://images.unsplash.com/photo-1557597774-9d273605dfa9?auto=format&fit=crop&w=1000&q=85', 'https://images.unsplash.com/photo-1563013544-824ae1b704d3?auto=format&fit=crop&w=700&q=85', 'https://images.unsplash.com/photo-1633265486064-086b219458ec?auto=format&fit=crop&w=700&q=85'], alts: ['Acceso seguro a un edificio', 'Tecnología de seguridad', 'Cerradura inteligente'] },
  pos: { kicker: '04 — COMERCIO CONECTADO', title: 'Punto de venta', lead: 'Una caja ágil y una operación ordenada, desde el inventario hasta el último ticket.', number: '04', label: 'POS ECOSYSTEM', foot: 'Centraliza ventas, clientes e inventario para que tu equipo pueda enfocarse en atender.', drawer: 'Servicios de punto de venta', list: [
    { title: 'Ventas e inventario', detail: 'Registra ventas y actualiza existencias en un mismo flujo para saber qué se vende, qué queda y qué debes reponer.', tags: ['Existencias claras', 'Operación ágil'], image: 0 },
    { title: 'Facturación y cortes', detail: 'Organiza cierres de caja y consulta los movimientos del día con reportes que ayudan a cuadrar la operación.', tags: ['Cierres simples', 'Reportes'], image: 1 },
    { title: 'Multi-sucursal', detail: 'Centraliza productos y consulta resultados de distintas ubicaciones para mantener una operación consistente al crecer.', tags: ['Varias ubicaciones', 'Vista central'], image: 2 },
    { title: 'CRM y lealtad', detail: 'Conoce mejor a tus clientes, conserva su historial y crea beneficios para impulsar que vuelvan a comprar.', tags: ['Historial de clientes', 'Fidelización'], image: 0 }
  ], images: ['https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?auto=format&fit=crop&w=1000&q=85', 'https://images.unsplash.com/photo-1556740749-887f6717d7e4?auto=format&fit=crop&w=700&q=85', 'https://images.unsplash.com/photo-1528698827591-e19ccd7bc23d?auto=format&fit=crop&w=700&q=85'], alts: ['Pago con terminal', 'Compra con tarjeta', 'Tienda moderna'] }
};
let currentScreen = $('#inicio'), isChanging = false;
function show(id) { if (isChanging || currentScreen.id === id) return; isChanging = true; const next = $('#' + id), wipe = $('#pageTransition'); wipe.classList.add('run'); setTimeout(() => { currentScreen.classList.remove('active'); next.classList.add('active'); currentScreen = next; next.scrollTop = 0; window.scrollTo(0, 0) }, 260); setTimeout(() => { wipe.classList.remove('run'); isChanging = false }, 820) }
function populateCollage(d) { const imageIds = ['collageMain', 'collageTop', 'collageBottom']; imageIds.forEach((id, index) => { $('#' + id).src = d.images[index]; $('#' + id).alt = d.alts[index] }) }
const serviceModal = $('#serviceModal');
let currentService = null;
let serviceOpener = null;
function renderServiceAccordion(service) {
  const list = $('#serviceAccordionList');
  list.replaceChildren();
  service.list.forEach((item, index) => {
    const article = document.createElement('article');
    article.className = 'service-accordion-item';
    const trigger = document.createElement('button');
    const panelId = `serviceDetail-${index}`;
    trigger.type = 'button';
    trigger.className = 'service-accordion-trigger';
    trigger.setAttribute('aria-expanded', 'false');
    trigger.setAttribute('aria-controls', panelId);
    const title = document.createElement('span');
    title.className = 'service-accordion-title';
    title.textContent = item.title;
    const marker = document.createElement('span');
    marker.className = 'service-accordion-marker';
    marker.setAttribute('aria-hidden', 'true');
    marker.textContent = '+';
    trigger.append(title, marker);

    const panel = document.createElement('div');
    panel.className = 'service-accordion-panel';
    panel.id = panelId;
    panel.setAttribute('role', 'region');
    panel.setAttribute('aria-label', item.title);
    panel.setAttribute('aria-hidden', 'true');
    const content = document.createElement('div');
    content.className = 'service-accordion-content';
    const image = document.createElement('img');
    image.className = 'service-accordion-image';
    image.src = service.images[item.image ?? index % service.images.length];
    image.alt = service.alts[item.image ?? index % service.alts.length];
    image.loading = 'lazy';
    const copy = document.createElement('div');
    copy.className = 'service-accordion-copy';
    const description = document.createElement('p');
    description.textContent = item.detail;
    const tags = document.createElement('div');
    tags.className = 'service-accordion-tags';
    item.tags.forEach(label => {
      const tag = document.createElement('span');
      tag.textContent = label;
      tags.append(tag);
    });
    copy.append(description, tags);
    content.append(image, copy);
    panel.append(content);
    trigger.addEventListener('click', () => {
      const expanded = trigger.getAttribute('aria-expanded') === 'true';
      trigger.setAttribute('aria-expanded', String(!expanded));
      panel.setAttribute('aria-hidden', String(expanded));
      article.classList.toggle('expanded', !expanded);
    });
    article.append(trigger, panel);
    list.append(article);
  });
}
function openServiceModal(service, opener = document.activeElement) {
  if (!service) return;
  serviceOpener = opener;
  serviceModal.dataset.service = Object.keys(services).find(key => services[key] === service) || 'web';
  $('#serviceModalNumber').textContent = `${service.number} — ${service.label}`;
  $('#serviceModalKicker').textContent = service.kicker;
  $('#serviceDialogTitle').textContent = service.drawer;
  $('#serviceDialogIntro').textContent = service.lead;
  renderServiceAccordion(service);
  serviceModal.classList.add('open');
  serviceModal.setAttribute('aria-hidden', 'false');
  serviceModal.inert = false;
  document.body.classList.add('service-modal-open');
  requestAnimationFrame(() => $('#closeServiceModal').focus());
}
function closeServiceModal(restoreFocus = true) {
  if (!serviceModal.classList.contains('open')) return;
  serviceModal.classList.remove('open');
  serviceModal.setAttribute('aria-hidden', 'true');
  serviceModal.inert = true;
  document.body.classList.remove('service-modal-open');
  if (restoreFocus) serviceOpener?.focus();
}
const siteMenu = $('#siteMenu');
const menuToggle = $('#menuButton');
const menuPanel = $('.site-menu-panel');
function openSiteMenu() {
  siteMenu.classList.add('open');
  siteMenu.setAttribute('aria-hidden', 'false');
  menuToggle.setAttribute('aria-expanded', 'true');
  menuToggle.setAttribute('aria-label', 'Cerrar menú');
  setTimeout(() => $('#closeMenu').focus(), 0);
}
function closeSiteMenu(restoreFocus = true) {
  siteMenu.classList.remove('open');
  siteMenu.setAttribute('aria-hidden', 'true');
  menuToggle.setAttribute('aria-expanded', 'false');
  menuToggle.setAttribute('aria-label', 'Abrir menú');
  if (restoreFocus) menuToggle.focus();
}
menuToggle.addEventListener('click', () => siteMenu.classList.contains('open') ? closeSiteMenu() : openSiteMenu());
$('#closeMenu').addEventListener('click', () => closeSiteMenu());
$('#menuBackdrop').addEventListener('click', () => closeSiteMenu());
menuPanel.addEventListener('click', event => {
  const item = event.target.closest('[data-menu-screen], [data-menu-service]');
  if (!item) return;
  closeSiteMenu();
  if (item.dataset.menuService) {
    document.querySelector(`.service-trigger[data-service="${item.dataset.menuService}"]`)?.click();
  } else {
    show(item.dataset.menuScreen);
  }
});
$('#menuQuote').addEventListener('click', () => {
  closeSiteMenu();
  openModal();
});
const aboutCards = [...document.querySelectorAll('.about-card')];
if ('IntersectionObserver' in window) {
  const aboutObserver = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('in-view');
      aboutObserver.unobserve(entry.target);
    });
  }, { threshold: .12, rootMargin: '0px 0px -24px 0px' });
  aboutCards.forEach(card => aboutObserver.observe(card));
} else {
  aboutCards.forEach(card => card.classList.add('in-view'));
}
document.addEventListener('keydown', event => {
  if (!siteMenu.classList.contains('open')) return;
  if (event.key === 'Escape') { closeSiteMenu(); return; }
  if (event.key !== 'Tab') return;
  const focusable = [...menuPanel.querySelectorAll('button, a[href], input, textarea, [tabindex]:not([tabindex="-1"])')]
    .filter(element => !element.disabled);
  if (!focusable.length) return;
  const first = focusable[0], last = focusable[focusable.length - 1];
  if (event.shiftKey && document.activeElement === first) { event.preventDefault(); last.focus(); }
  else if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first.focus(); }
});
document.querySelectorAll('.service-trigger').forEach(btn => btn.addEventListener('click', () => { const d = services[btn.dataset.service]; currentService = d; btn.classList.add('is-selected'); setTimeout(() => btn.classList.remove('is-selected'), 650); $('#detailKicker').textContent = d.kicker; $('#detailTitle').textContent = d.title; $('#detailLead').textContent = d.lead; $('#detailNumber').textContent = d.number; $('#detailLabel').textContent = d.label; $('#detailFoot').textContent = d.foot; populateCollage(d); show('detail') }));
document.querySelectorAll('.back-home').forEach(b => b.addEventListener('click', () => show('inicio'))); $('#backButton').addEventListener('click', () => show('inicio')); $('#aboutButton').addEventListener('click', () => show('about')); $('#faqButton').addEventListener('click', () => show('faq'));
$('#moreButton').addEventListener('click', () => openServiceModal(currentService));
$('#closeServiceModal').addEventListener('click', () => closeServiceModal());
$('#serviceBackdrop').addEventListener('click', () => closeServiceModal());
$('#serviceQuote').addEventListener('click', () => {
  closeServiceModal(false);
  $('#moreButton').focus();
  openModal();
});
serviceModal.addEventListener('keydown', event => {
  if (event.key === 'Escape') { closeServiceModal(); return; }
  if (event.key !== 'Tab') return;
  const focusable = [...serviceModal.querySelectorAll('button:not([disabled]):not([tabindex="-1"])')];
  if (!focusable.length) return;
  const first = focusable[0], last = focusable[focusable.length - 1];
  if (event.shiftKey && document.activeElement === first) { event.preventDefault(); last.focus(); }
  else if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first.focus(); }
});
const modal = $('#contactModal');
const quoteSteps = [...document.querySelectorAll('.quote-step')];
const quoteAnswers = {};
let quoteStep = 0;
let quoteOpener = null;
function renderQuoteStep() {
  quoteSteps.forEach((step, index) => {
    step.hidden = index !== quoteStep;
    step.classList.toggle('active', index === quoteStep);
  });
  $('#quoteStepLabel').textContent = `PASO ${quoteStep + 1} DE ${quoteSteps.length}`;
  $('#quoteProgress').style.width = `${((quoteStep + 1) / quoteSteps.length) * 100}%`;
  $('#quoteBack').hidden = quoteStep === 0;
  $('#quoteNext').innerHTML = quoteStep === quoteSteps.length - 1 ? 'PREPARAR WHATSAPP <b>↗</b>' : 'CONTINUAR <b>→</b>';
  $('#quoteError').hidden = true;
}
function openModal() {
  quoteStep = 0;
  quoteOpener = document.activeElement;
  Object.keys(quoteAnswers).forEach(key => delete quoteAnswers[key]);
  document.querySelectorAll('.quote-step input[type="radio"]').forEach(input => { input.checked = false });
  $('#quoteName').value = '';
  $('#quoteNotes').value = '';
  modal.classList.add('open');
  modal.setAttribute('aria-hidden', 'false');
  renderQuoteStep();
  setTimeout(() => $('#closeModal').focus(), 0);
}
function closeModal() {
  modal.classList.remove('open');
  modal.setAttribute('aria-hidden', 'true');
  quoteOpener?.focus();
}
$('#heroContact').addEventListener('click', openModal);
$('#detailContact').addEventListener('click', openModal);
document.querySelectorAll('.about-contact').forEach(x => x.addEventListener('click', openModal));
$('#closeModal').addEventListener('click', closeModal);
modal.addEventListener('click', e => { if (e.target === modal) closeModal() });
document.addEventListener('keydown', e => {
  if (!modal.classList.contains('open')) return;
  if (e.key === 'Escape') { closeModal(); return; }
  if (e.key !== 'Tab') return;
  const focusable = [...modal.querySelectorAll('button, input, textarea, a[href], [tabindex]:not([tabindex="-1"])')]
    .filter(el => !el.disabled && !el.closest('[hidden]'));
  if (!focusable.length) return;
  const first = focusable[0], last = focusable[focusable.length - 1];
  if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
  else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
});
$('#quoteBack').addEventListener('click', () => { if (quoteStep > 0) { quoteStep--; renderQuoteStep() } });
$('#quoteNext').addEventListener('click', () => {
  const selected = document.querySelector(`.quote-step[data-step="${quoteStep}"] input[type="radio"]:checked`);
  if (quoteStep < quoteSteps.length - 1 && !selected) {
    $('#quoteError').hidden = false;
    return;
  }
  if (selected) quoteAnswers[selected.name] = selected.value;
  if (quoteStep < quoteSteps.length - 1) {
    quoteStep++;
    renderQuoteStep();
    document.querySelector('.quote-step.active h2')?.focus();
    return;
  }
  const name = $('#quoteName').value.trim();
  const notes = $('#quoteNotes').value.trim();
  const message = [
    'Hola, MACROSAP. Quiero cotizar un proyecto.',
    '',
    `Tipo de proyecto: ${quoteAnswers.project}`,
    `Objetivo: ${quoteAnswers.goal}`,
    `Tamaño / alcance: ${quoteAnswers.scale}`,
    `Sistemas actuales: ${quoteAnswers.systems}`,
    `Tiempo para comenzar: ${quoteAnswers.timeline}`,
    `Presupuesto estimado: ${quoteAnswers.budget}`,
    `Implementación / soporte: ${quoteAnswers.support}`,
    name && `Nombre / empresa: ${name}`,
    notes && `Detalles: ${notes}`
  ].filter(Boolean).join('\n');
  window.open(`https://wa.me/525551064052?text=${encodeURIComponent(message)}`, '_blank', 'noopener');
});
let slide = 0; const slides = document.querySelectorAll('.slide'), dots = document.querySelectorAll('.slider-dots b'); setInterval(() => { slides[slide].classList.remove('active'); dots[slide].classList.remove('active'); slide = (slide + 1) % slides.length; slides[slide].classList.add('active'); dots[slide].classList.add('active'); $('#slideCount').textContent = `0${slide + 1} / 03` }, 3800); dots[0].classList.add('active');
