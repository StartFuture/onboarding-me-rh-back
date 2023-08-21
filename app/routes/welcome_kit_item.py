from fastapi import APIRouter, status, HTTPException, Path
from app.dao.dao_welcome_kit_item import createWelcomeKitItem, getAll, getOne, updateWelcomeKitItem, deleteWelcomeKitItem
from fastapi.responses import JSONResponse
from app.schemas.welcome_kit_item import WelcomeKitItem

router = APIRouter(
    prefix="/welcome-kit-item",
    tags=[
        "welcome kit item"
    ]
)
    
@router.post('/create-welcome-kit-item/')
def create_WKItem(wk_item_info: WelcomeKitItem):

    if wk_item_info.name == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing Name")
    
    if wk_item_info.image == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing Image")
      
    welcome_kit_item = createWelcomeKitItem(wk_item_info)
    return welcome_kit_item

@router.get('/getall-welcome-kit-item/')
def getAll_WKItems():
    welcome_kit_item_list = getAll()
    if welcome_kit_item_list:
        return welcome_kit_item_list
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Nothing here"})
    
@router.get('/getone-welcome-kit-item/{welcome_kit_item_id}')
def get_WK(welcome_kit_item_id: int = Path(description="The ID of the Welcome Kit Item")):
    welcome_kit_item_list = getOne(welcome_kit_item_id)

    if welcome_kit_item_list:
        return welcome_kit_item_list
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Nothing here"})
    

@router.put('/update-welcome-kit-item/{welcome_kit_item_id}')
def update_WKItem(welcome_kit_item_id: int, welcome_kit_item_info: WelcomeKitItem):
    welcome_kit_item_listOne = getOne(welcome_kit_item_id)

    if welcome_kit_item_info.name == None:
        welcome_kit_item_info.name = welcome_kit_item_listOne[0]['name']
    
    if welcome_kit_item_info.image == None:
        welcome_kit_item_info.image = welcome_kit_item_listOne[0]['image']

    welcome_kit_item = updateWelcomeKitItem(welcome_kit_item_id, welcome_kit_item_info)
    return welcome_kit_item

@router.delete('/delete-welcome-kit-item/{welcome_kit_item_id}')
def delete_WKItem(welcome_kit_item_id: int):

    welcome_kit_item_list = getOne(welcome_kit_item_id)

    if len(welcome_kit_item_list) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Nothing here"})
    else:
        deleteWelcomeKitItem(welcome_kit_item_id)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"Success" : f"ID {welcome_kit_item_id} deleted"})