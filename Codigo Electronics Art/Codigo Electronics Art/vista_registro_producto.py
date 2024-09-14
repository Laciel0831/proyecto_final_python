import tkinter as tk
from tkinter import ttk, messagebox

modificar=False
class VistaProducto(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Registro de Producto")
        self.geometry("700x600")
        self.resizable(True, True)
        self.create_widgets()

    def create_widgets(self):
        frameRegistro = tk.LabelFrame(self, text="Formulario de Gestión de Producto")
        frameRegistro.place(x=50, y=50, width=570, height=620)

        # Etiquetas y campos de entrada
        self.textNombre = tk.StringVar()
        self.textDescripcion = tk.StringVar()
        self.textCategoria = tk.StringVar()
        listopciones = ['Acción', 'Aventura', 'Estrategia', 'Deportivo', 'Arcade']
        self.opcion = tk.StringVar()
        self.opcion.set(listopciones[0])
        self.textPrecio = tk.StringVar()
        self.textVendidos = tk.StringVar()
        
        labelNombre = tk.Label(frameRegistro, text="Nombre:", font=("Arial", 13), bg="thistle", relief="groove")
        labelNombre.grid(row=0, column=0, padx=5, pady=5)
        self.nombre_entry = tk.Entry(frameRegistro, textvariable=self.textNombre)
        self.nombre_entry.grid(row=0, column=1, padx=5, pady=5)

        labelDescripcion = tk.Label(frameRegistro, text="Descripción:", font=("Arial", 13), bg="thistle", relief="groove")
        labelDescripcion.grid(row=1, column=0, padx=5, pady=5)
        self.descripcion_entry = tk.Entry(frameRegistro, textvariable=self.textDescripcion)
        self.descripcion_entry.grid(row=1, column=1, padx=5, pady=5)

        labelCategoria = tk.Label(frameRegistro, text="Categoría:", font=("Arial", 13), bg="thistle", relief="groove")
        labelCategoria.grid(row=0, column=2, padx=5, pady=5)
        self.categoria_entry = tk.OptionMenu(frameRegistro, self.opcion, *listopciones)
        self.categoria_entry.grid(row=0, column=3, padx=5, pady=5)

        labelPrecio = tk.Label(frameRegistro, text="Precio:", font=("Arial", 13), bg="thistle", relief="groove")
        labelPrecio.grid(row=1, column=2, padx=5, pady=5)
        self.precio_entry = tk.Entry(frameRegistro, textvariable=self.textPrecio)
        self.precio_entry.grid(row=1, column=3, padx=5, pady=5)

        labelVendidos = tk.Label(frameRegistro, text="Vendidos:", font=("Arial", 13), bg="thistle", relief="groove")
        labelVendidos.grid(row=3, column=1, padx=5, pady=5)
        self.vendidos_entry = tk.Entry(frameRegistro, textvariable=self.textVendidos)
        self.vendidos_entry.grid(row=3, column=2, padx=5, pady=5)

        MensajeProductos = tk.Label(frameRegistro, text="Productos Registrados", fg="saddle brown", font=("times", 13, 'bold'))
        MensajeProductos.grid(column=0, row=4, columnspan=4, padx=5)

        self.tablaProductos = ttk.Treeview(frameRegistro,selectmode="none")
        self.tablaProductos.grid(column=0, row=5, columnspan=4, pady=5)
        self.tablaProductos['columns'] = ("Id", "Nombre", "Descripción", "Categoria", "Precio", "Vendidos")
        self.tablaProductos.column("#0", width=0, stretch=tk.NO)
        self.tablaProductos.column("Id", width=50, anchor=tk.CENTER)
        self.tablaProductos.column("Nombre", width=100, anchor=tk.CENTER)
        self.tablaProductos.column("Descripción", width=100, anchor=tk.CENTER)
        self.tablaProductos.column("Categoria", width=100, anchor=tk.CENTER)
        self.tablaProductos.column("Precio", width=100, anchor=tk.CENTER)
        self.tablaProductos.column("Vendidos", width=100, anchor=tk.CENTER)
        self.tablaProductos.heading("#0", text="")
        self.tablaProductos.heading("Id", text="Id", anchor=tk.CENTER)
        self.tablaProductos.heading("Nombre", text="Nombre", anchor=tk.CENTER)
        self.tablaProductos.heading("Descripción", text="Descripción", anchor=tk.CENTER)
        self.tablaProductos.heading("Categoria", text="Categoria", anchor=tk.CENTER)
        self.tablaProductos.heading("Precio", text="Precio", anchor=tk.CENTER)
        self.tablaProductos.heading("Vendidos", text="Vendidos", anchor=tk.CENTER)
        self.tablaProductos.bind("<<TreeviewSelect>>",self.seleccionarProducto)

        # Botón de gestión de producto
        self.botonRegistrar = tk.Button(frameRegistro, text="Registrar Producto", command=self.registrar_producto, bg="blue", fg="white", font=("Arial", 10, 'bold'))
        self.botonRegistrar.grid(column=0, row=6, pady=5, columnspan=4)
        self.botonModificar = tk.Button(frameRegistro, text="Seleccionar Producto", command=self.ActualizarProducto, bg="blue", fg="white", font=("Arial", 10, 'bold'))
        self.botonModificar.grid(column=0, row=7, pady=5, columnspan=4)
        self.botonEliminar = tk.Button(frameRegistro, text="Eliminar Producto", command=self.eliminarProducto, bg="blue", fg="white", font=("Arial", 10, 'bold'))
        self.botonEliminar.grid(column=0, row=8, pady=5, columnspan=4)
        self.botonFiltrarCategorias = tk.Button(frameRegistro, text="Filtrar por Categoría", command=self.mostrar_categorias, bg="blue", fg="white", font=("Arial", 10, 'bold'))
        self.botonFiltrarCategorias.grid(column=0, row=9, pady=5, columnspan=4)
        
        self.Modificarfalso()

    def mostrar_categorias(self):
        categorias = ['Acción', 'Aventura', 'Estrategia', 'Deportivo', 'Arcade']
        menu = tk.Menu(self, tearoff=0)
        for categoria in categorias:
            menu.add_command(label=categoria, command=lambda c=categoria: self.filtrar_por_categoria(c))
        menu.post(self.winfo_pointerx(), self.winfo_pointery())

    def filtrar_por_categoria(self, categoria):
        productos = self.controller.filtrarProductosPorCategoria(categoria)  # Obtén todos los productos
        print("Datos recibidos de filtrarProductosPorCategoria:", productos)  # Imprime los datos para verificar
        self.vaciar_tabla()
        for producto in productos:
            print("Producto procesado:", producto)  # Imprime cada producto para verificar
            # Usa la clave correcta para acceder a la categoría
            if "categoria" in producto:
                if producto["categoria"].lower() == categoria.lower():  # Comparación insensible a mayúsculas/minúsculas
                    # Ajusta el formato de los datos si es necesario
                    values = (
                        producto.get("codigo", ""),
                        producto.get("nombre", ""),
                        producto.get("descripcion", ""),
                        producto.get("categoria", ""),
                        producto.get("precio", ""),
                        producto.get("vendido", "")
                    )
                    self.tablaProductos.insert("", "end", values=values)
            else:
                print("Clave 'categoria' no encontrada en:", producto)

    def vaciar_tabla(self):
        filas = self.tablaProductos.get_children()
        for fila in filas:
            self.tablaProductos.delete(fila)

    def infoProducto(self,filas):
        self.vaciar_tabla()
        for fila in filas:
            id = fila[0]
            self.tablaProductos.insert("", tk.END, id=id, values=fila)

    def eliminarProducto(self):
        id_seleccionado = self.tablaProductos.selection()  # Devuelve una tupla o lista con los IDs seleccionados
        if not id_seleccionado:
            messagebox.showerror("Error", "No se ha seleccionado ningún registro")
        else:
            id = id_seleccionado[0]  # Obtener el primer elemento de la lista
            try:
                
                if int(id) > 0:
                    self.controller.EliminacionProducto(id)  # Llama al controlador para eliminar el producto
                    self.tablaProductos.delete(id)  # Elimina la fila en la tabla
                    self.limpiar_campos()  # Limpia los campos de entrada
                    messagebox.showinfo("Acción Realizada Exitosamente", "Producto eliminado con éxito")
                    self.controller.ActualizarCatalogo()
                else:
                    messagebox.showerror("Error", "No se puede eliminar el producto con ID 0")
            except ValueError:
                messagebox.showerror("Error", "El ID seleccionado no es válido")


    def registrar_producto(self):
        # Obtener datos de los campos de entrada
        if modificar==False:
            nombre = self.nombre_entry.get()
            descripcion = self.descripcion_entry.get()
            categoria = self.opcion.get() 
            precio = self.precio_entry.get()
            vendidos = self.vendidos_entry.get()

            # Validar los datos ingresados
            if not all([nombre, descripcion, categoria, precio, vendidos]):
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
                self.controller.registrarProducto(nombre, descripcion, categoria, precio, vendidos)
                messagebox.showinfo("Éxito", "Producto registrado correctamente.")
                self.limpiar_campos()
                self.controller.tablaProductos()
            except Exception as e:
                messagebox.showerror("Error", f"Error al registrar el producto: {e}")
            self.controller.ActualizarCatalogo()
        else:
            self.Modificarfalso()

    def seleccionarProducto(self, event=None):
        seleccionado = self.tablaProductos.selection()
        if seleccionado:
            item = self.tablaProductos.item(seleccionado[0])
            values = item['values']
            self.nombre_entry.delete(0, tk.END)
            self.nombre_entry.insert(0, values[1])
            self.descripcion_entry.delete(0, tk.END)
            self.descripcion_entry.insert(0, values[2])
            self.opcion.set(values[3])
            self.precio_entry.delete(0, tk.END)
            self.precio_entry.insert(0, values[4])
            self.vendidos_entry.delete(0, tk.END)
            self.vendidos_entry.insert(0, values[5])
            # Cambia el estado para modificación
            self.ModificarTrue()

    def ActualizarProducto(self):
        if modificar==True:
            nombre = self.nombre_entry.get()
            descripcion = self.descripcion_entry.get()
            categoria = self.opcion.get() 
            precio = self.precio_entry.get()
            vendidos = self.vendidos_entry.get()
            seleccion = self.tablaProductos.selection()

            id_producto = seleccion[0]

            # Validar los datos ingresados
            if not all([nombre, descripcion, categoria, precio, vendidos]):
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
                self.controller.modificarProducto(id_producto,nombre, descripcion, categoria, precio, vendidos)
                messagebox.showinfo("Éxito", "Producto Modificado correctamente.")
                self.limpiar_campos()
                self.controller.tablaProductos()
            except Exception as e:
                messagebox.showerror("Error", f"Error al Modificar el producto: {e}")
            self.controller.ActualizarCatalogo()
        else:
            self.ModificarTrue()

    def Modificarfalso(self):
        global modificar
        modificar = False
        self.tablaProductos.config(selectmode=None)
        self.botonRegistrar.config(text="Registrar Producto")
        self.botonModificar.config(text="Seleccionar Producto")
        self.botonEliminar.config(state='disabled')

    def ModificarTrue(self):
        global modificar
        modificar = True
        self.tablaProductos.config(selectmode="browse")
        self.botonRegistrar.config(text="Regresar",command=self.deshabilitarSeleccion)
        self.botonModificar.config(text="Modificar Producto")
        self.botonEliminar.config(state='normal')

    def deshabilitarSeleccion(self):
        self.tablaProductos.config(selectmode='none')
        selected_items = self.tablaProductos.selection()
        for item in selected_items:
            self.tablaProductos.selection_remove(item)
        self.limpiar_campos()
        self.Modificarfalso()
        self.botonRegistrar.config(command=self.registrar_producto)

    def limpiar_campos(self):
        self.nombre_entry.delete(0, tk.END)
        self.descripcion_entry.delete(0, tk.END)
        self.opcion.set('Acción') 
        self.precio_entry.delete(0, tk.END)
        self.vendidos_entry.delete(0, tk.END)
