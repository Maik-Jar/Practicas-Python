# Ejercicio 4: Agrega código al programa anterior para determinar quién tiene la mayoría de mensajes en el archivo.
# Después de que todos los datos hayan sido leídos y el diccionario haya sido creado, mira a través del diccionario
# utilizando un bucle máximo (ve Capítulo 5: Bucles máximos y mínimos) para encontrar quién tiene la mayoría de 
# mensajes e imprimir cuántos mensajes tiene esa persona.

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

lst= list(emails.keys())
contador= 0
llave = None

for i in lst:

    if emails[i] > contador:
        contador = emails[i]
        llave = i

print(llave, emails[llave])
