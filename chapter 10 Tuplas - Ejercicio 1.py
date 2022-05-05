# Ejercicio 1: Revisa el programa anterior de este modo: Lee y analiza las líneas “From” y extrae las
# direcciones de correo. Cuenta el número de mensajes de cada persona utilizando un diccionario. 

# Después de que todos los datos hayan sido leídos, imprime la persona con más envíos, creando una lista de tuplas 
# (contador, email) del diccionario. Después ordena la lista en orden inverso e imprime la persona que tiene más envíos.

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
    emails[word[1]] = emails.get(word[1], 0) + 1


lst= list()

for clave, valor in list(emails.items()):
    lst.append((valor, clave))

lst.sort(reverse= True)

for clave, valor in lst[:1]:
    print(valor, clave)