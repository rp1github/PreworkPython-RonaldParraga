'''
Ejercicio 7: Calculadora Simple

Crea un programa que realice operaciones aritméticas simples (suma, resta,
multiplicación, división) según la elección del usuario.

'''

numero1 = 0
numero2 = 0
resultado = 0
operador = ' '

def suma(numero1, numero2):
    return numero1 + numero2

def resta(numero1, numero2):
    return numero1 - numero2

def multiplica(numero1, numero2):
    return numero1 * numero2

def divide(numero1, numero2):
    return numero1 / numero2

numero1 = int(input('Por favor, ingresa el primer número: '))
numero2 = int(input('Por favor, ingresa el segundo número: '))
operador = str(input('Por favor, ingresa el operador aritmético (+, -, *, /): '))


if operador == "+":
    resultado = suma(numero1, numero2) # Llama a la función y almacena el resultado en la variable 
elif operador == '-':
    resultado = resta(numero1, numero2) # Llama a la función y almacena el resultado en la variable 
elif operador == '*':
    resultado = multiplica(numero1, numero2) # Llama a la función y almacena el resultado en la variable 
elif operador == '/':
    resultado = divide(numero1, numero2) # Llama a la función y almacena el resultado en la variable     
else:
    print("El operador ingresado no es válido, vuelve a intentarlo")

print('El resultado es:', resultado) 