import pickle
from Herencia import Vehiculos

fbinary= open('Objetos_serializados', 'rb')

objetos_deserealizados= pickle.load(fbinary)

fbinary.close()

del(fbinary)

for c in objetos_deserealizados:
    print(c.estado())

