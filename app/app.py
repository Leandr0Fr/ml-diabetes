from flask import Flask, render_template
from model import model_predict

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    #Obtener los datos del formulario
    #Vemos si retornamos el mismo html modificando una variable
    #O otro html con el resultado y demas
    result = str(model_predict())
    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)