'''
Se piensa repartir una herencia entre 3 hermanos, la repartición será 
de la siguiente manera:
 Al hermano mayor le tocará el 30% del total de la herencia, al 
hermano intermedio le tocará el 37% del total de la herencia y al 
hermano menor lo que queda. 
Desarrolle un algoritmo que permita calcular y mostrar cuanto le 
tocó a cada uno
'''

total_herencia = float(input("Ingrese el total de la herencia: "))

hermano_mayor = total_herencia * 0.30
hermano_medio = total_herencia * 0.37
hermano_menor = total_herencia - (hermano_mayor + hermano_medio)

print(f"El hermano mayor recibirá: {hermano_mayor}")
print(f"El hermano del medio recibirá: {hermano_medio}")
print(f"El hermano menor recibirá: {hermano_menor}")