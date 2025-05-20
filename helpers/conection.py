import pymysql
import os
from dotenv import load_dotenv


load_dotenv()


def Connection():
    return pymysql.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        db=os.getenv('DB_NAME'),
        #auth_plugin='mysql_native_password' # Mantener si es necesario para tu configuración MySQL
    )