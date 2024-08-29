import tkinter as tk
from tkinter import ttk
class vista_catalogo(tk.Frame):
    def __init__(self, master=None, controller=None):
        super().__init__(master)
        self.master = master
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        self.master.title("Catálogo de Productos")
        self.master.geometry("800x600")  # Configura el tamaño de la ventana

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

        # Frame de navegación (Home, Products, About, Contact)
        nav_frame = tk.Frame(scrollable_frame)
        nav_frame.pack(side="top", fill="x")

        home_button = tk.Button(nav_frame, text="Home")
        home_button.pack(side="left", padx=5)

        products_button = tk.Button(nav_frame, text="Products")
        products_button.pack(side="left", padx=5)

        about_button = tk.Button(nav_frame, text="About")
        about_button.pack(side="left", padx=5)

        contact_button = tk.Button(nav_frame, text="Contact")
        contact_button.pack(side="left", padx=5)

        # Frame de categorías
        category_frame = tk.Frame(scrollable_frame)
        category_frame.pack(side="top", fill="x")

        categories = ["Categoría 1", "Categoría 2", "Categoría 3", "Categoría 4", "Categoría 5"]
        for category in categories:
            category_button = tk.Button(category_frame, text=category)
            category_button.pack(side="left", padx=5, pady=5)

        # Frame de contenido (Catálogo)
        content_frame = tk.Frame(scrollable_frame)
        content_frame.pack(fill="both", expand=True)

        catalog_title = tk.Label(content_frame, text="Título del catálogo", font=("Arial", 14))
        catalog_title.pack(pady=10)

        product_grid = tk.Frame(content_frame)
        product_grid.pack()

        # Creación de la cuadrícula de productos
        for i in range(4):
            for j in range(4):
                product_frame = tk.Frame(product_grid, bd=1, relief="solid", width=150, height=150)
                product_frame.grid(row=i, column=j, padx=5, pady=5)

                product_image = tk.Label(product_frame, text="Imagen", bg="lightgrey", width=10, height=5)
                product_image.pack(pady=5)

                product_name = tk.Label(product_frame, text="Nombre Producto")
                product_name.pack()

                product_category = tk.Label(product_frame, text="Categoría")
                product_category.pack()

                product_price = tk.Label(product_frame, text="Precio")
                product_price.pack()

        # Botón para cambiar a la vista de reportes
        report_button = tk.Button(content_frame, text="Reporte", command=self.controller.show_report_view)
        report_button.pack(pady=10)

        # Frame inferior de navegación
        bottom_nav_frame = tk.Frame(scrollable_frame)
        bottom_nav_frame.pack(side="bottom", fill="x")

        home_nav_button = tk.Button(bottom_nav_frame, text="Home")
        home_nav_button.pack(side="left", padx=5)

        apps_nav_button = tk.Button(bottom_nav_frame, text="Apps")
        apps_nav_button.pack(side="left", padx=5)

        games_nav_button = tk.Button(bottom_nav_frame, text="Games")
        games_nav_button.pack(side="left", padx=5)

        movies_nav_button = tk.Button(bottom_nav_frame, text="Movies")
        movies_nav_button.pack(side="left", padx=5)

        books_nav_button = tk.Button(bottom_nav_frame, text="Books")
        books_nav_button.pack(side="left", padx=5)
