import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import os
class vista_catalogo(tk.Frame):
    def __init__(self, master, controller,usuariotext,rol):
        super().__init__(master)
        self.master = master
        self.controller = controller
        self.usuario=usuariotext
        self.rol = rol
        self.create_widgets()

    def create_widgets(self):
        self.master.title("Catálogo de Productos")
        self.master.geometry("800x600")
        self.master.resizable(True, True)
        self.master.config(bg="white")

        # Frame superior (Nombre de la empresa y logo)
        top_frame = tk.Frame(self.master, bg="#004d99")
        top_frame.pack(fill="both", expand=True)

        company_name = tk.Label(top_frame, text="Bienvenido ELECTRONICS ART,", font=("Arial", 16, "bold"), fg="white", bg="#004d99")
        company_name.pack(side="left", padx=8, pady=8)

        #Usuario Ingresado
        user_name = tk.Label(top_frame, text=f"usuario {self.rol}: {self.usuario}", font=("Arial", 12, "bold"), fg="white", bg="#004d99")
        user_name.pack(side="left", padx=8, pady=8)

        # Cargar la imagen del logo (reemplaza "ruta_al_logo.png" con la ruta de tu archivo de imagen)
        self.rutaImagen="imagenes/electronicsArt.jpg"
        if not os.path.exists(self.rutaImagen):
            print(f"Error: La ruta de la imagen no existe: {self.rutaImagen}")
            return
        try:
            imagen = Image.open(self.rutaImagen)
            imagen = imagen.resize((165, 140))
            self.logo_image = ImageTk.PhotoImage(imagen)
            
            # Etiqueta para mostrar el logo
            logo = tk.Label(top_frame, image=self.logo_image, bg="#004d99")  
            logo.pack(side="right", padx=8, pady=8)
        except Exception as e:
            print(f"Error al abrir o procesar la imagen: {e}")

        # Frame principal para el contenido
        main_frame = tk.Frame(self.master, bg="#f0f0f0")
        main_frame.pack(fill="both", expand=True)

        # Canvas y Scrollbars
        canvas = tk.Canvas(main_frame, bg="#f0f0f0")
        scrollbar_y = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollbar_x = tk.Scrollbar(main_frame, orient="horizontal", command=canvas.xview)
        scrollable_frame = tk.Frame(canvas, bg="#f0f0f0")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar_y.pack(side="right", fill="y")
        canvas.configure(yscrollcommand=scrollbar_y.set)

        # Frame de categorías
        self.category_frame = tk.Frame(scrollable_frame, bg="#0073e6")
        self.category_frame.pack(side="top", fill="x", pady=10)

        # Frame de contenido (Catálogo)
        self.content_frame = tk.Frame(scrollable_frame, bg="#f0f0f0")
        self.content_frame.pack(fill="both", expand=True,side='top')

        catalog_title = tk.Label(self.content_frame, text="Catálogo de Productos", font=("Arial", 16, "bold"), bg="#f0f0f0", fg="#333333")
        catalog_title.pack(pady=10)

        self.product_grid = tk.Frame(self.content_frame, bg="#f0f0f0")
        self.product_grid.pack()

        # Cargar el catálogo inicial
        self.update_category_buttons()  # Actualiza los botones de categoría
        self.update_catalog()  # Cargar todos los productos al iniciar la vista
        
        # Botones para cambiar a la vista de reportes y registrar productos
        button_frame = tk.Frame(self.master, bg="#f0f0f0")
        button_frame.pack(side="bottom", fill="x", pady=10)

        report_button = tk.Button(button_frame, text="Reporte de Ventas", command=self.cambiarVistaReporte, bg="#004d99", fg="white", font=("Arial", 12), relief="groove")
        report_button.pack(side="top", padx=10,pady=20)

        register_button = tk.Button(button_frame, text="Gestionar Venta de Productos", command=self.cambiarVista, bg="#004d99", fg="white", font=("Arial", 12), relief="groove")
        register_button.pack(side="top", padx=10)

    def update_category_buttons(self):
        """Actualiza los botones de categoría en la vista."""
        for widget in self.category_frame.winfo_children():
            widget.destroy()

        categories = self.controller.ActualizarCategoria()
        for category in categories:
            category_button = tk.Button(self.category_frame, text=f"{category}", command=lambda cat=category: self.update_catalog(cat),
                                        bg="#0059b3", fg="white", font=("Arial", 12), relief="groove")
            category_button.pack(side="left", padx=10, pady=5)

    def cambiarVistaReporte(self):
        self.master.iconify()
        self.controller.vistaReporte()

    def cambiarVista(self):
        self.master.iconify()
        self.controller.vistaRegistroProducto()
    def update_catalog(self, category=None):
        self.ruta="imagenes/plsystation.jpg"
        imagen = Image.open(self.ruta)
        imagen = imagen.resize((100, 80))
        self.imagenProducto = ImageTk.PhotoImage(imagen)
        if not os.path.exists(self.ruta):
            print(f"Error: La ruta de la imagen no existe: {self.ruta}")
            return

        """Actualiza el catálogo con productos filtrados por categoría."""
        # Limpiar el contenido actual
        for widget in self.product_grid.winfo_children():
            widget.destroy()

        # Obtener los productos filtrados por categoría
        if category:
            products = self.controller.ActualizarProductoCategoria(category)
        else:
            products = self.controller.ActualizarProductos()

        # Crear la cuadrícula de productos
        for i, product in enumerate(products):
            product_frame = tk.Frame(self.product_grid, bd=2, relief="solid", width=150, height=150, bg="white")
            product_frame.grid(row=i // 4, column=i % 4, padx=10, pady=10)

            product_image = tk.Label(product_frame, image=self.imagenProducto, bg="#c0c0c0", width=100, height=80)
            product_image.pack(pady=5)

            product_name = tk.Label(product_frame, text=product[1], font=("Arial", 16), bg="white",)
            product_name.pack()

            product_category = tk.Label(product_frame, text=product[2], font=("Arial", 12, "italic"), bg="white", fg="#666666")
            product_category.pack()

            product_price = tk.Label(product_frame, text=f"${product[4]:.2f}", font=("Arial", 13, "bold"), bg="white", fg="#004d99")
            product_price.pack()
    
    def mensaje(self,texto):
        messagebox.showwarning("Acción Invalida",texto)

    def mensajeError(self,texto):
        messagebox.showerror("ERROR:",texto)
