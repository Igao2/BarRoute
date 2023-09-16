from flask import Flask,render_template,request,jsonify
from dicionario import conveersao,dividir_distancias,alterar_valores
from subidaencosta import iniciar
from tempera import iniciarr

app = Flask(__name__)

@app.route("/")
def index():
   
    return render_template("index.html")

@app.route("/", methods=['POST'])
def post():
   distanciaa = request.form['distanciaAtual']
   distanciaentre = request.form['distanciasi']
   nomesbar = request.form['nomesbar']
   
   nome,numero,numero2 =  conveersao(distanciaentre,nomesbar,distanciaa)

   n = dividir_distancias(numero)
   
   
   percursoencosta,distanciaencosta,nomes = iniciar(n,nome) 
   percursotempera,distanciatempera,nomez = iniciarr(n,nome)
   return render_template("index.html",percursoencosta = percursoencosta,distanciaencosta = distanciaencosta, nomesencosta = nomes,percursosimulada=percursotempera, distanciassimulada = distanciatempera, nomessimulada = nomez)

 
if __name__ == "__main__":
    app.run()




