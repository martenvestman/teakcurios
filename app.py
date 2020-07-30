from flask import Flask, render_template, request

from scripts.blocket import blocket
from scripts.bukowskis import bukowskis
from scripts.lauritz import lauritz
from scripts.antikkompaniet import antikkompaniet

app = Flask(__name__)

db = []

for item in blocket():
    db.append(item)
for item in bukowskis():
    db.append(item)
for item in lauritz():
    db.append(item)
for item in antikkompaniet():
    db.append(item)


@app.route('/')
def home():
    return render_template('index.html', db=db)


@app.route('/search', methods=['GET', 'POST'])
def search():
    keyword = request.form['search'].replace(" ", "%20")
    print(keyword)
    pdb = []
    try:
        print('try')
        for items in blocket(keyword):
            pdb.append(items)
    except:
        print('except')

    try:
        for items in bukowskis(keyword):
            pdb.append(items)
    except:
        pass

    try:
        for items in lauritz(keyword):
            pdb.append(items)
    except:
        pass

    try:
        for items in antikkompaniet(keyword):
            pdb.append(items)
    except:
        pass

    return render_template('index.html', db=pdb)


@app.route('/bukowskis')
def bukowskis_only():
    pdb = []
    for item in db:
        if item['site'] == 'Bukowskis':
            pdb.append(item)
    return render_template('index.html', db=pdb)


@app.route('/blocket')
def blocket_only():
    pdb = []
    for item in db:
        if item['site'] == 'Blocket':
            pdb.append(item)
    return render_template('index.html', db=pdb)


@app.route('/lauritz')
def lauritz_only():
    pdb = []
    for item in db:
        if item['site'] == 'Lauritz':
            pdb.append(item)
    return render_template('index.html', db=pdb)

@app.route('/linneolump')
def linneolump_only():
    pdb = []
    for item in db:
        if item['site'] == 'Linne&Lump':
            pdb.append(item)
    return render_template('index.html', db=pdb)

@app.route('/antikkompaniet')
def antikkompaniet_only():
    pdb = []
    for item in db:
        if item['site'] == 'Antikkompaniet':
            pdb.append(item)
    return render_template('index.html', db=pdb)

if __name__ == "__main__":
    app.run(debug=False)
