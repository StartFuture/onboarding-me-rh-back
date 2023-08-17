from fastapi import APIRouter, status, HTTPException, Path
from app.dao.dao_company import createCompany, getAll, getOne, updateCompany, deleteCompany
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.schemas.company import Company, CompanyUpdate

router = APIRouter(
    prefix="/company",
    tags=[
        "company"
    ]
)
    
@router.post('/create-company/')
def create_company(company_info: Company):
    company_list = getAll()

    if company_info.company_name == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing Company Name")
    if company_info.trading_name == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing Trading Name")
    if company_info.company_password == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing Company Password")

    for company in company_list:
        if (company_info.email == company['email']):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")
        elif (company_info.cnpj == company['cnpj']):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="CNPJ already exists")
        
    company = createCompany(company_info)
    company_json = jsonable_encoder(company)
    return JSONResponse(status_code=status.HTTP_200_OK, content=company_json)

@router.get('/getall-company/')
def getAll_company():
    company_list = getAll()
    if company_list:
        return company_list
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Nothing here"})
    
@router.get('/getone-company/{company_id}')
def get_company(company_id: int = Path(description="The ID of the Company")):
    company_list = getOne(company_id)

    if company_list:
        return company_list
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Nothing here"})
    

@router.put('/update-company/{company_id}')
def update_company(company_id: int, company_info: CompanyUpdate):
    company_listOne = getOne(company_id)

    if company_info.company_name == None:
        company_info.company_name = company_listOne[0]['company_name']
    
    if company_info.trading_name == None:
        company_info.trading_name = company_listOne[0]['trading_name']
    
    if company_info.logo == None:
        company_info.logo = company_listOne[0]['logo']

    if company_info.cnpj == None:
        company_info.cnpj = company_listOne[0]['cnpj']

    if company_info.email == None:
        company_info.email = company_listOne[0]['email']
    
    if company_info.company_password == None:
        company_info.company_password = company_listOne[0]['company_password']

    if company_info.state_register == None:
        company_info.state_register = company_listOne[0]['state_register']

    company_listAll = getAll()

    for company in company_listAll:
        if (company_info.email == company['email']):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")
        elif (company_info.cnpj == company['cnpj']):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="CNPJ already exists")

    company = updateCompany(company_id, company_info)
    company_json = jsonable_encoder(company)
    return JSONResponse(status_code=status.HTTP_200_OK, content=company_json)

@router.delete('/delete-company/{company_id}')
def delete_company(company_id: int):

    company_list = getOne(company_id)

    if len(company_list) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Nothing here"})
    else:
        deleteCompany(company_id)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"Success" : f"ID {company_id} deleted"})