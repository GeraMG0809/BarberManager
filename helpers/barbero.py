from helpers.conection import * 

def select_barbero(name:str):
    barberManager = Connection()

    with barberManager.cursor() as cursor:
        cursor.execute(f"SELECT * FROM Barbero WHERE nombre_barbero = {name}")
        barber = cursor.fecthone()

    barberManager.close()
    return barber

def select_barbero_id(nombre_barbero):
    barberManager = Connection()
    with barberManager.cursor() as cursor:
        cursor.execute("SELECT id_barbero FROM Barbero WHERE nombre_barbero = %s", (nombre_barbero,))
        resultado = cursor.fetchone()
    barberManager.close()
    
    return resultado[0] if resultado else None


def select_barbers():
    barberManager = Connection()

    barberos = list
    with barberManager.cursor() as cursor:
        cursor.execute("SELECT * FROM Barbero WHERE estado = 'ACTIVO'")
        barberos = cursor.fetchall()

    barberManager.close()
    return barberos

