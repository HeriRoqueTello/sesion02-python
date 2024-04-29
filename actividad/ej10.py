'''
Una imprenta ha lanzado al mercado la venta al por mayor del cuaderno de 100 hojas mentor que 
es distribuido a nivel nacional. El importe compra se calcula multiplicando el precio de la docena 
por la cantidad de docenas adquiridas. Como oferta, la imprenta aplica un descuento del 12% del 
importe compra. El importe a pagar se calcula restando el importe de la compra menos el importe 
del descuento y sumando el costo del transporte. Dado el precio de la docena, la cantidad de 
docenas adquiridas y el costo del transporte, diseñe un algoritmo que determine el importe 
compra, el importe del descuento y el importe a pagar que le corresponden a un cliente
'''

precio_docenas = float(input("Ingrese el precio por docena: "))
cantidad_docenas = float(input("Ingrese la cantidad de docenas: "))
costo_transporte = float(input("Ingrese el costo de transporte: "))

importe_compra = precio_docenas * cantidad_docenas
descuento = importe_compra * 0.12
importe_pagar = importe_compra - descuento + costo_transporte

print(f"El importe de la compra es: S/ {importe_compra}")
print(f"El descuento es: S/ {descuento}")
print(f"El importe a pagar es: S/ {importe_pagar}")
