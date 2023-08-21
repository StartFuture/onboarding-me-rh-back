
from app.dao.dao import connect_database
from app.schemas.welcome_kit import WelcomeKit

def createWelcomeKit(welcome_kit: WelcomeKit):

    connection, cursor = connect_database()

    query = f""" INSERT into WelcomeKit(name, image)
    VALUES ("{welcome_kit.name}",
    "{welcome_kit.image}"
    )
    """

    cursor.execute(query)
    connection.commit()

    if (connection.is_connected()):
        cursor.close()
        connection.close()

    return welcome_kit

def getAll():

    connection, cursor = connect_database()

    query = f"""SELECT * from WelcomeKit
    """

    cursor.execute(query)
    
    welcome_kit_list = cursor.fetchall()

    if (connection.is_connected()):
        cursor.close()
        connection.close()

    return welcome_kit_list

def getOne(id: int):

    connection, cursor = connect_database()

    query = f"""SELECT * from WelcomeKit
    WHERE id={id}
    """

    cursor.execute(query)
    
    welcome_kit_list = cursor.fetchall()

    if (connection.is_connected()):
        cursor.close()
        connection.close()

    return welcome_kit_list

def updateWelcomeKit(id: int, welcome_kit: WelcomeKit):

    connection, cursor = connect_database()

    query = f"""UPDATE WelcomeKit
    SET name="{welcome_kit.name}",
    image="{welcome_kit.image}"
    WHERE id={id}
    """

    cursor.execute(query)
    connection.commit()

    if (connection.is_connected()):
        cursor.close()
        connection.close()

    return id, welcome_kit

def deleteWelcomeKit(id: int):

    connection, cursor = connect_database()

    query = f"""DELETE FROM WelcomeKit WHERE id={id};
    """

    cursor.execute(query)
    connection.commit()

    if (connection.is_connected()):
        cursor.close()
        connection.close()

    return id

