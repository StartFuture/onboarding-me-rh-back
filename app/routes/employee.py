from fastapi import APIRouter, status, HTTPException, Path
from app.dao.dao_employee import createEmployee, getAll, getOne, updateEmployee, updateEmployeeLogin, deleteEmployee
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.schemas.employee import Employee, EmployeeUpdate, EmployeeUpdateLogin

from fastapi import APIRouter

router = APIRouter(
    prefix="/employee",
    tags=["employee"]
)

@router.post('/create-employee/')
def create_employee(employee_info: Employee):
    employee_list = getAll()

    if employee_info.first_name == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing First Name")
    if employee_info.surname == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing Surame")
    if employee_info.birthdate == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing Birthdate")
    if employee_info.employee_role == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing Role")
    if employee_info.employee_password == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing Password")
    if employee_info.level_access == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing Level Access")
    if employee_info.company_id == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing Company Id")
    if employee_info.address_id == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing Address Id")
    

    for employee in employee_list:
        if (employee_info.email == employee['email']):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")
        elif (employee_info.cpf == employee['cpf']):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="CPF already exists")
        
    employee = createEmployee(employee_info)
    employee_json = jsonable_encoder(employee)
    return JSONResponse(status_code=status.HTTP_200_OK, content=employee_json)

@router.get('/getall-employee/')
def getAll_employee():
    employee_list = getAll()
    if employee_list:
        return employee_list
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Nothing here"})
    
@router.get('/getone-employee/{employee_id}')
def get_employee(employee_id: int = Path(description="The ID of the Employee")):
    employee_list = getOne(employee_id)

    if employee_list:
        return employee_list
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Nothing here"})


@router.put('/update-employee/{employee_id}')
def update_employee(employee_id: int, employee_info: EmployeeUpdate):
    employee_listOne = getOne(employee_id)

    if employee_info.first_name == None:
        employee_info.first_name = employee_listOne[0]['first_name']
    
    if employee_info.surname == None:
        employee_info.surname = employee_listOne[0]['surname']
    
    if employee_info.birthdate == None:
        employee_info.birthdate = employee_listOne[0]['birthdate']

    if employee_info.employee_role == None:
        employee_info.employee_role = employee_listOne[0]['employee_role']

    if employee_info.email == None:
        employee_info.email = employee_listOne[0]['email']

    if employee_info.employee_password == None:
        employee_info.employee_password = employee_listOne[0]['employee_password']

    if employee_info.phone_number == None:
        employee_info.phone_number = employee_listOne[0]['phone_number']
    
    if employee_info.cpf == None:
        employee_info.cpf = employee_listOne[0]['cpf']

    if employee_info.level_access == None:
        employee_info.level_access = employee_listOne[0]['level_access']

    if employee_info.company_id == None:
        employee_info.company_id = employee_listOne[0]['company_id']

    if employee_info.address_id == None:
        employee_info.address_id = employee_listOne[0]['address_id']

    employee_listAll = getAll()

    for employee in employee_listAll:
        if (employee_info.email == employee['email']):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")
        elif (employee_info.cpf == employee['cpf']):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="CPF already exists")

    employee = updateEmployee(employee_id, employee_info)
    employee_json = jsonable_encoder(employee)
    return JSONResponse(status_code=status.HTTP_200_OK, content=employee_json)

@router.put('/update-employeeLogin/{employee_id}')
def update_employeeLogin(employee_id: int, employee_info: EmployeeUpdateLogin):
    employee_listOne = getOne(employee_id)

    if employee_info.email == None:
        employee_info.email = employee_listOne[0]['email']

    if employee_info.employee_password == None:
        employee_info.employee_password = employee_listOne[0]['employee_password']

    employee_listAll = getAll()

    for employee in employee_listAll:
        if (employee_info.email == employee['email']):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")
        elif (employee_info.employee_password == employee['employee_password']):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Password already exists")

    employee = updateEmployeeLogin(employee_id, employee_info)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"Success" : f"Login from Employee ID {employee_id} updated"})

@router.delete('/delete-employee/{employee_id}')
def delete_employee(employee_id: int):

    employee_list = getOne(employee_id)

    if len(employee_list) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Nothing here"})
    else:
        deleteEmployee(employee_id)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"Success" : f"ID {employee_id} deleted"})
