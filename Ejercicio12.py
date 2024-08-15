'''
Ejercicio 12: Calculadora de Área de un Rectángulo

Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la
longitud y el ancho del rectángulo.
'''

longitud = 0
ancho = 0
area = 0

def calcula_area(longitud, ancho):
    return longitud * ancho

ancho = int(input('Por favor, ingresa el ancho en cm: '))
longitud = int(input('Por favor, ingresa la longitud en cm: '))
area_rectangulo  = calcula_area(longitud, ancho) # Llama a la función y almacena el resultado en la variable
print('El área del rectángulo es:', area_rectangulo, 'cm2') 
