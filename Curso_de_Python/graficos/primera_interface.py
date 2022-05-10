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

# CLASE Frame()

# Intanciado de la clase Frame
miFrame= Frame() 
# metodo pack() permite empaquetar mi objeto de tipo Frame dentro de la raiz (objeto de tipo Tk).
miFrame.pack(expand= 1, fill= 'both') # NOTA: El metodo pack() admite algunos parametros que permiten configurar el comportamiento inicial del Frame.
# metodo config() permite configurar algunos atributos y comportamiento del Frame por medio valores pasados por parametros.
miFrame.config(bg='#FFD6C0', width='650', height='350') # NOTA: Ver documentación de la clase Frame().

# metodo mainloop() permite mostra la ventana, este debe ser siempre el ultimo metodo que se ejecute.
raiz.mainloop() 