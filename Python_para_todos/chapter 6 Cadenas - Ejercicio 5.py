# Ejercicio 5: Toma el siguiente código en Python que almacena una cadena:
# str = 'X-DSPAM-Confidence:0.8475'
# Utiliza find y una parte de la cadena para extraer la porción de la cadena
# después del carácter dos puntos y después utiliza la función float para
# convertir la cadena extraída en un número de punto flotante.

cadena = 'X-DSPAM-Confidence:0.8475'

decimal= float(cadena[cadena.find(':')+1:])

