import tkinter as tk
from tkinter import ttk

from utils import generate_hash_bytes, get_password_list
from main_gui import run_main

class MasterKey(tk.Frame):

    def __init__(self, master, hash_bytes):
        super().__init__(master)
        self.hash_bytes = hash_bytes
        self.grid_rowconfigure(0, minsize=30, uniform='row')
        self.grid_rowconfigure(1, minsize=30, uniform='row')
        self.grid_rowconfigure(2, minsize=30, uniform='row')
        self.grid_rowconfigure(3, minsize=30, uniform='row')
        self.grid_columnconfigure(0, minsize=100, uniform='col')
        self.grid_columnconfigure(1, minsize=100, uniform='col')
        self.pack(anchor=tk.CENTER, fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Etiqueta principal
        ttk.Label(self, text='Password Generator | Jose Araya').grid(row=0, column=0, columnspan=2)

        # Cuadro de texto para ingresar la MasterKey
        ttk.Label(self, text='Introduzca la clave maestra: ').grid(row=1, column=0, sticky=tk.E)
        self.input = ttk.Entry(self, show='*')
        self.input.grid(row=1, column=1)

        # Mensajes 
        self.messages_var = tk.StringVar()
        self.messages_label = ttk.Label(self, textvariable=self.messages_var)
        self.messages_label.grid(row=2, column=0, columnspan=2)

        # Boton Crear
        self.continue_button = ttk.Button(self, text='Ingresar', command=self.continue_button_handler)
        self.continue_button.grid(row=3, column=0, columnspan=2)

    def continue_button_handler(self):

        masterkey = self.input.get()
        if (masterkey == ''):
            # El usuario no ingreso nada en el campo de texto
            self.messages_var.set('Campo vacio')
            
        elif (generate_hash_bytes(masterkey) == self.hash_bytes):
            # Cerramos la ventana actual
            self.master.destroy()

            # Abrimos la GUI principal y le pasamos la lista de claves
            run_main(masterkey)

        else:
            # Los hashes no coinciden por lo tanto la masterkey es incorrecta
            self.messages_var.set('MasterKey incorrecta')
            self.input.delete(0,tk.END)
            
def run_masterkey(hash_bytes = bytes):

    root = tk.Tk()

    MasterKey(root, hash_bytes)

    root.title('MasterKey')
    root.resizable(False, False)
    root.eval('tk::PlaceWindow . center')

    root.mainloop()

if __name__ == '__main__':

    run_masterkey()