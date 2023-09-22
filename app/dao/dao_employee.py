from app.dao.dao import connect_database
from app.schemas.employee import Employee, EmployeeUpdate, EmployeeUpdateLogin, EmployeeUpdateInfo
from mysql.connector import Error

def createEmployee(employee: Employee, address_id):

    try:
        connection, cursor = connect_database()

        cpf = employee.cpf
        cpf_tratado = cpf.replace(".","").replace("-","")

        phone = employee.phone_number
        phone_tratado = phone.replace("+","").replace("(", "").replace(")","").replace("-","")

        query = f""" INSERT into Employee(first_name, surname, birthdate, employee_role, email, employee_password, phone_number, cpf, level_access, company_id, address_id)
        VALUES ("{employee.first_name}",
        "{employee.surname}",
        "{employee.birthdate}",
        "{employee.employee_role}",
        "{employee.email}",
        "{employee.employee_password}",
        "{phone_tratado}",
        "{cpf_tratado}",
        "{employee.level_access}",
        "{employee.company_id}",
        "{address_id}"
        )
        """
        cursor.execute(query)
        connection.commit()

        query = f"""SELECT LAST_INSERT_ID() as employee_id FROM Employee
        """

        cursor.execute(query)

        employee_id = cursor.fetchone()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return employee_id
    
    except Error as erro:
        return {"Error: {}".format(erro)}

def getAll():

    try:
        connection, cursor = connect_database()

        query = f"""SELECT id, first_name, surname, birthdate, employee_role, email, employee_password, phone_number, cpf, level_access, company_id, address_id from Employee
        """

        cursor.execute(query)
        
        emplyee_list = cursor.fetchall()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return emplyee_list
    
    except Error as erro:
        return {"Error: {}".format(erro)}
    
def getAllWithTracking():

    try:
        connection, cursor = connect_database()

        query = f"""SELECT 
        e.id, 
        e.first_name, 
        e.surname, 
        e.birthdate, 
        e.employee_role, 
        e.email, 
        e.phone_number, 
        e.cpf, 
        e.company_id, 
        e.address_id,
        t.id as tracking_id,
        t.tracking_code,
        t.status,
        t.employee_id,
        t.welcome_kit_id
        from Employee e, Tracking t
        where e.id = t.employee_id
        """

        cursor.execute(query)
        
        emplyee_list = cursor.fetchall()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return emplyee_list
    
    except Error as erro:
        return {"Error: {}".format(erro)}

def getAllPaginated(page: int):
    page = page -1
    offset: int = page*10

    connection, cursor = connect_database()

    query = f"""SELECT * FROM Employee
                LIMIT 10 OFFSET {offset};
    """

    cursor.execute(query)
    
    emplyee_list = cursor.fetchall()

    if (connection.is_connected()):
        cursor.close()
        connection.close()

    return emplyee_list

def getOne(id: int):
        
    try:
        connection, cursor = connect_database()

        query = f"""SELECT id, first_name, surname, birthdate, employee_role, email, employee_password, phone_number, cpf, level_access, company_id, address_id from Employee
        WHERE id={id}
        """

        cursor.execute(query)
        
        employee_list = cursor.fetchall()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return employee_list
    
    except Error as erro:
        return {"Error: {}".format(erro)}

def getEmployeeInfo(id: int):

    try:

        connection, cursor = connect_database()

        query = f"""SELECT CONCAT(e.first_name," ",e.surname) as full_name, 
        e.cpf, 
        e.birthdate, 
        e.employee_role, 
        e.email, 
        e.phone_number, 
        a.zipcode, 
        a.state,
        a.city, 
        a.street,
        a.num,
        a.complement,
        t.welcome_kit_id,
        t.status,
        t.tracking_code
        FROM Employee e
        INNER JOIN Address a
        ON e.address_id = a.id
        INNER JOIN Tracking t
        ON e.id = t.employee_id
        WHERE e.id={id}
        """

        cursor.execute(query)
        
        employee_list = cursor.fetchall()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return employee_list
    
    except Error as erro:
        return {"Error: {}".format(erro)}

def getAllEmployeeInfo():
        
    try:
        connection, cursor = connect_database()

        query = f"""SELECT CONCAT(e.first_name," ",e.surname) as full_name, 
        e.cpf, 
        e.birthdate, 
        e.employee_role, 
        e.email, 
        e.phone_number, 
        a.zipcode, 
        a.state,
        a.city, 
        a.street,
        a.num,
        a.complement,
        t.welcome_kit_id,
        t.status,
        t.tracking_code
        FROM Employee e
        INNER JOIN Address a
        ON e.address_id = a.id
        INNER JOIN Tracking t
        ON e.id = t.employee_id
        """

        cursor.execute(query)
        
        employee_list = cursor.fetchall()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return employee_list
    
    except Error as erro:
        return {"Error: {}".format(erro)}

def getByNameOrCPF(name: str = None, surname: str = None, cpf: str = None):

    connection, cursor = connect_database()

    if name != None and surname != None:
        query = f"""SELECT * from Employee
        WHERE Employee.first_name = '{name}' and Employee.surname = '{surname}';
        """

    if cpf != None:
        query = f"""SELECT * from Employee
        WHERE cpf={cpf}
        """
    cursor.execute(query)
    
    employee_list = cursor.fetchall()

    if (connection.is_connected()):
        cursor.close()
        connection.close()

    return employee_list

def getAllOderByCpfOrNamePaginated(page: int, cpf: bool = False, name: bool = False):
    page = page -1
    offset: int = page*10

    connection, cursor = connect_database()

    if cpf == True:
        query = f"""SELECT * FROM Employee ORDER BY cpf
                    LIMIT 10 OFFSET {offset};
        """

    if name == True:
        query = f"""SELECT * FROM Employee ORDER BY first_name
                    LIMIT 10 OFFSET {offset};
        """

    cursor.execute(query)
    
    emplyee_list = cursor.fetchall()

    if (connection.is_connected()):
        cursor.close()
        connection.close()

    return emplyee_list


def updateEmployee(id: int, employee: EmployeeUpdate):

    try:
        connection, cursor = connect_database()

        cpf = employee.cpf
        cpf_tratado = cpf.replace(".","").replace("-","")

        phone = employee.phone_number
        phone_tratado = phone.replace("+","").replace("(", "").replace(")","").replace("-","")

        query = f"""UPDATE Employee
        SET first_name="{employee.first_name}",
        surname="{employee.surname}",
        birthdate="{employee.birthdate}",
        employee_role="{employee.employee_role}",
        email="{employee.email}",
        employee_password="{employee.employee_password}",
        phone_number="{phone_tratado}",
        cpf="{cpf_tratado}",
        level_access="{employee.level_access}",
        company_id={employee.company_id},
        address_id={employee.address_id}
        WHERE id={id}
        """

        cursor.execute(query)
        connection.commit()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return id, employee
    
    except Error as erro:
        return {"Error: {}".format(erro)}

def updateEmployeeLogin(id: int, employee: EmployeeUpdateLogin):

    try:
        connection, cursor = connect_database()

        query = f"""UPDATE Employee
        SET
        email="{employee.email}",
        employee_password="{employee.employee_password}"
        WHERE id={id}
        """

        cursor.execute(query)
        connection.commit()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return id, employee
    
    except Error as erro:
        return {"Error: {}".format(erro)}

def updateEmployeeInfo(id: int, employee: EmployeeUpdateInfo):

    try:
        connection, cursor = connect_database()

        cpf = employee.cpf
        cpf_tratado = cpf.replace(".","").replace("-","")

        phone = employee.phone_number
        phone_tratado = phone.replace("+","").replace("(", "").replace(")","").replace("-","")

        zipcode = employee.zipcode
        zipcode_tratado = zipcode.replace("-","")

        query = f"""UPDATE Employee e
        INNER JOIN Address a
        ON e.address_id = a.id
        INNER JOIN Tracking t
        ON e.id = t.employee_id
        SET
        e.first_name="{employee.first_name}",
        e.surname="{employee.surname}",
        e.cpf="{cpf_tratado}",
        e.birthdate="{employee.birthdate}",
        e.employee_role="{employee.employee_role}",
        e.email="{employee.email}",
        e.phone_number="{phone_tratado}",
        a.zipcode="{zipcode_tratado}",
        a.state="{employee.state}",
        a.city="{employee.city}", 
        a.street="{employee.street}",
        a.num="{employee.num}",
        a.complement="{employee.complement}",
        t.tracking_code="{employee.tracking_code}",
        t.status="{employee.status}"
        WHERE e.id={id}
        """

        cursor.execute(query)
        connection.commit()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return id, employee
    
    except Error as erro:
        return {"Error: {}".format(erro)}

def deleteEmployee(id: int):

    try:
        connection, cursor = connect_database()

        query = f"""DELETE FROM Employee WHERE id={id};
        """

        cursor.execute(query)
        connection.commit()

        if (connection.is_connected()):
            cursor.close()
            connection.close()

        return id
    
    except Error as erro:
        return {"Error: {}".format(erro)}

