import mysql.connector
import json
from datetime import datetime, date, time
from mysql.connector import Error
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
         self.codigo = None
         
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
    @property
    def codigo(self):
        return self._codigo
    
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
    @categoria.setter
    def codigo(self, codigo):
        self._codigo = codigo
    
         
    def registrarProducto(nombre, descripcion, categoria, precio, vendido, dia, hora):

            conexion1 = conexion.crearConexion()
            cursor = conexion1.cursor()
            cursor.execute(f"INSERT INTO productos (`nombre`, `descripcion`, `categoria`, `precio`, `vendido`, `dia`, `hora`) VALUES ('{nombre}','{descripcion}','{categoria}','{precio}','{vendido}','{dia}','{hora}')")
            conexion1.commit()
            print("Datos guardados")
            
    def agregarVenta(codigo, cantidad):
            conexion1 = conexion.crearConexion()
            cursor = conexion1.cursor()
            cursor.execute(f"UPDATE `productos` SET `vendido`= {cantidad} WHERE codigo = {codigo}")
            conexion1.commit()
            print("Venta realizada")
                        
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
    def consultarMayor():
        conexion1 = conexion.crearConexion()
        cursor = conexion1.cursor()
        cursor.execute(f"SELECT * FROM productos ORDER BY vendido DESC LIMIT 3")
        consulta = cursor.fetchall()
        return consulta
    def consultarMenor():
        conexion1 = conexion.crearConexion()
        cursor = conexion1.cursor()
        cursor.execute(f"SELECT * FROM productos ORDER BY vendido ASC LIMIT 3")
        consulta = cursor.fetchall()
        return consulta
             
    def generarInforme(base , dia):
            with open(f'{dia}', 'w', encoding='utf8') as archivo:
                base1 = f'Los datos de los productos generales son: {base}'  
                json.dump(base1, archivo)
            print("informe generado")
                
    
dia1 = now.date()
hora1 = now.time()
modelo.dia = dia1
modelo.hora = hora1

modelo.base = modelo.consultarDatos()
#print(modelo.base)
#resultado = modelo.consultarCategoria('limpieza')
#print(resultado)
modelo.generarInforme(modelo.base, modelo.dia)
#nombre1 = input("nombre")
#descripcion1 = input("descrip")
#categoria1 = input("categoria")
#precio1 = float(input("precio"))
#vendido1 = int(input("vendido"))


#modelo.nombre = nombre1
#modelo.descripcion = descripcion1
#modelo.categoria = categoria1
#modelo.precio = precio1
#modelo.vendido = vendido1
#modelo.registrarProducto(modelo.nombre, modelo.descripcion, modelo.categoria, modelo.precio, modelo.vendido, modelo.dia, modelo.hora)
#codigo1 = int(input('codigo'))
#cantidad = int(input('cantidad'))
#modelo.codigo = codigo1
#modelo.vendido = cantidad
#modelo.agregarVenta(modelo.codigo, modelo.vendido)

#menores = modelo.consultarMenor()
#print(menores)
