# Ejercicio 1: Escribe una función llamada RECORTAR que toma una lista y la modifica, removiendo el primer 
# y último elemento, y regresa None. Después escribe una función llamada MEDIO que toma una 
# lista y regresa una nueva lista que contiene todo excepto el primero y último elementos.

def recortar(lista):

    for i in lista:
        
        t = ''

        if lista.index(i) == 0:
            lista.remove(i)
        elif lista.index(i) == (len(lista)-1):
            t = lista.remove(i)
            return t
              

def medio(lista):

    nueva_lista = []

    for i in lista:

        if lista.index(i) != 0 and lista.index(i) != (len(lista)-1):
            nueva_lista.append(i)
    
    return nueva_lista

t = ['a', 'b', 'c', 'd', 'e', 'f']

print('Funcion medio: ',medio(t))
print('lista antes de la llamada a la funcion recortar: ', t)
print('Funcion recortar: ',recortar(t))
print('lista despues de la llamada a la funcion recortar: ',t)