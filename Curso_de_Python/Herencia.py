class Vehiculos():

    def __init__(self, marca, modelo):
        
        self.marca= marca
        self.modelo= modelo
        self.enmarcha= False
        self.acelera= False
        self.frena= False
    
    def arrancar(self):
        self.enmarcha= True

    def acelerar(self):
        self.acelera= True

    def frenar(self):
        self.frena= True

    def estado(self):
        print('Marca: ', self.marca, '\nModelo: ',self.modelo, '\nEn marcha: ', self.enmarcha, '\nAcelerando: ',
         self.acelera, '\nFrenando:', self.frena)

class Moto(Vehiculos):
    calibrar= ''

    def calibrando(self):
        self.calibrar= 'Voy calibrando.'

    def estado(self):
        print('Marca: ', self.marca, '\nModelo: ',self.modelo, '\nEn marcha: ', self.enmarcha, '\nAcelerando: ',
         self.acelera, '\nFrenando:', self.frena, '\n', self.calibrar)

class Furgoneta(Vehiculos):

    def carga(self, cargar):
        self.cargado= cargar

        if (self.cargado):
            return 'La Furgoneta está cargada.'
        else:
            return 'La Furgoneta no está cargada.'

class VEelectricos(Vehiculos):

    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia= 100

    def cargarEnergia(self):
        self.cargando= True

class BicicletaElenctrica(VEelectricos):
    
    def estado(self):
        return super().estado()

####################################################################
#miMoto= Moto('Honda', 'Lead 100')
#miMoto.calibrando()
#miMoto.estado()
####################################################################
#miFurgoneta= Furgoneta('Pegout', 'Kangoo')
#miFurgoneta.arrancar()
#miFurgoneta.estado()
#print(miFurgoneta.carga(True))
####################################################################
#miBici= BicicletaElenctrica('tesla', 'cic')
#miBici.estado()
