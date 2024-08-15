'''
Ejercicio 10: Determinar el Día de la Semana

Escribe un programa que determine el día de la semana correspondiente a un
número ingresado por el usuario (1 para lunes, 2 para martes, etc.).
'''

lista_nro = [1, 2, 3, 4, 5, 6, 7]

dicc_semana = {
    1: 'lunes', 
    2: 'martes', 
    3: 'miercoles', 
    4: 'jueves', 
    5: 'viernes', 
    6: 'sabado', 
    7: 'domingo'
}

numero = int(input('Por favor, ingresa el número del día de la semana: '))
if numero not in lista_nro:
    print('El número:', numero, 'No corresponde a un día de la semana.') 
else:
    for clave, valor in dicc_semana.items():
        if clave == numero:
            print('El día de la semana es:', valor) 
            break
