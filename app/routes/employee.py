from app.schemas.employee import Employee

from fastapi import APIRouter

router = APIRouter(
    prefix="/employee",
    tags=["employee"]
)

@router.post("/")
async def post_employee(employee: Employee):
    return employee
