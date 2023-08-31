from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

dicionario = { 'A':{"B":5,"C":6},
              'B':{"D":3},
              'C':{"D":4, "E":2},
              'D':{"E":1},
              'E':{"E":0}}

@app.route("/", methods=['POST'])
def post():
    valorA = request.form['valorA']
    valorE = request.form['valorE']
    
  
    
if __name__ == "__main__":
    app.run()




