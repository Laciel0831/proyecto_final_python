import tkinter as tk
from tkinter import ttk

class vista_catalogo(tk.Frame):
    def __init__(self, master, controller):
        super().__init__(master)
        self.master = master
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        self.master.title("Catálogo de Productos")
        self.master.geometry("800x600")

        # Frame principal para el contenido
        main_frame = tk.Frame(self.master)
        main_frame.pack(fill="both", expand=True)

        # Canvas y Scrollbars
        canvas = tk.Canvas(main_frame)
        scrollbar_y = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollbar_x = tk.Scrollbar(main_frame, orient="horizontal", command=canvas.xview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar_y.pack(side="right", fill="y")
        scrollbar_x.pack(side="bottom", fill="x")
        canvas.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

        # Frame superior (Nombre de la empresa y logo)
        top_frame = tk.Frame(scrollable_frame, bg="lightgrey")
        top_frame.pack(side="top", fill="x")

        company_name = tk.Label(top_frame, text="Nombre de la empresa", font=("Arial", 16))
        company_name.pack(side="left", padx=10, pady=10)

        logo = tk.Label(top_frame, text="LOGO", bg="grey", width=20, height=5)
        logo.pack(side="right", padx=10, pady=10)

        # Frame de categorías
        self.category_frame = tk.Frame(scrollable_frame)
        self.category_frame.pack(side="top", fill="x")

        # Frame de contenido (Catálogo)
        self.content_frame = tk.Frame(scrollable_frame)
        self.content_frame.pack(fill="both", expand=True)

        catalog_title = tk.Label(self.content_frame, text="Título del catálogo", font=("Arial", 14))
        catalog_title.pack(pady=10)

        self.product_grid = tk.Frame(self.content_frame)
        self.product_grid.pack()

        # Botón para cambiar a la vista de reportes
        report_button = tk.Button(self.content_frame, text="Reporte", command=self.controller.vistaReporte)
        report_button.pack(pady=10)

        # Cargar el catálogo inicial
        self.update_category_buttons()  # Actualiza los botones de categoría
        self.update_catalog()  # Cargar todos los productos al iniciar la vista

    def update_category_buttons(self):
        """Actualiza los botones de categoría en la vista."""
        for widget in self.category_frame.winfo_children():
            widget.destroy()

        categories = self.controller.get_all_categories()
        for category in categories:
            category_button = tk.Button(self.category_frame, text=category, command=lambda cat=category: self.update_catalog(cat))
            category_button.pack(side="left", padx=5, pady=5)

    def update_catalog(self, category=None):
        """Actualiza el catálogo con productos filtrados por categoría."""
        # Limpiar el contenido actual
        for widget in self.product_grid.winfo_children():
            widget.destroy()

        # Obtener los productos filtrados por categoría
        if category:
            products = self.controller.get_products_by_category(category)
        else:
            products = self.controller.get_all_products()

        # Crear la cuadrícula de productos
        for i, product in enumerate(products):
            product_frame = tk.Frame(self.product_grid, bd=1, relief="solid", width=150, height=150)
            product_frame.grid(row=i // 4, column=i % 4, padx=5, pady=5)

            product_image = tk.Label(product_frame, text="Imagen", bg="lightgrey", width=10, height=5)
            product_image.pack(pady=5)

            product_name = tk.Label(product_frame, text=product[0])  # Cambia el índice según el formato del modelo
            product_name.pack()

            product_category = tk.Label(product_frame, text=product[2])  # Cambia el índice según el formato del modelo
            product_category.pack()

            product_price = tk.Label(product_frame, text=f"${product[3]:.2f}")  # Cambia el índice según el formato del modelo
            product_price.pack()













