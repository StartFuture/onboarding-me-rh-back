from app.dao.dao import connect_database
from app.schemas.employee import Employee, EmployeeUpdate, EmployeeUpdateLogin

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
    print(query)

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

    print(query)

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

