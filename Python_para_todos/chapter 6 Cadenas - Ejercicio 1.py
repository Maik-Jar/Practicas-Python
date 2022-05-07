# Ejercicio 1: Escribe un bucle while que comience con el último carácter
# en la cadena y haga un recorrido hacia atrás hasta el primer carácter
# en la cadena, imprimiendo cada letra en una línea independiente.

cadena= 'hola'
i= 0

while i < len(cadena):
    i += +1
    print(cadena[-i])
    