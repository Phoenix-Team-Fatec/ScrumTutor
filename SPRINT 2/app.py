from flask import Flask, render_template, request, redirect

class avaliacao:
    def __init__(self, papel, proatividade, autonomia, colaboracao, entrega):
        self.papel = papel
        self.proatividade = proatividade
        self.autonomia = autonomia
        self.colaboracao = colaboracao
        self.entrega = entrega

app = Flask("__name__")

app.secret_key = 'phoenix'

notas = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Eventos')
def Eventos():
    return render_template('eventos.html')

@app.route('/Pacer')
def pacer():
    return render_template('pacer.html', listas = notas)


@app.route('/Criar', methods=['POST',])
def criar():
    papel = 'P.O'
    proatividade = request.form['proat_po']
    autonomia = request.form['aut_po']
    colaboracao = request.form['colab_po']
    entrega = request.form['entrega_po']
    po = avaliacao(papel, proatividade, autonomia, colaboracao, entrega)
    notas.append(po)

    papel = 'S.M'
    proatividade = request.form['proat_sm']
    autonomia = request.form['aut_sm']
    colaboracao = request.form['colab_sm']
    entrega = request.form['entrega_sm']
    sm = avaliacao(papel, proatividade, autonomia, colaboracao, entrega)
    notas.append(sm)

    papel = 'D.T'
    proatividade = request.form['proat_dt']
    autonomia = request.form['aut_dt']
    colaboracao = request.form['colab_dt']
    entrega = request.form['entrega_dt']
    dt = avaliacao(papel, proatividade, autonomia, colaboracao, entrega)
    
    notas.append(dt)
    return redirect('/Pacer')


@app.route('/artefatos')
def artefatos():
    return render_template('artefatos.html')

@app.route('/Papéis')
def papeis():
    return render_template('papeis.html')

@app.route('/Apendice')
def apendice():
    return render_template('apendice.html')

@app.route('/Bibliografia')
def bibliografia():
    return render_template('bibliografia.html')

app.run(debug=True)