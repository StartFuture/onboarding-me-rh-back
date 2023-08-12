from app.dao.dao import connect_database

def getAll():

    connection, cursor = connect_database()

    query = f"""SELECT * from adm_default
    """

    cursor.execute(query)
    
    adm_list = cursor.fetchall()

    if (connection.is_connected()):
        cursor.close()
        connection.close()

    return adm_list

def getOne(id: int):

    connection, cursor = connect_database()

    query = f"""SELECT * from adm_default
    WHERE id={id}
    """

    cursor.execute(query)
    
    adm_list = cursor.fetchall()

    if (connection.is_connected()):
        cursor.close()
        connection.close()

    return adm_list