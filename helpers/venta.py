from helpers.conection import *
from models.venta_model import *

# Insertar una nueva venta
def insert_venta(id_cita, tipo_pago, monto_final):
    conexion = Connection()
    try:
        with conexion.cursor() as cursor:
            sql = """
                INSERT INTO Ventas (id_cita, fecha, tipo_pago, monto_final)
                VALUES (%s, NOW(), %s, %s)
            """
            valores = (id_cita, tipo_pago, monto_final)
            cursor.execute(sql, valores)
            conexion.commit()
    finally:
        conexion.close()

# Obtener una venta por ID
def select_venta(id_venta):
    conexion = Connection()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM Ventas WHERE id_venta = %s", (id_venta,))
        resultado = cursor.fetchone()
    conexion.close()

    return Venta(resultado).to_dict() if resultado else None

# Obtener todas las ventas activas
def select_all_ventas():
    conexion = Connection()
    ventas = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM Ventas WHERE estado = 'ACTIVO'")
        resultados = cursor.fetchall()
        for venta in resultados:
            ventas.append(Venta(venta).to_dict())
    conexion.close()
    return ventas
