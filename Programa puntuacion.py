try:

    def calcula_calificacion(puntuacion):
        resultado= None

        if puntuacion > 1.0:
            resultado= 'El número que esta ingresando es mayor a 1.0'
        elif puntuacion >= 0.9:
            resultado= 'Sobresaliente'
        elif puntuacion >= 0.8:
            resultado ='Notable'
        elif puntuacion >= 0.7:
            resultado= 'Bien'
        elif puntuacion >= 0.6:
            resultado= 'Suficiente'
        elif puntuacion < 0.6:
            resultado= 'Insuficiente'

        return resultado
   
    print(calcula_calificacion(float(input('Introduzca puntuación: '))))

except:
    print('Por favor introduzca un número.')