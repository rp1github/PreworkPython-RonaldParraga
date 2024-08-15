'''
Ejercicio 6: Verificación de Palíndromo

Crea un programa que verifique si una palabra ingresada por el usuario es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
'''

palabra = str(input('Por favor, ingresa una palabra: '))

palabra_invertida = palabra[::-1]
print(palabra_invertida)

if palabra == palabra_invertida:
    print(palabra, 'Es un palíndromo')
else:
    print('No es un palíndromo')


'''
funcion explicada en el documento de funciones

def es_palindromo(palabra):
    palabra = palabra.lower()
    return palabra == palabra[::-1]

print(es_palindromo('python')) 
'''
