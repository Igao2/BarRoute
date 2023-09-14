from flask import Flask,render_template,request,jsonify
from dicionario import conveersao,dividir_distancias
from buscas import iniciar

app = Flask(__name__)

@app.route("/")
def index():
   
    return render_template("index.html")

@app.route("/", methods=['POST'])
def post():
   
   distanciaentre = request.form['distanciasi']
   nomesbar = request.form['nomesbar']
   
   nome,numero =  conveersao(distanciaentre,nomesbar)
   n = dividir_distancias(numero)
   percurso,distancia,nomes = iniciar(n,nome) 
   return render_template("index.html",percurso = percurso,distancia = distancia, nomes = nomes)

 
if __name__ == "__main__":
    app.run()




