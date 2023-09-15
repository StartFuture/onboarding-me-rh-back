from fastapi import APIRouter, Depends, Query, status, HTTPException, Path
from fastapi.encoders import jsonable_encoder
from app.dao import dao_welcome_kit as daoWelcomeKit
from fastapi.responses import JSONResponse
from app.schemas import welcome_kit as schemas_wk
from fastapi_pagination import Page, Params, paginate

router = APIRouter(
    prefix="/welcome-kit",
    tags=[
        "welcome kit"
    ]
)
    
@router.post('/create-welcome-kit/')
def create_WK(wk_info: schemas_wk.WelcomeKit):

    if wk_info.name == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing Name")
    
    welcome_kit = daoWelcomeKit.createWelcomeKit(wk_info)
    wk_json = jsonable_encoder(welcome_kit)
    return JSONResponse(status_code=status.HTTP_200_OK, content=wk_json)

@router.get('/getall-welcome-kit/')
def getAll_WK():
    welcome_kit_list = daoWelcomeKit.getAll()
    if welcome_kit_list:
        wk_json = jsonable_encoder(welcome_kit_list)
        return JSONResponse(status_code=status.HTTP_200_OK, content=wk_json)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Nothing here"})
    
@router.get('/getone-welcome-kit/{welcome_kit_id}')
def get_WK(welcome_kit_id: int = Path(description="The ID of the Welcome Kit")):
    welcome_kit_list = daoWelcomeKit.getOne(welcome_kit_id)

    if welcome_kit_list:
        wk_json = jsonable_encoder(welcome_kit_list)
        return JSONResponse(status_code=status.HTTP_200_OK, content=wk_json)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Nothing here"})

@router.put('/update-welcome-kit/{welcome_kit_id}')
def update_WK(welcome_kit_id: int, welcome_kit_info: schemas_wk.WelcomeKit):
    welcome_kit_listOne = daoWelcomeKit.getOne(welcome_kit_id)

    if welcome_kit_info.name == None:
        welcome_kit_info.name = welcome_kit_listOne[0]['name']
    
    if welcome_kit_info.image == None:
        welcome_kit_info.image = welcome_kit_listOne[0]['image']

    welcome_kit = daoWelcomeKit.updateWelcomeKit(welcome_kit_id, welcome_kit_info)
    wk_json = jsonable_encoder(welcome_kit)
    return JSONResponse(status_code=status.HTTP_200_OK, content=wk_json)

@router.delete('/delete-welcome-kit/{welcome_kit_id}')
def delete_WK(welcome_kit_id: int):

    welcome_kit_list = daoWelcomeKit.getOne(welcome_kit_id)

    if len(welcome_kit_list) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Nothing here"})
    else:
        daoWelcomeKit.deleteWelcomeKit(welcome_kit_id)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"Success" : f"ID {welcome_kit_id} deleted"})

@router.get('/getall-wk-paginated/')
def getAll_wk_paginated(page: int):
    welcome_kit_list = daoWelcomeKit.getAllPaginated(page)
    if welcome_kit_list:
        wk_paginate_json = jsonable_encoder(welcome_kit_list)
        return JSONResponse(status_code=status.HTTP_200_OK, content=wk_paginate_json)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Nothing here"})
    
@router.get('/get-wk-byname')
def get_wk_byname(name: str = Query(default=None, description="The name of the Welcome Kit")):
    welcome_kit_list = daoWelcomeKit.getWkByName(name)

    if welcome_kit_list:
        wk_json = jsonable_encoder(welcome_kit_list)
        return JSONResponse(status_code=status.HTTP_200_OK, content=wk_json)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Nothing here"})

@router.get('/filter-wk-byname')
def filter_wk_byname(name: str = Query(default=None, description="The name of the Welcome Kit")):
    welcome_kit_listAll = daoWelcomeKit.getAll()
    
    welcome_kit_list = list(filter(lambda obj: name.lower() in obj['name'].lower(), welcome_kit_listAll))

    if welcome_kit_list:
        wk_json = jsonable_encoder(welcome_kit_list)
        return JSONResponse(status_code=status.HTTP_200_OK, content=wk_json)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Nothing here"})
    