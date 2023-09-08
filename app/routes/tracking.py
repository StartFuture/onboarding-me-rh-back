from fastapi import APIRouter, status, HTTPException, Path
from fastapi.encoders import jsonable_encoder
from app.dao import dao_tracking as daoTracking
from fastapi.responses import JSONResponse
from app.schemas import tracking as schemas_tracking


router = APIRouter(
    prefix="/tracking",
    tags=[
        "tracking"
    ]
)
    
@router.post('/create-tracking/')
def create_tracking(tracking_info: schemas_tracking.Tracking):

    if tracking_info.tracking_code == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing Tracking Code")
    if tracking_info.status == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing Status")
    if tracking_info.employee_id == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing Employee Id")
    if tracking_info.welcome_kit_id == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing Welcome Kit Id")
    
    tracking_list = daoTracking.getAll()

    for tracking in tracking_list:
        if (tracking_info.tracking_code == tracking['tracking_code']):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Tracking Code already exists")
    
    tracking = daoTracking.createTracking(tracking_info)
    tracking_json = jsonable_encoder(tracking)
    return JSONResponse(status_code=status.HTTP_200_OK, content=tracking_json)

@router.get('/getall-tracking/')
def getAll_tracking():
    tracking_list = daoTracking.getAll()
    if tracking_list:
        tracking_json = jsonable_encoder(tracking_list)
        return JSONResponse(status_code=status.HTTP_200_OK, content=tracking_json)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Nothing here"})
    
@router.get('/getone-tracking/{tracking_id}')
def get_tracking(tracking_id: int = Path(description="The ID of the Tracking")):
    tracking_list = daoTracking.getOne(tracking_id)

    if tracking_list:
        tracking_json = jsonable_encoder(tracking_list)
        return JSONResponse(status_code=status.HTTP_200_OK, content=tracking_json)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Nothing here"})
    

@router.put('/update-tracking/{tracking_id}')
def update_tracking(tracking_id: int, tracking_info: schemas_tracking.TrackingUpdate):
    tracking_listOne = daoTracking.getOne(tracking_id)

    if tracking_info.tracking_code == None:
        tracking_info.tracking_code = tracking_listOne[0]['tracking_code']
    
    if tracking_info.status == None:
        tracking_info.status = tracking_listOne[0]['status']

    tracking_list = daoTracking.getAll()

    for tracking in tracking_list:
        if (tracking_info.tracking_code == tracking['tracking_code']):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Tracking Code already exists")

    tracking = daoTracking.updateTracking(tracking_id, tracking_info)
    tracking_json = jsonable_encoder(tracking)
    return JSONResponse(status_code=status.HTTP_200_OK, content=tracking_json)

@router.delete('/delete-tracking/{tracking_id}')
def delete_tracking(tracking_id: int):

    tracking_list = daoTracking.getOne(tracking_id)

    if len(tracking_list) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Nothing here"})
    else:
        daoTracking.deleteTracking(tracking_id)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"Success" : f"ID {tracking_id} deleted"})