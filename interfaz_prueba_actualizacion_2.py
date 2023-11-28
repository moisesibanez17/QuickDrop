import tkinter as tk
from tkinter import ttk, messagebox

class InterfazGrafica(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Interfaz Prueba")
        self.geometry("700x400")

        # Fondo de imagen para el menú principal
        #self.background_image = tk.PhotoImage(file="C:/Users/Alex/Documents/ALEX/archivos/Estudio/Ingenieria/5 semestre/Analisis de algoritmos/Proyecto final/imagen2.png")  
        #self.background_label = tk.Label(self, image=self.background_image)
        #self.background_label.place(relwidth=1, relheight=1)

        self.frame_inicio = ttk.Frame(self)
        self.frame_inicio.grid(row=1, column=0, sticky="nsew")

        self.frame_configuracion = ttk.Frame(self)
        self.frame_configuracion.grid(row=1, column=0, sticky="nsew")

        self.frame_configuracion_almacen = ttk.Frame(self)
        self.frame_configuracion_almacen.grid(row=1, column=0, sticky="nsew")

        self.frame_configuracion_vehiculos = ttk.Frame(self)
        self.frame_configuracion_vehiculos.grid(row=1, column=0, sticky="nsew")

        self.btn_iniciar = ttk.Button(self, text="Iniciar programa", command=self.iniciar_programa, width=50)
        self.btn_configuracion = ttk.Button(self, text="Configuración del programa", command=self.configuracion_programa, width=50)
        self.btn_salir = ttk.Button(self, text="Salir del programa", command=self.salir_programa, width=50)

        self.btn_iniciar.grid(row=1, column=0, pady=10)
        self.btn_configuracion.grid(row=2, column=0, pady=10)
        self.btn_salir.grid(row=3, column=0, pady=10)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(4, weight=1)

        self.etiqueta_configuracion = ttk.Label(self.frame_configuracion, text="Configuración del programa")
        self.etiqueta_configuracion.grid(row=0, column=0, padx=20, pady=20)
        self.btn_configuracion_almacen = ttk.Button(self.frame_configuracion, text="Configurar almacen", command=self.configuracion_programa_almacen, width=50)
        self.btn_configuracion_vehiculo = ttk.Button(self.frame_configuracion, text="Configurar vehiculos", command=self.configuracion_programa_vehiculos, width=50)

        self.etiqueta_configuracion_almacen = ttk.Label(self.frame_configuracion_almacen, text="Configuracion del almacen")
        self.etiqueta_configuracion_almacen.grid(row=0, column=0, padx=20, pady=20)

        self.etiqueta_configuracion_vehiculos = ttk.Label(self.frame_configuracion_vehiculos, text="Configuracion del almacen")
        self.etiqueta_configuracion_vehiculos.grid(row=0, column=0, padx=20, pady=20)

        self.btn_regresar_menu_principal = ttk.Button(self.frame_configuracion, text="Regresar al Menú Principal", command=self.mostrar_inicio, width=50)
        self.btn_regresar_menu_principal.grid(row=1, column=0, pady=10)

        self.btn_regresar_sub_menu = ttk.Button(self.frame_configuracion_almacen, text="Regresar a la configuracion del programa", command=self.configuracion_programa, width=50)
        self.btn_regresar_sub_menu.grid(row=1, column=0, pady=10)

        self.btn_regresar_sub_menu1 = ttk.Button(self.frame_configuracion_vehiculos, text="Regresar a la configuracion del programa", command=self.configuracion_programa, width=50)
        self.btn_regresar_sub_menu1.grid(row=1, column=0, pady=10)

        self.frame_configuracion.columnconfigure(0, weight=1)
        self.frame_configuracion.rowconfigure(2, weight=1)

        self.frame_configuracion_almacen.columnconfigure(0, weight=1)
        self.frame_configuracion_almacen.rowconfigure(2, weight=1)

        self.frame_configuracion_vehiculos.columnconfigure(0, weight=1)
        self.frame_configuracion_vehiculos.rowconfigure(3, weight=1)

        self.frame_configuracion.grid_remove()
        self.frame_configuracion_almacen.grid_remove()
        self.frame_configuracion_vehiculos.grid_remove()

    def iniciar_programa(self):
        print("Iniciando programa")

    def configuracion_programa(self):
        self.frame_inicio.grid_remove()
        self.btn_iniciar.grid_remove()
        self.btn_configuracion.grid_remove()
        self.btn_salir.grid_remove()
        self.frame_configuracion_almacen.grid_remove()
        self.frame_configuracion_vehiculos.grid_remove()
        self.frame_configuracion.grid()
        self.btn_configuracion_almacen.grid(row=1, column=0, pady=10)
        self.btn_configuracion_vehiculo.grid(row=2, column=0, pady=10)
        self.btn_regresar_menu_principal.grid(row=3, column=0, pady=10)

    def configuracion_programa_almacen(self):
        self.frame_configuracion.grid_remove()
        self.btn_configuracion_almacen.grid_remove()
        self.frame_configuracion_almacen.grid()
        self.btn_regresar_sub_menu.grid(row=1, column=0, pady=10)
    
    def configuracion_programa_vehiculos(self):
        self.frame_configuracion.grid_remove() 
        self.btn_configuracion_vehiculo.grid_remove()
        self.frame_configuracion_vehiculos.grid()
        self.btn_regresar_sub_menu1.grid(row=1, column=0, pady=10)

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
