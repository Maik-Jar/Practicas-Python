vemail = input('Por favor, ingrese su correo: ')

varoba = 0
vpunto = 0

for i in vemail:

    if i == "@":
        varoba += 1
    
    if i == ".":
        vpunto += 1

if varoba == 1 and (vpunto > 0 and vpunto <= 2):
    print('email correcto.')
else:
    print('email incorrecto.')