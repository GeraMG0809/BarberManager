import pymysql

def Connection()-> pymysql.connections.Connection:
    return pymysql.connect(
        host="localhost",
        user='root',
        password='1234',
        db='barbermanager'
    )