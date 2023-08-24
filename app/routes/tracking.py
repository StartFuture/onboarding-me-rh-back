from fastapi import APIRouter, status, HTTPException, Path
from fastapi.encoders import jsonable_encoder
from app.dao.dao_tracking import createTracking, getAll, getOne, updateTracking, deleteTracking
from fastapi.responses import JSONResponse
from app.schemas.tracking import Tracking, TrackingUpdate


router = APIRouter(
    prefix="/tracking",
    tags=[
        "tracking"
    ]
)
    
@router.post('/create-tracking/')
def create_tracking(tracking_info: Tracking):

    if tracking_info.tracking_code == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing Tracking Code")
    if tracking_info.status == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing Status")
    if tracking_info.employee_id == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing Employee Id")
    if tracking_info.welcome_kit_id == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing Welcome Kit Id")
    
    tracking_list = getAll()

    for tracking in tracking_list:
        if (tracking_info.tracking_code == tracking['tracking_code']):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Tracking Code already exists")
    
    tracking = createTracking(tracking_info)
    tracking_json = jsonable_encoder(tracking)
    return JSONResponse(status_code=status.HTTP_200_OK, content=tracking_json)

@router.get('/getall-tracking/')
def getAll_tracking():
    tracking_list = getAll()
    if tracking_list:
        return tracking_list
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Nothing here"})
    
@router.get('/getone-tracking/{tracking_id}')
def get_tracking(tracking_id: int = Path(description="The ID of the Tracking")):
    tracking_list = getOne(tracking_id)

    if tracking_list:
        return tracking_list
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Nothing here"})
    

@router.put('/update-tracking/{tracking_id}')
def update_tracking(tracking_id: int, tracking_info: TrackingUpdate):
    tracking_listOne = getOne(tracking_id)

    if tracking_info.tracking_code == None:
        tracking_info.tracking_code = tracking_listOne[0]['tracking_code']
    
    if tracking_info.status == None:
        tracking_info.status = tracking_listOne[0]['status']

    tracking_list = getAll()

    for tracking in tracking_list:
        if (tracking_info.tracking_code == tracking['tracking_code']):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Tracking Code already exists")

    tracking = updateTracking(tracking_id, tracking_info)
    tracking_json = jsonable_encoder(tracking)
    return JSONResponse(status_code=status.HTTP_200_OK, content=tracking_json)

@router.delete('/delete-tracking/{tracking_id}')
def delete_tracking(tracking_id: int):

    tracking_list = getOne(tracking_id)

    if len(tracking_list) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Nothing here"})
    else:
        deleteTracking(tracking_id)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"Success" : f"ID {tracking_id} deleted"})