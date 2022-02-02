# -*- coding: utf-8 -*-
from PyPDF2.pdf import PdfFileWriter, PdfFileReader
import random

def mergePages(password):
    frontPage = 'frontPage.pdf'
    tablePage = 'tablepage.pdf'
    table = 'table.pdf'
    pathAndFile = r'static\Reference List.pdf'

    frontPage = PdfFileReader(frontPage).getPage(0)
    tableBase = PdfFileReader(tablePage).getPage(0)
    pdfReader = PdfFileReader(table)
    pdfWriter = PdfFileWriter()

    pdfWriter.addPage(frontPage)

    for i in range(pdfReader.numPages):
        page = pdfReader.getPage(i)
        page.mergePage(tableBase)
        pdfWriter.addPage(page)

    passwordChars = ''
    content = ''
    if password == 'true':
        char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
                'U', 'V', 'W', 'X', 'Y', 'Z', '^', '_' 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for i in range(10):
            passwordChars = passwordChars + char[random.randint(0,len(char)-1)]
        content = content + ('Password: ') + passwordChars
        pdfWriter.encrypt(passwordChars)

    with open(pathAndFile, 'wb') as out:
        pdfWriter.write(out)

    return content