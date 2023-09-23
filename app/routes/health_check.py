from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.responses import JSONResponse

router = APIRouter(
    prefix="/healthcheck",
    tags=[
        "healthcheck"
    ]
)


@router.get("/ping")
def get_health_check():
    return JSONResponse(status_code=status.HTTP_200_OK, content={"msg": "pong"})
    