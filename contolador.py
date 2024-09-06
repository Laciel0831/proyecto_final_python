import tkinter as tk
import json
from vista_catalogo import vista_catalogo
from vista_reporte import ReportView
from vista_login import Login
from vista_registro_producto import VistaRegistroProducto 
from modelo import modelo
from datetime import datetime

ahora = datetime.now()

class Controlador:
    def __init__(self, ventana):
        self.ventana = ventana
        self.modelo = modelo()
        self.inicioSesion()
    
    def inicioSesion(self):
        self.vista = Login(self.ventana, self)

    def Validar_formulario(self, usuario, contraseña):
        if len(usuario) != 0 and len(contraseña) != 0:
            if self.modelo.validarUsuario(usuario, contraseña):
                texto = "Bienvenido Usuario"
                self.vista.Validar_formulario_completo(texto)
                self.vista.ocultarWidgets()
                self.vistaCatalogo()
            else:
                texto = "Usuario o contraseña incorrectos"
                self.vista.Limpiar_login(texto)
                return True
        else:
            texto = "Ingrese su usuario y contraseña!!!"
            self.vista.Limpiar_login(texto)
            return False

    def vistaCatalogo(self):
        self.vista = vista_catalogo(self.ventana, self)
        self.vista.pack(fill="both", expand=True)

    def vistaReporte(self):
        self.vistaInforme = tk.Toplevel(self.ventana)
        self.vistaInforme.geometry("1000x600")
        self.vista = ReportView(self.vistaInforme, self)
        self.vista.pack(fill="both", expand=True)

    def vistaRegistroProducto(self):
        self.vistaRegistro = VistaRegistroProducto(self)
        self.vistaRegistro.grab_set() 

    def generarInforme(self):
        dia = ahora.date()
        hora = ahora.time()
        datos = self.modelo.consultarDatos()
        with open(f'{dia}.json', 'w', encoding='utf8') as archivo:
            productos = {"productos": datos, "informe_realizado_a": str(hora)}
            json.dump(productos, archivo, indent=4)

    def ActualizarCategoria(self):
        """Devuelve una lista de todas las categorías."""
        return [cat[0] for cat in self.modelo.consultarCategoria()] 

    def ActualizarProductoCategoria(self, categoria):
        """Devuelve los productos de una categoría específica."""
        return self.modelo.consultarCategoria(categoria)

    def ActualizarProductos(self):
        """Devuelve todos los productos disponibles."""
        return self.modelo.consultarDatos()

    def registrarProducto(self, nombre, descripcion, categoria, precio, vendidos, dia, hora):
        """Método para registrar un nuevo producto usando el modelo."""
        self.modelo.registrarProducto(nombre, descripcion, categoria, precio, vendidos, dia, hora)

if __name__ == "__main__":
    ventana = tk.Tk()
    app = Controlador(ventana)
    ventana.mainloop()