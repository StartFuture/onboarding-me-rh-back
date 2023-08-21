
from app.dao.dao import connect_database
from app.schemas.welcome_kit_item import WelcomeKitItem

def createWelcomeKitItem(welcome_kit_item: WelcomeKitItem):

    connection, cursor = connect_database()

    query = f""" INSERT into WelcomeKitItem(name, image)
    VALUES ("{welcome_kit_item.name}",
    "{welcome_kit_item.image}"
    )
    """

    cursor.execute(query)
    connection.commit()

    if (connection.is_connected()):
        cursor.close()
        connection.close()

    return welcome_kit_item

def getAll():

    connection, cursor = connect_database()

    query = f"""SELECT * from WelcomeKitItem
    """

    cursor.execute(query)
    
    welcome_kit_item_list = cursor.fetchall()

    if (connection.is_connected()):
        cursor.close()
        connection.close()

    return welcome_kit_item_list

def getOne(id: int):

    connection, cursor = connect_database()

    query = f"""SELECT * from WelcomeKitItem
    WHERE id={id}
    """

    cursor.execute(query)
    
    welcome_kit_item_list = cursor.fetchall()

    if (connection.is_connected()):
        cursor.close()
        connection.close()

    return welcome_kit_item_list

def updateWelcomeKitItem(id: int, welcome_kit_item: WelcomeKitItem):

    connection, cursor = connect_database()

    query = f"""UPDATE WelcomeKitItem
    SET name="{welcome_kit_item.name}",
    image="{welcome_kit_item.image}"
    WHERE id={id}
    """

    cursor.execute(query)
    connection.commit()

    if (connection.is_connected()):
        cursor.close()
        connection.close()

    return id, welcome_kit_item

def deleteWelcomeKitItem(id: int):

    connection, cursor = connect_database()

    query = f"""DELETE FROM WelcomeKitItem WHERE id={id};
    """

    cursor.execute(query)
    connection.commit()

    if (connection.is_connected()):
        cursor.close()
        connection.close()

    return id

