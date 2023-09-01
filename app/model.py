import joblib

# Nombre del archivo donde se encuentra el modelo guardado
file = 'model/modelo_entrenado.joblib'

# Cargar el modelo utilizando joblib
model = joblib.load(file)

def model_predict(form):
    predicted = model.predict_proba(form)
    result =  predicted[:, 1][0] * 100
    return result