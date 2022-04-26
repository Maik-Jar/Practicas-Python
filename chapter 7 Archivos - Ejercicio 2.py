# Ejercicio 2: Escribe un programa que solicite un nombre de archivo y después lea
# ese archivo buscando las líneas que tengan la siguiente forma: X-DSPAM-Confidence: 0.8475

name_file = input('Please, write the file name: ')

file_manager = open(name_file)

spam_prom = 0
count = 0

for line in file_manager:

    if line.find('X-DSPAM-Confidence:') == -1: 
        continue

    count += +1
    spam_prom += + float(line[20:])
    
print(spam_prom/count)