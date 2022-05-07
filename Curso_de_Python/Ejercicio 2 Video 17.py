numero= 0
total= 0

while True:
    try:
        numero= int(input('Introduce un número por favor: '))

        if numero < 0:
            print(f'Has introducido un número negativo: {numero}.\n')
            break

        total += numero
    except:
        print('Entrada invalida. Por favor introduzca solo números.')

print(f'El programa ha finalizado. la suma total de todos los números introducidos es: {total}')