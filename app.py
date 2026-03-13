from flask import Flask, render_template, request, redirect
from models.requisito import recuperar_requisitos, excluir_requisitos


app = Flask (__name__)


@app.route('/')
def pagina_principal():
    return render_template('index.html')

@app.route('/requisitos')
def pagina_requisitos():
    requisitos = recuperar_requisitos()
    return render_template('requisitos.html', requisitos = requisitos)

@app.route("/delete/<codigo>")
def deletar_requisitos(codigo):
    excluir_requisitos(codigo)
    return redirect ('/requisitos')


@app.route("/inserir", methods = ["POST"])
def cadastrar_requisitos():
   descricao = request.form.get("descricao")
   nivel= request.form.get("nivel")
   valor = request.form.get ("valor") 


app.run (debug=True)