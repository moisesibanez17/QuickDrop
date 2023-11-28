import tkinter as tk
from tkinter import ttk, messagebox

class InterfazGrafica(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Interfaz Prueba")
        self.geometry("700x400")

        self.frame_inicio = ttk.Frame(self)
        self.frame_inicio.grid(row=1, column=0, sticky="nsew")

        self.frame_configuracion = ttk.Frame(self)
        self.frame_configuracion.grid(row=0, column=0, sticky="nsew")

        self.btn_iniciar = ttk.Button(self, text="Iniciar programa", command=self.iniciar_programa, width=50)
        self.btn_configuracion = ttk.Button(self, text="Configuración del programa", command=self.configuracion_programa, width=50)
        self.btn_salir = ttk.Button(self, text="Salir del programa", command=self.salir_programa, width=50)

        self.btn_iniciar.grid(row=1, column=0, pady=10)
        self.btn_configuracion.grid(row=2, column=0, pady=10)
        self.btn_salir.grid(row=3, column=0, pady=10)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(4, weight=1)

        self.etiqueta_configuracion = ttk.Label(self.frame_configuracion, text="Este es un submenú de configuración")
        self.etiqueta_configuracion.pack(padx=20, pady=20)

        self.btn_regresar = ttk.Button(self.frame_configuracion, text="Regresar al Menú Principal", command=self.mostrar_inicio, width=50)
        self.btn_regresar.pack(pady=10)

        self.frame_configuracion.grid_remove()

    def iniciar_programa(self):
        print("Iniciando programa")

    def configuracion_programa(self):
        self.frame_inicio.grid_remove()
        self.btn_iniciar.grid_remove()
        self.btn_configuracion.grid_remove()
        self.btn_salir.grid_remove()
        self.frame_configuracion.grid()

    def mostrar_inicio(self):
        self.frame_configuracion.grid_remove()
        self.frame_inicio.grid()
        self.btn_iniciar.grid()
        self.btn_configuracion.grid()
        self.btn_salir.grid()

    def salir_programa(self):
        respuesta = messagebox.askquestion("Salir", "¿Estás seguro de que quieres salir del programa?")
        if respuesta == 'yes':
            self.destroy()

if __name__ == "__main__":
    app = InterfazGrafica()
    app.mainloop()
