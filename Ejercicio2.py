'''
Ejercicio 2: Calculadora de Propina

Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo
una propina del 15% sobre el total de la cuenta.
'''

TotalConIva = float(input('Por favor, ingresa el total de la cuenta: '))
PorcentajePropina = 15
print('Propina:', PorcentajePropina,'%')
TotalPagar = ((PorcentajePropina / 100) * TotalConIva) + TotalConIva
print('El monto total a pagar es:', TotalPagar, 'Euros')
