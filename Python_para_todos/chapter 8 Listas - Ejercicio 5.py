# Ejercicio 5: Escribir un programa para leer a través de datos de una bandeja de entrada de correo y cuando 
# encuentres una línea que comience con “From”, dividir la línea en palabras utilizando la función split.
# Estamos interesados en quién envió el mensaje, lo cual es la segunda palabra en las líneas que comienzan con From.

file_manager = open(input('Ingresa un nombre de archivo: '))
contador = 0

for line in file_manager:
    #print(len(line.strip()))
    if len(line.strip()) == 0: continue
    
    words = line.split()

    if words[0] == 'From':
        print(words[1])
        contador += +1

print('Hay '+str(contador)+' lineas en el archivo con la palabra From al inicio.')