from tkinter import *

def login(username, password):

    vCredenciales= dict()

    file_manager= open('usuarios.txt')

    for line in file_manager:

        k= line.strip()
        usurario= k.split(': ')
    
        vCredenciales[usurario[0]]= usurario[1]

    if vCredenciales['username']== username and vCredenciales['password']== password:
        
        root2= Tk()
        root2.title('Acceso!!')
        root2.resizable(0,0)

        miFrame2= Frame(root2)
        miFrame2.config(bg='red' ,width='650', height='350')
        miFrame2.pack()

        lbMensaje= Label(miFrame2, text='Has podido acceder!!', font=5, fg='black')
        lbMensaje.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        root2.mainloop()

# Raiz
root= Tk()
root.title('Login')
root.resizable(0,0)

vUsername= StringVar()
vPassword= StringVar()

# Frame
miFrame= Frame(root)
miFrame.config(bg='#FFD6C0', width='650', height='350')
miFrame.pack(expand= 1, fill= 'both')
miFrame.pack()

# Label
lbUsername= Label(miFrame, text='Username:')
lbPassword= Label(miFrame, text='Password:')
lbUsername.grid(row=0, column=0, padx=5, pady=5, sticky='e')
lbPassword.grid(row=1, column=0, padx=5, pady=5, sticky='e')

# Entry
tfUsername= Entry(miFrame)
tfPassword= Entry(miFrame, textvariable= vPassword)
tfPassword.config(show='*')
tfUsername.grid(row=0, column=1, padx=5, pady=5)
tfPassword.grid(row=1, column=1, padx=5, pady=5,)

# Button
btEntrar= Button(miFrame, text='Entrar', command=lambda:login(tfUsername.get(), tfPassword.get()))
btEntrar.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()