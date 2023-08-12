from fastapi import APIRouter, status, HTTPException, Path
from fastapi.responses import JSONResponse
from app.dao.dao_getLogin import getAll, getOne

route_get = APIRouter(
    prefix="/adm",
    tags=[
        "adm"
    ]
)

@route_get.get('/getall-adm/')
def getAll_adm():
    adm_list = getAll()
    if adm_list:
        return JSONResponse(status_code=status.HTTP_200_OK, content=adm_list)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Nothing here"})
    
@route_get.get('/get-one-adm/{adm_id}')
def get_adm(adm_id: int = Path(description="The ID of the Adm")):
    adm_list = getOne(adm_id)
    if adm_list:
        return JSONResponse(status_code=status.HTTP_200_OK, content=adm_list)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Nothing here"})