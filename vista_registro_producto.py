import tkinter as tk
from tkinter import ttk, messagebox

class VistaRegistroProducto(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Registro de Producto")
        self.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        # Frame de entrada de datos
        input_frame = tk.Frame(self)
        input_frame.pack(pady=10, padx=10, fill="x")

        # Etiquetas y campos de entrada
        tk.Label(input_frame, text="Nombre:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.nombre_entry = tk.Entry(input_frame)
        self.nombre_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Descripción:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.descripcion_entry = tk.Entry(input_frame)
        self.descripcion_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Categoría:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.categoria_entry = tk.Entry(input_frame)
        self.categoria_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Precio:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.precio_entry = tk.Entry(input_frame)
        self.precio_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Vendidos:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.vendidos_entry = tk.Entry(input_frame)
        self.vendidos_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Día:").grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.dia_entry = tk.Entry(input_frame)
        self.dia_entry.grid(row=5, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Hora:").grid(row=6, column=0, padx=5, pady=5, sticky="e")
        self.hora_entry = tk.Entry(input_frame)
        self.hora_entry.grid(row=6, column=1, padx=5, pady=5)

        # Botón para registrar el producto
        register_button = tk.Button(self, text="Registrar Producto", command=self.registrar_producto)
        register_button.pack(pady=10)

    def registrar_producto(self):
        # Obtener datos de los campos de entrada
        nombre = self.nombre_entry.get()
        descripcion = self.descripcion_entry.get()
        categoria = self.categoria_entry.get()
        precio = self.precio_entry.get()
        vendidos = self.vendidos_entry.get()
        dia = self.dia_entry.get()
        hora = self.hora_entry.get()

        # Validar los datos ingresados
        if not all([nombre, descripcion, categoria, precio, vendidos, dia, hora]):
            messagebox.showwarning("Entrada inválida", "Por favor, complete todos los campos.")
            return

        try:
            precio = float(precio)
            vendidos = int(vendidos)
        except ValueError:
            messagebox.showwarning("Entrada inválida", "El precio debe ser un número y los vendidos un entero.")
            return

        # Registrar el producto en la base de datos
        try:
            self.controller.registrarProducto(nombre, descripcion, categoria, precio, vendidos, dia, hora)
            messagebox.showinfo("Éxito", "Producto registrado correctamente.")
            self.limpiar_campos()
        except Exception as e:
            messagebox.showerror("Error", f"Error al registrar el producto: {e}")

    def limpiar_campos(self):
        self.nombre_entry.delete(0, tk.END)
        self.descripcion_entry.delete(0, tk.END)
        self.categoria_entry.delete(0, tk.END)
        self.precio_entry.delete(0, tk.END)
        self.vendidos_entry.delete(0, tk.END)
        self.dia_entry.delete(0, tk.END)
        self.hora_entry.delete(0, tk.END)








