vcontrasena = input('Ingrese su contraseña: ')
vcontrador = len(vcontrasena)
vvalidacion = True

if vcontrador < 8:
    print('Contraseña incorrecta.')
else:    
    for i in range(vcontrador):
        if vcontrasena[i] == " ":
            vvalidacion = False
    
    if vvalidacion:
        print('Contraseña OK')
    else:
        print('Contraseña incorrecta.')