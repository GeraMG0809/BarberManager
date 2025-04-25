import pymysql

def Connection()-> pymysql.connections.Connection:
    return pymysql.connect(host="localhost", user='root',password='gerardojr0809',db='barberManager')
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()  # Cargar variables del archivo .env

def Connection() -> pymysql.connections.Connection:
    return pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        db=os.getenv("DB_NAME")
    )
