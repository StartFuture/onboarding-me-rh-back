from fastapi import APIRouter, status, HTTPException, Path
from app.dao import dao_employee as daoEmployee
from app.dao import dao_address as daoAddress
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.schemas import employee as schemas_employee

from fastapi import APIRouter

router = APIRouter(
    prefix="/employee",
    tags=["employee"]
)

@router.post('/create-employee/')
def create_employee(employee_info: schemas_employee.Employee):
    employee_list = daoEmployee.getAll()

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
        
    employee = daoEmployee.createEmployee(employee_info)
    employee_json = jsonable_encoder(employee)
    return JSONResponse(status_code=status.HTTP_200_OK, content=employee_json)

@router.get('/getall-employee/')
def getAll_employee():
    employee_list = daoEmployee.getAll()
    if employee_list:
        employee_json = jsonable_encoder(employee_list)
        return JSONResponse(status_code=status.HTTP_200_OK, content=employee_json)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Nothing here"})
    
@router.get('/getone-employee/{employee_id}')
def get_employee(employee_id: int = Path(description="The ID of the Employee")):
    employee_list = daoEmployee.getOne(employee_id)

    if employee_list:
        employee_json = jsonable_encoder(employee_list)
        return JSONResponse(status_code=status.HTTP_200_OK, content=employee_json)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Nothing here"})
    
@router.get("/get-employee-info/{employee_id}")
def get_employee_info(employee_id: int):
    
    employee = daoEmployee.getEmployeeInfo(employee_id)
    
    if employee:
        employee_json = jsonable_encoder(employee)
        return JSONResponse(status_code=status.HTTP_200_OK, content=employee_json)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Nothing here"})


@router.put('/update-employee/{employee_id}')
def update_employee(employee_id: int, employee_info: schemas_employee.EmployeeUpdate):
    employee_listOne = daoEmployee.getOne(employee_id)

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

    employee_listAll = daoEmployee.getAll()

    for employee in employee_listAll:
        if (employee_info.email == employee['email']):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")
        elif (employee_info.cpf == employee['cpf']):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="CPF already exists")

    employee = daoEmployee.updateEmployee(employee_id, employee_info)
    employee_json = jsonable_encoder(employee)
    return JSONResponse(status_code=status.HTTP_200_OK, content=employee_json)

@router.put('/update-employeeLogin/{employee_id}')
def update_employeeLogin(employee_id: int, employee_info: schemas_employee.EmployeeUpdateLogin):
    employee_listOne = daoEmployee.getOne(employee_id)

    if employee_info.email == None:
        employee_info.email = employee_listOne[0]['email']

    if employee_info.employee_password == None:
        employee_info.employee_password = employee_listOne[0]['employee_password']

    employee_listAll = daoEmployee.getAll()

    for employee in employee_listAll:
        if (employee_info.email == employee['email']):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")
        elif (employee_info.employee_password == employee['employee_password']):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Password already exists")

    employee = daoEmployee.updateEmployeeLogin(employee_id, employee_info)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"Success" : f"Login from Employee ID {employee_id} updated"})

@router.put('/update-employee-info/{employee_id}')
def update_employee_info(employee_id: int, employee_info: schemas_employee.EmployeeUpdateInfo):
    employee_listOne = daoEmployee.getEmployeeInfo(employee_id)

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

    if employee_info.phone_number == None:
        employee_info.phone_number = employee_listOne[0]['phone_number']
    
    if employee_info.cpf == None:
        employee_info.cpf = employee_listOne[0]['cpf']

    if employee_info.street == None:
        employee_info.street = employee_listOne[0]['street']

    if employee_info.zipcode == None:
        employee_info.zipcode = employee_listOne[0]['zipcode']

    if employee_info.city == None:
        employee_info.city = employee_listOne[0]['city']

    if employee_info.state == None:
        employee_info.state = employee_listOne[0]['state']    

    if employee_info.num == None:
        employee_info.num = employee_listOne[0]['num']
    
    if employee_info.complement == None:
        employee_info.complement = employee_listOne[0]['complement']

    if employee_info.tracking_code == None:
        employee_info.tracking_code = employee_listOne[0]['tracking_code']

    if employee_info.status == None:
        employee_info.status = employee_listOne[0]['status']

    employee_listAll = daoEmployee.getAllEmployeeInfo()

    for employee in employee_listAll:
        if (employee_info.email == employee['email']):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")
        elif (employee_info.cpf == employee['cpf']):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="CPF already exists")
        elif (employee_info.tracking_code == employee['tracking_code']):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Tracking Code already exists")

    employee = daoEmployee.updateEmployeeInfo(employee_id, employee_info)
    employee_json = jsonable_encoder(employee)
    return JSONResponse(status_code=status.HTTP_200_OK, content=employee_json)

@router.delete('/delete-employee/{employee_id}')
def delete_employee(employee_id: int):

    employee_listOne = daoEmployee.getOne(employee_id)

    if len(employee_listOne) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Nothing here"})
    else:
        daoEmployee.deleteEmployee(employee_id)

    employee_listAll = daoEmployee.getAll()

    for employee in employee_listAll:

        print("address id: ", employee_listOne[0]["address_id"])

        if (employee_listOne[0]["address_id"] == employee['address_id']):
            break
        else:
            daoAddress.deleteAddress(employee_listOne[0]["address_id"])

    return JSONResponse(status_code=status.HTTP_200_OK, content={"Success" : f"ID {employee_id} deleted"})
