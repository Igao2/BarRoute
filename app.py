from flask import Flask,render_template,request,jsonify
from dicionario import conveersao,dividir_distancias,dic
from sa import Solucao_Inicial,Gerar_Problema,Avalia
from subidaencosta import iniciar
app = Flask(__name__)

@app.route("/")
def index():
   
    return render_template("index.html")

@app.route("/", methods=['POST'])
def post():
   distanciaa = request.form['distanciaAtual']
   distanciaentre = request.form['distanciasi']
   nomes = request.form['nome']
   latitude = request.form['latitudelongitude']
   
   
   nome,numero,latitudee =  conveersao(distanciaentre,nomes,latitude)

   n = dividir_distancias(numero)
   
   
   cursoencosta,distanciaencosta,ordemencosta,lat = iniciar(n,nome,latitudee)
   print("Antes de dividir"+str(len(lat)))
   for i in range(len(lat)):
       muda = lat[i].replace(",","/")
       lat[i] = muda

   print(len(lat))
   return render_template("index.html",distanciaencosta ="Distancia Subida de Encosta:"+str(distanciaencosta),cursoencosta ="Curso Subida de encosta:" +str(cursoencosta),ordemencosta = "\n Bares:"+str(ordemencosta),lat=lat)

 
if __name__ == "__main__":
    app.run()




