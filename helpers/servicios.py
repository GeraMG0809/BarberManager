from helpers.conection import *
from models.servicios_modal import *



def get_servicio_id(name):
    barberManager = Connection()

    with barberManager.cursor() as cursor:
        cursor.execute(f"SELECT id_servicio FROM Servicios WHERE nombre_servicio = %s",(name))
        id = cursor.fetchone()

    barberManager.close()

    return id[0] if id else None

def get_servicios():
    barberManager =Connection()

    paquetes = []
    with barberManager.cursor() as cursor:
        cursor.execute("SELECT * FROM Servicios WHERE estado = 'ACTIVO'")
        servicios = cursor.fetchall()
    
        for paquete in servicios:
            paquetes.append(Servicio(paquete).to_dict())

    barberManager.close()
    return paquetes

def modify_servicio(campo:str,valor)->bool:
    barberManager = Connection()

    columnas = ["nombre_servicios","servicios","precio"]

    if campo not in columnas:
        return False

    with barberManager.cursor() as cursor:
        sql =f"UPDATE Servicios SET {campo} = %s"
        cursor.execute(sql,(valor,))
    
    barberManager.commit()
    barberManager.close()
    return True
