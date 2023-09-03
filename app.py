from flask import Flask, render_template, request
from model import model_predict
from util import *

app = Flask(__name__)
app.static_folder = 'templates/static'

@app.route("/")
def home():
    return render_template("index.html", Diabetes = "Posibilidad de Diabetes")

@app.route('/predict', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
            form = [[
            request.form.get('HighBP'),
            request.form.get('HighChol'),
            request.form.get('CholCheck'),
            bmi(request.form.get('Height'),request.form.get('Weight')),
            request.form.get('Smoker'),
            request.form.get('Stroke'),
            request.form.get('HeartDiseaseorAttack'),
            request.form.get('PhysActivity'),
            request.form.get('Fruits'),
            request.form.get('Veggies'),
            request.form.get('HvyAlcoholConsump'),
            request.form.get('PhysHlth'),
            request.form.get('DiffWalk'),  
            request.form.get('Sex'),
            obtain_group(request.form.get('Age'))]]
            result = str(model_predict(form))
            return render_template('index.html', Diabetes = "Posibilidad del " + result)
    return render_template('form.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)