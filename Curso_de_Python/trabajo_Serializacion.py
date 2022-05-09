import pickle as pc

# Codigo para serializar un objeto.
lista_nombre= ['Pedro', 'Ana', 'Maria', 'Isabel']

fbinario= open('lista_nombres', 'wb') # Abre el fichero en modo escritura binaria (wr).

pc.dump(lista_nombre, fbinario) # Crea el fichero binario, el primer parametro es el objeto a serializar, el segundo es el nombre del archivo abierto en memoria.

fbinario.close()

del(fbinario)

# Codigo para recuperar el objeto serializado.

fserializado = open('lista_nombres', 'rb') # Abre el fichero en modo lectura binaria (rb).

lista_nombre_recuperada= pc.load(fserializado) # Carga el fichero binario (load()) y lo volca en una variable.

print(lista_nombre_recuperada)