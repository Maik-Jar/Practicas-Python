# Ejercicio 3: Escribe un programa que lee un archivo e imprime las letras en order decreciente de frecuencia. 
# El programa debe convertir todas las entradas a minúsculas y contar solamente las letras a-z. El programa no debe 
# contar espacios, dígitos, signos de puntuación, o cualquier cosa que no sean las letras a-z. Encuentra ejemplos de
# texto en idiomas diferentes, y observa cómo la frecuencia de letras es diferente en cada idioma.

import string
manejador = open('romeo.txt')
contadores = dict()

for linea in manejador:
    linea = linea.translate(str.maketrans('', '', string.punctuation))
    linea = linea.lower()
    palabras = linea.split()

    for palabra in palabras:
        for letra in palabra:
            if letra not in contadores:
                contadores[letra] = 1
            else:
                contadores[letra] += 1

# Ordenar el diccionario por valor
lst = list(contadores.items())

#for clave, valor in list(contadores.items()):
#    lst.append((valor, clave))

lst.sort()

for clave, valor in lst:
    print(clave, valor)
