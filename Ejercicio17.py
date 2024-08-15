'''
Ejercicio 17: Conversor de Millas a Kilómetros

Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo
que 1 milla equivale a 1.60934 kilómetros.
'''

Millas = int(input('Por favor, ingresa la distancia en millas: '))

Kilometros = round(Millas * 1.60934)
print(Millas, 'Millas son', Kilometros, 'Kilómetros')
