import joblib

# Nombre del archivo donde se encuentra el modelo guardado
file = 'model/modelo_1.0.2.joblib'

# Cargar el modelo utilizando joblib
model = joblib.load(file)

def model_predict(list):
    predicted = model.predict_proba(list)
    result =  f"{predicted[:, 1][0] * 100:.1f}%"
    return result  