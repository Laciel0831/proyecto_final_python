import mysql.connector
from mysql.connector import Error
from tkinter import *
from tkinter import ttk
from tkinter import messagebox , Image


def crearConexion():
    connection = mysql.connector.connect(
        host = 'localhost',
        database = 'catalogo',
        user = 'root',
        password = ''
    )
    return connection



def verificacion_conexion(datoConexion):
    if datoConexion.is_connected():
        print("conexion exitosa a la base de datos")
        cursor = datoConexion.cursor()
        cursor.execute("SELECT * FROM productos")
        resultados = cursor.fetchall()
        print(resultados) 
        
        
def registrar(datoconexion):
    cursor = datoconexion.cursor()
    codigo = input("digite es")
    nombres = input("nombre")
    cursor.execute("INSERT INTO alumnos(idAlumnos,nombreAlumno) VALUES (%s, %s)", (codigo, nombres))
    print("registro insertado")
    datoconexion.commit()
        
aux = crearConexion()
aux2 = verificacion_conexion(aux)






class Login:
    db_name='database_proyecto.db'
    
    def __init__(self,ventana_login):
        self.window=ventana_login  
        self.window.title("INGRESAR AL SISTEMA")
        self.window.geometry("330x370")
        self.window.resizable(0,0)
        self.window.config(bd=10)
        
        "--------------- Titulo --------------------"
        titulo= Label(ventana_login, text="INICIAR SESION",fg="black",font=("Comic Sans", 13,"bold"),pady=10).pack()



        "--------------- Marco --------------------"
        marco = LabelFrame(ventana_login, text="Ingrese sus datos",font=("Comic Sans", 10,"bold"))
        marco.config(bd=2)
        marco.pack()

        "--------------- Formulario --------------------"
        label_usuario=Label(marco,text="usuario: ",font=("Comic Sans", 10,"bold")).grid(row=0,column=0,sticky='s',padx=5,pady=10)
        self.usuario_login=Entry(marco,width=25)
        self.usuario_login.focus()
        self.usuario_login.grid(row=0, column=1, padx=5, pady=10)

        label_nombres=Label(marco,text="Contraseña: ",font=("Comic Sans", 10,"bold")).grid(row=1,column=0,sticky='s',padx=10,pady=10)
        self.password_login=Entry(marco,width=25,show="*")
        self.password_login.grid(row=1, column=1, padx=10, pady=10)
        
        "--------------- Frame botones --------------------"
        frame_botones=Frame(ventana_login)
        frame_botones.pack()

        "--------------- Botones --------------------"
        boton_ingresar=Button(frame_botones,text="INGRESAR",command=self.Login,height=2,width=12,bg="green",fg="white",font=("Comic Sans", 10,"bold")).grid(row=0, column=1, padx=10, pady=15)
        
        
    def Validar_formulario_completo(self):
        if len(self.usuario_login.get()) !=0 and len(self.password_login.get()) !=0:
            return True
        else:
             messagebox.showerror("ERROR DE INGRESO", "Ingrese su usuario y contraseña!!!")
        self.Limpiar_login()    
    
    def Limpiar_login(self):
            self.usuario_login.delete(0, END)
            self.password_login.delete(0, END)

    def Login(self):
        try:
            if(self.Validar_formulario_completo()):
                usuario= self.usuario_login.get()
                password= self.password_login.get()
                dato = self.Validar_login(usuario, password)
                if (dato != []):
                    messagebox.showinfo("BIENVENIDO", "Datos ingresados correctamente")
                    self.__init__(self,ventana_producto=ventana_login)
                else:
                    messagebox.showerror("ERROR DE INGRESO", "usuario o contraseña incorrecto") 
                self.Limpiar_login()
        except:
            messagebox.showerror("ERROR", "Ha ocurrido un error, reinicie el programa")
            self.Limpiar_login()
   



#verificar si el modulo ha sido ejecutado correctamente  
if __name__ == '__main__':
    ventana_login=Tk()
    application=Login(ventana_login)
    ventana_login.mainloop()
