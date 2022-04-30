# Ejercicio 3: Escribe un programa para leer a través de un historial de correos, construye un histograma
# utilizando un diccionario para contar cuántos mensajes han llegado de cada dirección de correo electrónico, 
# e imprime el diccionario.

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
    days[word[1]] = days.get(word[1], 0) + 1

print(days)