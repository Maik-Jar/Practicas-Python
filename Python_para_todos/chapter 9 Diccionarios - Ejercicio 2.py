# Ejercicio 2: Escribir un programa que clasifica cada mensaje de correo dependiendo del día de la semana en que se 
# recibió. Para hacer esto busca las líneas que comienzan con “From”, después busca por la tercer palabra y mantén
# un contador para cada uno de los días de la semana. Al final del programa imprime los contenidos de tu diccionario 
# (el orden no importa).

# Línea de ejemplo:
# From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# Ejemplo de ejecución:
# python dow.py
# Ingresa un nombre de archivo: mbox-short.txt
# {'Fri': 20, 'Thu': 6, 'Sat': 1}

file_name = input('Ingresa un nombre de archivo: ')

try:
    file_manager= open(file_name)
except:
    print('No se puede abrir el archivo:',file_name)
    exit()

days = dict()

for line in file_manager:

    word= line.split()

    if len(word) == 0 or word[0] != 'From' or len(word) < 2 : continue
    #print(line) 
    days[word[2]] = days.get(word[2], 0) + 1

print(days)