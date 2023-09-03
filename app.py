from flask import Flask, render_template, request, url_for
from model import model_predict

app = Flask(__name__)
app.static_folder = 'templates/static'
@app.route("/")
def home():
    return render_template("index.html")

# Inicializa dos listas: una para las claves (nombres de las variables) y otra para los valores de las variables
keys_list = []
values_list = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Define las variables y sus nombres
        variables = {
            'BMI': request.form.get('BMI'),
            'Age': request.form.get('Age'),
            'PhysHlth': request.form.get('PhysHlth'),
            'Sex': request.form.get('Sex'),
            'HighBP': request.form.get('HighBP'),
            'HighChol': request.form.get('HighChol'),
            'CholCheck': request.form.get('CholCheck'),
            'Smoker': request.form.get('Smoker'),
            'HeartDiseaseorAttack': request.form.get('HeartDiseaseorAttack'),
            'PhysActivity': request.form.get('PhysActivity'),
            'Fruits': request.form.get('Fruits'),
            'Veggies': request.form.get('Veggies'),
            'HvyAlcoholConsump': request.form.get('HvyAlcoholConsump'),
            'DiffWalk': request.form.get('DiffWalk'),
           # 'Diabetes': request.form.get('Diabetes'),   
        }

        # Almacena las claves (nombres de las variables) en la lista de claves
        keys_list.extend(variables.keys())

        # Almacena los valores de las variables en la lista de valores
        values_list.extend(variables.values())

        return render_template('results.html', variables=variables)
    return render_template('form.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)