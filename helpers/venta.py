from helpers.conection import *
from models.venta_model import *

# Insertar una nueva venta
def insert_venta(id_cita, id_producto, tipo_pago, monto_final):
    """
    Inserta una nueva venta en la base de datos
    Args:
        id_cita: ID de la cita
        id_producto: ID del producto vendido
        tipo_pago: 'Efectivo' o 'Tarjeta'
        monto_final: Monto total de la venta
    """
    conexion = Connection()
    try:
        with conexion.cursor() as cursor:
            sql_venta = """
                INSERT INTO Ventas (id_cita, id_producto, fecha, tipo_pago, monto_final, estado)
                VALUES (%s, %s, NOW(), %s, %s, 'ACTIVO')
            """
            cursor.execute(sql_venta, (id_cita, id_producto, tipo_pago, monto_final))
            conexion.commit()
            return cursor.lastrowid
    except Exception as e:
        print(f"Error al insertar venta: {e}")
        conexion.rollback()
        return None
    finally:
        conexion.close()

# Obtener una venta por ID
def select_venta(id_venta):
    conexion = Connection()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT v.*, p.nombre_producto, p.precio as precio_producto
                FROM Ventas v 
                JOIN Productos p ON v.id_producto = p.id_producto
                WHERE v.id_venta = %s
            """, (id_venta,))
            resultado = cursor.fetchone()
            return Venta(resultado).to_dict() if resultado else None
    except Exception as e:
        print(f"Error al obtener venta por ID: {e}")
        return None
    finally:
        conexion.close()

# Obtener todas las ventas activas
def select_all_ventas():
    conexion = Connection()
    ventas = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT v.*, p.nombre_producto, p.precio as precio_producto
                FROM Ventas v 
                JOIN Productos p ON v.id_producto = p.id_producto
                WHERE v.estado = 'ACTIVO'
                ORDER BY v.fecha DESC
            """)
            resultados = cursor.fetchall()
            for venta in resultados:
                ventas.append(Venta(venta).to_dict())
        return ventas
    except Exception as e:
        print(f"Error al obtener todas las ventas: {e}")
        return []
    finally:
        conexion.close()
