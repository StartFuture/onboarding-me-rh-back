from app.dao.dao import connect_database
from app.schemas.adm import Adm, UpdateAdm
from fastapi import APIRouter
from fastapi import Path, HTTPException, status
from typing import Optional

router = APIRouter(
    prefix="/adm",
    tags=[
        "adm"
    ]
)

adm_default = {}

@router.get('/get-adm-by-email')
def get_adm(email: Optional[str] = None):
    for adm_id in adm_default:
        if adm_default[adm_id].email == email:
            return adm_default[adm_id]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Email not found")

@router.post('/create-login/{adm_id}')
def create_login(adm_id: int, adm: Adm):
    if adm_id in adm_default:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="ID already exists")
    
    for id in adm_default:
        if adm_default[id].email == adm.email:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")
        
    adm_default[adm_id] = adm
    return adm_default[adm_id]

@router.put('/update-login/{adm_id}')
def update_login(adm_id: int, adm: UpdateAdm):
    if adm_id not in adm_default:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID not found")
    
    for id in adm_default:
        if adm_default[id].email == adm.email:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists")
    
    if adm.email != None:
        adm_default[adm_id].email = adm.email
    
    if adm.password != None:
        adm_default[adm_id].password = adm.password

    return adm_default[adm_id]

@router.delete('/delete-login')
def delete_login(adm_id: int):
    if adm_id not in adm_default:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID not found")
    del adm_default[adm_id]
    return {"Success" : "ID deleted"}