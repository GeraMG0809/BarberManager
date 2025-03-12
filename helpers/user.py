from helpers.conection import *
from models.User_model import *
    

def new_user(name: str, telefono: str, email: str, password: str) -> bool: 
    barberManager = Connection()  # Suponiendo que esta función devuelve una conexión válida con pymysql

    with barberManager.cursor() as cursor:
        cursor.execute("SELECT * FROM Usuario WHERE correo_electronico = %s", (email,))
        res = cursor.fetchone()

    if res is not None:  # Si el usuario ya existe
        return False
    
    with barberManager.cursor() as cursor:
        cursor.execute(
            "INSERT INTO Usuario (nombre_usuario, telefono_usuario, correo_electronico, contraseña) VALUES (%s, %s, %s, %s)",
            (name, telefono, email, password)  # 👈 Pasar los valores como una tupla
        )

    barberManager.commit()  # Guardar los cambios
    barberManager.close()  # Cerrar la conexión
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


