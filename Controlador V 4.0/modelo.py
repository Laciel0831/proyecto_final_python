import mysql.connector
from mysql.connector import Error

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

    @staticmethod
    def validarUsuario(usuario, contraseña):
        conexion1 = conexion.crearConexion()
        if conexion1 is None:
            return False
        cursor = conexion1.cursor(dictionary=True)
        sql = "SELECT * FROM usuarios WHERE usuario = %s AND contrasena = %s"
        cursor.execute(sql, (usuario, contraseña))
        ContraseñaConsulta = cursor.fetchone()
        cursor.close()
        conexion1.close()
        return ContraseñaConsulta is not None

    def obtenerRolUsuario(self, usuario):
            conexion1 = conexion.crearConexion()
            cursor = conexion1.cursor()
            cursor.execute("SELECT rol FROM usuarios WHERE usuario = %s", (usuario,))
            rol = cursor.fetchone()
            cursor.close()
            conexion1.close()
            return rol[0] if rol else None

    def registrarProducto(self,nombre, descripcion, categoria, precio, vendido):
            conexion1 = conexion.crearConexion()
            cursor = conexion1.cursor()
            cursor.execute(f"INSERT INTO productos (nombre,descripcion,categoria,precio,vendido) VALUES ('{nombre}','{descripcion}','{categoria}','{precio}','{vendido}')")
            conexion1.commit()

    def eliminarProducto(self,codigo):
            conexion1 = conexion.crearConexion()
            cursor = conexion1.cursor()
            cursor.execute(f"DELETE FROM productos WHERE codigo={codigo}")
            conexion1.commit()

    def ActualizarProducto(self,codigo,nombre, descripcion, categoria, precio, vendido):
        conexion1 = conexion.crearConexion()
        cursor=conexion1.cursor()
        sql =f"UPDATE productos SET nombre = %s, descripcion = %s, categoria = %s, precio = %s, vendido = %s WHERE codigo = %s"
        cursor.execute(sql, (nombre, descripcion, categoria, precio, vendido, codigo))
        conexion1.commit()
        cursor.close()
        conexion1.close()

    def consultarDatos(self):
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

    def consultarMayor(self):
        conexion1 = conexion.crearConexion()
        cursor = conexion1.cursor()
        cursor.execute("SELECT nombre, vendido FROM productos ORDER BY vendido DESC LIMIT 3")
        consulta = cursor.fetchall()
        conexion1.close()
        return consulta

    def consultarMenor(self):
        conexion1 = conexion.crearConexion()
        cursor = conexion1.cursor()
        cursor.execute("SELECT nombre, vendido FROM productos ORDER BY vendido ASC LIMIT 3")
        consulta = cursor.fetchall()
        conexion1.close()
        return consulta