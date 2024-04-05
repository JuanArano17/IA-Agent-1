from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Inches
from EconomyAgent import getResult
from datetime import date

doc = Document()

style = doc.styles['Normal']
font = style.font
font.name = 'Times New Roman'
font.size = Pt(14)
day = date.today()

title = doc.add_paragraph(f'\nAnálisis de la Economía Argentina dia {day}')
title.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
title_run = title.runs[0]
title_run.bold = True
title_run.font.size = Pt(24)

doc.add_paragraph('\n\n')
content = doc.add_paragraph(getResult())
content.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY

# Guardar el documento
doc.save('Analisis_Economia_Argentina.docx')
