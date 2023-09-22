
from app.dao.dao import connect_database
from mysql.connector import Error

def createWelcomeKit_WKItem(welcome_kit_id, item_id):

    try:
        connection, cursor = connect_database()

        query = f""" INSERT into WelcomeKit_WelcomeKitItem(welcome_kit_id, item_id)
        VALUES ("{welcome_kit_id}",
        "{item_id}"
        )
        """

        cursor.execute(query)
        connection.commit()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return {welcome_kit_id, item_id}
    
    except Error as erro:
        return {"Error: {}".format(erro)}