# Ejercicio 3: Encapsula este código en una función llamada cuenta, y
# hazla genérica de tal modo que pueda aceptar una cadena y una letra
# como argumentos.

palabra = input('Por favor introduzca una palabra: ')
letra= input('Introduzca la letra que desea contar: ')

def cuenta (cadena, letra):
    contador = 0
    
    for i in cadena:
        if i == letra:
            contador = contador + 1

    print(contador)

cuenta(palabra, letra)