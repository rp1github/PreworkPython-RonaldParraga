'''
Ejercicio 4: Contador de Vocales

Crea un programa que cuente el número de vocales en una palabra ingresada por el
usuario.
'''

vocales = 'aeiouAEIOU'
NumeroVocales = 0

palabra = str(input('Por favor, ingresa una palabra: '))

for letra in palabra:
    if letra in vocales:
        print('Vocal enocntrada:', letra)
        NumeroVocales += 1
print('Número de vocales en la palabra:', NumeroVocales)
