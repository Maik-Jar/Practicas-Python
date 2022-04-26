numero= 0
num2= 0

while True:
    try:
        numero= int(input('Introduce un número por favor: '))

        if num2 > numero:
            print(f'Has introducido un número menor al anterior: {num2} > {numero}.\n')
            break

        num2 = numero
    except:
        print('Entrada invalida. Por favor introduzca solo números.')

print('El programa ha finalizado.')