email= input('Introduce un E-mail: ')

if (email.find('@') == -1) or (email.find('@') == 0) or (email.rfind('@') == len(email)-1):  
    print('El email',email,'no es correcto.')
else:
    print('El email',email,'es correcto.')