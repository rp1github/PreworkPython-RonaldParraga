'''
Ejercicio 16: Contador de Números Pares e Impares

Crea un programa que cuente y muestre la cantidad de números pares e impares en
una lista ingresada por el usuario.
'''

fin = int(input('Por favor, ingresa el número final de tu lista: '))

def lista_pares(n):
    return [i for i in range(n+1)
             if i % 2 == 0]
print('La lista de números pares es:', lista_pares(fin)) 

def lista_impares(n):
    return [i for i in range(n+1)
             if i % 2 != 0]
print('La lista de números impares es:', lista_impares(fin)) 
