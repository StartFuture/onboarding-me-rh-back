from fastapi import APIRouter, status, HTTPException, Path
from app.dao.dao_welcome_kit import createWelcomeKit, getOne, updateWelcomeKit, deleteWelcomeKit, createWelcomeKit_WKItem
from app.dao.dao_welcome_kit import getAll as getAllWk
from app.dao.dao_welcome_kit_item import getAll as getAllItem
from fastapi.responses import JSONResponse
from app.schemas.welcome_kit import WelcomeKit
from app.schemas.welcome_kit_wk_item import WelcomeKit_WKItem


router = APIRouter(
    prefix="/welcome-kit",
    tags=[
        "welcome kit"
    ]
)
    
@router.post('/create-welcome-kit/')
def create_WK(wk_info: WelcomeKit):

    if wk_info.name == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing Name")
      
    welcome_kit = createWelcomeKit(wk_info)
    return welcome_kit

@router.get('/getall-welcome-kit/')
def getAll_WK():
    welcome_kit_list = getAllWk()
    if welcome_kit_list:
        return welcome_kit_list
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Nothing here"})
    
@router.get('/getone-welcome-kit/{welcome_kit_id}')
def get_WK(welcome_kit_id: int = Path(description="The ID of the Welcome Kit")):
    welcome_kit_list = getOne(welcome_kit_id)

    if welcome_kit_list:
        return welcome_kit_list
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Nothing here"})
    

@router.put('/update-welcome-kit/{welcome_kit_id}')
def update_WK(welcome_kit_id: int, welcome_kit_info: WelcomeKit):
    welcome_kit_listOne = getOne(welcome_kit_id)

    if welcome_kit_info.name == None:
        welcome_kit_info.name = welcome_kit_listOne[0]['name']
    
    if welcome_kit_info.image == None:
        welcome_kit_info.image = welcome_kit_listOne[0]['image']

    welcome_kit = updateWelcomeKit(welcome_kit_id, welcome_kit_info)
    return welcome_kit

@router.delete('/delete-welcome-kit/{welcome_kit_id}')
def delete_WK(welcome_kit_id: int):

    welcome_kit_list = getOne(welcome_kit_id)

    if len(welcome_kit_list) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Nothing here"})
    else:
        deleteWelcomeKit(welcome_kit_id)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"Success" : f"ID {welcome_kit_id} deleted"})

@router.post('/create-welcome-kit-wkitem/')
def create_WK_WKItem(wk_wkitem_info: WelcomeKit_WKItem):

    if wk_wkitem_info.welcome_kit_id == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing Welcome Kit Id")
    if wk_wkitem_info.item_id == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing Item Id")
    
    wk_list = getAllWk()
    wk_item_list = getAllItem()
    print(wk_list)
    print(wk_item_list)

    for wk in wk_list:
        if (wk_wkitem_info.welcome_kit_id == wk['id']):
            print(wk)
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Welcome Kit Id doesn't exist")
        
    for wk_item in wk_item_list:
        if (wk_wkitem_info.item_id == wk_item['id']):
            print(wk_item)
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Item Id doesn't exist")   

    wk_wkitem = createWelcomeKit_WKItem(wk_wkitem_info)
    return wk_wkitem