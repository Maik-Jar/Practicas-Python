from tkinter import * 


# CLASE Tk()

# Instanciando la clase Tk
raiz= Tk()
# metodo title() te permite agregar un titulo a la ventana.
raiz.title("Ventana de prueba") 
# metodo geometry() te permite modificar el ancho y el largo de la venta.
#raiz.geometry('650x350') # NOTA: La raiz se ajusta al tamaño del Frame, por lo que es conveniente darle tamaño al Frame y no a la raiz.
# metodo resizable() permite indicar si se puede o no redimencionar el ancho o el largo de la venta.
raiz.resizable(True,True) 
# metodo config() permite configurar algunos atributos y comportamiento de la ventana medio valores pasados por parametros.
raiz.config(bg='#51E5FF') # NOTA: Ver documentación de la clase Tk().

miNombre= StringVar()

# CLASE Frame()

# Instanciado de la clase Frame
miFrame= Frame() 
# metodo pack() permite empaquetar mi objeto de tipo Frame dentro de la raiz (objeto de tipo Tk).
miFrame.pack(expand= 1, fill= 'both') # NOTA: El metodo pack() admite algunos parametros que permiten configurar el comportamiento inicial del Frame.
# metodo config() permite configurar algunos atributos y comportamiento del Frame por medio valores pasados por parametros.
miFrame.config(bg='#FFD6C0', width='650', height='350') # NOTA: Ver documentación de la clase Frame().

# CLASE Label()

# Instanciado de la clase Label
miLabel= Label(miFrame, text= 'Hola mi señores.') # La clase Label admite un primer parametro que es a que widget pertenece y luego las otras son opcines. Ver documentación.
# metodo place() permite especificar en que parte estara el texto dentro del widget al que pertenece.
#miLabel.place(x=5, y=5)
miLabel.grid(row=0, column=0, padx=10, pady=10, sticky='e')
# Forma corta.
#Label(miFrame, text= 'Hola mi señores.').place(x=5, y=5)

# CLASE Entry()

cuadroTexto= Entry(miFrame, textvariable= miNombre)
#cuadroTexto.place(x=5, y=35)
cuadroTexto.grid(row=0, column=1, padx=10, pady=10)

cuadroPass= Entry(miFrame)
#cuadroTexto.place(x=5, y=35)
cuadroPass.grid(row=1, column=1, padx=10, pady=10)
cuadroPass.config(show='*')
# metodo mainloop() permite mostra la ventana, este debe ser siempre el ultimo metodo que se ejecute.

# CLASE Text()

textoComentario= Text(miFrame, width= 16, height= 5)

textoComentario.grid(row=3, column=1, padx=10, pady=10)

# CLASE Scrollbar()

scroll= Scrollbar(miFrame, command=textoComentario.yview)
scroll.grid(row=3, column=1, sticky='nse', padx=11, pady=11)
textoComentario.config(yscrollcommand= scroll.set)

# CLASE Button()

def codigoboton():
    miNombre.set('brian')

miBoton= Button(raiz, text='Envio', command=codigoboton)
miBoton.pack()

raiz.mainloop() 