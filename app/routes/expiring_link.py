from app.services.link import Link
from fastapi import APIRouter, status, HTTPException

router = APIRouter(
    prefix="/expiring_link",
    tags=[
        "expiring_link"
    ]
)

@router.get('/create-expiring-link/')
def create_expiring_link(link_base: str) -> str:
    
    try:
        response: str = Link.create_expiring_link(link_base)
        return response
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"msg": e})

@router.get('/read-expiring-link/')
def read_expiring_link(link: str) -> bool:
    
    return Link.is_link_valid(link)


    