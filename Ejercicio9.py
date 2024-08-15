'''
Ejercicio 9: Conversor de Divisas

Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que
1 dólar es igual a 0.85 euros.
'''

euros = 0
dolares = 0

def calcula_euros(dolares):
    return dolares * 0.85

dolares = float(input('Por favor, ingresa el importe en dolares: '))
euros  = calcula_euros(dolares) # Llama a la función y almacena el resultado en la variable
print('El equivalentes es:', euros, 'Euros') 