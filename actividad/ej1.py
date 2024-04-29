'''
Una empresa desea que se le realice un algoritmo con el que pueda 
hallar el sueldo neto de cada trabajador; si estos tienen un 
descuento del 10% del sueldo básico y una bonificación equivalente 
al 20% del sueldo básico.
'''

sueldo = float(input("Introduce el sueldo del trabajador: "))

bonificacion = sueldo * 0.20
descuento = sueldo * 0.10
sueldo_neto = sueldo + bonificacion - descuento

print(f"El sueldo neto del trabajador es: {sueldo_neto}") 