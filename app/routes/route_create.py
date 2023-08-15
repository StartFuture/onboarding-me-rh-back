from fastapi import APIRouter, status, HTTPException
from app.dao.dao_createLogin import createLogin
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.dao.dao_getLogin import getAll
from app.schemas.adm import Adm

route_create = APIRouter(
    prefix="/adm",
    tags=[
        "adm"
    ]
)
    
@route_create.post('/create-adm/{adm_id}')
def create_adm(adm_id: int, adm_info: Adm):
    adm_list = getAll()

    for adm in adm_list:
        if (adm_id == adm['id']):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ID already exists")
        elif (adm_info.email == adm['email']):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")
        
    adm = createLogin(adm_id, adm_info)
    adm_json = jsonable_encoder(adm)
    return JSONResponse(status_code=status.HTTP_200_OK, content=adm_json)