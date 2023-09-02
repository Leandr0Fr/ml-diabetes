from flask import Flask, render_template
from model import model_predict
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# @app.route('/predict', methods=['POST'])
# def predict():
#     #Obtener los datos del formulario
#     #Vemos si retornamos el mismo html modificando una variable
#     #O otro html con el resultado y demas
#     result = str(model_predict())
#     return result
    
# Esto es lo nuevo, a partir de aca se guardan las variables en una lista

# dataList = []

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         diabetes = request.form.get('Diabetes')
#         high_bp = request.form.get('HighBP')
#         high_chol = request.form.get('HighChol')
#         chol_check = request.form.get('CholCheck')
#         bmi = request.form.get('BMI')
#         smoker = request.form.get('Smoker')
#         heartDesease = request.form.get('HeartDiseaseorAttack')
#         physicalActivity = request.form.get('PhysActivity')
#         fruits = request.form.get('Fruits')
#         veggies = request.form.get('Veggies')
#         alcoholic = request.form.get('HvyAlcoholConsump')
#         physicalHealth = request.form.get('PhysHlth')
#         walkingDifficulty = request.form.get('DiffWalk')
#         sex = request.form.get('Sex')
#         age = request.form.get('Age')

#         form_data = {
#             'Diabetes': diabetes,
#             'HighBP': high_bp,
#             'HighChol': high_chol,
#             'CholCheck': chol_check,
#             'BMI': bmi,
#             'Smoker': smoker,
#             'HeartDiseaseorAttack': heartDesease,
#             'PhysActivity': physicalActivity,
#             'Fruits': fruits,
#             'Veggies': veggies,
#             'HvyAlcoholConsump': alcoholic,
#             'PhysHlth': physicalHealth,
#             'DiffWalk': walkingDifficulty,
#             'Sex': sex,
#             'Age': age
#         }

#         dataList.append(form_data)

#         return render_template('results.html', form_data=form_data) 
#     return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    #Obtener los datos del formulario
    #Vemos si retornamos el mismo html modificando una variable
    #O otro html con el resultado y demas
    result = str(model_predict())
    return result

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)