from fastapi import APIRouter, status, HTTPException, Path
from fastapi.encoders import jsonable_encoder
from app.dao.dao_address import createAddress, getAll, getOne, updateAddress, deleteAddress
from fastapi.responses import JSONResponse
from app.schemas.address import Address, AddressUpdate


router = APIRouter(
    prefix="/address",
    tags=[
        "address"
    ]
)
    
@router.post('/create-address/')
def create_address(address_info: Address):

    if address_info.num == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing Number")
    if address_info.zipcode == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing Zipcode")
    if address_info.street == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing Street")
    if address_info.district == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing District")
    if address_info.city == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing City")
    if address_info.state == "":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing State")
      
    address = createAddress(address_info)
    address_json = jsonable_encoder(address)
    return JSONResponse(status_code=status.HTTP_200_OK, content=address_json)

@router.get('/getall-address/')
def getAll_Address():
    address_list = getAll()
    if address_list:
        return address_list
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Nothing here"})
    
@router.get('/getone-address/{address_id}')
def getOne_Address(address_id: int = Path(description="The ID of the Address")):
    address_list = getOne(address_id)

    if address_list:
        return address_list
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Nothing here"})
    

@router.put('/update-address/{address_id}')
def update_Address(address_id: int, address_info: AddressUpdate):
    address_listOne = getOne(address_id)

    if address_info.num == None:
        address_info.num = address_listOne[0]['num']
    if address_info.complement == None:
        address_info.complement = address_listOne[0]['complement']
    if address_info.zipcode == None:
        address_info.zipcode = address_listOne[0]['zipcode']
    if address_info.street == None:
        address_info.street = address_listOne[0]['street']
    if address_info.district == None:
        address_info.district = address_listOne[0]['district']
    if address_info.city == None:
        address_info.city = address_listOne[0]['city']
    if address_info.state == None:
        address_info.state = address_listOne[0]['state']

    address = updateAddress(address_id, address_info)
    address_json = jsonable_encoder(address)
    return JSONResponse(status_code=status.HTTP_200_OK, content=address_json)

@router.delete('/delete-address/{address_id}')
def delete_Address(address_id: int):

    address_list = getOne(address_id)

    if len(address_list) == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": "Nothing here"})
    else:
        deleteAddress(address_id)

    return JSONResponse(status_code=status.HTTP_200_OK, content={"Success" : f"ID {address_id} deleted"})