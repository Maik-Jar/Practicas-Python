# Ejercicio 1: Descargar una copia del archivo www.py4e.com/code3/words.txt
# Escribe un programa que lee las palabras en words.txt y las almacena como claves en un diccionario.
# No importa qué valores tenga. Luego puedes utilizar el operador in como una forma rápida de revisar si una
# cadena está en el diccionario.

file_manager = open('words.txt')
words= []
words_dict= dict()

for line in file_manager:
    words = words+line.split()
    for i in words:
        words_dict[i]= len(i)

for i in range(len(words)-1):
    print('Word: <<', words[i], '>> in words dictionary: ', words[i] in words_dict)
