'''
Dadas las cantidades de dinero aportadas por Ana, Raquel y Lucía para formar un 
capital, diseñe un programa que determine el monto del capital formado y el 
porcentaje de dicho capital que aporta cada una.
'''

ana_aporte = float(input("Ingrese el aporte de Ana: "))
raquel_aporte = float(input("Ingrese el aporte de Raquel: "))
lucia_aporte = float(input("Ingrese el aporte de Lucía: "))
total_aporte = ana_aporte + raquel_aporte + lucia_aporte


# ! Porcentajes de aporte
ana_porcentaje = ana_aporte / total_aporte * 100
raquel_porcentaje = raquel_aporte / total_aporte * 100
lucia_porcentaje = lucia_aporte / total_aporte * 100


print(f"Ana aportó el {round(ana_porcentaje, 2)}%")
print(f"Raquel aportó el {round(raquel_porcentaje, 2)}%")
print(f"Lucía aportó el {round(lucia_porcentaje, 2)}%")
print(f"El monto total de la capital es: {total_aporte}")