from helpers.conection import *
from models.citas_model import *



def new_cita(id_barb:int,id_usuario:int,fecha:str,hora:str,id_paquete:int):
    barberManager = Connection()

    with barberManager.cursor() as cursor:
        cursor.execute("INSERT INTO Cita(id_barbero, id_usuario, id_servicio, hora_cita, fecha) VALUES (%s, %s, %s, %s, %s)", 
               (id_barb, id_usuario, id_paquete, hora, fecha))

    barberManager.commit()
    barberManager.close()


def select_citas_pendientes():
    barberManager = Connection()
    citas = []

    with barberManager.cursor() as cursor:
        cursor.execute("""
            SELECT 
                C.id_cita,
                U.nombre_usuario,
                B.nombre_barbero,
                S.nombre_servicio,
                S.precio,
                C.fecha,
                C.hora_cita,
                C.estado
            FROM Cita C
            JOIN Usuario U ON C.id_usuario = U.id_usuario
            JOIN Barbero B ON C.id_barbero = B.id_barbero
            JOIN Servicios S ON C.id_servicio = S.id_servicio
            WHERE C.estado = 'PENDIENTE'
        """)
        resultados = cursor.fetchall()

        for fila in resultados:
            cita = Cita(fila)
            citas.append(cita.to_dict())

    barberManager.close()
    return citas




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
    barberManager = Connection()
    horarios_disponibles = [f"{hora}:00" for hora in range(9, 20)]

    with barberManager.cursor() as cursor:
        cursor.execute(f"SELECT hora_cita FROM Cita WHERE id_barbero = {id_barbero} AND fecha = '{fecha}'")
        horario_ocupado = [fila[0] for fila in cursor.fetchall()]

    barberManager.close()

    horarios_libres = [hora for hora in horarios_disponibles if hora not in horario_ocupado]
    return horarios_libres
  # Asegurar cierre de conexión incluso si hay error

def actualizar_estado_cita(id_cita: int, estado: str) -> bool:
    """
    Actualiza el estado de una cita
    Args:
        id_cita: ID de la cita a actualizar
        estado: Nuevo estado de la cita ('PENDIENTE', 'FINALIZADA', etc.)
    Returns:
        bool: True si se actualizó correctamente, False en caso contrario
    """
    barberManager = Connection()
    try:
        with barberManager.cursor() as cursor:
            sql = "UPDATE Cita SET estado = %s WHERE id_cita = %s"
            cursor.execute(sql, (estado, id_cita))
            barberManager.commit()
            return True
    except Exception as e:
        print(f"Error al actualizar estado de cita: {e}")
        barberManager.rollback()
        return False
    finally:
        barberManager.close()

def select_cita_by_id(id_cita: int):
    """
    Obtiene los detalles completos de una cita por su ID.
    Args:
        id_cita: ID de la cita a buscar.
    Returns:
        dict: Diccionario con los detalles de la cita o None si no se encuentra.
    """
    barberManager = Connection()
    try:
        with barberManager.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    C.id_cita,
                    U.nombre_usuario,
                    U.telefono_usuario, -- Incluir el teléfono del usuario
                    B.nombre_barbero,
                    S.nombre_servicio,
                    S.precio,
                    C.fecha,
                    C.hora_cita,
                    C.estado
                FROM Cita C
                JOIN Usuario U ON C.id_usuario = U.id_usuario
                JOIN Barbero B ON C.id_barbero = B.id_barbero
                JOIN Servicios S ON C.id_servicio = S.id_servicio
                WHERE C.id_cita = %s
            """, (id_cita,))
            resultado = cursor.fetchone()
            if resultado:
                # Mapear los resultados a un diccionario para facilitar el acceso
                cita_dict = {
                    'id_cita': resultado[0],
                    'cliente': resultado[1],
                    'telefono_cliente': resultado[2], # Teléfono del cliente
                    'barbero': resultado[3],
                    'servicio': resultado[4],
                    'precio': resultado[5],
                    'fecha': str(resultado[6]), # Convertir fecha a string
                    'hora': str(resultado[7]), # Convertir hora a string
                    'estado': resultado[8]
                }
                return cita_dict
            else:
                return None
    except Exception as e:
        print(f"Error al obtener cita por ID: {e}")
        return None
    finally:
        barberManager.close()
