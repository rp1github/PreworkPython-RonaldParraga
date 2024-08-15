'''
Ejercicio 14: Calculadora de Descuento

Crea un programa que calcule el precio final de un artículo después de aplicar un
descuento del 20%.
'''

PrecioProducto = 0
PorcentajeDescuento = 20
PrecioProducto = int(input('Por favor, ingresa el precio del artículo: '))

print('Descuento aplicable:', PorcentajeDescuento,'%')
TotalPagar = PrecioProducto - ((PorcentajeDescuento / 100) * PrecioProducto) 
print('El precio final del artículo es:', TotalPagar, 'Euros')
