import mysql.connector
import json
from datetime import datetime, date, time
from mysql.connector import Error
from tkinter import *
from tkinter import ttk
from tkinter import messagebox , Image
now = datetime.now()

class conexion:
    
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
            
            
        
aux = conexion.crearConexion()
aux2 = conexion.verificacion_conexion(aux)






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
            print("validado")
            return True
        else:
             messagebox.showerror("ERROR DE INGRESO", "Ingrese su usuario y contraseña!!!")
        self.Limpiar_login()    
    
    def Limpiar_login(self):
            self.usuario_login.delete(0, END)
            self.password_login.delete(0, END)

    def Login(self):
        
            if(self.Validar_formulario_completo()):
                usuario= self.usuario_login.get()
                password= self.password_login.get()
                conexion1 = conexion.crearConexion()
                cursor = conexion1.cursor()
                cursor.execute(f"SELECT * FROM usuarios WHERE usuario = '{usuario}' AND contrasena = '{password}'")
                print(usuario)
                consulta = cursor.fetchall()
                print(consulta)
                
                                          #SELECT usuario, contrasena FROM usuarios WHERE usuario == %s AND contrasena == %s", (usuario, password))
                
                if (consulta != []):
                    messagebox.showinfo("BIENVENIDO", "Datos ingresados correctamente")
                    
                else:
                    messagebox.showerror("ERROR DE INGRESO", "usuario o contraseña incorrecto") 
                self.Limpiar_login()
        
 
class modelo:
    def __init__(self) -> None:
         self._nombre = None
         self._descripcion = None
         self._categoria = None
         self._precio = None
         self._vendido = None
         self._dia = None
         self._hora = None
         self._base = []
         
    @property
    def nombre(self):
        return self._nombre
    @property
    def descripcion(self):
        return self._descripcion
    @property
    def categoria(self):
        return self._categoria
    @property
    def precio(self):
        return self._precio
    @property
    def vendido(self):
        return self._vendido
    @property
    def dia(self):
        return self._dia
    @property
    def hora(self):
        return self._hora
    @property
    def base(self):
        return self._base
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = descripcion
    @categoria.setter
    def categoria(self, categoria):
        self._categoria = categoria
    @precio.setter
    def precio(self, precio):
        self._precio = precio
    @vendido.setter
    def vendido(self, vendido):
        self._vendido = vendido
    @dia.setter
    def dia(self, dia):
        self._dia = dia
    @hora.setter
    def hora(self, hora):
        self._hora = hora
    @categoria.setter
    def base(self, base):
        self._base = base
    
         
    def registrarProducto(nombre, descripcion, categoria, precio, vendido, dia, hora):

            conexion1 = conexion.crearConexion()
            cursor = conexion1.cursor()
            cursor.execute(f"INSERT INTO productos (`nombre`, `descripcion`, `categoria`, `precio`, `vendido`, `dia`, `hora`) VALUES ('{nombre}','{descripcion}','{categoria}','{precio}','{vendido}','{dia}','{hora}')")
            conexion1.commit()
            print("Datos guardados")
            
    def consultarDatos():
        conexion1 = conexion.crearConexion()
        cursor = conexion1.cursor()
        cursor.execute(f"SELECT * FROM productos")
        consulta = cursor.fetchall()
        return consulta
    
    def consultarCategoria(categoria):
        conexion1 = conexion.crearConexion()
        cursor = conexion1.cursor()
        cursor.execute(f"SELECT * FROM productos WHERE categoria = '{categoria}'")
        consulta = cursor.fetchall()
        return consulta
        
        
    #def generar_archivo():
     #   datos2 = modelo.consultarDatos()
      #  json_dato=json.dumps(datos2)
       # print(json_dato)
        #serializar a no json
       # sin_jason = json.loads(json_dato)
       # print(sin_jason)
        
        #serializar y escribir en un archivo
        
            
    
            
    def generarInforme(dia):
            with open(f'{dia}', 'w', encoding='utf8') as archivo:
                
                json.dumps(modelo._base, archivo)
            print("informe generado")
                
    
#verificar si el modulo ha sido ejecutado correctamente  
#if __name__ == '__main__':
#    ventana_login=Tk()
#    application=Login(ventana_login)
#    ventana_login.mainloop()
#    fecha = now.date()
#    print(fecha)
dia1 = now.date()
hora1 = now.time()
modelo._base = modelo.consultarDatos()
print(modelo._base)
resultado = modelo.consultarCategoria('limpieza')
print(resultado)
#modelo.generarInforme(dia1)
nombre1 = input("nombre")
descripcion1 = input("descrip")
categoria1 = input("categoria")
precio1 = float(input("precio"))
vendido1 = int(input("vendido"))


modelo.nombre = nombre1
modelo.descripcion = descripcion1
modelo.categoria = categoria1
modelo.precio = precio1
modelo.vendido = vendido1
modelo.dia = dia1
modelo.hora = hora1

modelo.registrarProducto(modelo.nombre, modelo.descripcion, modelo.categoria, modelo.precio, modelo.vendido, modelo.dia, modelo.hora)