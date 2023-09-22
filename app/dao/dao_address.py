from app.dao.dao import connect_database
from app.schemas.address import Address, AddressUpdate
from mysql.connector import Error

def createAddress(address: Address):
    try:
        connection, cursor = connect_database()

        zipcode = address.zipcode
        zipcode_tratado = zipcode.replace("-","")

        query = f""" INSERT into Address(num, complement, zipcode, street, district, city, state)
        VALUES ("{address.num}",
        "{address.complement}",
        "{zipcode_tratado}",
        "{address.street}",
        "{address.district}",
        "{address.city}",
        "{address.state}"
        )
        """

        cursor.execute(query)
        connection.commit()

        query = f"""SELECT LAST_INSERT_ID() as address_id FROM Address
        """

        cursor.execute(query)

        address_id = cursor.fetchone()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return address_id
    
    except Error as erro:
        return {"Error: {}".format(erro)}

def getAll():

    try:
        connection, cursor = connect_database()

        query = f"""SELECT id, num, complement, zipcode, street, district, city, state from Address
        """

        cursor.execute(query)
        
        address_list = cursor.fetchall()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return address_list
    
    except Error as erro:
        return {"Error: {}".format(erro)}

def getOne(id: int):

    try: 
        connection, cursor = connect_database()

        query = f"""SELECT id, num, complement, zipcode, street, district, city, state from Address
        WHERE id={id}
        """

        cursor.execute(query)
        
        address_list = cursor.fetchall()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return address_list

    except Error as erro:
        return {"Error: {}".format(erro)}

def updateAddress(id: int, address: AddressUpdate):

    try:
        connection, cursor = connect_database()

        zipcode = address.zipcode
        zipcode_tratado = zipcode.replace("-","")

        query = f"""UPDATE Address
        SET num="{address.num}",
        complement="{address.complement}",
        zipcode="{zipcode_tratado}",
        street="{address.street}",
        district="{address.district}",
        city="{address.city}",
        state="{address.state}"
        WHERE id={id}
        """

        cursor.execute(query)
        connection.commit()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return id, address

    except Error as erro:
        return {"Error: {}".format(erro)}
    
def deleteAddress(id: int):

    try:
        connection, cursor = connect_database()

        query = f"""DELETE FROM Address WHERE id={id};
        """

        cursor.execute(query)
        connection.commit()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return id
    
    except Error as erro:
        return {"Error: {}".format(erro)}