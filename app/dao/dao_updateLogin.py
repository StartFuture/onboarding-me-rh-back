from app.dao.dao import connect_database
from app.schemas.adm import UpdateAdm

def updateLogin(id: int, adm: UpdateAdm):

    connection, cursor = connect_database()

    query = f""" UPDATE adm_default
    SET email="{adm.email}", password="{adm.password}" 
    WHERE id={id}
    """

    cursor.execute(query)
    connection.commit()

    if (connection.is_connected()):
        cursor.close()
        connection.close()

    return id, adm