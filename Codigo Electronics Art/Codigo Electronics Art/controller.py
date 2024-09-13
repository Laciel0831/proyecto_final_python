import tkinter as tk
from vista_catalogo import vista_catalogo
from vista_reporte import ReportView
from vista_login import Login 

class Controller:
    def __init__(self, root):
        self.root = root
        self.show_login_view()

    def show_login_view(self):
        # Mostrar la vista de login
        self.current_view = Login(self.root,self)

    def mostar_vista_catalogo(self):
        # Eliminar la vista de login y mostrar el catálogo
        self.current_view.pack_forget()
        self.current_view = vista_catalogo(master=self.root, controller=self)
        self.current_view.pack(fill="both", expand=True)

    def show_report_view(self):
        report_window = tk.Toplevel(self.root)  # Crear una nueva ventana para el reporte
        report_window.geometry("800x600")  # Tamaño de la ventana para la vista de reportes
        self.current_view = ReportView(master=report_window)
        self.current_view.pack(fill="both", expand=True)

    def login_successful(self):
        # Llamado después de un login exitoso para mostrar el catálogo
        self.mostar_vista_catalogo()

if __name__ == "__main__":
    root = tk.Tk()
    app = Controller(root)
    root.mainloop()


