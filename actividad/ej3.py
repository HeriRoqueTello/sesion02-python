'''
Una empresa de taxi cobra por una carrera 5 soles por kilómetro 
recorrido y 2 soles por minuto, de la suma de ambos datos se 
obtiene el costo total de la carrera. Determine el monto a pagar por 
una carrera.
'''

kilometros = float(input("Introduce la distancia en kilómetros: "))
tiempo = float(input("Introduce el tiempo en minutos: "))

km_costo = kilometros * 5
tiempo_costo = tiempo * 2

print(f"El costo total del viaje es: {km_costo + tiempo_costo}")