class Coche():

    def desplazamiento(self):
        print('Me desplazo utilizando 4 ruedas.')

class Moto():

    def desplazamiento(self):
        print('Me desplazo utilizando 2 ruedas.')

class Camion():

    def desplazamiento(self):
        print('Me desplazo utilizando 8 ruedas.')

def dezplazamiento(vehiculos):
    vehiculos.desplazamiento()

miVehiculo= Moto()

dezplazamiento(miVehiculo)