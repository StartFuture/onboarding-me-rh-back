
from app.dao.dao import connect_database
from app.schemas.address import Address, AddressUpdate

def createAddress(address: Address):

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

    if (connection.is_connected()):
        cursor.close()
        connection.close()

    return address

def getAll():

    connection, cursor = connect_database()

    query = f"""SELECT * from Address
    """

    cursor.execute(query)
    
    address_list = cursor.fetchall()

    if (connection.is_connected()):
        cursor.close()
        connection.close()

    return address_list

def getOne(id: int):

    connection, cursor = connect_database()

    query = f"""SELECT * from Address
    WHERE id={id}
    """

    cursor.execute(query)
    
    address_list = cursor.fetchall()

    if (connection.is_connected()):
        cursor.close()
        connection.close()

    return address_list

def updateAddress(id: int, address: AddressUpdate):

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

def deleteAddress(id: int):

    connection, cursor = connect_database()

    query = f"""DELETE FROM Address WHERE id={id};
    """

    cursor.execute(query)
    connection.commit()

    if (connection.is_connected()):
        cursor.close()
        connection.close()

    return id