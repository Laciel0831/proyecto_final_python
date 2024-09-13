import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import os

class ReportView(tk.Frame):
    def __init__(self, master, controlador):
        super().__init__(master)
        self.master = master
        self.controlador = controlador
        self.create_widgets()

    def create_widgets(self):
        self.master.title("Informe de Productos - Administrador")

        # Frame superior (Nombre de la empresa) - Fondo azul
        top_frame = tk.Frame(self.master, bg="blue")
        top_frame.pack(side="top", fill="x")

        company_name = tk.Label(top_frame, text="Electronic Arts", font=("Arial", 24), fg="white", bg="blue")
        company_name.pack(side="left", padx=10, pady=10)
        # Cargar la imagen del logo (reemplaza "ruta_al_logo.png" con la ruta de tu archivo de imagen)
        self.rutaImagen="imagenes/electronicos.jpg"
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


        # Frame de contenido (Informe de Productos)
        content_frame = tk.Frame(self.master, bg="dodgerblue2")
        content_frame.pack(fill="both", expand=True)

        report_title = tk.Label(content_frame, text="Informe de Productos", font=("Arial", 14), fg="white", bg="dodgerblue2")
        report_title.pack(pady=10)

        # Tablas de productos más y menos vendidos
        tables_frame = tk.Frame(content_frame, bg="dodgerblue2")
        tables_frame.pack()

        # Tabla de Más Vendidos
        sold_frame = tk.Frame(tables_frame, bd=1, relief="solid", bg="cyan")
        sold_frame.grid(row=0, column=0, padx=10)

        sold_label = tk.Label(sold_frame, text="Más Vendidos", font=("Arial", 12), fg="black", bg="cyan")
        sold_label.pack()

        # Tabla personalizada (Treeview no permite fácilmente cambiar el fondo, por lo que se usa `style`)
        self.sold_table = ttk.Treeview(sold_frame, columns=("Producto", "Cantidad"), show="headings")
        self.sold_table.heading("Producto", text="Nombre Producto")
        self.sold_table.heading("Cantidad", text="Cantidad")
        self.sold_table.pack()

        # Tabla de Menos Vendidos
        unsold_frame = tk.Frame(tables_frame, bd=1, relief="solid", bg="cyan")
        unsold_frame.grid(row=0, column=1, padx=10)

        unsold_label = tk.Label(unsold_frame, text="Menos Vendidos", font=("Arial", 12), fg="black", bg="cyan")
        unsold_label.pack()

        self.unsold_table = ttk.Treeview(unsold_frame, columns=("Producto", "Cantidad"), show="headings")
        self.unsold_table.heading("Producto", text="Nombre Producto")
        self.unsold_table.heading("Cantidad", text="Cantidad")
        self.unsold_table.pack()

        # Botón para generar informe (personalizado)
        generate_report_button = tk.Button(content_frame, text="Generar Informe", command=self.informe, bg="blue", fg="white", activebackground="darkgreen")
        generate_report_button.pack(pady=10)

        # Cargar datos en las tablas
        self.load_data()

        # Personalizar Treeview (colores de las filas y cabecera)
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", background="white", foreground="black", rowheight=25, fieldbackground="white")
        style.configure("Treeview.Heading", background="grey", foreground="white", font=("Arial", 10, "bold"))

        # Alternar colores en las filas
        style.map("Treeview", background=[('selected', 'lightblue')])

    def load_data(self):
    # Obtiene los datos del controlador
        mas_vendidos = self.controlador.obtener_mas_vendidos()
        menos_vendidos = self.controlador.obtener_menos_vendidos()

    # Limpiar tablas
        for item in self.sold_table.get_children():
            self.sold_table.delete(item)
        for item in self.unsold_table.get_children():
            self.unsold_table.delete(item)

    # Insertar datos en la tabla de Más Vendidos
        for producto in mas_vendidos:

            nombre_producto = producto[0]  
            cantidad = producto[1] 
            self.sold_table.insert('', 'end', values=(nombre_producto, cantidad))


        for producto in menos_vendidos:
            nombre_producto = producto[0]  
            cantidad = producto[1]  
            self.unsold_table.insert('', 'end', values=(nombre_producto, cantidad))

    def informe(self):
        # Generar el informe (función que se llama al presionar el botón)
        messagebox.showinfo("Solicitud Realizada", "Informe Generado Exitosamente")
        self.controlador.generarInforme()