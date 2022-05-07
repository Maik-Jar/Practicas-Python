# Diccionario como un conjunto de contadores Ej. 1
print('Diccionario como un conjunto de contadores Ej. if\n')
palabra = 'brontosaurio'
d = dict()
for c in palabra: # Recorre toda la cadena.
    if c not in d: # Evalua si x clave (en este caso las claves son letras (c)) no se encuentra en el diccionario. 
        d[c] = 1 # Agrega la nueva clave con valor 1
    else:
        d[c] = d[c] + 1 # Incrementa en 1 el valor de la clave exitente.
print(d)

# Diccionario como un conjunto de contadores Ej. 2 (metodo get())
print('\nDiccionario como un conjunto de contadores Ej. get()\n')
palabra = 'brontosaurio'
d = dict()
for c in palabra: # Recorre toda la cadena.
    d[c] = d.get(c,0) + 1 # Como las claves en un diccionario son unicas, cada nueva clave sera agregada, mientras
                         # que las existentes causaran que el valor que les pertenece sea modificado. get() obtendra
                         # el valor de x clave y lo incrementara en 1, si la clave no existe devolvera 0 que es el valor por defecto.
print(d)