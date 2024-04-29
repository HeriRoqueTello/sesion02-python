'''
Una empresa ha decidido otorgar una bonificación a sus empleados por única vez. La 
bonificación estará compuesta de la suma de una bonificación por hijos más una 
bonificación por tiempo de servicio. La bonificación por hijos será igual a S/. 25 por cada hijo. 
La bonificación por tiempo de servicio será igual a S/. 50 por cada año de tiempo de servicio. 
Dado el número de hijos y el número de años de tiempo de servicio, diseñe un algoritmo que 
determine el importe de la bonificación por hijos, el importe de la bonificación por tiempo 
de servicio y el importe de la bonificación total que le corresponden a un empleado.
'''

hijos = int(input("Introduce el número de hijos: "))
bonificacion_hijos = hijos * 25

tiempo_servicio = int(input("Introduce el tiempo de servicio en años: "))
bonificacion_tiempo = tiempo_servicio * 50

print(f"La bonificación por hijos es: {bonificacion_hijos}")
print(f"La bonificación por tiempo de servicio es: {bonificacion_tiempo}")
print(f"La bonificación total es: {bonificacion_hijos + bonificacion_tiempo}")