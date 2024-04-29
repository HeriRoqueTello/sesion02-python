'''
Se ingresa un monto de dinero de 5 cifras, y reporte cuantos billetes 
de 200, 100, 50, 20, 10 y monedas de 5, 2 y 1 sol se necesitan para 
completar el número
'''

importe = int(input("Ingrese el importe: "))
# Lista de billetes y monedas
lista =[200, 100, 50, 20, 10, 5, 2, 1]
# Lista de soluciones donde cada posición representa la cantidad de billetes o monedas de la lista
solucion =[0, 0, 0, 0, 0, 0, 0, 0]
 
 
# Recorremos la lista de billetes y monedas
for i in range(0, len(lista)):
    # Calculamos cuantas monedas o billetes de la lista[i] necesitamos
    resto = lista[i]
    # Se hace un ciclo restando el importe y el billete o moneda de la lista[i] hasta que sea menor a 0
    while importe - resto >= 0:
        solucion[i] += 1
        importe -= resto
 
# Imprimimos la solución recorriendo el array de soluciones
for i in range(0, len(solucion)):
    # Si la solución[i] es mayor a 0, imprimimos cuantas monedas o billetes de la lista[i] necesitamos
    if solucion[i] > 0:
        print(f'{solucion[i]} monedas de {lista[i]}')