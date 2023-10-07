from flask import Flask, render_template

app = Flask("__name__")


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Eventos')
def Eventos():
    return render_template('eventos.html')

@app.route('/Pacer')
def pacer():
    return render_template('pacer.html')

@app.route('/artefatos')
def artefatos():
    return render_template('artefatos.html')

@app.route('/Papéis')
def papeis():
    return render_template('papeis.html')
@app.route('/Apendice')
def apendice():
    return render_template('apendice.html')



app.run(debug=True)