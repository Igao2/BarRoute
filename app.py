from flask import Flask,render_template,request,jsonify
from dicionario import conveersao,dividir_distancias,dic
from tempera import iniciarr
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
   cursotempera,distanciatempera,ordemtempera,lon =  iniciarr(n,nome,latitudee)
   print("Antes de dividir"+str(len(lat)))
   for i in range(len(lat)):
       muda = lat[i].replace(",","/")
       lat[i] = muda
   for i in range(len(lon)):
       muda = lon[i].replace(",","/")
       lon[i] = muda
   print(len(lat))
   return render_template("index.html",distanciaencosta ="\n Distancia Subida de Encosta:"+str(distanciaencosta),cursoencosta ="Curso Subida de encosta:" +str(cursoencosta),ordemencosta = "\n Bares:"+str(ordemencosta),lat=lat,cursotempera = "\n Curso Tempera:"+str(cursotempera),distanciatempera="\n Distancia tempera:"+str(distanciatempera),ordemtempera="\n Ordem dos bares:"+str(ordemtempera),long = lon)

 
if __name__ == "__main__":
    app.run()




