
from app.dao.dao import connect_database
from app.schemas.welcome_kit_item import WelcomeKitItem
from mysql.connector import Error

def createWelcomeKitItem(welcome_kit_item: WelcomeKitItem):

    try:
        connection, cursor = connect_database()

        query = f""" INSERT into WelcomeKitItem(name, image)
        VALUES (%s, %s)
        """

        cursor.execute(query, (welcome_kit_item.name, welcome_kit_item.image))
        connection.commit()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return welcome_kit_item
    
    except Error as erro:
        return {"Error: {}".format(erro)}

def getAll():

    try:
        connection, cursor = connect_database()

        query = f"""SELECT id, name, image from WelcomeKitItem
        """

        cursor.execute(query)
        
        welcome_kit_item_list = cursor.fetchall()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return welcome_kit_item_list
    
    except Error as erro:
        return {"Error: {}".format(erro)}

def getOne(id: int):

    try:
        connection, cursor = connect_database()

        query = f"""SELECT id, name, image from WelcomeKitItem
        WHERE id={id}
        """

        cursor.execute(query)
        
        welcome_kit_item_list = cursor.fetchall()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return welcome_kit_item_list
    
    except Error as erro:
        return {"Error: {}".format(erro)}

def updateWelcomeKitItem(id: int, welcome_kit_item: WelcomeKitItem):

    try:
        connection, cursor = connect_database()

        query = f""" UPDATE WelcomeKitItem
        SET name="%s",
        image="%s"
        WHERE id=%s
        """

        cursor.execute(query, (welcome_kit_item.name, welcome_kit_item.image, id))
        connection.commit()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return id, welcome_kit_item
    
    except Error as erro:
        return {"Error: {}".format(erro)}

def deleteWelcomeKitItem(id: int):

    try:
        connection, cursor = connect_database()

        query = f"""DELETE FROM WelcomeKitItem WHERE id={id};
        """

        cursor.execute(query)
        connection.commit()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return id
    
    except Error as erro:
        return {"Error: {}".format(erro)}

