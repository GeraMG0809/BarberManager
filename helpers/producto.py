from helpers.conection import * 
from models.producto_model import Producto
from mysql.connector import Error

def select_producto(nombre_producto: str):
    conexion = Connection()
    producto = None

    try:
        with conexion.cursor() as cursor:
            sql = "SELECT * FROM Productos WHERE Nombre_producto = %s"
            cursor.execute(sql, (nombre_producto,))
            resultado = cursor.fetchone()
            if resultado:
                producto = Producto(resultado).to_dict()
    finally:
        conexion.close()

    return producto


def select_producto_id(nombre_producto: str):
    conexion = Connection()
    id_producto = None

    try:
        with conexion.cursor() as cursor:
            sql = "SELECT id_producto FROM Productos WHERE Nombre_producto = %s"
            cursor.execute(sql, (nombre_producto,))
            resultado = cursor.fetchone()
            if resultado:
                id_producto = resultado[0]
    finally:
        conexion.close()

    return id_producto


def select_productos():
    conexion = Connection()
    productos = []

    try:
        with conexion.cursor() as cursor:
            sql = "SELECT * FROM Productos WHERE estado = 'ACTIVO'"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            productos = [Producto(row).to_dict() for row in resultados]
    finally:
        conexion.close()

    return productos


def insert_producto(categoria, precio, nombre_producto, estado='ACTIVO'):
    conexion = Connection()

    try:
        with conexion.cursor() as cursor:
            sql = """
                INSERT INTO Productos (categoria, precio, estado, Nombre_producto)
                VALUES (%s, %s, %s, %s)
            """
            valores = (categoria, precio, estado, nombre_producto)
            cursor.execute(sql, valores)
            conexion.commit()
    finally:
        conexion.close()


def update_producto(id_producto, categoria=None, precio=None, estado=None, nombre_producto=None):
    conexion = Connection()

    try:
        with conexion.cursor() as cursor:
            campos = []
            valores = []

            if categoria:
                campos.append("categoria = %s")
                valores.append(categoria)
            if precio is not None:
                campos.append("precio = %s")
                valores.append(precio)
            if estado:
                campos.append("estado = %s")
                valores.append(estado)
            if nombre_producto:
                campos.append("Nombre_producto = %s")
                valores.append(nombre_producto)

            if campos:
                sql = f"UPDATE Productos SET {', '.join(campos)} WHERE id_producto = %s"
                valores.append(id_producto)
                cursor.execute(sql, tuple(valores))
                conexion.commit()
    finally:
        conexion.close()


def delete_producto(id_producto):
    conexion = Connection()

    try:
        with conexion.cursor() as cursor:
            sql = "DELETE FROM Productos WHERE id_producto = %s"
            cursor.execute(sql, (id_producto,))
            conexion.commit()
    finally:
        conexion.close()



def select_producto_precio(nombre_producto: str):
    conexion = Connection()
    precio_producto = None

    try:
        with conexion.cursor() as cursor:
            sql = "SELECT precio FROM Productos WHERE Nombre_producto = %s"
            cursor.execute(sql, (nombre_producto,))
            resultado = cursor.fetchone()
            if resultado:
                precio_producto = resultado[0]  # El precio está en la primera posición
    finally:
        conexion.close()

    return precio_producto
