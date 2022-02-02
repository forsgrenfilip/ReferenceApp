# -*- coding: utf-8 -*-
import pandas as pd
def getDataCSV(segments, countries, models, years, path=r'aliRefData.csv', removeMissingInfo = True):
    xl_file = pd.read_csv(path,';',encoding='iso-8859-15')
    xl_file.columns = ['INDUSTRY', 'MODEL', 'YEAR', 'COUNTRY', 'PURCHASER AND/OR USER','-']
    xl_file = xl_file[~xl_file['YEAR'].isin(['Unknown'])]
    if removeMissingInfo:
        xl_file = xl_file[~xl_file['INDUSTRY'].isin(['Unknown','-',])]
        xl_file = xl_file[~xl_file['MODEL'].isin(['Unknown','-',])]
        xl_file = xl_file[~xl_file['COUNTRY'].isin(['Unknown','-',])]

    xl_file['YEAR'] = xl_file['YEAR'].astype(int)
    xl_file = xl_file[xl_file['YEAR'] >= years[0]]
    xl_file = xl_file[xl_file['YEAR'] <= years[1]]
    if 'ALL' not in segments:
        xl_file = xl_file[xl_file['INDUSTRY'].isin(segments)]
    if 'ALL' not in countries:
        xl_file = xl_file[xl_file['COUNTRY'].isin(countries)]
    if 'ALL' not in models:
        xl_file = xl_file[xl_file['MODEL'].isin(models)]
    
    
    xl_file = xl_file.fillna('-')
    purchase = xl_file.T.values.tolist()[-1]
    xl_file = xl_file.drop(xl_file.columns[-1], axis=1)
    xl_file = xl_file.sort_values(by=['YEAR', 'COUNTRY', 'INDUSTRY'], ascending=[False, True, True])
    refs = xl_file.values.tolist()

    #clean out ugly values
    blanks = ['Unknown','Nan' 'nan', 'Null']   
    for i in range(len(refs)):
        for j in range(len(refs[0])):
            if any(x == refs[i][j] for x in blanks):
                refs[i][j] = '-'
    for i in range(len(purchase)):
        if any(x == purchase[i] for x in blanks):
            purchase[i] = '-'
    
    return refs, purchase