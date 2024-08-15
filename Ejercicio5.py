'''
Ejercicio 5: Suma de Números Pares

Escribe un programa que calcule la suma de todos los números pares del 1 al 100.
'''

SumaPares = 0
i = 1

while i <= 100:
    if i % 2 == 0:
        SumaPares += i
    i += 1
print('La suma de todos los números pares es:', SumaPares)
