from flask import Flask,render_template,request,jsonify

app = Flask(__name__)

@app.route("/")
def index():
   
    return render_template("index.html")

@app.route("/", methods=['POST'])
def post():
   value = request.form["valueA"]
  
   
if __name__ == "__main__":
    app.run()




