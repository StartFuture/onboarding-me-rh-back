from app.dao.dao import connect_database

def createLogin(id: int):

    connection, cursor = connect_database()

    query = f"""

    """

#     INSERT into Company (company_name, trading_name, cnpj, email, company_password)
# VALUES ('teste', 'teste2', '12345678901234', 'teste@teste.com', 'teste')
# ;

    cursor.execute(query)

    # adm_list = cursor.fetchone()

    connection.close()

    # return adm_list