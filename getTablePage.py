# -*- coding: utf-8 -*-
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

def getTablePage(numPages, numRefs, header):
    pdfmetrics.registerFont(
        TTFont('aktivGrotisk', 'fonts/AktivGroteskCorp-Bold.ttf')
    )
    tablePage = canvas.Canvas('tablePage.pdf')
    tablePage.setTitle('tablePage')
    for i in range(numPages):
        try :
            tablePage.drawImage(r'images\tableHeaders\\' + header + 'TableHeader.png', 3.8*mm, 259*mm, 202.4*mm, 35*mm)
        except:
            tablePage.drawImage(r'images\tableHeaders\TableHeader.png', 3.8*mm, 259*mm, 202.4*mm, 35*mm)
            tablePage.setFillColorCMYK(0,0.49,0.85,0)
            tablePage.setFont('aktivGrotisk', 30)
            tablePage.drawString(86*mm, 279*mm, header.upper())
        tablePage.setFillGray(0.93)
        tablePage.setFont('aktivGrotisk', 20)
        tablePage.drawString(86*mm, 270*mm, str(numRefs) + ' References')
        tablePage.showPage
    tablePage.save()
