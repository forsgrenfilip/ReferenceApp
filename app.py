# -*- coding: utf-8 -*-p
from flask import Flask, render_template, request
from getFrontPage import getFrontPage
from getTable import getTable
from getTablePage import getTablePage
from merge import mergePages
from getDataCSV import getDataCSV
from esesesnx import go

app=Flask(__name__,template_folder='template')
# The first page the user will see
@app.route('/', methods=['POST', 'GET'])
@app.route('/AliRef', methods=['GET', "POST"])
def index():
    # render_template automatically looks for templates in the "templates" directory
    if request.method == 'POST':
        segments = request.form['segments'].split(', ')
        countries = request.form['countries'].split(', ')
        models = request.form['models'].split(', ')
        minYear = int(request.form['minYear'])
        maxYear = int(request.form['maxYear'])
        password = request.form['password']
        data,purchase = getDataCSV(segments, countries, models, [minYear,maxYear])
        header = getFrontPage(segments,countries)
        numPages = getTable(data, purchase)
        getTablePage(numPages,len(data),header)
        content = mergePages(password)
        return render_template('AliRef.html', content=content)
    else:
        return render_template('AliRef.html')
if __name__ == '__main__':
    app.run(debug=True)

