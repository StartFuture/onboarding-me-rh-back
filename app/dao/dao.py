import mysql.connector

from app.parameters import HOST, USERNAME, PASSWORD, DATABASE, PORT

def connect_database(host = HOST, user = USERNAME, password = PASSWORD, database = DATABASE, port = PORT):
    connection = mysql.connector.connect(
        host = host,
        port = port,
        user = user,
        password = password,
        database = database
    )
    cursor = connection.cursor(dictionary=True)

    return connection, cursor