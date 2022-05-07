# Ejercicio 3: Algunas veces cuando los programadores se aburren o quieren divertirse un poco, agregan un inofensivo Huevo de Pascua
# a su programa. Modifica el programa que pregunta al usuario por el nombre de archivo para que imprima un mensaje divertido cuando el
# usuario escriba “na na boo boo” como nombre de archivo.

name_file = input('Please, write the file name: ')

try :
    file_manager = open(name_file)

    spam_prom = 0
    count = 0

    for line in file_manager:

        if line.find('X-DSPAM-Confidence:') == -1: 
            continue

        count += +1
        spam_prom += + float(line[20:])
    
    print(spam_prom/count)

except:
    if name_file.__eq__('na na boo boo'):
        print('NA NA BOO BOO PARA TI - Te he atrapado!')
    else:
        print('El archivo no puede ser abierto: ',name_file)