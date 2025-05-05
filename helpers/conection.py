import pymysql

def Connection()-> pymysql.connections.Connection:
    return pymysql.connect(host="localhost", user='root',password='Gerardojr0809+',db='barberManager')