
class Coche():

    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False

    def arrancar(self):
        self.enmarcha= True

    def estado(self):
        if self.enmarcha:
            return "El coche esta en marcha."
        else:
            return "El coche esta parado."

miCoche= Coche()
miCoche.arrancar()

print(miCoche.largoChasis)
print(miCoche.estado())
