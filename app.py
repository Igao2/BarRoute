from flask import Flask,render_template,request,jsonify
from dicionario import conveersao,dividir_distancias,dic
from sa import Solucao_Inicial,Gerar_Problema,Avalia
app = Flask(__name__)

@app.route("/")
def index():
   
    return render_template("index.html")

@app.route("/", methods=['POST'])
def post():
   distanciaa = request.form['distanciaAtual']
   distanciaentre = request.form['distanciasi']
   nomes = request.form['nome']
   
   nome,numero,n2 =  conveersao(distanciaentre,nomes,distanciaa)

   n = dividir_distancias(numero)
   
   

   m1 = Gerar_Problema(len(n),n)
   si = Solucao_Inicial(len(n))

   avalia = Avalia(m1,si)
   print(avalia)
   



   
   return render_template("index.html",solucaoinicial ="Solucao inicial:"+str(si),avalia ="Avalia:" +str(avalia))

 
if __name__ == "__main__":
    app.run()




