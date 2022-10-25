import tkinter as tk
from tkinter import ttk

from utils import get_password_list

class GeneratePaswordForm(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, ipadx=10)
        self.grid_rowconfigure(0, minsize=30, uniform='row')
        self.grid_rowconfigure(1, minsize=30, uniform='row')
        self.grid_rowconfigure(2, minsize=30, uniform='row')
        self.grid_rowconfigure(3, minsize=30, uniform='row')
        self.grid_rowconfigure(4, minsize=30, uniform='row')
        self.grid_rowconfigure(5, minsize=30, uniform='row')
        self.grid_rowconfigure(6, minsize=30, uniform='row')
        self.grid_rowconfigure(7, minsize=30, uniform='row')
        self.grid_columnconfigure(0, minsize=100, uniform='col')
        self.grid_columnconfigure(1, minsize=100, uniform='col')

        # Etiqueta principal
        ttk.Label(self, text='Generador de claves').grid(row=0, column=0, columnspan=2)

        # Concepto 
        ttk.Label(self, text='Concepto: ').grid(row=1, column=0, sticky=tk.E)
        self.concept_entry = ttk.Entry(self)
        self.concept_entry.grid(row=1, column=1)

        # Longitud 
        ttk.Label(self, text='Longitud: ').grid(row=2, column=0, sticky=tk.E)
        self.length_entry = ttk.Entry(self)
        self.length_entry.grid(row=2, column=1)

        # Numeros 
        self.numbers_checkbox = ttk.Checkbutton(self)
        self.numbers_checkbox.grid(row=3, column=0, sticky=tk.E)
        ttk.Label(self, text='Numeros').grid(row=3, column=1, sticky=tk.W)

        # Simbolos
        self.simbols_checkbox = ttk.Checkbutton(self)
        self.simbols_checkbox.grid(row=4, column=0, sticky=tk.E)
        ttk.Label(self, text='Simbolos').grid(row=4, column=1, sticky=tk.W)

        # Password 
        self.password_generated = ttk.Label(self)
        self.password_generated.grid(row=5, column=0, columnspan=2)

        # Mensajes
        self.message = ttk.Label(self)
        self.message.grid(row=6, column=0, columnspan=2)

        # Boton Generar 
        self.generate_button = ttk.Button(self, text='Generar', command=self.master.generate_button_handler)
        self.generate_button.grid(row=7, column=0)

        # Boton Almacenar 
        self.save_button = ttk.Button(self, text='Almacenar', command=self.master.save_button_handler)
        self.save_button.grid(row=7, column=1)
        
class PasswordListFrame(tk.Frame):

    def __init__(self, master, password_list = []):
        super().__init__(master)
        self.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.password_list = password_list

        # Seccion de cabeceras
        self.headers_frame = tk.Frame(self)
        self.headers_frame.grid_columnconfigure(0, minsize=300, uniform='col')
        self.headers_frame.grid_columnconfigure(1, minsize=300, uniform='col')
        self.headers_frame.pack(side=tk.TOP, fill=tk.X)

        # Etiqueta principal
        ttk.Label(self.headers_frame, text='Lista de claves').grid(row=0, column=0, columnspan=2)

        # Encabezados de la tabla
        ttk.Label(self.headers_frame, text='Concepto').grid(row=1, column=0)
        ttk.Label(self.headers_frame, text='Clave').grid(row=1, column=1)

        # Canvas lista
        self.canvas = tk.Canvas(self, bg='white')
        self.canvas.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)

        # Barra para hacer Scroll en el canvas de la lista
        self.scroll_bar = ttk.Scrollbar(self.canvas, orient=tk.VERTICAL)
        self.scroll_bar.pack(fill=tk.Y, side=tk.RIGHT)

    def render_password_list(self):
        pass

class MainWindow(tk.Tk):

    def __init__(self, password_list = []):
        super().__init__()

        self.password_list = password_list

        self.form = GeneratePaswordForm(self)
        self.password_list_frame = PasswordListFrame(self)

        self.title('Passwor Generator | Ing. Jose B. Araya')
        self.resizable(False, False)
        self.eval('tk::PlaceWindow . center')
        # self.iconbitmap('images/password_generator.ico')

        self.mainloop()

    def save_button_handler():
        pass

    def generate_button_handler():
        pass

if __name__ == '__main__':
    MainWindow()