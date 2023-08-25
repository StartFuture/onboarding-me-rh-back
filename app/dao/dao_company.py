from app.dao.dao import connect_database
from app.schemas.company import Company, CompanyUpdate, CompanyUpdateLogin
from mysql.connector import Error

def createCompany(company: Company):

    try:
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
    
    except Error as erro:
        return {"Error: {}".format(erro)}

def getAll():

    try: 
        connection, cursor = connect_database()

        query = f"""SELECT id, company_name, trading_name, logo, cnpj, email, company_password, state_register from Company
        """

        cursor.execute(query)
        
        company_list = cursor.fetchall()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return company_list
    
    except Error as erro:
        return {"Error: {}".format(erro)}

def getOne(id: int):
    try:

        connection, cursor = connect_database()

        query = f"""SELECT id, company_name, trading_name, logo, cnpj, email, company_password, state_register from Company
        WHERE id={id}
        """

        cursor.execute(query)
        
        company_list = cursor.fetchall()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return company_list
    
    except Error as erro:
        return {"Error: {}".format(erro)}

def updateCompany(id: int, company: CompanyUpdate):

    try:
        connection, cursor = connect_database()

        cnpj = company.cnpj
        cnpj_tratado = cnpj.replace(".", "").replace("/","").replace("-","")

        query = f"""UPDATE Company
        SET company_name="{company.company_name}",
        trading_name="{company.trading_name}",
        logo={company.logo},
        cnpj="{cnpj_tratado}",
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
    
    except Error as erro:
        return {"Error: {}".format(erro)}

def updateCompanyLogin(id: int, company: CompanyUpdateLogin):

    try:
        connection, cursor = connect_database()

        query = f"""UPDATE Company
        SET
        email="{company.email}",
        company_password="{company.company_password}"
        WHERE id={id}
        """

        print(query)

        cursor.execute(query)
        connection.commit()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return id, company
    
    except Error as erro:
        return {"Error: {}".format(erro)}

def deleteCompany(id: int):

    try:
        connection, cursor = connect_database()

        query = f"""DELETE FROM Company WHERE id={id};
        """

        cursor.execute(query)
        connection.commit()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return id
    
    except Error as erro:
        return {"Error: {}".format(erro)}

