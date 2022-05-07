# Ejercicio 6: Reescribe el programa que pide al usuario una lista de números e imprime el máximo y el mínimo 
# de los números al final cuando el usuario ingresa “hecho”. Escribe el programa para almacenar los números
# que el usuario ingrese en una lista, y utiliza las funciones max() y min() para calcular el máximo y el mínimo 
# después de que el bucle termine.

valor= None
lista= []

while True:
    try:
        valor= input('Introduzca un número: ')

        if valor.lower() == 'fin':
            break
       
        lista.append(int(valor))

    except:
        print('Entrada invalida')

print(max(lista), min(lista))