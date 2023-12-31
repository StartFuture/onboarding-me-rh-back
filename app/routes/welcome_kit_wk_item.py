from fastapi import APIRouter, status, HTTPException, Body
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from app.dao import dao_welcome_kit_wk_item as daoWkWkItem
from app.dao import dao_welcome_kit as daoWK
from app.dao import dao_welcome_kit_item as daoWkItem
from app.schemas import welcome_kit_wk_item as schemas_wk_wkitem


router = APIRouter(
    prefix="/welcome-kit-wk-item",
    tags=[
        "welcome kit - welcome kit item"
    ]
)

def create_Link_WK_WKItem(welcome_kit_id, item_id):
    if welcome_kit_id == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing Welcome Kit Id")
    if item_id == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing Item Id")
    
    wk_list = daoWK.getOne(welcome_kit_id)
    wk_item_list = daoWkItem.getOne(item_id)

    if wk_list:
        pass
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Welcome Kit Id doesn't exist"})
    
    if wk_item_list:
        pass
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Item Id doesn't exist"}) 

    wk_wkitem = daoWkWkItem.createWelcomeKit_WKItem(welcome_kit_id, item_id)
    return jsonable_encoder(wk_wkitem)

@router.post('/create-welcome-kit-wkitem/')
def create_WK_WKItem(wk_wkitem_info: schemas_wk_wkitem.WelcomeKit_WKItem = Body(description="Associates a WK Id with an Item Id")):

    return JSONResponse(status_code=status.HTTP_200_OK, content=wk_item_json)