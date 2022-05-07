# Ejercicio 4: Descargar una copia de un archivo www.py4e.com/code3/romeo.txt.
# Escribir un programa para abrir el archivo romeo.txt y leerlo línea por línea. Para cada línea, dividir la línea en una lista de palabras
# utilizando la función split. Para cada palabra, revisar si la palabra ya se encuentra previamente en la lista. Si la palabra no está en la lista,
# agregarla a la lista. Cuando el programa termine, ordenar e imprimir las palabras resultantes en orden alfabético.

file_manager = open(input('Introduzca nombre del archivo: '))
words_list = []

for line in file_manager:

    words = line.split()
    #print(words)
    for i in range(len(words)):
        #print(i)
        if words[i] not in words_list:
            words_list.append(words[i])

words_list.sort()
print(words_list)