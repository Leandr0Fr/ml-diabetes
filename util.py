#estatura en centimetros y peso en kg
def imc(height, weight):
    if weight <= 0 or height <= 0:
        raise ValueError("El peso y la altura deben ser valores positivos.")
    return weight / (height ** 2)