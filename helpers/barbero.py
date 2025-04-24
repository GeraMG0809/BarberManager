from helpers.conection import * 
from models.barbero_model import *
from mysql.connector import Error

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

    barberos = []
    with barberManager.cursor() as cursor:
        cursor.execute("SELECT * FROM Barbero WHERE estado = 'ACTIVO'")
        resultados = cursor.fetchall()

        for barb in resultados:
            barberos.append(Barbero(barb).to_dict())

    barberManager.close()
    return barberos


def insert_barbero(nombre, telefono, nombre_imagen):
    conexion = Connection()
    
    try:
        with conexion.cursor() as cursor:
            sql = "INSERT INTO Barbero (nombre_barbero, telefono, imagenes) VALUES (%s, %s, %s)"
            valores = (nombre, telefono, nombre_imagen)
            cursor.execute(sql, valores)
            conexion.commit()
    finally:
        conexion.close()