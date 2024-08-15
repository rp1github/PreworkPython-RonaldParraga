'''
Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)

Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.
'''

peso = 0
altura = 0
imc = 0

def calcula_imc(peso, altura):
    return peso / (altura * altura)

peso = int(input('Por favor, ingresa tu peso: '))
altura = float(input('Por favor, ingresa tu altura: '))

imc = calcula_imc(peso, altura) # Llama a la función y almacena el resultado en la variable 
print('El Indice de Masa Corporal es:', imc) 