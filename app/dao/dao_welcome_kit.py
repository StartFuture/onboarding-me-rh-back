
from app.dao.dao import connect_database
from app.schemas.welcome_kit import WelcomeKit
from mysql.connector import Error

def createWelcomeKit(welcome_kit: WelcomeKit):

    try:
        connection, cursor = connect_database()

        query = f""" INSERT into WelcomeKit(name, image)
        VALUES (%s, %s)
        """

        cursor.execute(query, (welcome_kit.name, welcome_kit.image))

        connection.commit()

        query = f"""SELECT LAST_INSERT_ID() as id FROM WelcomeKit
        """

        cursor.execute(query)

        wk_id = cursor.fetchone()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return wk_id

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
        
        query = f""" SELECT
        wk.id as wk_id, 
        wk.name as wk_name, 
        wk.image as wk_image
        FROM WelcomeKit wk
        WHERE wk.id={id}
        """

        cursor.execute(query)
        welcome_kit = cursor.fetchone()

        query = f"""SELECT 
        i.id,
        i.name,
        i.image
        FROM WelcomeKit wk
        INNER JOIN WelcomeKit_WelcomeKitItem link
        ON wk.id = link.welcome_kit_id
        INNER JOIN WelcomeKitItem i
        ON i.id = link.item_id
        WHERE wk.id={id}
        """

        cursor.execute(query)
        
        welcome_kit["wk_items"] = cursor.fetchall()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return welcome_kit
    
    except Error as erro:
        return {"Error: {}".format(erro)}

def updateWelcomeKit(id: int, welcome_kit: WelcomeKit):

    try:
        connection, cursor = connect_database()

        query = f""" UPDATE WelcomeKit
        SET name="%s",
        image="%s"
        WHERE id=%s
        """

        cursor.execute(query, (welcome_kit.name, welcome_kit.image, id))

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
    

def getAllPaginated(page: int):

    try:
        limit: int = 6
        page = page -1
        offset: int = page*limit

        connection, cursor = connect_database()

        query = f"""SELECT id, name, image FROM WelcomeKit
                    LIMIT {limit} OFFSET {offset};
        """

        cursor.execute(query)
        
        emplyee_list = cursor.fetchall()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return emplyee_list
    
    except Error as erro:
        return {"Error: {}".format(erro)}
    
def getWkByName(name: str = None):

    try:
        connection, cursor = connect_database()

        if name != None:
            query = f"""SELECT id, name, image FROM WelcomeKit
            WHERE WelcomeKit.name = '{name}';
            """

        cursor.execute(query)
        
        welcome_kit_list = cursor.fetchall()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return welcome_kit_list
    
    except Error as erro:
        return {"Error: {}".format(erro)}