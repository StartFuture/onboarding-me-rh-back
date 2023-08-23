from app.dao.dao import connect_database
from app.schemas.employee import Employee, EmployeeUpdate, EmployeeUpdateLogin, EmployeeUpdateInfo

def createEmployee(employee: Employee):

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
    "{employee.address_id}"
    )
    """

    cursor.execute(query)
    connection.commit()

    if (connection.is_connected()):
        cursor.close()
        connection.close()

    return employee

def getAll():

    connection, cursor = connect_database()

    query = f"""SELECT * from Employee
    """

    cursor.execute(query)
    
    emplyee_list = cursor.fetchall()

    if (connection.is_connected()):
        cursor.close()
        connection.close()

    return emplyee_list

def getOne(id: int):

    connection, cursor = connect_database()

    query = f"""SELECT * from Employee
    WHERE id={id}
    """

    cursor.execute(query)
    
    employee_list = cursor.fetchall()

    if (connection.is_connected()):
        cursor.close()
        connection.close()

    return employee_list

def getEmployeeInfo(id: int):

    connection, cursor = connect_database()

    query = f"""SELECT CONCAT(e.first_name," ",e.surname) as full_name, 
    e.cpf, 
    e.employee_role, 
    e.birthdate, 
    e.email, 
    e.phone_number, 
    a.street, 
    a.zipcode, 
    a.city, 
    a.state
    FROM Employee e
    INNER JOIN Address a
    ON e.address_id = a.id
    WHERE e.id={id}
    """

    cursor.execute(query)
    
    employee_list = cursor.fetchall()

    if (connection.is_connected()):
        cursor.close()
        connection.close()

    return employee_list

def updateEmployee(id: int, employee: EmployeeUpdate):

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

def updateEmployeeLogin(id: int, employee: EmployeeUpdateLogin):

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

def updateEmployeeInfo(id: int, employee: EmployeeUpdateInfo):

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
    SET
    e.first_name="{employee.first_name}",
    e.surname="{employee.surname}",
    e.cpf="{cpf_tratado}",
    e.employee_role="{employee.employee_role}",
    e.birthdate="{employee.birthdate}",
    e.email="{employee.email}",
    e.phone_number="{phone_tratado}",
    a.street="{employee.street}",
    a.zipcode="{zipcode_tratado}",
    a.city="{employee.city}", 
    a.state="{employee.state}"
    WHERE e.id={id}
    """

    cursor.execute(query)
    connection.commit()

    if (connection.is_connected()):
        cursor.close()
        connection.close()

    return id, employee

def deleteEmployee(id: int):

    connection, cursor = connect_database()

    query = f"""DELETE FROM Employee WHERE id={id};
    """

    cursor.execute(query)
    connection.commit()

    if (connection.is_connected()):
        cursor.close()
        connection.close()

    return id

