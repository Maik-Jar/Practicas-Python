import pickle
from Herencia import Vehiculos

miCoche1= Vehiculos('Porche', 'Cayman')
miCoche2= Vehiculos('BMW', 'M3')
miCoche3= Vehiculos('Mercedes Benz', 'AMG')

coches= [miCoche1, miCoche2, miCoche3]

fbinary= open('objetos_serializados','wb')

pickle.dump(coches, fbinary)

fbinary.close()

del(fbinary)