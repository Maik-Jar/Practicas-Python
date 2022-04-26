valor= None
lista= []

while True:
    try:
        valor= input('Introduzca un número: ')

        if valor.lower() == 'fin':
            break
       
        lista.append(int(valor))

    except:
        print('Entrada invalida')

print(max(lista), min(lista))