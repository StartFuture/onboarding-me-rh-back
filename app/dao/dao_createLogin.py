from app.dao.dao import connect_database
from app.schemas.adm import Adm

def createLogin(id: int, adm: Adm):

    connection, cursor = connect_database()

    query = f""" INSERT into adm_default(id, email, password)
    VALUES ({id}, "{adm.email}", "{adm.password}")
    """

    cursor.execute(query)
    connection.commit()

    if (connection.is_connected()):
        cursor.close()
        connection.close()

    return id, adm