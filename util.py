#estatura en centimetros y peso en kg
def bmi(height, weight):
    h = int(height)
    w = int(weight)
    if w <= 0 or h <= 0:
        raise ValueError("El peso y la altura deben ser valores positivos.")
    return w / (h ** 2)

def obtener_grupo(e): # Falta conseguir la edad desde el formulario
    edad = int(e)
    grupo = None

    if edad <0:
        raise ValueError ("La edad debe ser válida")
    elif 0 <= edad < 18:
        return 0
    elif 18 <= edad <= 24:
        grupo = 1
    elif 25 <= edad <= 29:
        grupo = 2
    elif 30 <= edad <= 34:
        grupo = 3
    elif 35 <= edad <= 39:
        grupo = 4
    elif 40 <= edad <= 44:
        grupo = 5
    elif 45 <= edad <= 49:
        grupo = 6
    elif 50 <= edad <= 54:
        grupo = 7
    elif 55 <= edad <= 59:
        grupo = 8
    elif 60 <= edad <= 64:
        grupo = 9
    elif 65 <= edad <= 69:
        grupo = 10
    elif 70 <= edad <= 74:
        grupo = 11
    elif 75 <= edad <= 79:
        grupo = 12
    else:
        grupo = 13
    
    return grupo