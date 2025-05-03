import pymysql

def Connection():
    return pymysql.connect(
        host="db",                # Nombre del servicio de MySQL en docker-compose
        user="root",
        password="gerardojr0809",
        db="barberManager"
    )
