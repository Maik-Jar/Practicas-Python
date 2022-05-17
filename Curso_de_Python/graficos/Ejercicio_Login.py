from tkinter import *

vUsername= StringVar
vPassword= StringVar

def login(username, password):

    vCredenciales= dict()

    file_manager= open('usuarios.txt')

    for line in file_manager:

        k= line.strip()
        usurario= k.split(': ')
    
        vCredenciales[usurario[0]]= usurario[1]

    
    if vCredenciales[usurario[0]]== username.get():
        print(vCredenciales)
        
        root2= Tk()
        root2.title('Acceso!!')
        root2.resizable(0,0)

        miFrame2= Frame(root2)

        lbMensaje= Label(miFrame2, text='Has podido acceder!!')
        lbMensaje.pack()

        root2.mainloop()

# Raiz
root= Tk()
root.title('Login')
root.resizable(0,0)

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
tfPassword= Entry(miFrame)
tfPassword.config(show='*')
tfUsername.grid(row=0, column=1, padx=5, pady=5)
tfPassword.grid(row=1, column=1, padx=5, pady=5,)

# Button
btEntrar= Button(root, text='Entrar', command=login(tfUsername, tfPassword))
btEntrar.pack()

root.mainloop()