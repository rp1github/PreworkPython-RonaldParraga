'''
Ejercicio 15: Conversor de Tiempo

Escribe un programa que convierta un número de minutos en horas y minutos. Por
ejemplo, 145 minutos serían 2 horas y 25 minutos.
'''

minutos = int(input('Por favor, ingresa el número de minutos: '))
print(minutos, 'minutos equivalen a:', minutos // 60, 'Horas ', minutos % 60, 'Minutos' ) 
