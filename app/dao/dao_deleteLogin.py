from app.dao.dao import connect_database
from app.schemas.adm import Adm

def deleteLogin(id: int):

    connection, cursor = connect_database()

    query = f""" DELETE FROM adm_default WHERE id={id};
    """

    cursor.execute(query)
    connection.commit()

    if (connection.is_connected()):
        cursor.close()
        connection.close()

    return id