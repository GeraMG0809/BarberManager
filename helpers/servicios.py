from helpers.conection import *



def get_servicio_id(name):
    barberManager = Connection()

    with barberManager.cursor() as cursor:
        cursor.execute(f"SELECT id_servicio FROM Servicios WHERE nombre_servicio = %s",(name))
        id = cursor.fetchone()

    barberManager.close()

    return id[0] if id else None

def get_servicios():
    barberManager =Connection()

    servicios = list
    with barberManager.cursor() as cursor:
        cursor.execute("SELECT * FROM Servicios WHERE estado = 'ACTIVO'")
        servicios = cursor.fetchall()

    barberManager.close()

    return servicios