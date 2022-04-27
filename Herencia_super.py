class Persona():
    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre= nombre
        self.edad= edad
        self.lugar_residencia= lugar_residencia

    def descripcion(self):
        print('Nombre: ', self.nombre, '\nEdad: ', self.edad, '\nResidencia: ', self.lugar_residencia)

class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre, edad, lugar_residencia):
        super().__init__(nombre, edad, lugar_residencia)
        self.salario= salario
        self.antiguedad= antiguedad

    def descripcion(self):
        super().descripcion()
        print('Salario: ', self.salario, '\nAntiguedad: ', self.antiguedad)

antonio= Persona('Antonio', 55, 'Rep. Dom')

carlos= Empleado(1500, 15, 'carlos', 30, 'Mexico')

antonio.descripcion()
carlos.descripcion()