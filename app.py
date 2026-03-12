from flask import Flask, render_template, request, redirect
from models.requisito import recuperar_requisitos


app = Flask (__name__)


@app.route('/')
def pagina_principal():
    return render_template('index.html')

@app.route('/requisitos')
def pagina_requisitos():
    requisitos = recuperar_requisitos()
    return render_template('requisitos.html', requisitos = requisitos)

app.run (debug=True)