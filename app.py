from flask import Flask,render_template,request,jsonify
from dicionario import conveersao

app = Flask(__name__)

@app.route("/")
def index():
   
    return render_template("index.html")

@app.route("/", methods=['POST'])
def post():
   distanciaatual = request.form['distanciaAtual']
   distanciaentre = request.form['distanciasi']
   nome = request.form['nome']
   
   return conveersao(distanciaatual,distanciaentre,nome)
 
if __name__ == "__main__":
    app.run()




