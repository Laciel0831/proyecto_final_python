import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class ReportView(tk.Frame):
    def __init__(self, master,controlador):
        super().__init__(master)
        self.master = master
        self.controlador=controlador
        self.create_widgets()

    def create_widgets(self):
        self.master.title("Informe de Productos")

        # Frame superior (Nombre de la empresa y logo)
        top_frame = tk.Frame(self.master, bg="lightgrey")
        top_frame.pack(side="top", fill="x")

        company_name = tk.Label(top_frame, text="Nombre de la empresa", font=("Arial", 16))
        company_name.pack(side="left", padx=10, pady=10)

        logo = tk.Label(top_frame, text="LOGO", bg="grey", width=20, height=5)
        logo.pack(side="right", padx=10, pady=10)

        # Frame de navegación (Home, Products, About, Contact)
        nav_frame = tk.Frame(self.master)
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
        category_frame = tk.Frame(self.master)
        category_frame.pack(side="top", fill="x")

        categories = ["Categoría 1", "Categoría 2", "Categoría 3", "Categoría 4", "Categoría 5"]
        for category in categories:
            category_button = tk.Button(category_frame, text=category)
            category_button.pack(side="left", padx=5, pady=5)

        # Frame de contenido (Informe de Productos)
        content_frame = tk.Frame(self.master)
        content_frame.pack(fill="both", expand=True)

        report_title = tk.Label(content_frame, text="Informe de Productos", font=("Arial", 14))
        report_title.pack(pady=10)

        # Tablas de productos más y menos vendidos
        tables_frame = tk.Frame(content_frame)
        tables_frame.pack()

        # Tabla de Más Vendidos
        sold_frame = tk.Frame(tables_frame, bd=1, relief="solid")
        sold_frame.grid(row=0, column=0, padx=10)

        sold_label = tk.Label(sold_frame, text="Más Vendidos", font=("Arial", 12))
        sold_label.pack()

        self.sold_table = ttk.Treeview(sold_frame, columns=("Producto", "Cantidad"), show="headings")
        self.sold_table.heading("Producto", text="Nombre Producto")
        self.sold_table.heading("Cantidad", text="Cantidad")
        self.sold_table.pack()

        # Tabla de Menos Vendidos
        unsold_frame = tk.Frame(tables_frame, bd=1, relief="solid")
        unsold_frame.grid(row=0, column=1, padx=10)

        unsold_label = tk.Label(unsold_frame, text="Menos Vendidos", font=("Arial", 12))
        unsold_label.pack()

        self.unsold_table = ttk.Treeview(unsold_frame, columns=("Producto", "Cantidad"), show="headings")
        self.unsold_table.heading("Producto", text="Nombre Producto")
        self.unsold_table.heading("Cantidad", text="Cantidad")
        self.unsold_table.pack()

        # Botón para generar informe
        generate_report_button = tk.Button(content_frame, text="Generar Informe",command=self.informe)
        generate_report_button.pack(pady=10)

        # Frame inferior de navegación
        bottom_nav_frame = tk.Frame(self.master)
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

    def informe(self):
        self.controlador.generarInforme()
        messagebox.showinfo("Solicitud Realizada","Informe Generado Exitosamente")