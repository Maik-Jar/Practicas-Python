import socket as sc

misock = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
# En primer lugar, el programa realiza una conexión al puerto 80 del servidor www.py4e.com.
misock.connect(('data.pr4e.org', 80))
# Envia el comando GET seguido de una línea en blanco. \r\n representa un salto de línea (end of line, o EOL en
# inglés), así que \r\n\r\n significa que no hay nada entre dos secuencias de salto de línea. Ese es el equivalente 
# de una línea en blanco.
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
misock.send(cmd)
# escribimos un bucle que recibe los datos desde el socket en bloques de 512 caracteres y los imprime en pantalla 
# hasta que no quedan más datos por leer (es decir, la llamada a recv() devuelve una cadena vacía).

while True:
    datos = misock.recv(512)
    if len(datos) < 1:
        break
    print(datos.decode(),end='')

misock.close()
