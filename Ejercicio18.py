'''
Ejercicio 18: Contador de Palabras

Crea un programa que cuente la cantidad de palabras en una oración ingresada por
el usuario.
'''

TextoUsuario = str(input('Por favor, ingresa la oración para contar las palabras: '))
Palabras = TextoUsuario.split()
ContadorPalabras = len(Palabras)
print('La oración tiene', ContadorPalabras, 'palabras')