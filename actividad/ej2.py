'''
Una empresa paga a sus empleados además del sueldo base una 
bonificación especial de 80 soles por cada hijo. Realice un algoritmo 
que determine el monto de la bonificación y el monto total a pagar al 
trabajador
'''

sueldo_base = float(input("Introduce el sueldo base del trabajador: "))
hijos = int(input("Introduce el número de hijos del trabajador: "))

bonificacion = 80 * hijos

print(f"La bonificación por hijos es: {bonificacion}")
print(f"El sueldo neto del trabajador es: {sueldo_base + bonificacion}")