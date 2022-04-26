#man_archivo = open('mbox.txt')
#contador = 0
#for linea in man_archivo:
#   contador += + 1
#print('Contador de lineas: ', contador)

#man_archivo = open('mbox.txt')
#inp = man_archivo.read()
#print(len(inp))
#print(inp[:20])

#man_a = open('mbox.txt')
#contador = 0
#for linea in man_a:
#    if linea.startswith('From:'):
#        print(linea)

#man_a = open('mbox.txt')
#for linea in man_a:
#    linea = linea.rstrip()
#    if linea.startswith('From:'):
#        print(linea)

#man_a = open('mbox.txt')
#for linea in man_a:
#    linea = linea.rstrip()
    # Ignorar 'líneas que no nos interesan'
#    if not linea.startswith('From:'):
#        continue
    # Procesar la línea que nos 'interesa'
#    print(linea)

man_a = open('mbox.txt')
for linea in man_a:
    linea = linea.rstrip()
    if linea.find('@uct.ac.za') == -1: continue
    print(linea)
