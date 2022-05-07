# Ejercicio 2: Encontrar que línea del programa de arriba no está protegida (método guardián) propiamente.
# Trata de construir un archivo de texto que cause que el programa falle y después modifica el programa de
# modo que la línea es propiamente protegida y pruébalo para asegurarte que el programa es capaz de manejar
# tu nuevo archivo de texto.

# Ejercicio 3: Reescribe el código guardián en el ejemplo de arriba sin las dos sentencias if. En vez de eso, 
# utiliza una expresión lógica compuesta utilizando el operador lógico or con una sola sentencia if.

manejador = open('mbox-test.txt')
contador = 0

for linea in manejador:
    palabras = linea.split()
    #print('Depuración:', len(palabras))
    #if len(palabras) == 0 : continue
    if len(palabras) == 0 or palabras[0] != 'From' or len(palabras) < 2 : continue
    #if len(palabras) < 2: continue
    print(palabras[2]) #no esta protegida pues si no hay otra palabra despues del 'From' dara un error.
