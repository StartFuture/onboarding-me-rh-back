
from app.dao.dao import connect_database
from app.schemas.welcome_kit import WelcomeKit
from mysql.connector import Error

def createWelcomeKit(welcome_kit: WelcomeKit):

    try:
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

    except Error as erro:
        return {"Error: {}".format(erro)}

def getAll():

    try:
        connection, cursor = connect_database()

        query = f"""SELECT id, name, image from WelcomeKit
        """

        cursor.execute(query)
        
        welcome_kit_list = cursor.fetchall()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return welcome_kit_list
    
    except Error as erro:
        return {"Error: {}".format(erro)}

def getOne(id: int):

    try:
        connection, cursor = connect_database()

        query = f"""SELECT id, name, image from WelcomeKit
        WHERE id={id}
        """

        cursor.execute(query)
        
        welcome_kit_list = cursor.fetchall()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return welcome_kit_list
    
    except Error as erro:
        return {"Error: {}".format(erro)}

def updateWelcomeKit(id: int, welcome_kit: WelcomeKit):

    try:
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
    
    except Error as erro:
        return {"Error: {}".format(erro)}

def deleteWelcomeKit(id: int):

    try:
        connection, cursor = connect_database()

        query = f"""DELETE FROM WelcomeKit WHERE id={id};
        """

        cursor.execute(query)
        connection.commit()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return id
    
    except Error as erro:
        return {"Error: {}".format(erro)}