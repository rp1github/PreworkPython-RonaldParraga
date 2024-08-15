'''
Ejercicio 1: Conversor de Temperatura

Escribe un programa que convierta una temperatura de grados Celsius a grados
Fahrenheit.
'''

GradosCelsius = int(input('Por favor, ingresa la temperatrura en ºC: '))
GradosFahrenheit = (GradosCelsius * 9 // 5) + 32
print(GradosCelsius, 'ºC es equivalente a', GradosFahrenheit, 'ºF')
