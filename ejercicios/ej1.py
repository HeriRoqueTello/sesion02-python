'''
Diseñar un algoritmo que permita ingresar tres notas, y luego muestre 
el promedio que generan estas notas.
'''

nota1 = float(input("Ingrese la primera nota del alumno: "))
nota2 = float(input("Ingrese la segunda nota del alumno: "))
nota3 = float(input("Ingrese la tercera nota del alumno: "))

promedio = (nota1 + nota2 + nota3)/3

print(f"El promedio del alumno es:  {promedio.round(2)}")