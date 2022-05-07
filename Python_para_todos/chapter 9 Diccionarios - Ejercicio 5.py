# Ejercicio 5: Este programa almacena el nombre del dominio (en vez de la dirección) desde donde fue enviado el
# mensaje en vez de quién envió el mensaje (es decir, la dirección de correo electrónica completa). Al final del
# programa, imprime el contenido de tu diccionario.

file_name = input('Ingresa un nombre de archivo: ')

try:
    file_manager= open(file_name)
except:
    print('No se puede abrir el archivo:',file_name)
    exit()

domain = dict()

for line in file_manager:

    word= line.split()

    if len(word) == 0 or word[0] != 'From' or len(word) < 2 : continue
    #print(line) 
    word_extrac= word[1]
    #print(word_extrac[word_extrac.find('@'):]+1)

    domain[word_extrac[word_extrac.find('@')+1:]] = domain.get(word_extrac[word_extrac.find('@')+1:], 0) + 1

print(domain)