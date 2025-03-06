from helpers.conection import *
from models.User_model import *
    

def new_user(name:str,email:str,password:str,)-> bool: 
    barberManager = Connection()


    with barberManager.cursor() as cursor:
        cursor.execute(f"SELECT COUNT(*) FROM Usuario WHERE Correo_electronico = {email}")
        res = cursor.fetchone()

    if res != (0,):
        return False
    

    with barberManager.cursor() as cursor:
        cursor.execute(f"INSERT INTO Usuario(nombre_usuario,correo_electronico,constraseña) VALUES (%s,%s,%s)",{name},{email},{password})

    barberManager.commit()
    barberManager.close()
    return True

def select_user_id(id:int):
    barberManager = Connection()

    with barberManager.cursor() as cursor:
        cursor.execute(f"SELECT nombre_usuario,correo_electronico,contraseña FROM Usuario WHERE id_usuario = {id}")
        user = cursor.fetchone()

    barberManager.close()
    return user


def select_user_all()->list:
    barberManager =Connection()

    users :list
    with barberManager.cursor() as cursor:
        cursor.execute("SELECT id_usuario,nombre_usuario,correo_electronico FROM Usuario WHERE estado = 'ACTIVO'")
        users = cursor.fetchall()

    barberManager.close()
    return users


