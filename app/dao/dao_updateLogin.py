from app.dao.dao import connect_database

def updateLogin(id: int):

    connection, cursor = connect_database()

    query = f"""

    """

# UPDATE Company
# SET email = 'teste3@teste.com'
# WHERE id=1
# ;

    cursor.execute(query)

    # adm_list = cursor.fetchall()

    connection.close()

    # return adm_list