from app.dao.dao import connect_database
from app.schemas.admin import Adm, UpdateAdm

def createLogin(adm: Adm):

    connection, cursor = connect_database()

    query = f""" INSERT into adm_default(email, password)
    VALUES ("{adm.email}", "{adm.password}")
    """

    cursor.execute(query)
    connection.commit()

    if (connection.is_connected()):
        cursor.close()
        connection.close()

    return adm

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

def updateLogin(id: int, adm: UpdateAdm):

    connection, cursor = connect_database()

    query = f"""UPDATE adm_default
    SET email="{adm.email}", password="{adm.password}" 
    WHERE id={id}
    """

    cursor.execute(query)
    connection.commit()

    if (connection.is_connected()):
        cursor.close()
        connection.close()

    return id, adm

def deleteLogin(id: int):

    connection, cursor = connect_database()

    query = f"""DELETE FROM adm_default WHERE id={id};
    """

    cursor.execute(query)
    connection.commit()

    if (connection.is_connected()):
        cursor.close()
        connection.close()

    return id

