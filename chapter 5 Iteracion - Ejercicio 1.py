valor= None
total= 0
cantidad= 0

while True:
    try:
        valor= input('Introduzca un número: ')

        if valor.lower() == 'fin':
            break
       
        total+= int(valor)
        cantidad+= 1

    except:
        print('Entrada invalida')

print(total, cantidad, total/cantidad)

