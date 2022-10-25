import tkinter as tk
from tkinter import ttk

from utils import generate_hash_bytes, save_hash_bytes, update_password_list
from main_gui import run_main

class NewMasterKey(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.grid_rowconfigure(0, minsize=30, uniform='row')
        self.grid_rowconfigure(1, minsize=30, uniform='row')
        self.grid_rowconfigure(2, minsize=30, uniform='row')
        self.grid_rowconfigure(3, minsize=30, uniform='row')
        self.grid_rowconfigure(4, minsize=30, uniform='row')
        self.grid_columnconfigure(0, minsize=100, uniform='col')
        self.grid_columnconfigure(1, minsize=100, uniform='col')
        self.pack(anchor=tk.CENTER, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Etiqueta principal
        ttk.Label(self, text='Crear clave maestra ').grid(row=0, column=0, columnspan=2)

        # Cuadro de texto para ingresar la MasterKey
        ttk.Label(self, text='Introduzca la clave maestra: ').grid(row=1, column=0, sticky=tk.E)
        self.input1 = ttk.Entry(self, show='*')
        self.input1.grid(row=1, column=1)

        # Confirmar Masterkey
        ttk.Label(self, text='Confirme la clave maestra: ').grid(row=2, column=0, sticky=tk.E)
        self.input2 = ttk.Entry(self, show='*')
        self.input2.grid(row=2, column=1)

        # Mensajes
        self.messages_var = tk.StringVar() 
        self.messages_label = ttk.Label(self, textvariable=self.messages_var)
        self.messages_label.grid(row=3, column=0, columnspan=2)

        # Boton Crear
        self.create_button = ttk.Button(self, text='Crear', command=self.create_button_handler)
        self.create_button.grid(row=4, column=0, columnspan=2)

    def create_button_handler(self):

        print('Create button pressed...')

        password1 = self.input1.get()
        password2 = self.input2.get()

        if password1 == '' or password2 == '':
            self.messages_var.set('Campo vacio')
        elif password1 != password2:
            self.messages_var.set('Los campos no coinciden')
        else:
            # Guardamos el Hash de la MasterKey
            hash_bytes = generate_hash_bytes(password1)
            save_hash_bytes(hash_bytes)

            # Creamos un archivo encriptado
            update_password_list(password1, [])

            # Cerramos esta ventana y abrimos la principal
            self.master.destroy()
            run_main(password1)

def run_new_masterkey():

    root = tk.Tk()

    NewMasterKey(root)

    root.title('MasterKey')
    root.resizable(False, False)

    root.mainloop()

if __name__ == '__main__':
    run_new_masterkey()    