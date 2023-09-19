from flask import Flask,render_template,request,jsonify
from dicionario import conveersao,dividir_distancias
from sa import Solucao_Inicial,Gerar_Problema,Avalia
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
 
   m1 = Gerar_Problema(len(n),n)
   si = Solucao_Inicial(len(n),m1)

   avalia = Avalia(m1)
   print(avalia)
   



   
   return render_template("index.html",distancia = "Distancia entre os bares:"+str(m1),percursoencosta ="Solucao inicial:"+str(si),distanciaencosta ="Avalia:" +str(avalia))

 
if __name__ == "__main__":
    app.run()




