'''
Se ingresa un número de 3 cifras, deberá desarrollar un algoritmo 
que permita invertir el número.
 Ejemplo: se ingresa 375
 Debe retornar como resultado final 573
'''

numero = int(input("Ingrese un número de 3 cifras: "))

invert_num = numero % 10 * 100 + numero // 10 % 10 * 10 + numero // 100

print(f"El primer digito es: {numero % 10 * 100}") # 375 % 10 = 5 -> 5 * 100 = 500
print(f"El segundo digito es: {numero // 10 % 10 * 10}") # 375 // 10 = 37 -> 37 % 10 = 7 -> 7 * 10 = 70
print(f"El tercer digito es: {numero // 100}") # 375 // 100 = 3
print(f"El número invertido es: {invert_num}")