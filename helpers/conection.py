import pymysql
import os
from dotenv import load_dotenv

<<<<<<< HEAD
def Connection()-> pymysql.connections.Connection:
    return pymysql.connect(host="localhost", user='root', password='Gerardojr0809+', db='barberManager')
=======
load_dotenv()


def Connection():
    return pymysql.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        db=os.getenv('DB_NAME'),
        #auth_plugin='mysql_native_password' # Mantener si es necesario para tu configuración MySQL
    )
>>>>>>> 0ac6a7a595adb0b486dc117035bfbae8994ed256
