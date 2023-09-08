from fastapi import APIRouter, status, HTTPException, Path
from fastapi.encoders import jsonable_encoder
from app.dao import dao_welcome_kit_item as daoWkItem
from fastapi.responses import JSONResponse
from app.schemas import welcome_kit_item as schemas_wk_item

router = APIRouter(
    prefix="/welcome-kit-item",
    tags=[
        "welcome kit item"
    ]
)
    
@router.post('/create-welcome-kit-item/')
def create_WKItem(wk_item_info: schemas_wk_item.WelcomeKitItem):

    if wk_item_info.name == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing Name")
    
    if wk_item_info.image == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing Image")
    
    welcome_kit_item = daoWkItem.createWelcomeKitItem(wk_item_info)
    wk_item_json = jsonable_encoder(welcome_kit_item)
    return JSONResponse(status_code=status.HTTP_200_OK, content=wk_item_json)

@router.get('/getall-welcome-kit-item/')
def getAll_WKItems():
    welcome_kit_item_list = daoWkItem.getAll()
    if welcome_kit_item_list:
        wk_item_json = jsonable_encoder(welcome_kit_item_list)
        return JSONResponse(status_code=status.HTTP_200_OK, content=wk_item_json)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Nothing here"})
    
@router.get('/getone-welcome-kit-item/{welcome_kit_item_id}')
def get_WK(welcome_kit_item_id: int = Path(description="The ID of the Welcome Kit Item")):
    welcome_kit_item_list = daoWkItem.getOne(welcome_kit_item_id)

    if welcome_kit_item_list:
        wk_item_json = jsonable_encoder(welcome_kit_item_list)
        return JSONResponse(status_code=status.HTTP_200_OK, content=wk_item_json)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Nothing here"})
    

@router.put('/update-welcome-kit-item/{welcome_kit_item_id}')
def update_WKItem(welcome_kit_item_id: int, welcome_kit_item_info: schemas_wk_item.WelcomeKitItem):
    welcome_kit_item_listOne = daoWkItem.getOne(welcome_kit_item_id)

    if welcome_kit_item_info.name == None:
        welcome_kit_item_info.name = welcome_kit_item_listOne[0]['name']
    
    if welcome_kit_item_info.image == None:
        welcome_kit_item_info.image = welcome_kit_item_listOne[0]['image']

    welcome_kit_item = daoWkItem.updateWelcomeKitItem(welcome_kit_item_id, welcome_kit_item_info)
    wk_item_json = jsonable_encoder(welcome_kit_item)
    return JSONResponse(status_code=status.HTTP_200_OK, content=wk_item_json)

@router.delete('/delete-welcome-kit-item/{welcome_kit_item_id}')
def delete_WKItem(welcome_kit_item_id: int):

    welcome_kit_item_list = daoWkItem.getOne(welcome_kit_item_id)

    if len(welcome_kit_item_list) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Nothing here"})
    else:
        daoWkItem.deleteWelcomeKitItem(welcome_kit_item_id)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"Success" : f"ID {welcome_kit_item_id} deleted"})