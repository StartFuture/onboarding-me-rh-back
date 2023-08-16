from app.dao.dao import connect_database
from app.schemas.company import Company, CompanyUpdate

def createCompany(company: Company):

    connection, cursor = connect_database()

    cnpj = company.cnpj
    cnpj_tratado = cnpj.replace(".", "").replace("/","").replace("-","")

    query = f""" INSERT into Company(company_name, trading_name, logo, cnpj, email, company_password, state_register)
    VALUES ("{company.company_name}",
    "{company.trading_name}",
    "{company.logo}",
    "{cnpj_tratado}",
    "{company.email}",
    "{company.company_password}",
    "{company.state_register}"
    )
    """

    cursor.execute(query)
    connection.commit()

    if (connection.is_connected()):
        cursor.close()
        connection.close()

    return company

def getAll():

    connection, cursor = connect_database()

    query = f"""SELECT * from Company
    """

    cursor.execute(query)
    
    company_list = cursor.fetchall()

    if (connection.is_connected()):
        cursor.close()
        connection.close()

    return company_list

def getOne(id: int):

    connection, cursor = connect_database()

    query = f"""SELECT * from Company
    WHERE id={id}
    """

    cursor.execute(query)
    
    company_list = cursor.fetchall()

    if (connection.is_connected()):
        cursor.close()
        connection.close()

    return company_list

def updateCompany(id: int, company: CompanyUpdate):

    connection, cursor = connect_database()

    query = f"""UPDATE Company
    SET company_name="{company.company_name}",
    trading_name="{company.trading_name}",
    logo={company.logo},
    cnpj="{company.cnpj}",
    email="{company.email}",
    company_password="{company.company_password}",
    state_register="{company.state_register}" 
    WHERE id={id}
    """

    cursor.execute(query)
    connection.commit()

    if (connection.is_connected()):
        cursor.close()
        connection.close()

    return id, company

def deleteCompany(id: int):

    connection, cursor = connect_database()

    query = f"""DELETE FROM Company WHERE id={id};
    """

    cursor.execute(query)
    connection.commit()

    if (connection.is_connected()):
        cursor.close()
        connection.close()

    return id

