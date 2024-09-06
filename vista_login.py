import tkinter as tk
from tkinter import messagebox
class Login:
    db_name = 'database_proyecto.db'
    
    def __init__(self, ventana_login,controlador):
        self.controlador = controlador
        self.window = ventana_login  
        self.window.title("INGRESAR AL SISTEMA")
        self.window.geometry("330x300")
        self.window.resizable(0, 0)
        self.window.config(bd=10)
        
        "--------------- Titulo --------------------"
        self.label = tk.Label(self.window, text="INICIAR SESION", fg="black", font=("Comic Sans", 13, "bold"), pady=10)
        self.label.pack(fill='both',expand=True)

        "--------------- Marco --------------------"
        self.marco = tk.LabelFrame(self.window, text="Ingrese sus datos", font=("Comic Sans", 10, "bold"))
        self.marco.config(bd=2)
        self.marco.pack(fill='both',expand=True)

        "--------------- Formulario --------------------"
        tk.Label(self.marco, text="Usuario: ", font=("Comic Sans", 10, "bold")).grid(row=0, column=0, sticky='s', padx=5, pady=10)
        self.usuario_login = tk.Entry(self.marco, width=25)
        self.usuario_login.focus()
        self.usuario_login.grid(row=0, column=1, padx=5, pady=10)

        tk.Label(self.marco, text="Contraseña: ", font=("Comic Sans", 10, "bold")).grid(row=1, column=0, sticky='s', padx=10, pady=10)
        self.password_login = tk.Entry(self.marco, width=25, show="*")
        self.password_login.grid(row=1, column=1, padx=10, pady=10)
        
        "--------------- Frame botones --------------------"
        self.frame_botones = tk.Frame(self.window)
        self.frame_botones.pack(fill='both',expand=True)

        "--------------- Botones --------------------"
        tk.Button(self.frame_botones, text="INGRESAR", command=self.iniciar_sesion, height=2, width=12, bg="green", fg="white", font=("Comic Sans", 10, "bold")).pack(pady=15)
        
    def Validar_formulario_completo(self,texto):
        messagebox.showinfo("Ingreso Exitoso",texto)

    def Limpiar_login(self,texto):
        messagebox.showerror("ERROR DE INGRESO",texto)
        self.usuario_login.delete(0, tk.END)
        self.password_login.delete(0, tk.END)

    def iniciar_sesion(self):
            usuario = self.usuario_login.get()
            password = self.password_login.get()
            self.controlador.Validar_formulario(usuario, password)

    def ocultarWidgets(self):
        self.marco.pack_forget()
        self.label.pack_forget()
        self.frame_botones.pack_forget()




