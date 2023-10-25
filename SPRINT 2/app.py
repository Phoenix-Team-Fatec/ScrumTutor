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

    papel = ['P.O', 'S.M','D.T']
    proatividade = [request.form['proat_po'],request.form['proat_sm'],request.form['proat_dt'], ]
    autonomia = [request.form['aut_po'],request.form['aut_sm'],request.form['aut_dt']]
    colaboracao = [request.form['colab_po'],request.form['colab_sm'],request.form['colab_dt']]
    entrega = [request.form['entrega_po'],request.form['entrega_sm'],request.form['entrega_dt']]
    for i in range(len(papel)):
        avaliado = avaliacao(papel[i], proatividade[i], autonomia[i], colaboracao[i], entrega[i])
        notas.append(avaliado)
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