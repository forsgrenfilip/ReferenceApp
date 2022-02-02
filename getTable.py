# -*- coding: utf-8 -*-
from referenceInformation import referenceInformation
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
import math
from reportlab.platypus.flowables import PageBreak


def getTable(data, purchase, head = referenceInformation['head']):
    '''
    uses data to creat pdf with tables
    '''
    # All table Rows in Large list of lists (every 75th row is head, 0, 75,150...)
    tableRows =[]
    for i in range(len(data)*2+1):
        if i == 0:
            tableRows.append(head)
        elif i%74 == 0:
            tableRows.append(['','','','',purchase[math.floor(i/2-1)]])
            tableRows.append(head)
        elif i % 2 == 1:
            tableRows.append(data[math.floor(i/2)])
        else:
            tableRows.append(['','','','',purchase[math.floor(i/2-1)]])

    # Create empty doc (no elements). Also create elemnts space and table to insert.
    pdf = SimpleDocTemplate(
        'table.pdf'
    )
    elements = []
    space = Spacer(1, 30)

    numPages = math.ceil((len(tableRows)+1)/75)
    for i in range(numPages):
        k = i*75
        table = Table(tableRows[:][k:k+75])
        # Table body looks
        style = TableStyle([
            ('FONT', (0,0), (-1,0), 'Helvetica',14),
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#444444')),
            ('TEXTCOLOR', (0,0), (-1,0),  colors.HexColor('#EEEEEE')),
            ('LEFTPADDING',(0,0), (-1,0), 3),
            ('RIGHTPADDING',(0,0), (0,0), 32),
            ('RIGHTPADDING',(1,0), (1,0), 52),
            ('RIGHTPADDING',(2,0), (2,0), 8),
            ('RIGHTPADDING',(3,0), (3,0), 29),
            ('RIGHTPADDING',(4,0), (4,0), 20),
            ('BOTTOMPADDING',(0,0), (-1,0), 5),
            ('TOPPADDING',(0,0), (-1,0), 5),
            ('VALIGN',(0,1),(-1,-1),'MIDDLE'),
            ('BACKGROUND', (0,1), (-1,-1), colors.HexColor('#DDDDDD')),
            ('TEXTCOLOR', (0,1), (-1,-1),  colors.HexColor('#333333')),
            ('FONT', (-1,1), (-1,-1), 'Helvetica-Bold', 7),
            ('FONT', (0,1), (-2,-1),'Helvetica-Bold', 8),
            ('LEFTPADDING',(0,1), (-1,-1), 5),
            ('LEFTPADDING',(2,1), (2,-1), 8),
            ('RIGHTPADDING',(0,1), (-1,-1), 2),
            ('RIGHTPADDING',(1,1), (1,-1), 0),
            ('BOTTOMPADDING',(0,1), (-1,-1), 0),
            ('TOPPADDING',(0,1), (-1,-1), 0),
        ])
        table.setStyle(style)

        for i in range(len(tableRows[:][k:k+75])-1):
            if i % 2 == 1:
                for j in range(len(tableRows[0])-1):
                    style = TableStyle([
                        ('SPAN', (j,i), (j,i+1))
                    ])
                    table.setStyle(style)  
                if i % 4 == 1:
                    style = TableStyle([
                        ('BACKGROUND', (0,i), (-1,i+1), colors.HexColor('#EEEEEE'))
                    ])
                    table.setStyle(style)
        elements.append(space)
        elements.append(table)
        elements.append(PageBreak())

    pdf.build(elements)

    return numPages
    
    