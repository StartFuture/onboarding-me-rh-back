from fastapi import APIRouter, status, HTTPException, Path
from app.dao.dao_admin import createLogin, getAll, getOne, updateLogin, deleteLogin
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.schemas.admin import Adm, UpdateAdm

router = APIRouter(
    prefix="/adm",
    tags=[
        "adm"
    ]
)
    
@router.post('/create-adm/')
def create_adm(adm_info: Adm):
    adm_list = getAll()

    for adm in adm_list:
        if (adm_info.email == adm['email']):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")
        
    adm = createLogin(adm_info)
    adm_json = jsonable_encoder(adm)
    return JSONResponse(status_code=status.HTTP_200_OK, content=adm_json)

@router.get('/getall-adm/')
def getAll_adm():
    adm_list = getAll()
    if adm_list:
        return JSONResponse(status_code=status.HTTP_200_OK, content=adm_list)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Nothing here"})
    
@router.get('/getone-adm/{adm_id}')
def get_adm(adm_id: int = Path(description="The ID of the Adm")):
    adm_list = getOne(adm_id)
    if adm_list:
        return JSONResponse(status_code=status.HTTP_200_OK, content=adm_list)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Nothing here"})
    

@router.put('/update-adm/{adm_id}')
def update_adm(adm_id: int, adm_info: UpdateAdm):
    adm_listOne = getOne(adm_id)

    if adm_info.email == None:
        adm_info.email = adm_listOne[0]['email']
    
    if adm_info.password == None:
        adm_info.password = adm_listOne[0]['password']

    adm_listAll = getAll()

    for adm in adm_listAll:
        if (adm_info.email == adm['email']):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")

    adm = updateLogin(adm_id, adm_info)
    adm_json = jsonable_encoder(adm)
    return JSONResponse(status_code=status.HTTP_200_OK, content=adm_json)

@router.delete('/delete-adm/{adm_id}')
def delete_adm(adm_id: int):

    adm_list = getOne(adm_id)

    if len(adm_list) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Nothing here"})
    else:
        deleteLogin(adm_id)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"Success" : f"ID {adm_id} deleted"})