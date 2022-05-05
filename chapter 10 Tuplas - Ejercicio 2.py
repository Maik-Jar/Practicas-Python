# Ejercicio 2: Este programa cuenta la distribución de la hora del día para cada uno de los mensajes. Puedes extraer 
# la hora de la línea “From” buscando la cadena horaria y luego dividiendo la cadena en partes utilizando el carácter 
# colon. Una vez que hayas acumulado las cuentas para cada hora, imprime las cuentas, una por línea, ordenadas por 
# hora tal como se muestra debajo.

import re


file_name = input('Ingresa un nombre de archivo: ')

try:
    file_manager= open(file_name)
except:
    print('No se puede abrir el archivo:',file_name)
    exit()

emails = dict()

for line in file_manager:

    word= line.split()

    if len(word) == 0 or word[0] != 'From' or len(word) < 2 : continue
    #print(line)
    hour= word[5]
    emails[hour[0:2]] = emails.get(hour[0:2], 0) + 1

lst= list(emails.items())

#for clave, valor in list(emails.items()):
#    lst.append((valor, clave))

lst.sort()

for clave, valor in lst:
    print(clave, valor)