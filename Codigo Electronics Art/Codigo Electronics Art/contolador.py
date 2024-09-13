import tkinter as tk
import json
from vista_catalogo import vista_catalogo
from vista_reporte import ReportView
from vista_login import Login
from vista_registro_producto import VistaProducto
from modelo import modelo
from datetime import datetime
from tkinter import messagebox

ahora = datetime.now()

class Controlador:
    def __init__(self, ventana):
        self.ventana = ventana
        self.modelo = modelo()
        self.usuario_actual = None
        self.rol_actual = None
        self.inicioSesion()
    
    def inicioSesion(self):
        self.vista = Login(self.ventana, self)

    def Validar_formulario(self, usuario, contraseña):
        if len(usuario) != 0 and len(contraseña) != 0:
            if self.modelo.validarUsuario(usuario, contraseña):
                self.usuario_actual = usuario
                self.rol_actual = self.modelo.obtenerRolUsuario(usuario)
                texto = "Bienvenido Usuario"
                self.vista.Validar_formulario_completo(texto)
                self.vista.ocultarWidgets()
                self.vistaCatalogo(usuario, self.rol_actual)
            else:
                texto = "Usuario o contraseña incorrectos"
                self.vista.Limpiar_login(texto)
                return True
        else:
            texto = "Ingrese su usuario y contraseña!!!"
            self.vista.Limpiar_login(texto)
            return False

    def vistaCatalogo(self, usuariotext, rol):
        self.vista = vista_catalogo(self.ventana, self, usuariotext, rol)
        self.vista.pack(fill="both", expand=True)

    def ActualizarCatalogo(self):
        catalogo=None
        self.vista.update_catalog(catalogo)

    def vistaReporte(self):
        if self.rol_actual == 'admin':
            self.vistaInforme = tk.Toplevel(self.ventana)
            self.vistaInforme.geometry("1000x600")
            self.vista = ReportView(self.vistaInforme, self)
            self.vista.pack(fill="both", expand=True)
        else:
            messagebox.showerror("ERROR:","Se necesitan credenciales de administrador para acceder a los reportes.")

    def vistaRegistroProducto(self):
        self.vistaRegistro = VistaProducto(self)
        self.vistaRegistro.grab_set() 
        self.tablaProductos()

    def filtrarProductosPorCategoria(self, categoria):
        productos = self.modelo.obtenerProductosPorCategoria(categoria)
        return productos

    def generarInforme(self):
        dia = ahora.date()
        hora = ahora.time()
        datos = self.modelo.consultarDatos()
        with open(f'{dia}.txt', 'w', encoding='utf8') as archivo:
            productos =f"productos: {datos}, informe_realizado a las: {str(hora)}"
            json.dump(productos, archivo, indent=4)

    def EliminacionProducto(self,id):
        self.modelo.eliminarProducto(id)

    def ActualizarCategoria(self):
        """Devuelve una lista de todas las categorías."""
        return [cat[0] for cat in self.modelo.consultarCategoria()] 

    def ActualizarProductoCategoria(self, categoria):
        """Devuelve los productos de una categoría específica."""        
        return self.modelo.consultarCategoria(categoria)

    def ActualizarProductos(self):
        """Devuelve todos los productos disponibles."""
        return self.modelo.consultarDatos()

    def registrarProducto(self, nombre, descripcion, categoria, precio, vendidos):
        """Método para registrar un nuevo producto usando el modelo."""
        self.modelo.registrarProducto(nombre, descripcion, categoria, precio, vendidos)

    def modificarProducto(self,codigo,nombre, descripcion, categoria, precio, vendidos):
        self.modelo.ActualizarProducto(codigo,nombre, descripcion, categoria, precio, vendidos)

    def tablaProductos(self):
        if hasattr(self, 'vistaRegistro'):
            fila = self.modelo.consultarDatos()
            self.vistaRegistro.infoProducto(fila)
        else:
            print("Error: vistaRegistro no está inicializado.")

    def obtener_mas_vendidos(self):
        productos_mas_vendidos = self.modelo.consultarMayor()
        
        return productos_mas_vendidos

    def obtener_menos_vendidos(self):
        productos_menos_vendidos = self.modelo.consultarMenor()
        return productos_menos_vendidos

if __name__ == "__main__":
    ventana = tk.Tk()
    app = Controlador(ventana)
    ventana.mainloop()