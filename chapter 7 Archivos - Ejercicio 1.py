# Ejercicio 1: Escribe un programa que lea un archivo e imprima su contenido (línea por línea), todo en mayúsculas.

nombre_archivo = input('Ingresa un nombre de archivo: ')

try:
    manejador_archivo = open(nombre_archivo)
except:
    print('No se encuentra el siguiente archivo: ', nombre_archivo)

for linea in manejador_archivo:
    linea = linea.rstrip()
    print(linea.upper())