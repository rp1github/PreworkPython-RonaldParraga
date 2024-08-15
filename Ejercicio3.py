'''
Ejercicio 3: Verificación de Edad

Escribe un programa que solicite la edad de un usuario y determine si es mayor de
edad (mayor o igual a 18 años) o no.
'''

Edad = int(input('Por favor, ingresa tu edad: '))

if Edad >= 18:
    print('Es mayor de edad' )
else:
    print('No es mayor de edad, tiene', Edad, 'años' )
