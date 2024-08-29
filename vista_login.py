import tkinter as tk
from tkinter import messagebox
# Asegúrate de que este módulo esté disponible

class Login:
    db_name = 'database_proyecto.db'
    
    def __init__(self, ventana_login):
        self.window = ventana_login  
        self.window.title("INGRESAR AL SISTEMA")
        self.window.geometry("330x370")
        self.window.resizable(0, 0)
        self.window.config(bd=10)
        
        "--------------- Titulo --------------------"
        tk.Label(ventana_login, text="INICIAR SESION", fg="black", font=("Comic Sans", 13, "bold"), pady=10).pack()

        "--------------- Marco --------------------"
        marco = tk.LabelFrame(ventana_login, text="Ingrese sus datos", font=("Comic Sans", 10, "bold"))
        marco.config(bd=2)
        marco.pack()

        "--------------- Formulario --------------------"
        tk.Label(marco, text="Usuario: ", font=("Comic Sans", 10, "bold")).grid(row=0, column=0, sticky='s', padx=5, pady=10)
        self.usuario_login = tk.Entry(marco, width=25)
        self.usuario_login.focus()
        self.usuario_login.grid(row=0, column=1, padx=5, pady=10)

        tk.Label(marco, text="Contraseña: ", font=("Comic Sans", 10, "bold")).grid(row=1, column=0, sticky='s', padx=10, pady=10)
        self.password_login = tk.Entry(marco, width=25, show="*")
        self.password_login.grid(row=1, column=1, padx=10, pady=10)
        
        "--------------- Frame botones --------------------"
        frame_botones = tk.Frame(ventana_login)
        frame_botones.pack()

        "--------------- Botones --------------------"
        tk.Button(frame_botones, text="INGRESAR", command=self.iniciar_sesion, height=2, width=12, bg="green", fg="white", font=("Comic Sans", 10, "bold")).grid(row=0, column=1, padx=10, pady=15)
        
    def Validar_formulario_completo(self):
        if len(self.usuario_login.get()) != 0 and len(self.password_login.get()) != 0:
            print("validado")
            return True
        else:
            messagebox.showerror("ERROR DE INGRESO", "Ingrese su usuario y contraseña!!!")
            self.Limpiar_login()
            return False
    
    def Limpiar_login(self):
        self.usuario_login.delete(0, tk.END)
        self.password_login.delete(0, tk.END)

    def iniciar_sesion(self):
        if self.Validar_formulario_completo():
            usuario = self.usuario_login.get()
            password = self.password_login.get()
            #conexion1 = conexion.crearConexion()
            #cursor = conexion1.cursor()
            
            # Uso de parámetros para evitar inyección SQL
            #cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND contrasena = ?", (usuario, password))
            #consulta = cursor.fetchall()
            
            #if consulta:
                #messagebox.showinfo("BIENVENIDO", "Datos ingresados correctamente")
            #else:
                #messagebox.showerror("ERROR DE INGRESO", "Usuario o contraseña incorrectos")
            
            #self.Limpiar_login()




