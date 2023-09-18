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
   
   nome,numero,n2 =  conveersao(distanciaentre,nomesbar,distanciaa)

   n = dividir_distancias(numero)
 
   
   numero2 = dividir_distancias(n2)
   
   
   percursoencosta,distanciaencosta = iniciar(n,nome) 
   
   return render_template("index.html",percursoencosta ="Solucao inicial:"+str(percursoencosta),distanciaencosta ="Avalia:" +str(distanciaencosta))

 
if __name__ == "__main__":
    app.run()




