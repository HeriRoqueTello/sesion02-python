'''
Una tienda ha puesto en oferta la venta un producto ofreciendo un descuento 
denominado 10%+10% que consiste en aplicar dos descuentos del 10%. El importe compra 
se calcula multiplicando el precio del producto por la cantidad de unidades adquiridas. El 
primer descuento es igual al 10% del importe compra. El segundo descuento es igual al 
10% del importe que queda de restar el importe compra menos el importe del primer 
descuento. El importe del descuento total se calcula sumando el primer y el segundo 
descuento. El importe a pagar se calcula restando el importe compra menos el importe del 
descuento total. Dado el precio del producto y la cantidad de unidades adquiridas, diseñe 
un algoritmo que determine el importe de la compra, el importe del descuento total y el 
importe a pagar
'''

productos = float(input("Ingrese la cantidad de productos: "))
precio = float(input("Ingrese el precio del producto: "))

importe = productos * precio

desc_1 = importe * 0.10
importe_desc_1 = importe - desc_1
desc_2 = importe_desc_1 * 0.10
desc_total = desc_1 + desc_2

importe_total = importe - desc_total

print(f"El importe total es: {importe_total}")
print(f"El descuento total es: {desc_total}")