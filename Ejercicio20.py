'''
Ejercicio 20: Suma de Números en una Lista

Crea un programa que sume todos los números en una lista ingresada por el
usuario.
'''

inicio = int(input('Por favor, ingresa el número de inicio de tu lista: '))
fin = int(input('Por favor, ingresa el número final de tu lista: '))
i = inicio

def suma_lista(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma

lista_usuario = []
while i <= fin:
    lista_usuario.append(i)
    i = i + 1
print(lista_usuario)
print(suma_lista(lista_usuario)) 