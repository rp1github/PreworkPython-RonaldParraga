'''
Ejercicio 13: Verificación de Número Primo

Escribe un programa que determine si un número ingresado por el usuario es primo
o no.
'''

num = 0
n = 0
si_no = 'Si'

num = int(input('Por favor, ingresa un número: '))
for n in range(2, num):
        if num % n == 0:
            print('No es primo.', n, 'es divisor')
            si_no = 'No'
print('Conclusión: el número', num, si_no, 'es un número primo')
