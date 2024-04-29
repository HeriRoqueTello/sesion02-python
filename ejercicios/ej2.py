'''
Diseñar un algoritmo que permita calcular y mostrar el área y 
perímetro de un rectángulo ingresando como datos su base y altura
'''

base = float(input("Ingrese la base del rectangulo: "))
altura = float(input("Ingrese la altura del rectangulo: "))

perimetro = 2 * (base + altura)
area = base * altura

print(f"El perimetro del rectangulo es: {perimetro}")
print(f"El area del rectangulo es: {area}")