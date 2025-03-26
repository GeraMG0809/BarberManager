from helpers.conection import *
from models.citas_model import *



def new_cita(id_barb:int,id_usuario:int,fecha:str,hora:str,id_paquete:int):
    barberManager = Connection()

    with barberManager.cursor() as cursor:
        cursor.execute("INSERT INTO Cita(id_barbero,id_usuario,id_paquete,hora_cita,fecha) VALUES (%s,%s,%s,%s,%s)",{id_barb},{id_usuario},{id_paquete},{hora},{fecha})

    barberManager.commit()
    barberManager.close()


def select_citas_pendientes():
    barberManager = Connection()

    citas_pendientes = []
    with barberManager.cursor() as cursor:
        cursor.execute("SELECT * FROM Cita WHERE estado = 'PENDIENTE'")
        citas_pendientes.fetchall()
    
    barberManager.close()
    return citas_pendientes


def select_citas_finalizadas():
    barberManager = Connection()

    citas_finalizadas = []
    with barberManager.cursor() as cursor:
        cursor.execute("SELECT * FROM Cita WHERE estado = 'FINALIZADA'")
        citas_finalizadas.fetchall()
    
    barberManager.close()
    return citas_finalizadas


def select_cita_filter(tipo_filtro : str, filtro: str):
    barberManager = Connection()

    citas_filtradas= []
    #se envia el tipo de filtro (hora, fecha, barbero y el filtrado: 1:00pm, 18/03/2025)
    with barberManager.cursor() as cursor:
        cursor.execute(f"SELECT * FROM Cita WHERE {tipo_filtro} ={filtro}")
        citas_filtradas.fetchall()
    
    barberManager.close()
    return citas_filtradas


def Update_cita_fin(id_cita: int):
    barberManager = Connection()

    with barberManager.cursor() as cursor:
        cursor.execute(f"UPDATE Cita SET estado ='FINALIZADA' WHERE id_cita = {id_cita}")

    barberManager.commit()
    barberManager.close()

def citas_por_usuario(id_usuario:int):
    barberManager = Connection()

    with barberManager.cursor() as cursor:
        cursor.execute(f"SELECT COUNT(*) FROM Cita WHERE id_usuario = {id_usuario} AND estado = 'FINALIZADA'")
        num_citas = cursor.fetchone()
    
    barberManager.close()
    return num_citas


def select_citas_cancelada():
    barberManager = Connection()

    citas_canceladas = []
    with barberManager.cursor() as cursor:
        cursor.execute("SELECT * FROM Cita WHERE estado = 'CANCELADA")
        citas_canceladas = cursor.fetchall()

    barberManager.close()
    return citas_canceladas


def cancelar_cita(id_cita):
    barberManager = Connection()

    with barberManager.cursor() as cursor:
        cursor.execute(f"UPDATE Cita SET estado = 'CANCELADA' WHERE id_cita = {id_cita}")
    
    barberManager.close()


def modificar_cita(campo: str, modificacion:str, id_cita:int):
    barberManager = Connection()

    with barberManager.cursor() as cursor:
        cursor.execute(f"UPDATE Cita SET {campo} = {modificacion} WHERE id_cita = {id_cita}")
    
    barberManager.commit()
    barberManager.close()
    


def obtener_horarios_disponibles(id_barbero: int, fecha: str):
    if not id_barbero:  # Validar que id_barbero no esté vacío
        raise ValueError("El ID del barbero no puede estar vacío o ser None")

    barberManager = Connection()
    horarios_disponibles = [f"{hora}:00" for hora in range(9, 20)]

    try:
        with barberManager.cursor() as cursor:
            # Usar parámetros seguros para evitar inyección SQL
            cursor.execute("SELECT hora_cita FROM Cita WHERE id_barbero = %s AND fecha = %s", (id_barbero, fecha))
            horario_ocupado = [fila[0] for fila in cursor.fetchall()]

        horarios_libres = [hora for hora in horarios_disponibles if hora not in horario_ocupado]
        return horarios_libres

    finally:
        barberManager.close()  # Asegurar cierre de conexión incluso si hay error
