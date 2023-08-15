from fastapi import APIRouter, status, HTTPException
from fastapi.responses import JSONResponse
from app.dao.dao_getLogin import getOne
from app.dao.dao_deleteLogin import deleteLogin

route_delete = APIRouter(
    prefix="/adm",
    tags=[
        "adm"
    ]
)
    
@route_delete.delete('/delete-adm/{adm_id}')
def delete_adm(adm_id: int):

    adm_list = getOne(adm_id)

    if len(adm_list) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Nothing here"})
    else:
        deleteLogin(adm_id)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"Success" : f"ID {adm_id} deleted"})
