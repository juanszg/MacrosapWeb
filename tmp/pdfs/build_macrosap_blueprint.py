from reportlab.lib import colors
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from pathlib import Path

ROOT = Path(r'C:\Users\JuanA\OneDrive\Escritorio\ALPHYFY STUDIOS\MACROSAP\outputs')
OUT = ROOT / 'pdf' / 'MACROSAP_Blueprint_Proyecto.pdf'
TMP = ROOT / 'tmp' / 'pdfs'
TMP.mkdir(parents=True, exist_ok=True)
OUT.parent.mkdir(parents=True, exist_ok=True)

# Use Windows UI fonts for complete Spanish glyph support.
FONT_REG = r'C:\Windows\Fonts\segoeui.ttf'
FONT_BOLD = r'C:\Windows\Fonts\segoeuib.ttf'
if not Path(FONT_REG).exists(): FONT_REG = r'C:\Windows\Fonts\arial.ttf'
if not Path(FONT_BOLD).exists(): FONT_BOLD = r'C:\Windows\Fonts\arialbd.ttf'
pdfmetrics.registerFont(TTFont('Blueprint', FONT_REG))
pdfmetrics.registerFont(TTFont('Blueprint-Bold', FONT_BOLD))

INK = HexColor('#08243A')
ELECTRIC = HexColor('#146EF5')
LIME = HexColor('#D8FF55')
ICE = HexColor('#E7F7FA')
BLUE = HexColor('#B9E2F2')
GREEN = HexColor('#16894F')
ORANGE = HexColor('#FF6845')
PAPER = HexColor('#F7F7F1')
MUTED = HexColor('#547083')
LINE = HexColor('#D5E0E2')
WHITE = colors.white
PAGE_W, PAGE_H = A4

class BlueprintCanvas(Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []
    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()
    def save(self):
        n = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self._draw_page_number(n)
            Canvas.showPage(self)
        Canvas.save(self)
    def _draw_page_number(self, total):
        p = self._pageNumber
        if p == 1:
            return
        self.saveState()
        self.setStrokeColor(LINE); self.setLineWidth(.5)
        self.line(18*mm, 17*mm, PAGE_W-18*mm, 17*mm)
        self.setFont('Blueprint', 7.5); self.setFillColor(MUTED)
        self.drawString(18*mm, 11*mm, 'MACROSAP  /  BLUEPRINT DEL PROYECTO')
        self.drawRightString(PAGE_W-18*mm, 11*mm, f'{p:02d}  /  {total:02d}')
        self.restoreState()

def page_bg(c, doc):
    p = c.getPageNumber()
    c.saveState()
    if p == 1:
        c.setFillColor(INK); c.rect(0,0,PAGE_W,PAGE_H,fill=1,stroke=0)
        c.setStrokeColor(HexColor('#173B54')); c.setLineWidth(.35)
        step = 8*mm
        x=0
        while x < PAGE_W:
            c.line(x,0,x,PAGE_H); x += step
        y=0
        while y < PAGE_H:
            c.line(0,y,PAGE_W,y); y += step
        c.setStrokeColor(ELECTRIC); c.setLineWidth(1.1)
        c.rect(PAGE_W-70*mm, PAGE_H-93*mm, 41*mm, 41*mm, fill=0, stroke=1)
        c.setStrokeColor(HexColor('#26B6C8')); c.rect(PAGE_W-62*mm, PAGE_H-85*mm, 41*mm, 41*mm, fill=0, stroke=1)
        c.setFillColor(LIME); c.circle(PAGE_W-50*mm,PAGE_H-66*mm,2.5*mm,fill=1,stroke=0)
        c.setFillColor(ELECTRIC); c.rect(18*mm, PAGE_H-17*mm, 18*mm, 2.2*mm, fill=1, stroke=0)
    else:
        c.setFillColor(PAPER); c.rect(0,0,PAGE_W,PAGE_H,fill=1,stroke=0)
        c.setFillColor(INK); c.rect(0,PAGE_H-8*mm,PAGE_W,8*mm,fill=1,stroke=0)
        c.setFillColor(ELECTRIC); c.rect(18*mm,PAGE_H-20*mm,9*mm,1.4*mm,fill=1,stroke=0)
        c.setFont('Blueprint-Bold',7.5); c.setFillColor(INK)
        c.drawString(30*mm,PAGE_H-20.3*mm,'MACROSAP  /  GUIA DE IDENTIDAD Y FUNCIONAMIENTO')
    c.restoreState()

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='CoverKicker', fontName='Blueprint-Bold', fontSize=9, leading=12, textColor=BLUE, tracking=1.5, spaceAfter=7*mm))
styles.add(ParagraphStyle(name='CoverTitle', fontName='Blueprint-Bold', fontSize=38, leading=40, textColor=WHITE, spaceAfter=5*mm))
styles.add(ParagraphStyle(name='CoverSub', fontName='Blueprint', fontSize=12, leading=18, textColor=HexColor('#D2E8EF'), spaceAfter=5*mm))
styles.add(ParagraphStyle(name='H1bp', fontName='Blueprint-Bold', fontSize=22, leading=26, textColor=INK, spaceBefore=0, spaceAfter=2.5*mm))
styles.add(ParagraphStyle(name='H2bp', fontName='Blueprint-Bold', fontSize=11, leading=14, textColor=INK, spaceBefore=1.5*mm, spaceAfter=1.5*mm))
styles.add(ParagraphStyle(name='Bodybp', fontName='Blueprint', fontSize=8.7, leading=12.2, textColor=INK, spaceAfter=2.2*mm))
styles.add(ParagraphStyle(name='Smallbp', fontName='Blueprint', fontSize=7.4, leading=10, textColor=MUTED))
styles.add(ParagraphStyle(name='Labelbp', fontName='Blueprint-Bold', fontSize=7, leading=9, textColor=ELECTRIC, tracking=.7, spaceAfter=1.5*mm))
styles.add(ParagraphStyle(name='Whitebp', fontName='Blueprint', fontSize=8.5, leading=12, textColor=WHITE))
styles.add(ParagraphStyle(name='Tinybp', fontName='Blueprint', fontSize=6.6, leading=9, textColor=MUTED))
styles.add(ParagraphStyle(name='TableHeadbp', fontName='Blueprint-Bold', fontSize=7.3, leading=9, textColor=WHITE))
styles.add(ParagraphStyle(name='Tablebp', fontName='Blueprint', fontSize=7.3, leading=10, textColor=INK))

def P(text, style='Bodybp'): return Paragraph(text, styles[style])
def section_head(no, title, desc):
    return [P(f'SECCIÓN / {no}', 'Labelbp'), P(title, 'H1bp'), P(desc, 'Bodybp'), Spacer(1,2*mm)]
def card(title, body, width):
    t=Table([[P(title,'H2bp')],[P(body,'Smallbp')]], colWidths=[width])
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),WHITE),('BOX',(0,0),(-1,-1),.6,LINE),('LINEBEFORE',(0,0),(0,-1),2,ELECTRIC),('LEFTPADDING',(0,0),(-1,-1),9),('RIGHTPADDING',(0,0),(-1,-1),9),('TOPPADDING',(0,0),(-1,0),8),('BOTTOMPADDING',(0,0),(-1,0),1),('TOPPADDING',(0,1),(-1,1),2),('BOTTOMPADDING',(0,1),(-1,1),9)]))
    return t

def swatch(name, hx, usage, width):
    rgb=HexColor(hx)
    label_col = WHITE if hx in ['#08243A','#146EF5','#FF6845'] else INK
    inner=Table([[P(name,'H2bp')],[P(hx,'Labelbp')],[P(usage,'Smallbp')]], colWidths=[width-14])
    inner.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),WHITE),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,0),7),('BOTTOMPADDING',(0,0),(-1,-1),4)]))
    box=Table([[inner]], colWidths=[width], rowHeights=[31*mm])
    box.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),rgb),('BOX',(0,0),(-1,-1),.45,LINE),('VALIGN',(0,0),(-1,-1),'BOTTOM'),('BOTTOMPADDING',(0,0),(-1,-1),0),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),0),('TOPPADDING',(0,0),(-1,-1),0)]))
    return box

story=[]
# PAGE 1 — COVER
story += [Spacer(1,32*mm), P('MACROSAP  /  INVENTARIO DEL PRODUCTO DIGITAL','CoverKicker'), P('Blueprint<br/>del proyecto','CoverTitle'), P('Guía visual y funcional para entender qué contiene el sitio, cómo se organiza y qué tecnologías presenta el código.','CoverSub'), Spacer(1,12*mm)]
meta=Table([[P('TIPO DE PROYECTO','Labelbp'),P('ESTADO DOCUMENTADO','Labelbp')],[P('Sitio web estático de servicios','Whitebp'),P('HTML + CSS + JavaScript nativo','Whitebp')],[P('FECHA DE REVISIÓN','Labelbp'),P('ALCANCE','Labelbp')],[P('28 OCTUBRE 2026','Whitebp'),P('Interfaz, contenido y comportamiento del front-end','Whitebp')]],colWidths=[66*mm,94*mm])
meta.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),HexColor('#0E3048')),('BOX',(0,0),(-1,-1),.6,HexColor('#24516A')),('INNERGRID',(0,0),(-1,-1),.35,HexColor('#24516A')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),10),('RIGHTPADDING',(0,0),(-1,-1),10),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8)]))
story += [meta, Spacer(1,38*mm), P('PLANO DE LECTURA','Labelbp'), P('01  Identidad visual     /     02  Arquitectura del sitio     /     03  Interacciones     /     04  Recursos y notas técnicas','Whitebp'), PageBreak()]
# PAGE 2 — DESIGN SYSTEM
story += section_head('01','Sistema visual','Los tokens siguientes se toman de la hoja de estilos. Los acentos adicionales se identifican por su uso en componentes y títulos.')
colors_row=[swatch('Tinta', '#08243A','Texto principal y fondos oscuros',34*mm),swatch('Azul eléctrico','#146EF5','Acciones, selección y navegación',34*mm),swatch('Hielo','#E7F7FA','Fondo claro principal',34*mm),swatch('Azul claro','#B9E2F2','Superficies y contraste',34*mm),swatch('Lima','#D8FF55','Acento vivo y glow',34*mm)]
t=Table([colors_row],colWidths=[34*mm]*5)
t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),1.5),('RIGHTPADDING',(0,0),(-1,-1),1.5),('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0)]))
story += [t, Spacer(1,4*mm)]
second_row=[swatch('Verde de títulos','#16894F','Segunda frase en títulos de servicio',42*mm),swatch('Naranja','#FF6845','Punto de venta y acentos cálidos',42*mm),card('Líneas y fondos','La retícula azul tenue aporta textura de blueprint; bordes finos conectan tarjetas sin competir con el contenido.',76*mm)]
t=Table([second_row],colWidths=[42*mm,42*mm,76*mm]); t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),1.5),('RIGHTPADDING',(0,0),(-1,-1),1.5),('TOPPADDING',(0,0),(-1,-1),0)])); story += [t,Spacer(1,6*mm)]
fonts=[['FAMILIA','FUNCIÓN EN EL SITIO'],['Valley Sans → Red Hat Display → sans-serif','Texto general mediante variable --sans.'],['Exo 2','Titulares, nombres de servicios y jerarquías con carácter técnico.'],['DM Mono','Etiquetas, numeración, microcopy y datos de interfaz.']]
ft=Table([[P(x,'TableHeadbp') if i==0 else P(x,'Tablebp') for x in row] for i,row in enumerate(fonts)], colWidths=[75*mm,105*mm])
ft.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),INK),('ROWBACKGROUNDS',(0,1),(-1,-1),[WHITE,HexColor('#F0F4F2')]),('GRID',(0,0),(-1,-1),.45,LINE),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]))
story += [P('TIPOGRAFÍA','Labelbp'),ft,Spacer(1,4*mm),P('<b>Tratamiento:</b> titulares amplios, alto contraste, tarjetas tipo mosaico, iconografía SVG sin marcos pesados, brillos en acciones clave y movimiento moderado. El proyecto carga familias tipográficas desde Google Fonts; el fallback local puede variar si no hay conexión.','Bodybp'), PageBreak()]
# PAGE 3 — ARCHITECTURE
story += section_head('02','Mapa del sitio y archivos','La experiencia se implementa como una sola página con pantallas internas y contenido dinámico. No se detectó un framework ni un proceso de compilación en los archivos revisados.')
rows=[['ARCHIVO / CARPETA','RESPONSABILIDAD'],['index.html','Estructura de pantallas, menú, tarjetas, FAQs, diálogos y cuestionario.'],['style.css','Sistema visual, componentes, animaciones y reglas responsive.'],['script.js','Navegación, modal de servicios, cuestionario, historial, gestos y carrusel.'],['img/','Logos y recursos gráficos de marca; img/services/ contiene ilustraciones SVG por servicio.'],['pdf/','Documentos descargables presentes en el proyecto.']]
t=Table([[P(x,'TableHeadbp') if i==0 else P(x,'Tablebp') for x in row] for i,row in enumerate(rows)],colWidths=[42*mm,138*mm])
t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),INK),('ROWBACKGROUNDS',(0,1),(-1,-1),[WHITE,HexColor('#F0F4F2')]),('GRID',(0,0),(-1,-1),.45,LINE),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]))
story += [t,Spacer(1,5*mm),P('PANTALLAS PRINCIPALES','Labelbp')]
flow=[['01','Inicio','Cuadrícula de tarjetas con acceso a cuatro servicios, acerca de y preguntas frecuentes.'],['02','Detalle de servicio','Título, descripción, collage visual y acceso a servicios ampliados.'],['03','Acerca de MACROSAP','Presentación, proceso, mosaico de capacidades y bloque de descarga del perfil.'],['04','Preguntas frecuentes','Nueve acordeones con icono, respuestas ampliadas y botón fijo de regreso.']]
flowtab=Table([[P(a,'Labelbp'),P(b,'H2bp'),P(c,'Tablebp')] for a,b,c in flow],colWidths=[14*mm,42*mm,124*mm])
flowtab.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),WHITE),('GRID',(0,0),(-1,-1),.4,LINE),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]))
story += [flowtab,Spacer(1,5*mm),P('SERVICIOS MODELADOS','Labelbp'),P('<b>Desarrollo web:</b> sitios y e-commerce, aplicaciones, UX/UI, APIs y automatización.  <b>Bases de datos:</b> arquitectura, migración, dashboards y respaldos.  <b>Control de acceso:</b> biometría, visitantes, reportes e integración de asistencia.  <b>Punto de venta:</b> ventas, inventario, facturación, sucursales, CRM y lealtad.','Bodybp'),PageBreak()]
# PAGE 4 — INTERACTIONS
story += section_head('03','Interacciones y lógica','Comportamientos identificados en JavaScript y CSS. Los elementos operan en el navegador y varias acciones derivan el envío a WhatsApp.')
interactions=[
('Navegación','Menú lateral con inicio, servicios, acerca de, FAQ y enlaces de contacto. La marca vuelve al inicio.'),
('Historial y regreso','El cambio de pantallas actualiza history; Atrás del navegador recupera la pantalla anterior. En móvil, el gesto desde el borde izquierdo también vuelve.'),
('Servicios','Cada tarjeta abre su pantalla; “Ver servicios” despliega un diálogo centrado con acordeones, imágenes pequeñas, etiquetas, cierre y foco accesible.'),
('Cotizador','Cuestionario de 8 pasos con selección múltiple, progreso, validación, navegación atrás y campos opcionales de nombre e idea.'),
('WhatsApp','Al final construye un mensaje con proyecto, objetivo, alcance, sistemas, tiempo, presupuesto y soporte; abre WhatsApp para que la persona revise y envíe.'),
('Acerca de / animación','Mosaico de capacidades con aparición al entrar en viewport y CTA a cotización. Carrusel de portada cambia cada 3.8 segundos.'),
('FAQ','Nueve elementos desplegables; scroll propio en escritorio, scroll de página en móvil, iconos temáticos y retorno fijo.'),
('Accesibilidad básica','Diálogos con roles y etiquetas, cierre con Escape, gestión de foco, botones de cierre y respeto a prefers-reduced-motion en animaciones documentadas.')]
for title,body in interactions: story.append(card(title,body,174*mm)); story.append(Spacer(1,2*mm))
story += [Spacer(1,2*mm),P('FLUJO DE COTIZACIÓN','Labelbp')]
steps=Table([[P('01  Necesidad','Tablebp'),P('02  Objetivo','Tablebp'),P('03  Alcance','Tablebp'),P('04  Sistemas','Tablebp')],[P('05  Tiempo','Tablebp'),P('06  Presupuesto','Tablebp'),P('07  Acompañamiento','Tablebp'),P('08  Contexto + WhatsApp','Tablebp')]],colWidths=[45*mm]*4)
steps.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),ICE),('GRID',(0,0),(-1,-1),.45,HexColor('#C7DAE2')),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8)]))
story += [steps,PageBreak()]
# PAGE 5 — RESPONSIVE / ASSETS / TECHNICAL NOTES
story += section_head('04','Recursos, adaptabilidad y notas','Resumen para que puedas orientarte al editar contenido o planear la siguiente mejora.')
asset_rows=[['RECURSO','QUÉ CONTIENE'],['Marca','macro2.jpeg, macrosaplogo.jpeg y marco3.jpeg aparecen como variantes de palabra/símbolo/logotipo.'],['SVG de servicios','16 ilustraciones organizadas por tema: web, datos, acceso y punto de venta.'],['Fotografía','La portada y el mosaico de capacidades usan URLs de images.unsplash.com; requieren conexión para cargar.'],['Contacto','WhatsApp y teléfono: +52 55 5106 4052. Correo: macrosap@online.mx.']]
at=Table([[P(x,'TableHeadbp') if i==0 else P(x,'Tablebp') for x in row] for i,row in enumerate(asset_rows)],colWidths=[38*mm,142*mm])
at.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),INK),('ROWBACKGROUNDS',(0,1),(-1,-1),[WHITE,HexColor('#F0F4F2')]),('GRID',(0,0),(-1,-1),.45,LINE),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7)]))
story += [P('RECURSOS','Labelbp'),at,Spacer(1,5*mm),P('COMPORTAMIENTO RESPONSIVE','Labelbp')]
breaks=Table([[P('≤ 760 px','H2bp'),P('≤ 600 px','H2bp'),P('≤ 420 px','H2bp')],[P('La navegación y el contenido se adaptan a móvil; la página puede desplazarse verticalmente. Las tarjetas y mosaicos se reorganizan.', 'Smallbp'),P('El diálogo de servicios y la presentación cambian espaciado y distribución para pantallas angostas.','Smallbp'),P('Los titulares, opciones y tarjetas compactan medidas y tipografía para conservar legibilidad.','Smallbp')]],colWidths=[60*mm]*3)
breaks.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),WHITE),('GRID',(0,0),(-1,-1),.45,LINE),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8)]))
story += [breaks,Spacer(1,3*mm),P('<b>Breakpoints definidos en CSS:</b> 360, 420, 520, 600 y 760 px; también hay un ajuste para tabletas entre 761 y 1000 px. El cambio principal a móvil ocurre en 760 px; los demás refinan diálogos, tipografía y pantallas angostas.','Smallbp'),Spacer(1,4*mm),P('PUNTOS TÉCNICOS','Labelbp')]
notes=[
'<b>Arquitectura:</b> implementación estática, sin framework ni backend identificado en esta carpeta. El comportamiento de la interfaz vive en script.js.',
'<b>Dependencias de red:</b> fuentes externas de Google Fonts y fotografías alojadas en Unsplash. Si no hay conexión, entran las fuentes de respaldo, pero las fotos remotas pueden no aparecer.',
'<b>Datos de contacto:</b> el número está escrito en los enlaces de WhatsApp y teléfono; si cambia, actualizar index.html y el destino usado por el cotizador en script.js.',
'<b>Alcance de esta guía:</b> describe el código fuente inspeccionado el 28/10/2026; no afirma despliegue, integración con CRM ni servicios de servidor.'
]
for n in notes: story.append(P('•  '+n,'Bodybp'))
story += [Spacer(1,3*mm),P('EDITAR CON ORDEN','Labelbp'),P('Contenido y estructura: index.html  /  estilos, colores y breakpoints: style.css  /  navegación, interacciones y cotizador: script.js  /  imágenes e ilustraciones: img/  /  documentos: pdf/','Smallbp')]

doc=SimpleDocTemplate(str(OUT),pagesize=A4,rightMargin=18*mm,leftMargin=18*mm,topMargin=27*mm,bottomMargin=24*mm,title='MACROSAP — Blueprint del proyecto',author='MACROSAP',subject='Guía visual y funcional del sitio web')
doc.build(story,onFirstPage=page_bg,onLaterPages=page_bg,canvasmaker=BlueprintCanvas)
print(OUT)