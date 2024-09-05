import tkinter as tk
import json
from vista_catalogo import vista_catalogo
from vista_reporte import ReportView
from vista_login import Login 
from modelo import modelo
from datetime import datetime
ahora=datetime.now()
class controlador:

    def __init__(self,ven):
        self.ven =ven
        self.modelo=modelo
        self.inicioSesion()
    
    def inicioSesion(self):
        self.vista=Login(self.ven,self)

    def Validar_formulario(self,usuario,contraseña):
        if len(usuario) != 0 and len(contraseña) != 0:
            if modelo.validarUsuario(usuario, contraseña):
                texto = "Bienvenido Usuario"
                self.vista.Validar_formulario_completo(texto)
                self.vista.ocultarWidgets()
                self.vistaCatalogo()
            else:
                texto = "Usuario o contraseña incorrectos"
                self.vista.Limpiar_login(texto)
                return True
        else:
            texto="Ingrese su usuario y contraseña!!!"
            self.vista.Limpiar_login(texto)
            return False
    def vistaCatalogo(self):
        self.vista = vista_catalogo(self.ven,self)
        self.vista.pack(fill="both", expand=True)

    def vistaReporte(self):
        self.vistaInforme = tk.Toplevel(self.ven)
        self.vistaInforme.geometry("1000x600") 
        self.vista = ReportView(self.vistaInforme,self)
        self.vista.pack(fill="both", expand=True)

    def generarInforme(self):
        dia = ahora.date()
        hora = ahora.time()
        datos=self.modelo.consultarDatos()
        with open(f'{dia}', 'w', encoding='utf8') as archivo:
            productos = f'Los datos de los productos registrados son: {datos}'  
            productos +=f" /Informe realizado a las {hora}"
            json.dump(productos, archivo)

if __name__ == "__main__":
    ventana = tk.Tk()
    app = controlador(ventana)
    ventana.mainloop()