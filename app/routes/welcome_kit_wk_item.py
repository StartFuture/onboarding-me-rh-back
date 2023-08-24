from fastapi import APIRouter, status, HTTPException, Body
from app.dao.dao_welcome_kit_wk_item import createWelcomeKit_WKItem
from app.dao.dao_welcome_kit import getOne as getOneWk
from app.dao.dao_welcome_kit_item import getOne as getOneItem
from app.schemas.welcome_kit_wk_item import WelcomeKit_WKItem


router = APIRouter(
    prefix="/welcome-kit-wk-item",
    tags=[
        "welcome kit - welcome kit item"
    ]
)

@router.post('/create-welcome-kit-wkitem/')
def create_WK_WKItem(wk_wkitem_info: WelcomeKit_WKItem = Body(description="Associates a WK Id with an Item Id")):

    if wk_wkitem_info.welcome_kit_id == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing Welcome Kit Id")
    if wk_wkitem_info.item_id == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing Item Id")
    
    wk_list = getOneWk(wk_wkitem_info.welcome_kit_id)
    wk_item_list = getOneItem(wk_wkitem_info.item_id)

    if wk_list:
        pass
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Welcome Kit Id doesn't exist"})
    
    if wk_item_list:
        pass
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Item Id doesn't exist"}) 

    wk_wkitem = createWelcomeKit_WKItem(wk_wkitem_info)
    return wk_wkitem