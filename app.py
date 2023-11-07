from flask import Flask,render_template,request,jsonify
import random
from dicionario import conveersao,dividir_distancias,dic
from tempera import iniciarr
from subidaencosta import iniciar
from subidaencosta2 import iniciars

app = Flask(__name__)

@app.route("/")
def index():
   
    return render_template("index.html")

@app.route("/", methods=['POST'])
def post():
   barrinha = request.form['barrinha']
   print(barrinha)
   distanciaa = request.form['distanciaAtual']
   distanciaentre = request.form['distanciasi']
   nomes = request.form['nome']
   latitude = request.form['latitudelongitude']
   
   
   nome,numero,latitudee =  conveersao(distanciaentre,nomes,latitude)

   n = dividir_distancias(numero)
   
   sequencia_atual = list(range(len(n)))
   random.shuffle(sequencia_atual)
   cursoencosta,distanciaencosta,lat = iniciar(n,nome,latitudee,sequencia_atual)
   cursoencosta2,distanciaencosta2,lat2 = iniciars(n,nome,latitudee,sequencia_atual)
   cursotempera,distanciatempera,lon =  iniciarr(n,nome,latitudee,sequencia_atual)
   for i in range(len(lat)):
       muda = lat[i].replace(",","/")
       lat[i] = muda
   for i in range(len(lon)):
       muda = lon[i].replace(",","/")
       lon[i] = muda
   for i in range(len(lat2)):
       muda = lat2[i].replace(",","/")
       lat2[i] = muda
          

   if barrinha=="se":
       return render_template("index.html",distanciaencosta ="\n Distancia Subida de Encosta:"+str(distanciaencosta),cursoencosta ="Curso Subida de encosta:" +str(cursoencosta),lat=lat)
   elif barrinha == "se*":
        return render_template("index.html",distanciaencosta2 ="\n Distancia Subida de Encosta*:"+str(distanciaencosta2),cursoencosta2 ="Curso Subida de encosta*:" +str(cursoencosta2),lat2=lat2)
   elif barrinha =="temp":
       return render_template("index.html", distanciatempera = "\n Distancia Tempera:"+str(distanciatempera),cursotempera ="\n Curso Tempera:"+str(cursotempera),long = lon)
   elif barrinha =="todas":
        return render_template("index.html",distanciaencosta ="\n Distancia Subida de Encosta:"+str(distanciaencosta),cursoencosta ="Curso Subida de encosta:" +str(cursoencosta),lat=lat,cursotempera = "\n Curso Tempera:"+str(cursotempera),distanciatempera="\n Distancia tempera:"+str(distanciatempera),long = lon,distanciaencosta2 ="\n Distancia Subida de Encosta*:"+str(distanciaencosta2),cursoencosta2 ="Curso Subida de encosta*:" +str(cursoencosta2),lat2=lat2)

   
 
if __name__ == "__main__":
    app.run()




