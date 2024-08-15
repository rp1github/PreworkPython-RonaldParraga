'''
Ejercicio 11: Calculadora de Edad

Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad
actual.
'''

from datetime import datetime

año_nacimiento = 0
edad = 0
hoy = datetime.now()

año_nacimiento = int(input('Por favor, ingresa su año de nacimiento: '))
if año_nacimiento >= hoy.year or año_nacimiento <= 0:
    print('El número:', año_nacimiento, 'Está fuera del rango de años del cálculo de edad.') 
else:
    edad = hoy.year - año_nacimiento
    print('Tu edad es:', edad) 
