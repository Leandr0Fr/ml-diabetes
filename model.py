import joblib

# Nombre del archivo donde se encuentra el modelo guardado
file = 'app/model/modelo_entrenado.joblib'

# Cargar el modelo utilizando joblib
model = joblib.load(file)

def model_predict():
    #Aca falta definir como retornar el resultado
    #Retornamos solo el resultado o que onda
    form= [[0, 1,1,28,0,0, 1, 0,0,0, 0, 0, 0, 0, 12]]
    predicted = model.predict_proba(form)
    result =  predicted[:, 1][0] * 100
    return result