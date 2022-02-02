# -*- coding: utf-8 -*-
from referenceInformation import referenceInformation
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

def getFrontPage(segments, countries = [], models = [], headlineType='segment'):
    '''
    segments, countries and models are LISTS off all selected categorical parameters to form referncelist.
    headlineType is used to prioritize what headline to choose if two or more categorical headlines are "avalible".
    Avalible, in this case is defines as ONE excplicit parameter is elected within a category or hirachiacal level within category.

    *** current version only support segments and country***
    '''
    pdfmetrics.registerFont(
        TTFont('aktivGrotisk', 'fonts/AktivGroteskCorp-Bold.ttf')
    )
    segmentsLevelOne = referenceInformation['segmentsLevelOne']
    regions = referenceInformation['regions']
    countriesByRegion = referenceInformation['countriesByRegion']
    header  = 'General Industry'

    # finding segment header
    #defult segment>country>(model)
    if headlineType == 'segment' :

        # IF only one i selected, make it header.
        # ELSE find ONE selecter level ONE. Else header = General Industry
        if len(segments) == 1:
            header = segments[0]
        else:
            i=0
            j=0
            go = True
            while i+j < len(segments) and go:
                if segments[i] in segmentsLevelOne:
                    header = segments[i]
                    while j < len(segments[i+1:]) and go:
                        if segments[i+j+1] in segmentsLevelOne:
                            go = False
                            header  = 'General Industry'
                        j+=1
                i+=1

        # check for country header IF no segmentheader is found
        if header  == 'General Industry':

            # IF only one country was selctet, set header
            if len(countries) == 1:
                header = countries[0]
            else:
                # checking for only ONE selected region (level one)
                i=0
                j=0
                go = True
                while i+j < len(countries) and go:
                    if countries[i] in regions:
                        header = countries[i]
                        while j < len(countries[i+1:]) and go:
                            if countries[i+j+1] in regions:
                                go = False
                                header  = 'General Industry'
                            j+=1
                    i+=1
                # confirming no country outside selected ONE region (level two elections outside level one selection)
                if header != 'General Industry':
                    i=0
                    go = True
                    while i < len(countries) and go:
                        if countries[i] not in countriesByRegion[regions.index(header)]:
                            go = False
                            header  = 'General Industry'
                        i+=1
        
    
    if headlineType == 'country':
        # IF only one country was selctet, set header
        if len(countries) == 1:
            header = countries[0]
        else:
            # checking for only ONE selected region
            i=0
            j=0
            go = True
            while i+j < len(countries) and go:
                if countries[i] in regions:
                    header = countries[i]
                    while j < len(countries[i+1:]) and go:
                        if countries[i+j+1] in regions:
                            go = False
                            header  = 'General Industry'
                        j+=1
                i+=1
            # confirming no country outside selected ONE region (level two elections outside level one selection)
            if header != 'General Industry':
                i=0
                go = True
                print(countriesByRegion[regions.index(header)])
                while i < len(countries) and go:
                    if countries[i] not in countriesByRegion[regions.index(header)]:
                        go = False
                        header  = 'General Industry'
                    i+=1

        # check for country segment IF no country header is found
        if header  == 'General Industry':
            # IF only one i selected, make it header.
            # ELSE find ONE selecter level ONE. Else header = General Industry
            if len(segments) == 1:
                header = segments[0]
            else:
                i=0
                j=0
                go = True
                while i+j < len(segments) and go:
                    if segments[i] in segmentsLevelOne:
                        header = segments[i]
                        while j < len(segments[i+1:]) and go:
                            if segments[i+j+1] in segmentsLevelOne:
                                go = False
                                header  = 'General Industry'
                            j+=1
                    i+=1

        

    # Make front page (elemnts from top to bottom on page)
    frontPage = canvas.Canvas('frontPage.pdf')
    frontPage.setTitle('Ref')

    frontPage.drawImage(r'images\headerW.png', 0, 255*mm, 210*mm, 35*mm)
    frontPage.drawImage(r'images\toneOrange.png', 0, 245*mm, 230*mm, 10*mm)
    frontPage.drawInlineImage(r'images\main.jpg',-5*mm, 118*mm, 220*mm, 120*mm)
    frontPage.drawImage(r'images\refheader.jpg', 0, 73*mm, 230*mm, 38*mm)
    try:
        frontPage.drawImage(r'images\segHeader\\' + header + r'Header.png', 0, 35*mm, 230*mm, 38*mm)
    except:
        # enter the header in regular text
        frontPage.drawImage(r'images\backgroundSegments.png', 0, 35*mm, 230*mm, 38*mm)
        frontPage.setFillColorCMYK(0,0.49,0.85,0)
        frontPage.setFont('aktivGrotisk', 45)
        frontPage.drawString(13*mm, 49*mm, header.upper())
    frontPage.drawImage(r'images\toneOrange.png', 0, 25*mm, 230*mm, 10*mm)
    frontPage.save()

    return header