#estatura en centimetros y peso en kg
def bmi(height, weight):
    h = float(height) / 100
    w = int(weight)
    if w <= 0 or h <= 0:
        raise ValueError("El peso y la altura deben ser valores positivos.")
    return w / (h ** 2)

def obtain_group(a):
    age = int(a)
    group = None

    if age <0:
        raise ValueError ("La edad debe ser válida")
    elif 0 <= age < 18:
        return 0
    elif 18 <= age <= 24:
        group = 1
    elif 25 <= age <= 29:
        group = 2
    elif 30 <= age <= 34:
        group = 3
    elif 35 <= age <= 39:
        group = 4
    elif 40 <= age <= 44:
        group = 5
    elif 45 <= age <= 49:
        group = 6
    elif 50 <= age <= 54:
        group = 7
    elif 55 <= age <= 59:
        group = 8
    elif 60 <= age <= 64:
        group = 9
    elif 65 <= age <= 69:
        group = 10
    elif 70 <= age <= 74:
        group = 11
    elif 75 <= age <= 79:
        group = 12
    else:
        group = 13
    
    return group