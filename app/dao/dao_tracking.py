
from app.dao.dao import connect_database
from app.schemas.tracking import Tracking, TrackingUpdate
from mysql.connector import Error

def createTracking(tracking: Tracking, employee_id):

    try:
        connection, cursor = connect_database()

        query = f""" INSERT into Tracking(tracking_code, status, employee_id, welcome_kit_id)
        VALUES ("{tracking.tracking_code}",
        "{tracking.status}",
        "{employee_id}",
        "{tracking.welcome_kit_id}"
        )
        """

        cursor.execute(query)
        connection.commit()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return tracking
    
    except Error as erro:
        return {"Error: {}".format(erro)}
    
def getAll():

    try:
        connection, cursor = connect_database()

        query = f"""SELECT id, tracking_code, status, employee_id, welcome_kit_id from Tracking
        """

        cursor.execute(query)
        
        tracking_list = cursor.fetchall()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return tracking_list
    
    except Error as erro:
        return {"Error: {}".format(erro)}

def getOne(id: int):

    try:
        connection, cursor = connect_database()

        query = f"""SELECT id, tracking_code, status, employee_id, welcome_kit_id from Tracking
        WHERE id={id}
        """

        cursor.execute(query)
        
        tracking_list = cursor.fetchall()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return tracking_list
    
    except Error as erro:
        return {"Error: {}".format(erro)}
    
def getOnebyEmployee(id: int):

    try:
        connection, cursor = connect_database()

        query = f"""SELECT id, tracking_code, status, employee_id, welcome_kit_id from Tracking
        WHERE employee_id={id}
        """

        cursor.execute(query)
        
        tracking_list = cursor.fetchall()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return tracking_list
    
    except Error as erro:
        return {"Error: {}".format(erro)}

def updateTracking(id: int, tracking: TrackingUpdate):

    try:
        connection, cursor = connect_database()

        query = f"""UPDATE Tracking
        SET tracking_code="{tracking.tracking_code}",
        status="{tracking.status}"
        WHERE id={id}
        """

        cursor.execute(query)
        connection.commit()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return id, tracking
    
    except Error as erro:
        return {"Error: {}".format(erro)}

def deleteTracking(id: int):

    try:
        connection, cursor = connect_database()

        query = f"""DELETE FROM Tracking WHERE id={id};
        """

        cursor.execute(query)
        connection.commit()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return id
    
    except Error as erro:
        return {"Error: {}".format(erro)}