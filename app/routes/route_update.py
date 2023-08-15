from fastapi import APIRouter, status, HTTPException
from app.dao.dao_updateLogin import updateLogin
from app.dao.dao_getLogin import getOne, getAll
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.schemas.adm import UpdateAdm

route_update = APIRouter(
    prefix="/adm",
    tags=[
        "adm"
    ]
)
    
@route_update.put('/update-adm/{adm_id}')
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
