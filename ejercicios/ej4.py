'''
Se ingresa un número de dos cifras, descomponerlo y luego mostrar la 
suma de sus componentes
'''

num = input("Ingrese un numero de 2 digitos: ")
# Se extraen los digitos del numero ya que es un string, el cual tiene indices como un array y los convertimos a enteros en interger para sumarlos
sum = int(num[0]) + int(num[1])
print(f"La suma de los digitos es: {sum}")
